---
artifact_id: SFA-ARCH-DEVELOPMENT-SYSTEM-001
artifact_type: architecture
subject: development-system
subject_layer: development
authority: controlled
status: active
owner: system_architect
supersedes: null
source_trace:
  - SFA-PRD-REPOSITORY-REBOOT-001
  - ADR-0002
---

# Development-System Architecture

## Control plane

Root PRDs define requirements, architecture documents define structure, ADRs
record decisions, the active plan sequences implementation, and
`PROJECT_STATUS.md` reports current state. These classes remain separate.

## Bootstrap runtime

`development/bootstrap-agent/` is the canonical stage-0 runtime used to
develop Sys4AI. It contains skills, the skill catalog, policies, profiles, and
host adapters. Hidden host directories contain generated bindings only.

## Development CLI and tools

`sfadev` validates the development structure, active authority, skill
catalog, host bindings, product boundary, trace, and evidence policy. It does
not become part of the `sys4ai` product CLI.

## State

`development/state/current-work.yaml` is the small current state source.
`backlog.yaml` contains explicitly deferred work. Neither file embeds a
completed transaction ledger.

## Evidence

- `development/evidence/current/`: bounded evidence for the active change.
- `development/evidence/releases/<version>/`: immutable release bundles.
- CI artifacts and local run directories: ephemeral execution detail.

Historical program records remain in the pre-reboot Git baseline and dedicated
archive.

## Validation direction

Root validation invokes development, product, and integration checks. Product
validation never invokes root development checks.
