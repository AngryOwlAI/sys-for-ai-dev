---
artifact_id: SFA-ARCH-INDEX-001
artifact_type: architecture
subject: development-system
subject_layer: development
authority: controlled
status: active
owner: system_architect
supersedes: null
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
  - SFA-PRD-REPOSITORY-REBOOT-001
---

# Architecture Index

Architecture explains how accepted requirements are divided and why. It does
not replace PRDs, ADRs, the active plan, current status, or observed evidence.

## Current architecture set

- [System context](system-context.md): D, H, M2, M1, M0, R and their allowed
  relationships.
- [Product architecture](product-architecture.md): host-neutral domain,
  services, ports, adapters, assets, and runtime state.
- [Development-system architecture](development-system-architecture.md):
  control plane, bootstrap runtime, development CLI, state, and evidence.
- [Authority and state model](authority-and-state-model.md): artifact metadata,
  independent status dimensions, and promotion rules.
- [Self-hosting model](self-hosting-model.md): trusted release, isolated
  candidate, independent verification, human promotion, and rollback.
- [Target-system model](target-system-model.md): generated package layers and
  target authority.
- [Host-adapter model](host-adapter-model.md): capabilities, permission
  precedence, and fail-closed behavior.

## Dependency rule

The root development system may build and validate the product. The product may
generate and validate targets. Neither the product nor a target may depend back
on the development workspace for runtime authority.
