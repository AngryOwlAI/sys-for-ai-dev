"""Pure governance checks used before any host action."""

from __future__ import annotations

from collections.abc import Mapping
import re
from typing import Any

from ..domain.models import ExecutionTransaction, ValidationIssue, ValidationResult


ARTIFACT_FIELDS = {
    "artifact_id",
    "artifact_type",
    "subject",
    "subject_layer",
    "authority",
    "status",
    "owner",
    "supersedes",
    "source_trace",
}
AUTHORITY_VALUES = {"canonical", "controlled", "reference", "generated", "historical"}
STATUS_VALUES = {
    "draft",
    "proposed",
    "accepted",
    "active",
    "completed",
    "superseded",
}
TRANSACTION_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


def validate_artifact_metadata(metadata: Mapping[str, Any]) -> ValidationResult:
    issues: list[ValidationIssue] = []
    missing = sorted(field for field in ARTIFACT_FIELDS if field not in metadata)
    for field in missing:
        issues.append(ValidationIssue("missing_metadata", f"missing {field}"))
    if metadata.get("authority") not in AUTHORITY_VALUES:
        issues.append(ValidationIssue("authority", "unknown authority value"))
    if metadata.get("status") not in STATUS_VALUES:
        issues.append(ValidationIssue("status", "unknown lifecycle status"))
    if metadata.get("authority") == "generated" and metadata.get("status") == "accepted":
        issues.append(
            ValidationIssue(
                "self_promotion",
                "generated material cannot mark itself accepted",
            )
        )
    return ValidationResult(not issues, tuple(issues))


def authorize_transaction(transaction: ExecutionTransaction) -> ValidationResult:
    issues: list[ValidationIssue] = []
    if not TRANSACTION_ID.fullmatch(transaction.transaction_id):
        issues.append(
            ValidationIssue(
                "transaction_id",
                "transaction ID must be a path-safe identifier of at most 128 characters",
            )
        )
    if not transaction.authorized_by:
        issues.append(ValidationIssue("authorization", "authorization source is required"))
    if not transaction.rollback:
        issues.append(ValidationIssue("rollback", "rollback behavior is required"))
    if not transaction.stop_conditions:
        issues.append(
            ValidationIssue("stop_conditions", "at least one stop condition is required")
        )
    if (
        transaction.material_self_change
        and transaction.actor
        in {transaction.authorized_by, transaction.approval_actor}
    ):
        issues.append(
            ValidationIssue(
                "self_approval",
                "a material self-change requires a separate approving actor",
            )
        )
    for action in transaction.actions:
        if not transaction.permissions.permits(action):
            issues.append(
                ValidationIssue(
                    "permission",
                    f"permission envelope does not allow {action.kind} {action.target}",
                )
            )
    return ValidationResult(not issues, tuple(issues))


def validate_promotion(
    *,
    candidate_actor: str,
    approving_actor: str,
    authority_class: str,
    rollback_release: str | None,
    independent_evidence: bool,
) -> ValidationResult:
    issues: list[ValidationIssue] = []
    if candidate_actor == approving_actor:
        issues.append(
            ValidationIssue("self_promotion", "candidate and approving actor must differ")
        )
    if authority_class == "generated":
        issues.append(
            ValidationIssue(
                "generated_authority",
                "generated output cannot be the promotion authority",
            )
        )
    if not rollback_release:
        issues.append(
            ValidationIssue("rollback", "promotion requires an available rollback release")
        )
    if not independent_evidence:
        issues.append(
            ValidationIssue(
                "independent_evidence",
                "promotion requires independent verification evidence",
            )
        )
    return ValidationResult(not issues, tuple(issues))
