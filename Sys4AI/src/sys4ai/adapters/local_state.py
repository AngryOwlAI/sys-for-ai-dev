"""YAML-backed local runtime state outside the installed package."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml


class LocalStateAdapter:
    def __init__(self, state_root: str | Path) -> None:
        self.root = Path(state_root).resolve()

    def _path(self, key: str) -> Path:
        if not key or "/" in key or "\\" in key:
            raise ValueError("state key must be a simple identifier")
        candidate = (self.root / f"{key}.yaml").resolve()
        if self.root not in candidate.parents:
            raise ValueError("state path escapes the configured state root")
        return candidate

    def load(self, key: str) -> Mapping[str, Any] | None:
        path = self._path(key)
        if not path.exists():
            return None
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(value, Mapping):
            raise ValueError(f"{path}: state must be a mapping")
        return value

    def save(self, key: str, value: Mapping[str, Any]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        self._path(key).write_text(
            yaml.safe_dump(dict(value), sort_keys=False),
            encoding="utf-8",
        )
