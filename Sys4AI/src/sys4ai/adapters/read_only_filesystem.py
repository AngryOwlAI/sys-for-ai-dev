"""Conservative host adapter that executes workspace reads only."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Mapping

from ..domain.models import Action
from .filesystem import FilesystemWorkspaceAdapter


class ReadOnlyFilesystemHostAdapter:
    """Execute read actions and return evidence without exposing file content."""

    def __init__(self, root: str | Path) -> None:
        self.workspace = FilesystemWorkspaceAdapter(root)

    def execute(self, action: Action) -> Mapping[str, object]:
        if action.kind != "read":
            raise ValueError("the read-only filesystem host accepts only read actions")
        content = self.workspace.read_bytes(action.target)
        return {
            "kind": action.kind,
            "target": action.target,
            "bytes": len(content),
            "sha256": hashlib.sha256(content).hexdigest(),
            "content_retained": False,
        }
