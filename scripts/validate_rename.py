#!/usr/bin/env python3
"""Validate Sys4AI naming migration boundaries."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


LEGACY_TERMS = (
    "sys" + "-for-ai-dev",
    "sys" + "-for-ai",
)

ALLOWED_CONTENT_PATHS = {
    "Sys4AI/control_records/completions/RECEIPT-SYS4AI-DEV-NAME-MIGRATION-001.yaml",
}


def main() -> int:
    root = _git_root()
    tracked_paths = _tracked_paths(root)
    errors: list[str] = []

    for path in tracked_paths:
        for term in LEGACY_TERMS:
            if term in path:
                errors.append(f"legacy name in tracked path: {path}")

    for path in tracked_paths:
        if path in ALLOWED_CONTENT_PATHS:
            continue
        full_path = root / path
        if not full_path.is_file():
            continue
        try:
            text = full_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for term in LEGACY_TERMS:
                if term in line:
                    errors.append(f"{path}:{line_number}: legacy name {term!r}")

    if errors:
        print("Sys4AI rename audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Sys4AI rename audit passed")
    return 0


def _git_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        text=True,
        capture_output=True,
    )
    return Path(result.stdout.strip())


def _tracked_paths(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


if __name__ == "__main__":
    raise SystemExit(main())
