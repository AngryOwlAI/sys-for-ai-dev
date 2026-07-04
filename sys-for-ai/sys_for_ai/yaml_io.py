"""Safe YAML helpers for sys-for-ai control records."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class YamlLoadError(RuntimeError):
    """Raised when a YAML file cannot be loaded safely."""


def load_yaml(path: str | Path) -> Any:
    """Load YAML from *path* with yaml.safe_load.

    Empty YAML files return an empty dictionary so validators can produce
    clearer missing-field errors.
    """

    target = Path(path)
    try:
        with target.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        raise YamlLoadError(f"Invalid YAML in {target}: {exc}") from exc
    except OSError as exc:
        raise YamlLoadError(f"Cannot read YAML file {target}: {exc}") from exc

    return {} if data is None else data


def dump_yaml(path: str | Path, data: Any) -> None:
    """Write YAML using safe_dump and stable key order."""

    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True)
