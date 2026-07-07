"""Memory preflight support."""

from __future__ import annotations

from pathlib import Path

from .lookup import lookup_memory
from .registry_catalog import memory_status
from .receipts import build_memory_preflight_receipt, write_memory_preflight_receipt
from .search import search_memory


DEFAULT_PREFLIGHT_QUERY = "source-first memory continue handoff AgentJob"


def run_memory_preflight(
    *,
    root: str | Path = ".",
    agentjob_id: str | None = None,
    handoff_id: str | None = None,
    queries: list[str] | None = None,
    write_receipt: bool = False,
) -> dict[str, object]:
    """Run a deterministic memory preflight and optionally write a receipt."""

    selected_agentjob_id = agentjob_id or "ADHOC-MEMORY-PREFLIGHT"
    selected_queries = queries or [DEFAULT_PREFLIGHT_QUERY]
    status_payload = memory_status(root)
    commands_run: list[dict[str, str]] = [
        {
            "command": "python -m sys_for_ai.cli memory status --json",
            "result": "pass" if status_payload.get("ok") else "fail",
        }
    ]
    if agentjob_id:
        commands_run.append(
            {
                "command": f"python -m sys_for_ai.cli memory lookup {agentjob_id} --json",
                "result": "pass" if lookup_memory(agentjob_id, root).get("ok") else "warn",
            }
        )
    if handoff_id:
        commands_run.append(
            {
                "command": f"python -m sys_for_ai.cli memory lookup {handoff_id} --json",
                "result": "pass" if lookup_memory(handoff_id, root).get("ok") else "warn",
            }
        )

    query_receipts: list[dict[str, object]] = []
    canonical_sources: list[dict[str, object]] = []
    registry_rows: list[dict[str, object]] = []
    stale_risks: list[dict[str, object]] = []

    for query in selected_queries:
        search_payload = search_memory(query, limit=10, root=root)
        hits = search_payload.get("hits", [])
        hit_ids = [str(hit.get("object_id")) for hit in hits if isinstance(hit, dict)]
        query_receipts.append({"query": query, "returned_object_ids": hit_ids})
        commands_run.append(
            {
                "command": f"python -m sys_for_ai.cli memory search {query!r} --limit 10 --json",
                "result": "pass" if search_payload.get("ok") else "fail",
            }
        )
        for hit in hits if isinstance(hits, list) else []:
            if not isinstance(hit, dict):
                continue
            row = {
                "path": str(hit.get("path", "")),
                "registry": str(hit.get("registry", "")),
                "row_id": str(hit.get("registry_row_id", "")),
            }
            if hit.get("required_next_action") == "inspect_canonical_source" and len(canonical_sources) < 3:
                canonical_sources.append({**row, "inspected_sections": ["registered source metadata"]})
            elif len(registry_rows) < 3:
                registry_rows.append({**row, "purpose": "Confirm memory hit registry evidence."})
            if hit.get("derivative"):
                stale_risks.append(
                    {
                        "risk_id": f"MEMPREFLIGHT-RISK-{len(stale_risks) + 1:03d}",
                        "status": "observed",
                        "notes": f"Derivative hit {hit.get('object_id')} requires source inspection.",
                    }
                )

    if not stale_risks:
        stale_risks.append(
            {
                "risk_id": "MEMPREFLIGHT-RISK-001",
                "status": "not_observed",
                "notes": "No generated derivative was used as source authority.",
            }
        )

    usable = bool(status_payload.get("ok")) and bool(canonical_sources or registry_rows)
    receipt = build_memory_preflight_receipt(
        agentjob_id=selected_agentjob_id,
        queries=query_receipts,
        canonical_sources_inspected=canonical_sources,
        registry_rows_inspected=registry_rows,
        stale_context_risks=stale_risks,
        commands_run=commands_run,
        usable_for_routing=usable,
        status="PASS_WITH_WARNINGS" if usable and status_payload.get("status") != "PASS" else ("PASS" if usable else "FAIL"),
    )
    receipt_path = None
    if write_receipt:
        receipt_path = write_memory_preflight_receipt(receipt, root=root)

    return {
        "ok": usable,
        "status": receipt["status"],
        "receipt": receipt,
        "receipt_path": str(receipt_path) if receipt_path else None,
        "memory_status": status_payload,
    }
