"""TOML helpers for Phase 1 configuration-source validation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover on Python 3.11+
    import tomli as tomllib  # type: ignore[no-redef]


MAX_TOML_BYTES = 1_000_000


class TomlLoadError(RuntimeError):
    """Raised when a TOML file cannot be loaded within Phase 1 limits."""


def load_toml(path: str | Path) -> dict[str, Any]:
    """Load TOML from *path* with a small Phase 1 size limit."""

    target = Path(path)
    try:
        data = target.read_bytes()
    except OSError as exc:
        raise TomlLoadError(f"Cannot read TOML file {target}: {exc}") from exc

    if len(data) > MAX_TOML_BYTES:
        raise TomlLoadError(f"{target}: TOML file exceeds {MAX_TOML_BYTES} byte Phase 1 limit")

    try:
        parsed = tomllib.loads(data.decode("utf-8"))
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as exc:
        raise TomlLoadError(f"Invalid TOML in {target}: {exc}") from exc

    if not isinstance(parsed, dict):
        raise TomlLoadError(f"{target}: expected TOML document to parse to a dictionary")
    return parsed
