"""Tests for context-45 temp_prd.md archive helpers."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
PRODUCT_ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-07-06-13-14-15"

ARCHIVE_HELPERS = [
    WORKSPACE_ROOT / ".agents/skills/codex-usage-metrics/scripts/archive_temp_prd.py",
    PRODUCT_ROOT / "skills/core/codex-usage-metrics/scripts/archive_temp_prd.py",
]


class TempPrdArchiveTests(unittest.TestCase):
    def test_no_temp_prd_is_noop(self) -> None:
        for script in ARCHIVE_HELPERS:
            with self.subTest(script=script), tempfile.TemporaryDirectory() as temp_dir:
                skill_dir = Path(temp_dir)

                result = _run(script, "--confirm-archive", skill_dir)

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertFalse((skill_dir / "archived_temp_prd").exists())
                self.assertIn("No temp_prd.md found", result.stdout)

    def test_check_is_non_mutating(self) -> None:
        for script in ARCHIVE_HELPERS:
            with self.subTest(script=script), tempfile.TemporaryDirectory() as temp_dir:
                skill_dir = Path(temp_dir)
                temp_prd = skill_dir / "temp_prd.md"
                temp_prd.write_text("checkpoint", encoding="utf-8")

                result = _run(script, "--check", skill_dir)

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual("checkpoint", temp_prd.read_text(encoding="utf-8"))
                self.assertFalse((skill_dir / "archived_temp_prd").exists())
                self.assertIn("Archive target if confirmed", result.stdout)

    def test_confirm_archive_moves_to_timestamped_target(self) -> None:
        for script in ARCHIVE_HELPERS:
            with self.subTest(script=script), tempfile.TemporaryDirectory() as temp_dir:
                skill_dir = Path(temp_dir)
                temp_prd = skill_dir / "temp_prd.md"
                temp_prd.write_text("checkpoint", encoding="utf-8")
                target = (
                    skill_dir
                    / "archived_temp_prd"
                    / f"temp_prd_date_{TIMESTAMP}.md"
                )

                result = _run(script, "--confirm-archive", skill_dir, TIMESTAMP)

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertFalse(temp_prd.exists())
                self.assertEqual("checkpoint", target.read_text(encoding="utf-8"))
                self.assertIn("Archived temp_prd.md", result.stdout)

    def test_archive_collision_fails_without_moving_source(self) -> None:
        for script in ARCHIVE_HELPERS:
            with self.subTest(script=script), tempfile.TemporaryDirectory() as temp_dir:
                skill_dir = Path(temp_dir)
                temp_prd = skill_dir / "temp_prd.md"
                temp_prd.write_text("new checkpoint", encoding="utf-8")
                archive_dir = skill_dir / "archived_temp_prd"
                archive_dir.mkdir()
                target = archive_dir / f"temp_prd_date_{TIMESTAMP}.md"
                target.write_text("old checkpoint", encoding="utf-8")

                result = _run(script, "--confirm-archive", skill_dir, TIMESTAMP)

                self.assertNotEqual(result.returncode, 0)
                self.assertEqual("new checkpoint", temp_prd.read_text(encoding="utf-8"))
                self.assertEqual("old checkpoint", target.read_text(encoding="utf-8"))
                self.assertIn("archive target already exists", result.stderr)

    def test_non_file_temp_prd_fails_safely(self) -> None:
        for script in ARCHIVE_HELPERS:
            with self.subTest(script=script), tempfile.TemporaryDirectory() as temp_dir:
                skill_dir = Path(temp_dir)
                temp_prd = skill_dir / "temp_prd.md"
                temp_prd.mkdir()

                result = _run(script, "--confirm-archive", skill_dir)

                self.assertNotEqual(result.returncode, 0)
                self.assertTrue(temp_prd.is_dir())
                self.assertFalse((skill_dir / "archived_temp_prd").exists())
                self.assertIn("not a regular file", result.stderr)

    @unittest.skipIf(not hasattr(os, "symlink"), "os.symlink unavailable")
    def test_symlink_temp_prd_fails_safely(self) -> None:
        for script in ARCHIVE_HELPERS:
            with self.subTest(script=script), tempfile.TemporaryDirectory() as temp_dir:
                skill_dir = Path(temp_dir)
                target = skill_dir / "real.md"
                target.write_text("checkpoint", encoding="utf-8")
                temp_prd = skill_dir / "temp_prd.md"
                os.symlink(target, temp_prd)

                result = _run(script, "--confirm-archive", skill_dir)

                self.assertNotEqual(result.returncode, 0)
                self.assertTrue(temp_prd.is_symlink())
                self.assertTrue(target.exists())
                self.assertFalse((skill_dir / "archived_temp_prd").exists())
                self.assertIn("not a regular file", result.stderr)


def _run(
    script: Path,
    action: str,
    skill_dir: Path,
    timestamp: str | None = None,
) -> subprocess.CompletedProcess[str]:
    command = [
        sys.executable,
        str(script),
        action,
        "--skill-dir",
        str(skill_dir),
    ]
    if timestamp:
        command.extend(["--timestamp", timestamp])
    return subprocess.run(command, text=True, capture_output=True, check=False)


if __name__ == "__main__":
    unittest.main()
