---
artifact_id: SFA-ARCH-SELF-HOSTING-001
artifact_type: architecture
subject: sys4ai
subject_layer: framework
authority: controlled
status: active
owner: system_architect
supersedes: implementation_plans/self_hosting_boundary_decision_record.md
source_trace:
  - ADR-0003
  - SFA-PRD-PRODUCT-BASELINE-001
---

# Self-Hosting Model

## Stage 0 — bootstrap

A host runs `development/bootstrap-agent/` against root project authority to
build Sys4AI. The bootstrap runtime cannot approve product purpose or release
promotion.

## Stage 1 — trusted product release

A versioned Sys4AI release is built, tested independently, and installed. It is
separate from its source repository and mutable target state.

## Stage 2 — controlled candidate generation

Trusted release N receives an approved development profile and may propose or
implement a bounded change only in a separate candidate workspace, for example
`worktrees/sys4ai-n-plus-1-candidate/`. It cannot mutate the trusted runtime
in place.

## Stage 3 — independent verification

The candidate is checked by product tests, integration tests, authority and
permission checks, regression tests, protected self-change holdouts, and a
separate verifier or evaluation context.

## Stage 4 — human promotion

An accountable human release owner may accept or reject candidate N+1. Release
N remains available for rollback.

## Fixed-point criterion

Self-hosting is meaningful when release N can use an approved profile to
produce a separate N+1 candidate that satisfies the same invariant suite
without hidden stage-0 behavior. It is proven by reproducibility and invariant
preservation, not by storing development records inside the product.
