"""Memory receipt helpers."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from ..yaml_io import dump_yaml


def build_memory_preflight_receipt(
    *,
    execution_transaction_id: str,
    queries: list[dict[str, object]],
    canonical_sources_inspected: list[dict[str, object]],
    registry_rows_inspected: list[dict[str, object]],
    stale_context_risks: list[dict[str, object]],
    commands_run: list[dict[str, str]],
    usable_for_routing: bool,
    status: str = "PASS_WITH_WARNINGS",
) -> dict[str, object]:
    """Build a memory preflight receipt object."""

    created_at = _utc_now()
    receipt_id = (
        f"MEMPREFLIGHT-{_slug(execution_transaction_id)}-"
        f"{created_at.replace(':', '').replace('-', '')}"
    )
    return {
        "memory_preflight_receipt_id": receipt_id,
        "schema_version": "1.0.0",
        "execution_profile_id": "portable_execution_transaction_v1",
        "execution_transaction_id": execution_transaction_id,
        "created_at": created_at,
        "status": status,
        "commands_run": commands_run,
        "queries": queries,
        "canonical_sources_inspected": canonical_sources_inspected,
        "registry_rows_inspected": registry_rows_inspected,
        "stale_context_risks": stale_context_risks,
        "usable_for_routing": usable_for_routing,
    }


def write_memory_preflight_receipt(
    receipt: dict[str, object],
    root: str | Path = ".",
) -> Path:
    """Write a memory preflight receipt under control records."""

    receipt_id = str(receipt["memory_preflight_receipt_id"])
    path = Path(root) / "control_records/memory_preflights" / f"{receipt_id}.yaml"
    dump_yaml(path, receipt)
    return path


def receipt_support_status() -> dict[str, object]:
    return {"ok": True, "status": "active"}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _slug(value: str) -> str:
    return "".join(char if char.isalnum() else "-" for char in value.upper()).strip("-")
