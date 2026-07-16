"""Deterministic source search over a target workspace."""

from __future__ import annotations

import re
from pathlib import Path


TEXT_SUFFIXES = {".csv", ".json", ".md", ".toml", ".txt", ".yaml", ".yml"}
SKIP_PARTS = {".git", ".venv", "__pycache__", "cache", "runs"}


def _files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and not any(part in SKIP_PARTS for part in path.parts)
    )


def _metadata(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def _title(text: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def search_sources(
    root: str | Path, query: str, limit: int = 10
) -> list[dict[str, object]]:
    target = Path(root).resolve()
    tokens = [token.casefold() for token in query.split() if token.strip()]
    hits: list[dict[str, object]] = []
    for path in _files(target):
        text = path.read_text(encoding="utf-8", errors="replace")
        haystack = f"{path.relative_to(target)} {text}".casefold()
        score = sum(haystack.count(token) for token in tokens)
        if score == 0:
            continue
        authority = _metadata(text, "authority") or "unknown"
        hits.append(
            {
                "path": path.relative_to(target).as_posix(),
                "artifact_id": _metadata(text, "artifact_id"),
                "title": _title(text),
                "authority": authority,
                "score": score,
                "required_next_action": (
                    "inspect source and accountable authority"
                    if authority in {"generated", "unknown"}
                    else "inspect source before relying on claim"
                ),
            }
        )
    return sorted(hits, key=lambda hit: (-int(hit["score"]), str(hit["path"])))[:limit]


def lookup_source(root: str | Path, query: str) -> dict[str, object] | None:
    target = Path(root).resolve()
    direct = target / query
    if direct.is_file() and target in direct.resolve().parents:
        text = direct.read_text(encoding="utf-8", errors="replace")
        return {
            "path": direct.relative_to(target).as_posix(),
            "artifact_id": _metadata(text, "artifact_id"),
            "title": _title(text),
            "authority": _metadata(text, "authority") or "unknown",
        }
    for path in _files(target):
        text = path.read_text(encoding="utf-8", errors="replace")
        if _metadata(text, "artifact_id") == query:
            return {
                "path": path.relative_to(target).as_posix(),
                "artifact_id": query,
                "title": _title(text),
                "authority": _metadata(text, "authority") or "unknown",
            }
    return None
