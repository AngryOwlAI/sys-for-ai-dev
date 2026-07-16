from __future__ import annotations

import pytest

from sys4ai.domain.models import (
    Action,
    ExecutionTransaction,
    PermissionEnvelope,
    SystemDefinition,
)
from sys4ai.governance.authority import (
    authorize_transaction,
    validate_artifact_metadata,
    validate_promotion,
)


def test_system_definition_rejects_unsafe_identifier() -> None:
    with pytest.raises(ValueError):
        SystemDefinition("unsafe id", "Unsafe", "Demonstrate rejection", "agent")
    with pytest.raises(ValueError):
        SystemDefinition("../unsafe", "Unsafe", "Demonstrate rejection", "agent")


def test_permission_envelope_is_fail_closed() -> None:
    envelope = PermissionEnvelope(allowed_reads=("requirements",))
    assert envelope.permits(Action("read", "requirements/product.md"))
    assert not envelope.permits(Action("write", "requirements/product.md"))
    assert not envelope.permits(Action("unknown", "requirements"))


def test_material_self_change_cannot_self_approve() -> None:
    transaction = ExecutionTransaction(
        transaction_id="self-change-001",
        subject="framework",
        actor="candidate-runtime",
        authorized_by="candidate-runtime",
        approval_actor="candidate-runtime",
        material_self_change=True,
        actions=(),
        permissions=PermissionEnvelope(),
        rollback="retain trusted release",
        stop_conditions=("stop on failed verification",),
    )
    result = authorize_transaction(transaction)
    assert not result.ok
    assert "self_approval" in {issue.code for issue in result.issues}


def test_generated_artifact_cannot_mark_itself_accepted() -> None:
    result = validate_artifact_metadata(
        {
            "artifact_id": "candidate-001",
            "artifact_type": "requirements",
            "subject": "target",
            "subject_layer": "target-instance",
            "authority": "generated",
            "status": "accepted",
            "owner": "target-owner",
            "supersedes": None,
            "source_trace": [],
        }
    )
    assert not result.ok
    assert "self_promotion" in {issue.code for issue in result.issues}


def test_release_promotion_requires_independent_human_boundary() -> None:
    result = validate_promotion(
        candidate_actor="candidate-runtime",
        approving_actor="candidate-runtime",
        authority_class="generated",
        rollback_release=None,
        independent_evidence=False,
    )
    assert not result.ok
    assert {issue.code for issue in result.issues} == {
        "self_promotion",
        "generated_authority",
        "rollback",
        "independent_evidence",
    }
