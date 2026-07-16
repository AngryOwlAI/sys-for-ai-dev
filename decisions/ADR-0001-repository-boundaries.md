---
artifact_id: ADR-0001
artifact_type: decision
subject: development-system
subject_layer: development
authority: controlled
status: accepted
owner: system_director
supersedes: null
source_trace:
  - SFA-PRD-REPOSITORY-REBOOT-001
---

# ADR-0001: Repository Boundaries

## Context

Development state, product assets, target fixtures, generated readers, and
historical evidence were physically mixed. Product validation reached into its
parent repository.

## Decision

Keep one monorepo during bootstrap, but enforce five planes and the dependency
direction development -> product -> generated target. `Sys4AI/` shall build
and test without its parent.

## Rejected alternatives

- Immediate multi-repository split: interfaces and release coordination are not
  stable enough.
- Preserve the mixed tree with more documentation: it does not enforce the
  boundary.

## Consequences

Cross-plane operations belong to root development tooling. Product-local
commands lose access to root PRDs, skills, workflows, and program history.
Historical material is retrieved from the tagged baseline or archive.

## Verification

Independent product build/test plus forbidden parent-reference scanning.
