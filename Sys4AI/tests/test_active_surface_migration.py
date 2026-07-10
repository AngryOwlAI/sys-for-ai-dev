from __future__ import annotations

import csv
from pathlib import Path
import unittest

from sys_for_ai.capability_migration import validate_capability_migration
from sys_for_ai.cli import build_parser
from sys_for_ai.validators import (
    validate_completion_receipts,
    validate_handoffs,
    validate_program_state,
)
from sys_for_ai.yaml_io import load_yaml


PRODUCT_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = PRODUCT_ROOT.parent


def _rows(name: str) -> list[dict[str, str]]:
    with (PRODUCT_ROOT / "registries" / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


class ActiveSurfaceMigrationTests(unittest.TestCase):
    def test_post_tx10_manifest_has_no_stale_active_surface(self) -> None:
        result = validate_capability_migration(
            PRODUCT_ROOT / "configs/capability_migration.toml",
            WORKSPACE_ROOT,
        )
        self.assertTrue(result.ok, result.messages)
        self.assertTrue(
            any(
                "active_surface_tx10: files=0 references=0" in message
                for message in result.messages
            ),
            result.messages,
        )

    def test_current_program_state_emits_portable_fields_only(self) -> None:
        result = validate_program_state(PRODUCT_ROOT / "control_records/program_state.yaml")
        self.assertTrue(result.ok, result.messages)
        state = load_yaml(PRODUCT_ROOT / "control_records/program_state.yaml")
        self.assertIn("active_execution_transaction_id", state)
        self.assertIn("current_state_evidence", state)
        self.assertIn("continuation_state", state)
        self.assertIn("cancellation_state", state)
        self.assertIn("escalation_state", state)
        self.assertNotIn("active_agentjob_id", state)

    def test_current_role_contract_uses_portable_authority_fields(self) -> None:
        role_rows = _rows("role_registry.csv")
        binding_rows = _rows("role_execution_binding_registry.csv")
        self.assertIn("may_create_execution_transactions", role_rows[0])
        self.assertNotIn("may_create_agentjobs", role_rows[0])
        self.assertIn("allowed_transaction_types", binding_rows[0])
        self.assertNotIn("allowed_agentjob_types", binding_rows[0])
        current = next(row for row in role_rows if row["role_id"] == "bounded_execution_planner")
        self.assertEqual("controlled", current["authority_status"])
        historical = next(
            row for row in role_rows if row["role_id"] == "control_loop_agentjob_planner"
        )
        self.assertEqual("superseded", historical["authority_status"])

    def test_historical_registry_rows_are_explicitly_noncurrent(self) -> None:
        rows = _rows("agentjob_registry.csv")
        self.assertTrue(rows)
        self.assertTrue(all(row["execution_profile"] == "legacy_execution_v0_2" for row in rows))
        self.assertTrue(all(row["lifecycle_status"] == "historical" for row in rows))
        self.assertTrue(all(row["authority_status"] == "historical" for row in rows))

    def test_memory_preflight_cli_uses_portable_transaction_selector(self) -> None:
        args = build_parser().parse_args(
            [
                "memory",
                "preflight",
                "--execution-transaction",
                "TX-TEST-MEMORY-PREFLIGHT-001",
            ]
        )
        self.assertEqual(
            "TX-TEST-MEMORY-PREFLIGHT-001",
            args.execution_transaction,
        )

    def test_portable_closeout_and_handoff_validate_with_history_present(self) -> None:
        receipt_result = validate_completion_receipts(PRODUCT_ROOT / "control_records/completions")
        handoff_result = validate_handoffs(PRODUCT_ROOT / "control_records/handoffs")
        self.assertTrue(receipt_result.ok, receipt_result.messages)
        self.assertTrue(handoff_result.ok, handoff_result.messages)
        receipt = load_yaml(
            PRODUCT_ROOT
            / "control_records/completions/RECEIPT-SFADEV-STRATEGIC-BASELINE-TX10-001.yaml"
        )
        handoff = load_yaml(
            PRODUCT_ROOT
            / "control_records/handoffs/HANDOFF-SFADEV-STRATEGIC-BASELINE-TX10-001.yaml"
        )
        self.assertEqual("TX-10-ACTIVE-SURFACE-MIGRATION", receipt["execution_transaction_id"])
        self.assertEqual("TX-11-TRACE-SCHEMA", handoff["next_execution_transaction_id"])


if __name__ == "__main__":
    unittest.main()
