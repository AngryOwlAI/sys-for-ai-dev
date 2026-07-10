from __future__ import annotations

import copy
import csv
import tempfile
import unittest
from pathlib import Path

from sys_for_ai.jsonschema_io import check_schema, load_json, validate_instance
from sys_for_ai.trace_migration import (
    GENERALIZED_HEADER,
    LEGACY_HEADER,
    migrate_legacy_trace_row,
    reverse_generalized_trace_row,
    validate_requirement_trace_migration,
)


PRODUCT_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = PRODUCT_ROOT / "schemas/contracts/requirement_trace_registry_row.schema.json"
TRACE_PATH = PRODUCT_ROOT / "registries/requirement_trace_registry.csv"


class TraceSchemaMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = load_json(SCHEMA_PATH)
        with TRACE_PATH.open(newline="", encoding="utf-8") as handle:
            cls.legacy_rows = list(csv.DictReader(handle))
        cls.generalized = migrate_legacy_trace_row(cls.legacy_rows[0])

    def test_schema_is_valid_draft_2020_12(self) -> None:
        self.assertEqual([], check_schema(self.schema))

    def test_live_legacy_row_remains_valid_during_transition(self) -> None:
        self.assertEqual([], validate_instance(self.legacy_rows[0], self.schema))

    def test_generalized_row_passes(self) -> None:
        self.assertEqual([], validate_instance(self.generalized, self.schema))
        self.assertEqual(GENERALIZED_HEADER, tuple(self.generalized))

    def test_generalized_row_is_exactly_reversible(self) -> None:
        expected = {field: self.legacy_rows[0][field] for field in LEGACY_HEADER}
        self.assertEqual(expected, reverse_generalized_trace_row(self.generalized))

    def test_covered_does_not_imply_implemented(self) -> None:
        data = copy.deepcopy(self.generalized)
        data["coverage_status"] = "covered"
        data["capability_status"] = "absent"
        self.assertEqual([], validate_instance(data, self.schema))

    def test_optional_profile_is_independent_of_coverage_and_capability(self) -> None:
        data = copy.deepcopy(self.generalized)
        data["requirement_id"] = "SFA-P1-INIT-EVID-002"
        data["applicability_status"] = "optional_profile"
        data["coverage_status"] = "covered"
        data["capability_status"] = "absent"
        self.assertEqual([], validate_instance(data, self.schema))

    def test_implemented_requires_implementation_artifact(self) -> None:
        self._assert_mutation_fails(
            lambda data: data.__setitem__("capability_status", "implemented")
        )

    def test_operational_requires_current_passing_evidence(self) -> None:
        data = copy.deepcopy(self.generalized)
        data["capability_status"] = "operational"
        data["implementation_artifacts"] = "Sys4AI/sys_for_ai/trace_migration.py"
        self.assertNotEqual([], validate_instance(data, self.schema))
        data["verification_status"] = "pass"
        data["evidence_status"] = "current"
        data["validation_evidence"] = "Sys4AI/tests/test_trace_schema_migration.py"
        self.assertEqual([], validate_instance(data, self.schema))

    def test_removed_rejects_active_implementation_path(self) -> None:
        data = copy.deepcopy(self.generalized)
        data["capability_status"] = "removed"
        data["evidence_status"] = "historical"
        data["implementation_artifacts"] = "Sys4AI/sys_for_ai/removed_runtime.py"
        self.assertNotEqual([], validate_instance(data, self.schema))

    def test_pass_requires_validation_evidence(self) -> None:
        self._assert_mutation_fails(
            lambda data: data.__setitem__("verification_status", "pass")
        )

    def test_waiver_requires_waiver_id(self) -> None:
        self._assert_mutation_fails(
            lambda data: data.__setitem__("verification_status", "waived")
        )

    def test_nonwaived_row_rejects_waiver_id(self) -> None:
        self._assert_mutation_fails(
            lambda data: data.__setitem__("verification_waiver_id", "WAIVER-001")
        )

    def test_reviewed_row_requires_review_date(self) -> None:
        self._assert_mutation_fails(
            lambda data: data.__setitem__("semantic_review_verdict", "sufficient")
        )

    def test_not_reviewed_row_rejects_review_date(self) -> None:
        self._assert_mutation_fails(
            lambda data: data.__setitem__("semantic_review_date", "2026-07-10")
        )

    def test_live_registry_dry_run_preserves_all_214_rows(self) -> None:
        before = TRACE_PATH.read_bytes()
        result = validate_requirement_trace_migration(TRACE_PATH, SCHEMA_PATH)
        self.assertTrue(result.ok, result.messages)
        self.assertIn("rows=214 trace_ids=214 requirement_ids=214", result.messages)
        self.assertEqual(before, TRACE_PATH.read_bytes())

    def test_duplicate_trace_id_fails_dry_run(self) -> None:
        rows = [copy.deepcopy(self.legacy_rows[0]), copy.deepcopy(self.legacy_rows[1])]
        rows[1]["trace_id"] = rows[0]["trace_id"]
        result = self._validate_temp_rows(rows)
        self.assertFalse(result.ok)
        self.assertTrue(any("duplicate trace ID" in message for message in result.messages))

    def test_header_drift_fails_dry_run(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "requirement_trace_registry.csv"
            path.write_text("trace_id,coverage_status\nTRACE-X,covered\n", encoding="utf-8")
            result = validate_requirement_trace_migration(path, SCHEMA_PATH)
        self.assertFalse(result.ok)
        self.assertTrue(any("exact legacy header" in message for message in result.messages))

    def test_extra_csv_value_fails_dry_run(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "requirement_trace_registry.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(LEGACY_HEADER)
                writer.writerow([self.legacy_rows[0][field] for field in LEGACY_HEADER] + ["extra"])
            result = validate_requirement_trace_migration(path, SCHEMA_PATH)
        self.assertFalse(result.ok)
        self.assertTrue(any("unexpected extra CSV values" in message for message in result.messages))

    def _assert_mutation_fails(self, mutate) -> None:
        data = copy.deepcopy(self.generalized)
        mutate(data)
        self.assertNotEqual([], validate_instance(data, self.schema))

    def _validate_temp_rows(self, rows: list[dict[str, str]]):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "requirement_trace_registry.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=LEGACY_HEADER)
                writer.writeheader()
                writer.writerows(rows)
            return validate_requirement_trace_migration(path, SCHEMA_PATH)


if __name__ == "__main__":
    unittest.main()
