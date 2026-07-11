from __future__ import annotations

import csv
from pathlib import Path
import shutil
import tempfile
import unittest

from sys_for_ai.cli import build_parser
from sys_for_ai.yaml_control_surface import validate_yaml_control_surface


ROOT = Path(__file__).resolve().parents[1]


class YamlControlSurfaceTests(unittest.TestCase):
    def test_live_yaml_control_surface_passes(self) -> None:
        result = validate_yaml_control_surface()
        self.assertTrue(result.ok, result.messages)
        self.assertTrue(any("11/11" in message for message in result.messages))

    def test_cli_and_make_surfaces_exist(self) -> None:
        args = build_parser().parse_args(["validate-yaml-control-surface"])
        self.assertEqual("validate-yaml-control-surface", args.command)
        self.assertIn("validate-yaml-control-surface:", (ROOT / "Makefile").read_text(encoding="utf-8"))

    def test_missing_validation_contract_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = self._fixture(Path(temporary))
            rows = self._read_rows(root / "registries/control_record_registry.csv")
            rows[0]["validation_contract_id"] = ""
            self._write_rows(root / "registries/control_record_registry.csv", rows)
            result = self._validate(root)
        self.assertFalse(result.ok)
        self.assertTrue(any("validation_contract_id must be populated" in message for message in result.messages))

    def test_missing_required_record_family_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = self._fixture(Path(temporary))
            rows = [
                row
                for row in self._read_rows(root / "registries/control_record_registry.csv")
                if row["record_type"] != "execution_transaction"
            ]
            self._write_rows(root / "registries/control_record_registry.csv", rows)
            result = self._validate(root)
        self.assertFalse(result.ok)
        self.assertTrue(any("bounded transactions" in message for message in result.messages))

    def test_unsafe_loader_call_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = self._fixture(Path(temporary))
            (root / "sys_for_ai/unsafe_fixture.py").write_text(
                "import yaml\nvalue = yaml.load('x')\n",
                encoding="utf-8",
            )
            result = self._validate(root)
        self.assertFalse(result.ok)
        self.assertTrue(any("unsafe yaml.load" in message for message in result.messages))

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
    def _fixture(root: Path) -> Path:
        shutil.copytree(ROOT / "sys_for_ai", root / "sys_for_ai")
        shutil.copytree(ROOT / "control_records", root / "control_records")
        (root / "registries").mkdir()
        for name in (
            "format_profile_registry.csv",
            "control_record_registry.csv",
            "validation_contract_registry.csv",
        ):
            shutil.copy2(ROOT / "registries" / name, root / "registries" / name)
        shutil.copytree(ROOT / "schemas", root / "schemas")
        (root / "docs").mkdir()
        shutil.copy2(
            ROOT / "docs/configuration_control_wiki_policy.md",
            root / "docs/configuration_control_wiki_policy.md",
        )
        shutil.copy2(ROOT / "pyproject.toml", root / "pyproject.toml")
        return root

    @staticmethod
    def _validate(root: Path):
        return validate_yaml_control_surface(
            root / "pyproject.toml",
            root / "registries/format_profile_registry.csv",
            root / "registries/control_record_registry.csv",
            root / "docs/configuration_control_wiki_policy.md",
            root / "sys_for_ai",
        )


if __name__ == "__main__":
    unittest.main()
