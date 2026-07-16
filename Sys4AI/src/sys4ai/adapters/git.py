"""Read-only Git workspace observations for verification and planning."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Mapping


class GitWorkspaceAdapter:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root).resolve()

    def _run(self, *arguments: str) -> str:
        result = subprocess.run(
            ["git", *arguments],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip() or "Git command failed")
        return result.stdout

    def status(self) -> Mapping[str, object]:
        return {
            "root": str(self.root),
            "porcelain": self._run("status", "--short"),
            "head": self._run("rev-parse", "HEAD").strip(),
        }

    def diff(self) -> str:
        return self._run("diff", "--")
