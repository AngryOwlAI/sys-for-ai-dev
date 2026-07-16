"""Bounded filesystem workspace adapter."""

from __future__ import annotations

from pathlib import Path


class FilesystemWorkspaceAdapter:
    def __init__(self, root: str | Path) -> None:
        self._root = Path(root).resolve()

    @property
    def root(self) -> Path:
        return self._root

    def resolve(self, relative: str) -> Path:
        candidate = (self._root / relative).resolve()
        if candidate != self._root and self._root not in candidate.parents:
            raise ValueError(f"path escapes workspace: {relative}")
        return candidate

    def read_text(self, relative: str) -> str:
        return self.resolve(relative).read_text(encoding="utf-8")

    def write_text(self, relative: str, content: str) -> Path:
        target = self.resolve(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def ensure_directory(self, relative: str) -> Path:
        target = self.resolve(relative)
        target.mkdir(parents=True, exist_ok=True)
        return target

    def read_bytes(self, relative: str) -> bytes:
        return self.resolve(relative).read_bytes()

    def write_bytes(self, relative: str, content: bytes) -> None:
        target = self.resolve(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
