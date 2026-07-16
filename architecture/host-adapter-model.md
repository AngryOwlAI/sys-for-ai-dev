---
artifact_id: SFA-ARCH-HOST-ADAPTER-001
artifact_type: architecture
subject: sys4ai
subject_layer: framework
authority: controlled
status: active
owner: system_architect
supersedes: null
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
---

# Host-Adapter Model

## Capability contract

A host profile describes user interaction, workspace files, terminal/test
execution, connectors/network, agent delegation, task state, memory/retrieval,
and target-runtime capabilities. Each capability states availability,
execution permission, evidence, fallback, degraded behavior, cancellation, and
limitations.

## Permission precedence

1. Platform and system constraints.
2. Host permissions.
3. Project authorization.
4. Bounded transaction permission envelope.
5. Task objective.

A lower layer cannot expand a higher layer. Unknown or unavailable capability
fails closed.

## Adapter obligations

- Translate host mechanisms into product ports without changing domain rules.
- Expose denials and capability gaps rather than simulating success.
- Avoid secrets in artifacts, logs, examples, and generated packages.
- Capture enough evidence to reproduce the capability decision.
- Require accountable approval for external writes, production effects, or
  authority expansion.

Codex is the first reference adapter. It is not a mandatory product dependency.
