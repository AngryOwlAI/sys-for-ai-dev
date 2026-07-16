from __future__ import annotations

from contextlib import redirect_stdout
import io
import json
import tempfile
import unittest
from pathlib import Path

from sfadev.cli import _status
from sfadev.validation import validate_product_boundary


class ProductBoundaryTests(unittest.TestCase):
    def test_forbidden_parent_reference_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            product = root / "Sys4AI"
            product.mkdir()
            (product / "example.py").write_text(
                'SOURCE = "../PRDs/product.md"\n', encoding="utf-8"
            )
            findings = validate_product_boundary(root)
            self.assertTrue(
                any("../PRDs" in finding.message for finding in findings)
            )

    def test_clean_minimal_product_has_no_text_findings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            product = root / "Sys4AI"
            product.mkdir()
            (product / "example.py").write_text("VALUE = 1\n", encoding="utf-8")
            findings = validate_product_boundary(root)
            self.assertEqual(findings, [])


class StatusTests(unittest.TestCase):
    def test_json_status_preserves_yaml_types(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "development/state"
            state.mkdir(parents=True)
            (state / "current-work.yaml").write_text(
                "active_work_item: null\n"
                "current_blockers: []\n"
                "updated_at: 2026-07-16\n",
                encoding="utf-8",
            )
            output = io.StringIO()
            with redirect_stdout(output):
                result = _status(root, as_json=True)
            payload = json.loads(output.getvalue())
            self.assertEqual(result, 0)
            self.assertIsNone(payload["active_work_item"])
            self.assertEqual(payload["current_blockers"], [])
            self.assertEqual(payload["updated_at"], "2026-07-16")


if __name__ == "__main__":
    unittest.main()
