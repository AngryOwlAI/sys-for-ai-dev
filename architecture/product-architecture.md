---
artifact_id: SFA-ARCH-PRODUCT-001
artifact_type: architecture
subject: sys4ai
subject_layer: framework
authority: controlled
status: active
owner: system_architect
supersedes: null
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
  - ADR-0004
---

# Product Architecture

## Architectural style

Sys4AI uses a host-neutral core with ports and adapters.

## Domain kernel

The domain package defines stable entities such as SystemDefinition,
StrategicIntent, Stakeholder, Requirement, ArchitectureDecision, Role, Skill,
Artifact, ArtifactRelationship, ExecutionTransaction, PermissionEnvelope,
Evidence, ValidationResult, LifecycleState, TargetSystemPackage, and
HostCapability.

The kernel contains no root-repository, Codex, GitHub, or fixed-filesystem
assumption.

## Application services

| Service | Responsibility |
|---|---|
| Discovery | Clarify intent, stakeholders, boundaries, scenarios, and unknowns |
| Specification | Produce controlled requirements |
| Architecture | Record drivers, alternatives, interfaces, and decisions |
| Planning | Convert accepted requirements into bounded work |
| Execution | Process explicitly authorized transactions |
| Verification | Validate structure, trace, behavior, and evidence |
| Target factory | Assemble target frameworks and target-system packages |
| Operations | Support run, maintenance, improvement, and retirement |
| Knowledge | Navigate canonical sources and relationships |
| Governance | Enforce authority, permissions, approval, and supersession |

## Ports

The product exposes protocols for model providers, human approval, workspace
access, files, source control, tools, state, artifact catalogs, events, clocks,
secrets, and host capabilities. Domain and application code depend on these
protocols, not concrete hosts.

## Adapters

Reference adapters cover a standalone CLI, filesystem workspaces, local state,
JSON/YAML artifacts, and a Codex host description. Git and GitHub adapters may
be added only behind explicit permissions.

## Assets and contracts

- `contracts/`: schemas, policies, catalogs, and profiles.
- `assets/`: portable skills, templates, assurance material, and domain-pack
  contracts.
- `examples/`: non-authoritative product examples.
- `docs/`: product-local explanation.

Assets are versioned inputs. They are not mutable run state.

## Runtime state

Target state defaults to:

    .sys4ai/
      workspace.yaml
      catalog/
      runs/<run-id>/
      generated/
      cache/

The installed package never stores development program history or current
target state.
