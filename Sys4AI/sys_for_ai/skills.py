"""Skill manifest helpers."""

from __future__ import annotations

from pathlib import Path

from .validators import ValidationResult, validate_skill_manifest


def validate_core_skills(manifest_path: str | Path) -> ValidationResult:
    return validate_skill_manifest(manifest_path)
