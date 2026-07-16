---
artifact_id: ADR-0005
artifact_type: decision
subject: development-system
subject_layer: development
authority: controlled
status: accepted
owner: system_director
supersedes: phase-1_environment_decision_record
source_trace:
  - SFA-PRD-REPOSITORY-REBOOT-001
---

# ADR-0005: Development Environment

## Context

The bootstrap development environment, product build environment, and generated
target runtime have different dependencies and permissions.

## Decision

Keep them separate:

- Root/development tooling validates project control and bootstrap assets.
- `Sys4AI/` declares and builds its own product dependencies.
- Each target package declares its own runtime and deployment dependencies.
- Host adapters report capabilities rather than assuming the development
  environment is available.

## Consequences

Root validation may orchestrate product and integration checks, but the product
cannot import root tools. Product dependencies are not automatically target
runtime dependencies.

## Verification

Run development, product, and integration checks in separate commands and build
the product from inside its own directory.
