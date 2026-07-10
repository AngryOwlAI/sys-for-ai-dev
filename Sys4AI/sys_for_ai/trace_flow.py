"""Walking-skeleton trace flow data models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class WalkingSkeletonArtifact:
    """One artifact in the active or historical walking-skeleton flow."""

    artifact_id: str
    flow_step: str
    artifact_type: str
    path: str
    subject_layer: str
    authority_status: str
    evidence_class: str
    upstream_ids: tuple[str, ...]
    downstream_ids: tuple[str, ...]
    validation_status: str

    def as_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation."""

        return {
            "artifact_id": self.artifact_id,
            "flow_step": self.flow_step,
            "artifact_type": self.artifact_type,
            "path": self.path,
            "subject_layer": self.subject_layer,
            "authority_status": self.authority_status,
            "evidence_class": self.evidence_class,
            "upstream_ids": list(self.upstream_ids),
            "downstream_ids": list(self.downstream_ids),
            "validation_status": self.validation_status,
        }


@dataclass(frozen=True)
class WalkingSkeletonLifecycleStage:
    """Explicit evidence obligations for one scoped lifecycle stage."""

    stage: str
    inputs: str
    responsible_role: str
    approving_role: str
    permissions: str
    activities: str
    outputs: str
    entry_criteria: str
    exit_criteria: str
    failure_behavior: str
    rollback_or_return: str
    evidence: str

    def as_dict(self) -> dict[str, str]:
        """Return a JSON-serializable representation."""

        return {
            "stage": self.stage,
            "inputs": self.inputs,
            "responsible_role": self.responsible_role,
            "approving_role": self.approving_role,
            "permissions": self.permissions,
            "activities": self.activities,
            "outputs": self.outputs,
            "entry_criteria": self.entry_criteria,
            "exit_criteria": self.exit_criteria,
            "failure_behavior": self.failure_behavior,
            "rollback_or_return": self.rollback_or_return,
            "evidence": self.evidence,
        }


@dataclass(frozen=True)
class WalkingSkeletonFlowReport:
    """Validation summary for the Phase 2 walking-skeleton flow."""

    flow_id: str
    target_system_id: str
    package_root: str
    result: str
    artifacts: tuple[WalkingSkeletonArtifact, ...]
    lifecycle_stages: tuple[WalkingSkeletonLifecycleStage, ...]
    historical_artifacts: tuple[WalkingSkeletonArtifact, ...]
    missing_artifacts: tuple[str, ...]
    trace_gaps: tuple[str, ...]
    warnings: tuple[str, ...]
    pending_artifacts: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation."""

        return {
            "flow_id": self.flow_id,
            "target_system_id": self.target_system_id,
            "package_root": self.package_root,
            "result": self.result,
            "artifacts_checked": len(self.artifacts),
            "artifacts": [artifact.as_dict() for artifact in self.artifacts],
            "lifecycle_stages": [stage.as_dict() for stage in self.lifecycle_stages],
            "historical_artifacts": [artifact.as_dict() for artifact in self.historical_artifacts],
            "missing_artifacts": list(self.missing_artifacts),
            "trace_gaps": list(self.trace_gaps),
            "warnings": list(self.warnings),
            "pending_artifacts": list(self.pending_artifacts),
        }
