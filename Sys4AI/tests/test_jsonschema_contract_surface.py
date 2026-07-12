from __future__ import annotations

import csv
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from sys_for_ai.cli import build_parser
from sys_for_ai.jsonschema_contract_surface import validate_jsonschema_contract_surface


ROOT = Path(__file__).resolve().parents[1]


class JsonSchemaContractSurfaceTests(unittest.TestCase):
    def test_live_jsonschema_contract_surface_passes(self) -> None:
        result = validate_jsonschema_contract_surface(product_root=ROOT)
        self.assertTrue(result.ok, result.messages)
        self.assertTrue(any("10/10" in message for message in result.messages))

    def test_cli_and_make_surfaces_exist(self) -> None:
        args = build_parser().parse_args(["validate-jsonschema-contract-surface"])
        self.assertEqual("validate-jsonschema-contract-surface", args.command)
        self.assertIn("validate-jsonschema-contract-surface:", (ROOT / "Makefile").read_text(encoding="utf-8"))

    def test_jsonschema_profile_assignment_drift_fails(self) -> None:
        with self._mutated_registry(
            "format_profile_registry.csv", "format_id", "fmt_jsonschema_contract", "primary_role", "document"
        ) as path:
            result = validate_jsonschema_contract_surface(format_profiles=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("fmt_jsonschema_contract primary_role" in message for message in result.messages))

    def test_duplicate_contract_id_fails(self) -> None:
        with self._mutated_registry(
            "validation_contract_registry.csv",
            "contract_id",
            "contract_handoff",
            "contract_id",
            "contract_completion_receipt",
        ) as path:
            result = validate_jsonschema_contract_surface(validation_contracts=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("duplicate contract_id" in message for message in result.messages))

    def test_missing_contract_owner_fails(self) -> None:
        with self._mutated_registry(
            "validation_contract_registry.csv", "contract_id", "contract_program_state", "owner", ""
        ) as path:
            result = validate_jsonschema_contract_surface(validation_contracts=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("owner must be populated" in message for message in result.messages))

    def test_declared_dialect_drift_fails(self) -> None:
        with self._mutated_registry(
            "validation_contract_registry.csv", "contract_id", "contract_program_state", "dialect", "draft-07"
        ) as path:
            result = validate_jsonschema_contract_surface(validation_contracts=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("dialect must be '2020-12'" in message for message in result.messages))

    def test_missing_schema_id_fails(self) -> None:
        with self._mutated_schema("program_state.schema.json", lambda schema: schema.pop("$id")) as (root, registry):
            result = validate_jsonschema_contract_surface(
                schemas_root=root,
                validation_contracts=registry,
                product_root=ROOT,
            )
        self.assertFalse(result.ok)
        self.assertTrue(any("$id must be populated" in message for message in result.messages))

    def test_invalid_draft_2020_12_schema_fails(self) -> None:
        with self._mutated_schema(
            "program_state.schema.json", lambda schema: schema.update(type="not-a-json-schema-type")
        ) as (root, registry):
            result = validate_jsonschema_contract_surface(
                schemas_root=root,
                validation_contracts=registry,
                product_root=ROOT,
            )
        self.assertFalse(result.ok)
        self.assertTrue(any("invalid Draft 2020-12 schema" in message for message in result.messages))

    def test_supersession_without_migration_evidence_fails(self) -> None:
        with self._mutated_registry(
            "validation_contract_registry.csv",
            "contract_id",
            "contract_program_state",
            "supersedes",
            "contract_state_snapshot",
        ) as path:
            result = validate_jsonschema_contract_surface(validation_contracts=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("supersession requires migration_evidence" in message for message in result.messages))

    def test_stale_generated_catalog_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            index = Path(temporary) / "index.md"
            by_target = Path(temporary) / "contracts-by-target.md"
            index.write_text("generated reader surface. It is not canonical\nstructural semantic truth\n", encoding="utf-8")
            shutil.copyfile(ROOT / "docs/generated/validation_contracts/contracts-by-target.md", by_target)
            result = validate_jsonschema_contract_surface(
                generated_index=index,
                generated_by_target=by_target,
                product_root=ROOT,
            )
        self.assertFalse(result.ok)
        self.assertTrue(any("stale catalog omits" in message for message in result.messages))

    def test_standalone_json_wiki_registration_fails(self) -> None:
        with self._mutated_registry(
            "derivative_registry.csv",
            "derivative_id",
            "der_validation_contracts_index",
            "derivative_type",
            "json_wiki_page",
        ) as path:
            result = validate_jsonschema_contract_surface(derivatives=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("standalone JSON wiki" in message for message in result.messages))

    @staticmethod
    def _mutated_registry(filename: str, id_field: str, row_id: str, field: str, value: str):
        temporary = tempfile.TemporaryDirectory()
        path = Path(temporary.name) / filename
        with (ROOT / "registries" / filename).open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        for row in rows:
            if row[id_field] == row_id:
                row[field] = value
                break
        else:
            temporary.cleanup()
            raise AssertionError(f"missing fixture row {row_id}")
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

        class TemporaryRegistry:
            def __enter__(self):
                return path

            def __exit__(self, exc_type, exc, traceback):
                temporary.cleanup()

        return TemporaryRegistry()

    @staticmethod
    def _mutated_schema(filename: str, mutation):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name) / "contracts"
        root.mkdir()
        source = ROOT / "schemas/contracts" / filename
        schema = json.loads(source.read_text(encoding="utf-8"))
        mutation(schema)
        target = root / filename
        target.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")

        registry = Path(temporary.name) / "validation_contract_registry.csv"
        with (ROOT / "registries/validation_contract_registry.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        for row in rows:
            if Path(row["path"]).name == filename:
                row["path"] = str(target)
                break
        with registry.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

        class TemporarySchema:
            def __enter__(self):
                return root, registry

            def __exit__(self, exc_type, exc, traceback):
                temporary.cleanup()

        return TemporarySchema()


if __name__ == "__main__":
    unittest.main()
