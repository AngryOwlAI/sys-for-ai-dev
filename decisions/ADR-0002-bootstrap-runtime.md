---
artifact_id: ADR-0002
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

# ADR-0002: Bootstrap Runtime

## Context

Canonical development skills were hidden under `.agents/`, compatibility
shims lived under `.codex/`, and portable product skill references created a
three-surface ownership problem.

## Decision

`development/bootstrap-agent/` is the canonical stage-0 runtime.
`.agents/` and `.codex/` are generated host bindings. Product skills under
`Sys4AI/assets/skills/` are independently versioned, host-neutral assets.

## Consequences

The generator and validator become development tools. A development skill
becomes a product asset only through explicit generalization and review.

## Verification

Every binding embeds and resolves its canonical path; canonical skills and
product assets validate independently.
