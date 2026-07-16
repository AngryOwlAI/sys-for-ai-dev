from __future__ import annotations

import csv
from pathlib import Path

from sys4ai.application.services import (
    ArchitectureService,
    DiscoveryService,
    ExecutionService,
    OperationsService,
    PlanningService,
    SpecificationService,
    TargetFactory,
    VerificationService,
)
from sys4ai.adapters.read_only_filesystem import ReadOnlyFilesystemHostAdapter
from sys4ai.domain.models import SystemDefinition


def _definition() -> SystemDefinition:
    return SystemDefinition(
        "repo-steward",
        "Repository Steward",
        "Propose bounded repository maintenance",
        "agentic-system",
    )


def test_full_target_lifecycle_is_structurally_verifiable(tmp_path: Path) -> None:
    target = tmp_path / "target"
    TargetFactory().generate(_definition(), target)
    DiscoveryService().record(target, "Clarify repository maintenance boundaries")
    SpecificationService().create(target)
    ArchitectureService().create(target)
    PlanningService().create(target)
    OperationsService().create(target)

    result = VerificationService().verify(target)
    assert result.ok
    assert result.warnings
    assert (target / ".sys4ai/workspace.yaml").is_file()
    assert (target / ".gitignore").read_text(encoding="utf-8").startswith(".sys4ai/")


def test_valid_transaction_is_recorded_but_not_executed(tmp_path: Path) -> None:
    target = TargetFactory().generate(_definition(), tmp_path / "target")
    transaction = {
        "transaction_id": "read-only-001",
        "subject": "repo-steward",
        "actor": "reference-runtime",
        "authorized_by": "target-owner",
        "actions": [
            {"kind": "read", "target": "requirements/product-requirements.md"}
        ],
        "permissions": {
            "allowed_reads": ["requirements"],
            "allowed_writes": [],
            "allowed_tools": [],
            "network_allowed": False,
            "external_writes_allowed": False,
        },
        "rollback": "read-only transaction",
        "stop_conditions": ["stop on permission mismatch"],
    }
    result = ExecutionService().process(target, transaction)
    run = target / ".sys4ai/runs/read-only-001"
    assert result.ok
    assert (run / "transaction.yaml").is_file()
    assert (run / "events.jsonl").is_file()
    assert (run / "evidence").is_dir()
    assert "executed: false" in (run / "result.yaml").read_text(encoding="utf-8")


def test_read_only_host_executes_permitted_action_with_bounded_evidence(
    tmp_path: Path,
) -> None:
    target = TargetFactory().generate(_definition(), tmp_path / "target")
    transaction = {
        "transaction_id": "bounded-read-001",
        "subject": "repo-steward",
        "actor": "reference-runtime",
        "authorized_by": "target-owner",
        "actions": [
            {"kind": "read", "target": "requirements/product-requirements.md"}
        ],
        "permissions": {
            "allowed_reads": ["requirements"],
            "allowed_writes": [],
            "allowed_tools": [],
            "network_allowed": False,
            "external_writes_allowed": False,
        },
        "rollback": "read-only transaction",
        "stop_conditions": ["stop on permission mismatch"],
    }
    result = ExecutionService().process(
        target,
        transaction,
        ReadOnlyFilesystemHostAdapter(target),
    )
    run = target / ".sys4ai/runs/bounded-read-001"
    assert result.ok
    assert "executed: true" in (run / "result.yaml").read_text(encoding="utf-8")
    evidence = (run / "evidence/action-001.yaml").read_text(encoding="utf-8")
    assert "sha256:" in evidence
    assert "content_retained: false" in evidence


def test_unsafe_transaction_identifier_cannot_escape_workspace(tmp_path: Path) -> None:
    target = TargetFactory().generate(_definition(), tmp_path / "target")
    result = ExecutionService().process(
        target,
        {
            "transaction_id": "../escape",
            "subject": "repo-steward",
            "actor": "runtime",
            "authorized_by": "owner",
            "actions": [],
            "permissions": {},
            "rollback": "none required",
            "stop_conditions": ["stop"],
        },
    )
    assert not result.ok
    assert not (target / ".sys4ai/runs/escape").exists()
    assert not (target / ".sys4ai/escape").exists()


def test_trace_rejects_parent_path_escape(tmp_path: Path) -> None:
    target = TargetFactory().generate(_definition(), tmp_path / "target")
    outside = tmp_path / "outside.md"
    outside.write_text("outside", encoding="utf-8")
    trace = target / "requirements/trace.csv"
    with trace.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("requirement_id", "artifact", "verification", "status"))
        writer.writerow(("REQ-001", "../../outside.md", "inspection", "candidate"))
    result = VerificationService().verify(target)
    assert not result.ok
    assert "trace_artifact" in {issue.code for issue in result.issues}
