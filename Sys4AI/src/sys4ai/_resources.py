"""Locate canonical product resources in a source tree or installed wheel."""

from __future__ import annotations

from pathlib import Path


def product_root() -> Path:
    source_root = Path(__file__).resolve().parents[2]
    if (source_root / "contracts").is_dir() and (source_root / "assets").is_dir():
        return source_root
    installed_root = Path(__file__).resolve().parent / "resources"
    if (installed_root / "contracts").is_dir() and (installed_root / "assets").is_dir():
        return installed_root
    raise FileNotFoundError("installed Sys4AI contracts and assets are unavailable")
