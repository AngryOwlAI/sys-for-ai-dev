"""Source-first memory package for sys-for-ai."""

from __future__ import annotations

from .bootstrap import bootstrap_registries
from .hashing import hash_path, update_hashes, validate_hashes
from .lookup import lookup_memory
from .preflight import run_memory_preflight
from .registry_catalog import MemoryCatalog, build_catalog, memory_status
from .search import search_memory

__all__ = [
    "MemoryCatalog",
    "bootstrap_registries",
    "build_catalog",
    "hash_path",
    "lookup_memory",
    "memory_status",
    "run_memory_preflight",
    "search_memory",
    "update_hashes",
    "validate_hashes",
]
