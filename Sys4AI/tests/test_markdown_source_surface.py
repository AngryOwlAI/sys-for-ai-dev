from __future__ import annotations

import csv
from pathlib import Path
import tempfile
import unittest

from sys_for_ai.cli import build_parser
from sys_for_ai.markdown_source_surface import validate_markdown_source_surface


ROOT = Path(__file__).resolve().parents[1]


class MarkdownSourceSurfaceTests(unittest.TestCase):
    def test_live_markdown_source_surface_passes(self) -> None:
        result = validate_markdown_source_surface(product_root=ROOT)
        self.assertTrue(result.ok, result.messages)
        self.assertTrue(any("4/4" in message for message in result.messages))

    def test_cli_and_make_surfaces_exist(self) -> None:
        args = build_parser().parse_args(["validate-markdown-source-surface"])
        self.assertEqual("validate-markdown-source-surface", args.command)
        self.assertIn("validate-markdown-source-surface:", (ROOT / "Makefile").read_text(encoding="utf-8"))

    def test_missing_markdown_authority_fails(self) -> None:
        registry = self._mutated_registry(
            "source_registry.csv",
            "source_id",
            "SRC-SYSTEM-DOCUMENT-SPINE",
            "authority_status",
            "",
        )
        with registry as path:
            result = validate_markdown_source_surface(sources=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("invalid or missing Markdown authority" in message for message in result.messages))

    def test_missing_representative_requirements_artifact_fails(self) -> None:
        registry = self._mutated_registry(
            "source_registry.csv",
            "source_id",
            "SRC-RDR-STRATEGIC-BASELINE-001",
            "source_id",
            "SRC-RDR-RENAMED",
        )
        with registry as path:
            result = validate_markdown_source_surface(sources=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("requirements artifact" in message for message in result.messages))

    def test_generated_markdown_canonical_status_fails(self) -> None:
        registry = self._mutated_registry(
            "derivative_registry.csv",
            "derivative_id",
            "der_configuration_control_index",
            "status",
            "canonical",
        )
        with registry as path:
            result = validate_markdown_source_surface(derivatives=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("invalid authority 'canonical'" in message for message in result.messages))

    def test_generated_markdown_missing_source_trace_fails(self) -> None:
        registry = self._mutated_registry(
            "derivative_registry.csv",
            "derivative_id",
            "der_configuration_control_index",
            "source_ids",
            "",
        )
        with registry as path:
            result = validate_markdown_source_surface(derivatives=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("lacks source trace" in message for message in result.messages))

    def test_generated_markdown_source_authority_inversion_fails(self) -> None:
        registry = self._mutated_registry(
            "source_registry.csv",
            "source_id",
            "SRC-SYSTEM-DOCUMENT-SPINE",
            "path",
            "docs/generated/configuration_control/index.md",
        )
        with registry as path:
            result = validate_markdown_source_surface(sources=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("cannot be registered as source authority" in message for message in result.messages))

    def test_unregistered_generated_markdown_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            generated_root = Path(temporary) / "generated"
            generated_root.mkdir()
            (generated_root / "orphan.md").write_text("# Unregistered derivative\n", encoding="utf-8")
            result = validate_markdown_source_surface(
                generated_root=generated_root,
                product_root=ROOT,
            )
        self.assertFalse(result.ok)
        self.assertTrue(any("unregistered generated Markdown" in message for message in result.messages))

    def test_csv_role_assignment_drift_fails(self) -> None:
        registry = self._mutated_registry(
            "format_profile_registry.csv",
            "format_id",
            "fmt_csv_registry",
            "primary_role",
            "document",
        )
        with registry as path:
            result = validate_markdown_source_surface(format_profiles=path, product_root=ROOT)
        self.assertFalse(result.ok)
        self.assertTrue(any("fmt_csv_registry primary_role" in message for message in result.messages))

    @staticmethod
    def _mutated_registry(
        filename: str,
        id_field: str,
        row_id: str,
        field: str,
        value: str,
    ):
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


if __name__ == "__main__":
    unittest.main()
