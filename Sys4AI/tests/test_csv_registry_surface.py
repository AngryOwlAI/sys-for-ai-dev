from __future__ import annotations

import csv
from pathlib import Path
import shutil
import tempfile
import unittest

from sys_for_ai.cli import build_parser
from sys_for_ai.csv_registry_surface import validate_csv_registry_surface
from sys_for_ai.registry_io import RegistryLoadError, read_registry


ROOT = Path(__file__).resolve().parents[1]


class CsvRegistrySurfaceTests(unittest.TestCase):
    def test_live_csv_registry_surface_passes(self) -> None:
        result = validate_csv_registry_surface()
        self.assertTrue(result.ok, result.messages)
        self.assertTrue(any("5/5" in message for message in result.messages))

    def test_cli_and_make_surfaces_exist(self) -> None:
        args = build_parser().parse_args(["validate-csv-registry-surface"])
        self.assertEqual("validate-csv-registry-surface", args.command)
        self.assertIn("validate-csv-registry-surface:", (ROOT / "Makefile").read_text(encoding="utf-8"))

    def test_malformed_csv_row_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "malformed.csv"
            path.write_text("row_id,value\none,valid,extra\n", encoding="utf-8")
            with self.assertRaisesRegex(RegistryLoadError, "more fields than its header"):
                read_registry(path)

    def test_duplicate_stable_row_id_fails(self) -> None:
        with self._registry_copy() as root:
            path = root / "source_registry.csv"
            rows = self._read_rows(path)
            rows[-1]["source_id"] = rows[-2]["source_id"]
            self._write_rows(path, rows)
            result = validate_csv_registry_surface(root, root / "registry_definition_registry.csv")
        self.assertFalse(result.ok)
        self.assertTrue(any("duplicate source_id" in message for message in result.messages))

    def test_unregistered_project_specific_registry_fails(self) -> None:
        with self._registry_copy() as root:
            (root / "project_observation_registry.csv").write_text(
                "observation_id,value\nOBS-001,example\n",
                encoding="utf-8",
            )
            result = validate_csv_registry_surface(root, root / "registry_definition_registry.csv")
        self.assertFalse(result.ok)
        self.assertTrue(any("registries without governed definitions" in message for message in result.messages))

    def test_orphan_derivative_source_reference_fails(self) -> None:
        with self._registry_copy() as root:
            path = root / "derivative_registry.csv"
            rows = self._read_rows(path)
            rows[0]["source_ids"] = "SRC-DOES-NOT-EXIST"
            self._write_rows(path, rows)
            result = validate_csv_registry_surface(root, root / "registry_definition_registry.csv")
        self.assertFalse(result.ok)
        self.assertTrue(any("orphan derivative" in message for message in result.messages))

    def test_missing_validation_contract_fails(self) -> None:
        with self._registry_copy() as root:
            path = root / "config_source_registry.csv"
            rows = self._read_rows(path)
            rows[0]["validation_contract_id"] = "contract_missing"
            self._write_rows(path, rows)
            result = validate_csv_registry_surface(root, root / "registry_definition_registry.csv")
        self.assertFalse(result.ok)
        self.assertTrue(any("missing contract" in message for message in result.messages))

    def test_stale_populated_hash_fails(self) -> None:
        with self._registry_copy() as root:
            path = root / "registry_definition_registry.csv"
            rows = self._read_rows(path)
            rows[0]["source_hash"] = "0" * 64
            self._write_rows(path, rows)
            result = validate_csv_registry_surface(root, path)
        self.assertFalse(result.ok)
        self.assertTrue(any("stale populated source_hash" in message for message in result.messages))

    def test_invalid_registry_authority_class_fails(self) -> None:
        with self._registry_copy() as root:
            path = root / "registry_definition_registry.csv"
            rows = self._read_rows(path)
            rows[0]["authority_status"] = "canonical"
            self._write_rows(path, rows)
            result = validate_csv_registry_surface(root, path)
        self.assertFalse(result.ok)
        self.assertTrue(any("invalid registry authority class" in message for message in result.messages))

    @staticmethod
    def _read_rows(path: Path) -> list[dict[str, str]]:
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))

    @staticmethod
    def _write_rows(path: Path, rows: list[dict[str, str]]) -> None:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def _registry_copy():
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name) / "registries"
        shutil.copytree(ROOT / "registries", root)

        class RegistryCopy:
            def __enter__(self):
                return root

            def __exit__(self, exc_type, exc, traceback):
                temporary.cleanup()

        return RegistryCopy()


if __name__ == "__main__":
    unittest.main()
