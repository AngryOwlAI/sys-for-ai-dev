"""Safe YAML artifact serialization adapter."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

import yaml


class YAMLArtifactAdapter:
    def load(self, path: str | Path) -> Mapping[str, Any]:
        source = Path(path)
        value = yaml.safe_load(source.read_text(encoding="utf-8"))
        if not isinstance(value, Mapping):
            raise ValueError(f"{source}: expected a mapping")
        return value

    def dump(self, path: str | Path, value: Mapping[str, Any]) -> None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump(dict(value), sort_keys=False), encoding="utf-8")
