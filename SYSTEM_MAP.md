---
artifact_id: SFA-ARCH-SYSTEM-MAP-001
artifact_type: architecture
subject: development-system
subject_layer: development
authority: controlled
status: active
owner: system_director
supersedes: null
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
  - SFA-PRD-REPOSITORY-REBOOT-001
---

# Sys4AI System Map

## Build and generation direction

    User and stakeholder intent
        -> root PRDs
        -> architecture and ADRs
        -> one active implementation plan
        -> bootstrap development system (D)
        -> portable Sys4AI product (M2)
        -> target framework (M1)
        -> target system instance (M0)

The host (H) supplies capabilities through adapters. Reader and evidence
surfaces (R) may report on every level but cannot authorize changes.

## Feedback direction

    target observation
        -> evidence or improvement proposal
        -> development review
        -> approved requirement or architecture change

No generated target, model output, runtime observation, cache, or generated
reader may directly promote itself into product authority.

## Physical planes

| Plane | Canonical roots | May depend on |
|---|---|---|
| Project control | `PRDs/`, `architecture/`, `decisions/`, `implementation_plans/` | registered evidence |
| Bootstrap development | `development/` | control plane and product |
| Product | `Sys4AI/` | product-local contracts and assets only |
| Integration and targets | `integration/` | installed product and fixtures |
| Evidence | `development/evidence/`, CI artifacts, local run directories | observed commands and artifacts |

## Prohibited reverse edges

- `Sys4AI/` to a parent path.
- `Sys4AI/` to `.agents/`, `.codex/`, root PRDs, root workflows, or
  development state.
- generated target content to product authority without controlled promotion.
- candidate self-hosting output to its own promotion decision.
