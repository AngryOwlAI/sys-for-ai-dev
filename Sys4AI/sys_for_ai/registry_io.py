"""CSV registry helpers for the source-first Phase 1 scaffold."""

from __future__ import annotations

import csv
from pathlib import Path


class RegistryLoadError(RuntimeError):
    """Raised when a registry cannot be read."""


def read_registry(path: str | Path) -> tuple[list[str], list[dict[str, str]]]:
    """Read a CSV registry and return its header plus row dictionaries."""

    target = Path(path)
    try:
        with target.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            header = list(reader.fieldnames or [])
            rows = [{key: value or "" for key, value in row.items()} for row in reader]
    except OSError as exc:
        raise RegistryLoadError(f"Cannot read registry {target}: {exc}") from exc
    return header, rows


def read_registry_rows(path: str | Path) -> list[dict[str, str]]:
    """Read rows from a CSV registry."""

    return read_registry(path)[1]


def rows_by_id(rows: list[dict[str, str]], id_field: str) -> dict[str, dict[str, str]]:
    """Index registry rows by *id_field*."""

    return {row.get(id_field, ""): row for row in rows if row.get(id_field)}


def resolve_registered_path(path: str, base_dir: str | Path = ".") -> Path:
    """Resolve paths written from either workspace-root or product-root context."""

    candidate = Path(path)
    if candidate.is_absolute():
        return candidate

    base = Path(base_dir).resolve()
    candidates = [base / candidate, base.parent / candidate]

    parts = candidate.parts
    if parts and parts[0] == base.name:
        candidates.insert(0, base / Path(*parts[1:]))

    if parts and parts[0] in {"PRDs", "implementation_plans"}:
        candidates.insert(0, base.parent / candidate)

    for item in candidates:
        if item.exists():
            return item
    return candidates[0]
