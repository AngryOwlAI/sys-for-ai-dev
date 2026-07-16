"""Stable domain models without host or filesystem assumptions."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import re
from typing import Any, Mapping


class SubjectLayer(str, Enum):
    DEVELOPMENT = "development"
    FRAMEWORK = "framework"
    TARGET_TEMPLATE = "target-template"
    TARGET_INSTANCE = "target-instance"
    DERIVATIVE = "derivative"


class AuthorityClass(str, Enum):
    CANONICAL = "canonical"
    CONTROLLED = "controlled"
    REFERENCE = "reference"
    GENERATED = "generated"
    HISTORICAL = "historical"


class LifecycleStage(str, Enum):
    DESIGN = "Design"
    DEVELOP = "Develop"
    IMPLEMENT = "Implement"
    TEST = "Test"
    RUN = "Run"
    MAINTAIN = "Maintain"
    IMPROVE = "Improve"
    RETIRE = "Retire"


class LifecycleState(str, Enum):
    PROPOSED = "proposed"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    RETIRED = "retired"


@dataclass(frozen=True)
class StrategicIntent:
    mission: str
    vision: str
    values: tuple[str, ...]


@dataclass(frozen=True)
class Stakeholder:
    stakeholder_id: str
    name: str
    interests: tuple[str, ...] = ()
    decision_rights: tuple[str, ...] = ()


@dataclass(frozen=True)
class SystemDefinition:
    system_id: str
    name: str
    intent: str
    target_kind: str
    coordination_pattern: str = "linear_workflow"
    operational_maturity: str = "concept"

    def __post_init__(self) -> None:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", self.system_id):
            raise ValueError("system_id must be a non-empty path-safe identifier")
        if not self.name.strip() or not self.intent.strip():
            raise ValueError("name and intent are required")


@dataclass(frozen=True)
class Requirement:
    requirement_id: str
    statement: str
    source_id: str
    verification_method: str


@dataclass(frozen=True)
class ArchitectureDecision:
    decision_id: str
    title: str
    status: str
    rationale: str


@dataclass(frozen=True)
class Role:
    role_id: str
    purpose: str
    authorities: tuple[str, ...] = ()
    skill_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class Skill:
    skill_id: str
    version: str
    outcomes: tuple[str, ...]


@dataclass(frozen=True)
class Artifact:
    artifact_id: str
    artifact_type: str
    subject: str
    subject_layer: SubjectLayer
    authority: AuthorityClass
    status: str
    owner: str
    supersedes: str | None = None
    source_trace: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArtifactRelationship:
    subject_id: str
    predicate: str
    object_id: str
    evidence_path: str


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    evidence_type: str
    path: str
    status: str
    freshness: str = "unknown"


@dataclass(frozen=True)
class HostCapability:
    capability_id: str
    status: str
    execution_allowed: bool
    permission_source: str
    evidence: str
    limitations: tuple[str, ...] = ()


@dataclass(frozen=True)
class TargetSystemPackage:
    definition: SystemDefinition
    root: str
    authority: AuthorityClass = AuthorityClass.GENERATED
    production_ready: bool = False


@dataclass(frozen=True)
class Action:
    kind: str
    target: str
    payload: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PermissionEnvelope:
    allowed_reads: tuple[str, ...] = ()
    allowed_writes: tuple[str, ...] = ()
    allowed_tools: tuple[str, ...] = ()
    network_allowed: bool = False
    external_writes_allowed: bool = False

    def permits(self, action: Action) -> bool:
        if action.kind == "read":
            return _matches(action.target, self.allowed_reads)
        if action.kind == "write":
            return _matches(action.target, self.allowed_writes)
        if action.kind == "tool":
            return action.target in self.allowed_tools
        if action.kind == "network":
            return self.network_allowed
        if action.kind == "external_write":
            return self.external_writes_allowed
        return False


@dataclass(frozen=True)
class ExecutionTransaction:
    transaction_id: str
    subject: str
    actor: str
    authorized_by: str
    actions: tuple[Action, ...]
    permissions: PermissionEnvelope
    material_self_change: bool = False
    approval_actor: str | None = None
    rollback: str = ""
    stop_conditions: tuple[str, ...] = ()


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    path: str | None = None


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    issues: tuple[ValidationIssue, ...] = ()
    warnings: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {
            "ok": self.ok,
            "issues": [
                {"code": issue.code, "message": issue.message, "path": issue.path}
                for issue in self.issues
            ],
            "warnings": list(self.warnings),
            "evidence": list(self.evidence),
        }


def _matches(target: str, allowed: tuple[str, ...]) -> bool:
    return any(
        target == prefix or target.startswith(prefix.rstrip("/") + "/")
        for prefix in allowed
    )
