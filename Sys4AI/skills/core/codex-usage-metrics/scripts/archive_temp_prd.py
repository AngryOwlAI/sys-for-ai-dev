#!/usr/bin/env python3
"""Check or archive a context-45 temp_prd.md file."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


TIMESTAMP_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}$")


class ArchiveError(ValueError):
    """Raised when the archive operation cannot proceed safely."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check for or archive a context-45 temp_prd.md checkpoint."
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument(
        "--check",
        action="store_true",
        help="Report whether temp_prd.md exists without moving it.",
    )
    action.add_argument(
        "--confirm-archive",
        action="store_true",
        help="Move temp_prd.md into archived_temp_prd/ with a timestamped name.",
    )
    parser.add_argument(
        "--skill-dir",
        type=Path,
        required=True,
        help="Path to the context-45 skill directory containing temp_prd.md.",
    )
    parser.add_argument(
        "--timestamp",
        help="Optional deterministic timestamp in yyyy-mm-dd-hh-mm-ss format.",
    )
    return parser.parse_args()


def archive_timestamp(value: str | None) -> str:
    if value is None:
        return datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")
    if not TIMESTAMP_RE.fullmatch(value):
        raise ArchiveError("timestamp must use yyyy-mm-dd-hh-mm-ss format")
    return value


def validate_skill_dir(skill_dir: Path) -> Path:
    resolved = skill_dir.expanduser().resolve()
    if not resolved.exists():
        raise ArchiveError(f"skill directory not found: {resolved}")
    if resolved.is_symlink() or not resolved.is_dir():
        raise ArchiveError(f"skill directory is not a real directory: {resolved}")
    return resolved


def validate_temp_prd(temp_prd: Path) -> bool:
    if not temp_prd.exists():
        return False
    if temp_prd.is_symlink() or not temp_prd.is_file():
        raise ArchiveError(f"temp_prd.md is not a regular file: {temp_prd}")
    return True


def archive_target(skill_dir: Path, timestamp: str) -> Path:
    return skill_dir / "archived_temp_prd" / f"temp_prd_date_{timestamp}.md"


def check(skill_dir: Path, timestamp: str) -> int:
    temp_prd = skill_dir / "temp_prd.md"
    target = archive_target(skill_dir, timestamp)
    if not validate_temp_prd(temp_prd):
        print(f"No temp_prd.md found: {temp_prd}")
        return 0
    print(f"temp_prd.md found: {temp_prd}")
    print(f"Archive target if confirmed: {target}")
    return 0


def confirm_archive(skill_dir: Path, timestamp: str) -> int:
    temp_prd = skill_dir / "temp_prd.md"
    if not validate_temp_prd(temp_prd):
        print(f"No temp_prd.md found: {temp_prd}")
        return 0

    archive_dir = skill_dir / "archived_temp_prd"
    if archive_dir.exists() and (archive_dir.is_symlink() or not archive_dir.is_dir()):
        raise ArchiveError(f"archive directory is not a real directory: {archive_dir}")

    target = archive_target(skill_dir, timestamp)
    if target.exists():
        raise ArchiveError(f"archive target already exists: {target}")

    archive_dir.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise ArchiveError(f"archive target already exists: {target}")

    temp_prd.rename(target)
    print(f"Archived temp_prd.md: {temp_prd} -> {target}")
    return 0


def main() -> int:
    args = parse_args()
    try:
        skill_dir = validate_skill_dir(args.skill_dir)
        timestamp = archive_timestamp(args.timestamp)
        if args.check:
            return check(skill_dir, timestamp)
        return confirm_archive(skill_dir, timestamp)
    except ArchiveError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
