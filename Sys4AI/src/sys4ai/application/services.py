"""Small application services composed over domain rules and adapters."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from ..adapters.filesystem import FilesystemWorkspaceAdapter
from ..assurance.validation import validate_target_package
from ..domain.models import SystemDefinition, ValidationResult
from ..generation.target_package import generate_target_package
from ..governance.authority import validate_artifact_metadata, validate_promotion
from ..memory.catalog import lookup_source, search_sources
from ..runtime.transactions import process_transaction
from ..ports import ToolExecutionPort


class DiscoveryService:
    def record(self, root: str | Path, intent: str) -> Path:
        workspace = FilesystemWorkspaceAdapter(root)
        content = "\n".join(
            [
                "---",
                "artifact_type: discovery",
                "authority: generated",
                "status: draft",
                "---",
                "",
                "# Discovery",
                "",
                "This record is a derivative discovery input. It is not an approved",
                "requirements baseline.",
                "",
                "## Intent",
                "",
                intent.strip(),
                "",
                "## Stakeholders and boundaries",
                "",
                "To be established with accountable participants.",
                "",
                "## Unknowns and evidence needs",
                "",
                "To be resolved before requirements promotion.",
                "",
            ]
        )
        return workspace.write_text("requirements/discovery.md", content)


class SpecificationService:
    def create(self, root: str | Path) -> tuple[Path, Path]:
        workspace = FilesystemWorkspaceAdapter(root)
        product = workspace.write_text(
            "requirements/product-requirements.md",
            "# Product Requirements\n\nCandidate requirements; target approval is required.\n",
        )
        system = workspace.write_text(
            "requirements/system-requirements.md",
            "# System Requirements\n\nDerived constraints; verification is not yet complete.\n",
        )
        return product, system


class ArchitectureService:
    DOCUMENTS = {
        "architecture/context.md": "# Context\n\nDefine actors and trust boundaries.\n",
        "architecture/components.md": "# Components\n\nDefine responsibilities and interfaces.\n",
        "architecture/interfaces.md": "# Interfaces\n\nDefine data flows and owners.\n",
        "architecture/deployment.md": "# Deployment\n\nNo deployment is authorized by this document.\n",
    }

    def create(self, root: str | Path) -> tuple[Path, ...]:
        workspace = FilesystemWorkspaceAdapter(root)
        return tuple(
            workspace.write_text(relative, content)
            for relative, content in self.DOCUMENTS.items()
        )


class PlanningService:
    def create(self, root: str | Path) -> Path:
        workspace = FilesystemWorkspaceAdapter(root)
        content = "\n".join(
            [
                "---",
                "artifact_type: implementation-plan",
                "authority: generated",
                "status: proposed",
                "---",
                "",
                "# Target Implementation Plan",
                "",
                "## Accepted requirements source",
                "",
                "Record the accountable requirements source before execution.",
                "",
                "## Bounded work",
                "",
                "Define ordered work items with permissions, validation, rollback,",
                "stop conditions, and evidence.",
                "",
            ]
        )
        return workspace.write_text("implementation-plan.md", content)


class ExecutionService:
    def process(
        self,
        root: str | Path,
        transaction: Mapping[str, Any],
        host: ToolExecutionPort | None = None,
    ) -> ValidationResult:
        return process_transaction(root, transaction, host)


class OperationsService:
    DOCUMENTS = {
        "operations/runbook.md": "# Runbook\n\nOperational authority is not yet established.\n",
        "operations/monitoring.md": "# Monitoring\n\nDefine signals and thresholds.\n",
        "operations/maintenance.md": "# Maintenance\n\nDefine update and incident cadence.\n",
        "operations/retirement.md": "# Retirement\n\nDefine authority withdrawal and archival.\n",
    }

    def create(self, root: str | Path) -> tuple[Path, ...]:
        workspace = FilesystemWorkspaceAdapter(root)
        return tuple(
            workspace.write_text(relative, content)
            for relative, content in self.DOCUMENTS.items()
        )


class VerificationService:
    def verify(self, root: str | Path) -> ValidationResult:
        return validate_target_package(root)


class TargetFactory:
    def generate(
        self,
        definition: SystemDefinition,
        output: str | Path,
        *,
        allow_existing: bool = False,
    ) -> Path:
        return generate_target_package(
            definition, output, allow_existing=allow_existing
        )


class KnowledgeService:
    def search(self, root: str | Path, query: str, limit: int = 10) -> list[dict[str, object]]:
        return search_sources(root, query, limit)

    def lookup(self, root: str | Path, query: str) -> dict[str, object] | None:
        return lookup_source(root, query)


class GovernanceService:
    def validate_artifact(self, metadata: Mapping[str, Any]) -> ValidationResult:
        return validate_artifact_metadata(metadata)

    def validate_release_promotion(
        self,
        *,
        candidate_actor: str,
        approving_actor: str,
        authority_class: str,
        rollback_release: str | None,
        independent_evidence: bool,
    ) -> ValidationResult:
        return validate_promotion(
            candidate_actor=candidate_actor,
            approving_actor=approving_actor,
            authority_class=authority_class,
            rollback_release=rollback_release,
            independent_evidence=independent_evidence,
        )
