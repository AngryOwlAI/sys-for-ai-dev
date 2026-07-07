from __future__ import annotations

import unittest

from sys_for_ai.memory import run_memory_preflight


class MemoryPreflightTests(unittest.TestCase):
    def test_preflight_returns_receipt(self) -> None:
        payload = run_memory_preflight(agentjob_id="AJ-P1-SKILL-SYNC-001", queries=["source-first memory"])
        self.assertTrue(payload["ok"])
        receipt = payload["receipt"]
        self.assertIsInstance(receipt, dict)
        self.assertEqual(receipt["agentjob_id"], "AJ-P1-SKILL-SYNC-001")
        self.assertTrue(receipt["canonical_sources_inspected"] or receipt["registry_rows_inspected"])


if __name__ == "__main__":
    unittest.main()
