# Self-Hosting Boundary Decision Record

Decision ID: SFA-EDR-SELFHOST-001
Status: Proposed
Date: 2026-07-06
Decision owner: Implementation initialization agent
Scope: `sys-for-ai-dev` using `sys-for-ai` concepts while `sys-for-ai` is under development

## Decision

`sys-for-ai-dev` may dogfood `sys-for-ai` memory and control-loop concepts as a self-hosting development system, but self-hosting records must distinguish product requirements, product reference implementation, development runtime skills, generated derivatives, and local retrieval surfaces.

## System context

- Framework system: `sys-for-ai`
- Development system: `sys-for-ai-dev`
- Target system for this implementation: `sys-for-ai`
- Self-hosting mode: `true`
- Reflection depth: `1`

## Rules

1. PRDs remain the authority for product requirements.
2. Active development runtime skills live under `.agents/skills/`.
3. Product scaffold skills under `sys-for-ai/skills/core/` are reference surfaces until promoted.
4. `/continue` advances at most one registered AgentJob per invocation.
5. Memory hits are navigation until verified against source files or registry rows.
6. Generated derivatives are noncanonical unless explicitly promoted by a source-authority AgentJob.
7. Activated AgentJobs, decisions, completions, and handoffs are superseded, not rewritten.
8. Codex compatibility shims must not become the product's only execution harness requirement.

## Rationale

The repository is intentionally self-hosting: the development workspace is using the product concepts while the product scaffold is still being built. This is acceptable only if the system keeps authority boundaries explicit and auditable.

## Consequences

- Control records must carry enough context to distinguish the framework system, development system, and target system.
- Memory and generated derivatives may improve navigation, but they cannot authorize requirements, routing, or permissions without source inspection evidence.
- Continuation work must be bounded by one AgentJob at a time.
