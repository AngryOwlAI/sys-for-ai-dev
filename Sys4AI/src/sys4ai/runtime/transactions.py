"""Validate and record a bounded transaction for host execution."""

from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
from typing import Any, Mapping

import yaml
import jsonschema

from .._resources import product_root
from ..domain.models import (
    Action,
    ExecutionTransaction,
    PermissionEnvelope,
    ValidationIssue,
    ValidationResult,
)
from ..governance.authority import authorize_transaction
from ..ports import ToolExecutionPort


def _validate_contract(value: Mapping[str, Any]) -> ValidationResult:
    schema_path = product_root() / "contracts/schemas/execution-transaction.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors = sorted(
        jsonschema.Draft202012Validator(schema).iter_errors(value),
        key=lambda error: list(error.absolute_path),
    )
    issues = tuple(
        ValidationIssue(
            "transaction_contract",
            error.message,
            "/".join(str(part) for part in error.absolute_path) or None,
        )
        for error in errors
    )
    return ValidationResult(not issues, issues)


def transaction_from_mapping(value: Mapping[str, Any]) -> ExecutionTransaction:
    permission_value = value.get("permissions")
    permission_value = (
        permission_value if isinstance(permission_value, Mapping) else {}
    )
    actions_value = value.get("actions")
    actions_value = actions_value if isinstance(actions_value, list) else []
    actions = tuple(
        Action(
            kind=str(action.get("kind", "")),
            target=str(action.get("target", "")),
            payload=action.get("payload", {})
            if isinstance(action.get("payload", {}), Mapping)
            else {},
        )
        for action in actions_value
        if isinstance(action, Mapping)
    )
    return ExecutionTransaction(
        transaction_id=str(value.get("transaction_id", "")),
        subject=str(value.get("subject", "")),
        actor=str(value.get("actor", "")),
        authorized_by=str(value.get("authorized_by", "")),
        actions=actions,
        permissions=PermissionEnvelope(
            allowed_reads=tuple(permission_value.get("allowed_reads", [])),
            allowed_writes=tuple(permission_value.get("allowed_writes", [])),
            allowed_tools=tuple(permission_value.get("allowed_tools", [])),
            network_allowed=bool(permission_value.get("network_allowed", False)),
            external_writes_allowed=bool(
                permission_value.get("external_writes_allowed", False)
            ),
        ),
        material_self_change=bool(value.get("material_self_change", False)),
        approval_actor=(
            str(value["approval_actor"]) if value.get("approval_actor") else None
        ),
        rollback=str(value.get("rollback", "")),
        stop_conditions=tuple(value.get("stop_conditions", [])),
    )


def process_transaction(
    workspace_root: str | Path,
    value: Mapping[str, Any],
    host: ToolExecutionPort | None = None,
) -> ValidationResult:
    contract_result = _validate_contract(value)
    if not contract_result.ok:
        return contract_result
    transaction = transaction_from_mapping(value)
    result = authorize_transaction(transaction)
    workspace = Path(workspace_root).resolve()
    if not (workspace / ".sys4ai/workspace.yaml").is_file():
        return ValidationResult(
            False,
            result.issues
            + (ValidationIssue("workspace", "workspace is not initialized"),),
        )
    if any(issue.code == "transaction_id" for issue in result.issues):
        return result
    run_root = (
        workspace
        / ".sys4ai"
        / "runs"
        / transaction.transaction_id
    )
    run_root.mkdir(parents=True, exist_ok=True)
    (run_root / "evidence").mkdir(exist_ok=True)
    (run_root / "transaction.yaml").write_text(
        yaml.safe_dump(dict(value), sort_keys=False),
        encoding="utf-8",
    )
    issues = list(result.issues)
    events: list[dict[str, object]] = [
        {
            "event": "authorization-checked",
            "ok": result.ok,
            "executed": False,
        }
    ]
    executed = False
    if result.ok and host is not None and transaction.actions:
        executed = True
        for index, action in enumerate(transaction.actions, start=1):
            try:
                receipt = dict(host.execute(action))
            except Exception as exc:
                issues.append(
                    ValidationIssue(
                        "execution",
                        f"host rejected action {index}: {exc}",
                        action.target,
                    )
                )
                executed = False
                events.append(
                    {"event": "action-failed", "index": index, "target": action.target}
                )
                break
            evidence_path = run_root / "evidence" / f"action-{index:03d}.yaml"
            evidence_path.write_text(
                yaml.safe_dump(receipt, sort_keys=False),
                encoding="utf-8",
            )
            events.append(
                {
                    "event": "action-completed",
                    "index": index,
                    "kind": action.kind,
                    "target": action.target,
                }
            )
    final_result = ValidationResult(
        not issues,
        tuple(issues),
        result.warnings,
        result.evidence,
    )
    payload = {
        "transaction_id": transaction.transaction_id,
        "authorization_valid": result.ok,
        "status": (
            "completed"
            if executed
            else "ready-for-host-execution"
            if final_result.ok
            else "blocked"
        ),
        "executed": executed,
        "issues": [asdict(issue) for issue in final_result.issues],
        "limitation": (
            "The standalone CLI validates and records authorization. "
            "A permitted host adapter must execute declared actions."
        ),
    }
    (run_root / "result.yaml").write_text(
        yaml.safe_dump(payload, sort_keys=False),
        encoding="utf-8",
    )
    events.append(
        {"event": "transaction-closed", "status": payload["status"], "executed": executed}
    )
    (run_root / "events.jsonl").write_text(
        "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
        encoding="utf-8",
    )
    return final_result
