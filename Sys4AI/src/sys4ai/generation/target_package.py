"""Generate a derivative target package with explicit layers."""

from __future__ import annotations

import csv
from pathlib import Path

import yaml

from ..adapters.filesystem import FilesystemWorkspaceAdapter
from ..domain.models import SystemDefinition
from ..runtime.workspace import initialize_workspace


DOCUMENTS = {
    "governance/mission.md": "# Mission\n\nDerived from approved target intent.\n",
    "governance/vision.md": "# Vision\n\nCandidate target vision.\n",
    "governance/values.md": "# Values\n\nCandidate target values.\n",
    "governance/authority.yaml": (
        "authority: derivative\napproval: unreviewed\n"
        "production_authority: absent\n"
    ),
    "requirements/discovery.md": (
        "# Discovery\n\nDerivative discovery record; not an approved baseline.\n"
    ),
    "requirements/product-requirements.md": (
        "# Product Requirements\n\nNo requirements are approved by generation alone.\n"
    ),
    "requirements/system-requirements.md": (
        "# System Requirements\n\nPromote only through target authority.\n"
    ),
    "architecture/context.md": "# Context\n\nDefine actors and trust boundaries.\n",
    "architecture/components.md": "# Components\n\nDefine target components.\n",
    "architecture/interfaces.md": "# Interfaces\n\nDefine external data flows.\n",
    "architecture/deployment.md": (
        "# Deployment\n\nNo production deployment is authorized.\n"
    ),
    "runtime/src/README.md": "# Runtime Source\n\nTarget implementation belongs here.\n",
    "runtime/config/README.md": "# Runtime Configuration\n\nNo secrets are committed.\n",
    "runtime/adapters/README.md": "# Runtime Adapters\n\nDeclare host and integration adapters.\n",
    "skills/README.md": "# Skills\n\nAccepted target skills belong here.\n",
    "contracts/README.md": "# Contracts\n\nTarget schemas and policies belong here.\n",
    "tests/README.md": "# Tests\n\nTarget verification belongs here.\n",
    "operations/runbook.md": "# Runbook\n\nOperational authority is not yet established.\n",
    "operations/monitoring.md": "# Monitoring\n\nDefine signals and thresholds.\n",
    "operations/maintenance.md": "# Maintenance\n\nDefine update and incident cadence.\n",
    "operations/retirement.md": "# Retirement\n\nDefine archival and authority withdrawal.\n",
    "evidence/acceptance-summary.md": (
        "# Acceptance Summary\n\nStructural generation only; no target acceptance is claimed.\n"
    ),
    "implementation-plan.md": (
        "# Target Implementation Plan\n\nProposed work only; approval and bounded transactions are required.\n"
    ),
    ".gitignore": ".sys4ai/\n__pycache__/\n.pytest_cache/\n",
}


def generate_target_package(
    definition: SystemDefinition,
    output: str | Path,
    *,
    allow_existing: bool = False,
) -> Path:
    target = initialize_workspace(
        output, definition, allow_existing=allow_existing
    )
    workspace = FilesystemWorkspaceAdapter(target)
    manifest = {
        "schema_version": "1.0.0",
        "target_system_id": definition.system_id,
        "name": definition.name,
        "intent": definition.intent,
        "target_kind": definition.target_kind,
        "coordination_pattern": definition.coordination_pattern,
        "operational_maturity": definition.operational_maturity,
        "authority": "derivative",
        "approval": "unreviewed",
        "package_status": "generated_candidate",
        "production_ready": False,
    }
    workspace.write_text(
        "target-system.yaml", yaml.safe_dump(manifest, sort_keys=False)
    )
    for relative, content in DOCUMENTS.items():
        workspace.write_text(relative, content)
    trace_path = workspace.resolve("requirements/trace.csv")
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    with trace_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("requirement_id", "artifact", "verification", "status"),
        )
        writer.writeheader()
        writer.writerow(
            {
                "requirement_id": "REQ-CAND-001",
                "artifact": "requirements/product-requirements.md",
                "verification": "planned",
                "status": "candidate",
            }
        )
    return target
