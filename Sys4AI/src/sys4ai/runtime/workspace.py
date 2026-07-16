"""Create and inspect target workspaces."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml

from ..adapters.filesystem import FilesystemWorkspaceAdapter
from ..domain.models import SystemDefinition


WORKSPACE_DIRECTORIES = (
    ".sys4ai/catalog",
    ".sys4ai/runs",
    ".sys4ai/generated",
    ".sys4ai/cache",
    "governance/decisions",
    "requirements",
    "architecture",
    "runtime/src",
    "runtime/config",
    "runtime/adapters",
    "skills",
    "contracts",
    "tests",
    "operations",
    "evidence",
)


def initialize_workspace(
    root: str | Path,
    definition: SystemDefinition,
    *,
    allow_existing: bool = False,
) -> Path:
    target = Path(root).resolve()
    if target.exists() and any(target.iterdir()) and not allow_existing:
        raise FileExistsError(f"workspace is not empty: {target}")
    target.mkdir(parents=True, exist_ok=True)
    workspace = FilesystemWorkspaceAdapter(target)
    for directory in WORKSPACE_DIRECTORIES:
        workspace.ensure_directory(directory)
    payload = {
        "schema_version": "1.0.0",
        "system_id": definition.system_id,
        "name": definition.name,
        "intent": definition.intent,
        "target_kind": definition.target_kind,
        "coordination_pattern": definition.coordination_pattern,
        "operational_maturity": definition.operational_maturity,
        "authority": "derivative",
        "approval": "unreviewed",
        "validation": "not-run",
    }
    workspace.write_text(
        ".sys4ai/workspace.yaml",
        yaml.safe_dump(payload, sort_keys=False),
    )
    return target


def load_workspace(root: str | Path) -> Mapping[str, Any]:
    path = Path(root).resolve() / ".sys4ai/workspace.yaml"
    if not path.exists():
        raise FileNotFoundError(f"workspace state missing: {path}")
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"{path}: workspace state must be a mapping")
    return value
