---
artifact_id: SFA-ARCH-SYSTEM-CONTEXT-001
artifact_type: architecture
subject: sys4ai-ecosystem
subject_layer: framework
authority: controlled
status: active
owner: system_architect
supersedes: null
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
---

# System Context

## Classified systems

| Symbol | System | Authority boundary |
|---|---|---|
| D | Sys4AI development context | Root PRDs, architecture, ADRs, active plan, bootstrap runtime, current state, and development evidence |
| H | Execution host | Capabilities and permissions supplied by Codex, CLI, CI, or another host |
| M2 | Sys4AI product | Product contracts, assets, runtime, and release identity |
| M1 | Target framework | Accepted rules and assets for a target class |
| M0 | Target instance | Concrete agentic system and its runtime workspace |
| R | Reader/evidence surfaces | Generated navigation, reports, logs, caches, receipts, and release bundles |

D is orthogonal to the M2/M1/M0 model hierarchy. It is not a higher model level.

## Allowed relationships

- D builds, tests, and releases M2 on H.
- M2 consumes H only through declared capability ports.
- M2 proposes or generates M1 packages.
- M1 is accepted by target authority before instantiating M0.
- M0 observations return to D as evidence or proposed improvements.
- R reports on sources but never authorizes them.

## Trust boundaries

- Human principals own purpose, authority expansion, production promotion, and
  material residual-risk acceptance.
- Hosts own the capabilities and platform permissions they actually expose.
- Sys4AI owns framework validation but cannot manufacture external approval.
- Target owners retain domain, operational, data, and production authority.
- Candidate self-hosting output is untrusted until independently verified and
  promoted.
