---
artifact_id: ADR-0003
artifact_type: decision
subject: sys4ai
subject_layer: framework
authority: controlled
status: accepted
owner: system_director
supersedes: DDR-P1-SELFHOST-001
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
  - SFA-PRD-REPOSITORY-REBOOT-001
---

# ADR-0003: Self-Hosting

## Context

The previous repository treated self-hosting as an always-on mixed state. That
made development history appear to be product runtime authority.

## Decision

Self-hosting is a release protocol: bootstrap runtime builds a trusted release;
the trusted release modifies only a separate candidate; an independent context
verifies the candidate; an accountable human promotes or rejects it; the prior
release remains available for rollback.

The candidate cannot approve its own purpose, authority, thresholds, safety
waivers, production readiness, or rollback deletion.

## Consequences

The development self-hosting profile lives outside the product. The product
ships only a generic profile schema and example. Self-hosting evidence is
development or release evidence, never product runtime state.

## Verification

Candidate-isolation, independent-verifier, protected-holdout, human-promotion,
and rollback tests must all pass before a self-hosting claim.
