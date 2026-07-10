# Sys4AI Skill Lifecycle PRD

**PRD module ID:** PRD-MOD-SKILL-LIFECYCLE
**Document status:** Decomposed draft
**Subject layer:** framework_product
**Source authority status:** derivative_draft
**Source PRDs:** PRDs/Sys4AI_phase-0_product_system_design_prd.md;PRDs/Sys4AI_phase-1_implementation_initialization_prd.md;PRDs/Sys4AI_phase-2_walking_skeleton_prd.md;PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md
**Source evidence:** PRDs/PRD_decomposition_strategy.md;implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md;Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml;Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml;Sys4AI/registries/prd_module_registry.csv;Sys4AI/registries/requirement_trace_registry.csv
**Owns requirement prefixes:** SFA-CORE-SKILL;SFA-P1-INIT-SKILL;SFA-P1-INIT-CORESKILL
**References requirement prefixes:** PRD-MOD-ROLE-GOVERNANCE;PRD-MOD-INIT-DISCOVERY;PRD-MOD-SOURCE-FIRST-MEMORY;PRD-MOD-VALIDATION-TRACEABILITY
**Promotion status:** not_promoted
**Last updated:** 2026-07-10

> Authority notice: This TX-19-MODULES regeneration is a noncanonical decomposition of the approved Phase 0 baseline, accepted Phase 1 initialization baseline, preserved Phase 2 source, controlled Phase 2 strategic addendum, and G-08 decision. It describes governed skill-lifecycle obligations only. It does not activate, install, promote, or authorize a skill, and it does not establish host capability, production readiness, or operational authority.

## 1. Purpose

Define the derivative skill-lifecycle boundary for proposals, provenance, adaptation, validation, activation, synchronization, deprecation, supersession, and separation between source-library, product-scaffold, compatibility, and runtime skill surfaces.

## 2. Source Authority Boundary

Canonical PRDs, controlled skill registries and policies, and accepted Director Decisions control skill requirements and activation. This draft summarizes and allocates those obligations without becoming a skill manifest or activation record. G-08 approves the exact Sys4AI vision and values; it does not create a skill, grant a model facilitation authority, or permit a skill to approve strategic content.

## 3. Owned Requirement Scope

Intended ownership prefixes:

- `SFA-CORE-SKILL`
- `SFA-P1-INIT-SKILL`
- `SFA-P1-INIT-CORESKILL`

These families cover governed core-skill manifests, adapter provenance, synchronization boundaries, lifecycle and authority status, role bindings, validation commands, activation constraints, controlled proposals, promotion, deprecation, and rejection of non-active packages on active runtime surfaces.

## 4. Referenced Modules

This draft depends on the following noncanonical module allocations:

- `PRD-MOD-ROLE-GOVERNANCE` for proposer, custodian, reviewer, approver, and operator duties.
- `PRD-MOD-INIT-DISCOVERY` for strategic-intent elicitation, candidate-state handling, approval, waiver, brownfield extraction, and conflict discovery.
- `PRD-MOD-SOURCE-FIRST-MEMORY` for source provenance, version, freshness, source hash, and ghost-authority controls.
- `PRD-MOD-VALIDATION-TRACEABILITY` for lifecycle, registry, source, activation, and supersession checks.

Cross-module references do not transfer requirement ownership or activate any skill.

## 5. Functional Scope

- Maintain explicit lifecycle states for proposed, candidate, controlled, active, deprecated, superseded, rejected, and historical skill surfaces as allowed by the governing registry contract.
- Preserve exact source provenance, local adaptation state, authority surface, role bindings, validators, dependencies, activation constraints, and supersession evidence.
- Keep source-library content, product-scaffold adapters, compatibility shims, and installed runtime skill surfaces distinct.
- Require controlled review and validation before activation; file presence or successful parsing is insufficient.
- Permit a `vision-and-values-facilitator` only as a candidate capability proposal or as a governed extension to an existing discovery skill.
- Require any such candidate to state its producer and consumer roles, inputs, outputs, approval boundary, privacy handling, escalation conditions, validators, and promotion evidence.
- Prohibit a candidate facilitator from approving purpose, vision, values, permissions, evaluation criteria, production promotion, or its own activation.
- Preserve additive migration and explicit supersession so in-progress or historical skill surfaces are not destructively rewritten.
- Keep host-specific invocation mechanics outside portable skill semantics until the applicable host capability is verified.

## 6. Non-Goals

- Create, install, register as active, or promote a `vision-and-values-facilitator` skill in TX-19.
- Claim that a candidate capability is available because this module mentions it.
- Promote this module or any skill package to canonical or active status.
- Allow a skill, model, facilitator, or proposer to self-approve strategic content or permission expansion.
- Restore retired AgentJob or `/continue` authoring and runtime surfaces.
- Treat generated documentation, memory hits, compatibility shims, or module summaries as source authority.
- Claim G-07 host verification, production readiness, operational authority, broad stakeholder consensus, or domain truth.

## 7. Traceability Requirements

- The PRD module registry must record this file as `draft` and `derivative_draft` with the exact ownership prefixes above.
- Every proposed or active skill must resolve to its controlled registry row, source provenance, lifecycle status, role bindings, validation commands, and activation evidence.
- A candidate `vision-and-values-facilitator` must resolve to a governed proposal row or an approved change to an existing discovery skill before implementation begins.
- Source and relationship rows must preserve provenance to Phase 0, Phase 1, preserved Phase 2, the Phase 2 addendum, the execution-model decision, G-08, and the strategic migration plan.
- Historical skill and AgentJob evidence may remain visible for provenance but cannot establish current skill availability or runtime capability.

## 8. Validation Requirements

- `make validate-prd-modules` must confirm module metadata, noncanonical status, ownership coverage, and no duplicate active ownership.
- `make validate-skill-lifecycle` must validate controlled lifecycle states, authority surfaces, activation constraints, and supersession.
- `make validate-core-skill-proposals` must reject incomplete or improperly promoted proposals.
- `make validate-skills` and `make validate-dev-skills` must validate the relevant product and development-system skill surfaces without conflating them.
- `make validate-roles` must validate role-to-skill and execution-binding constraints.
- `make validate-registry-graph` must validate source, skill, proposal, role, module, and relationship links.
- Aggregate product and repository validation must pass.
- Structural validation does not prove strategic quality, facilitator competence, host support, safety, stakeholder consensus, production readiness, operational capability, or domain truth.

## 9. Promotion Conditions

Promotion requires an explicit source-authority workflow naming the module or skill, exact authority surface, lifecycle transition, owner, producer and consumer roles, source provenance, validation evidence, activation constraints, rollback, supersession, and unresolved limitations. A proposed facilitator additionally requires accountable human approval of its scope and a separation-of-duties review; this module cannot supply that approval.

## 10. Open Issues

- Whether strategic-intent facilitation should be a new core capability or a governed extension to existing discovery skills remains undecided.
- The privacy, retention, and redaction contract for sensitive elicitation data requires review before facilitator implementation.
- Host-specific interaction and delegation mechanics remain unverified until G-07.
- Independent evaluation and production promotion remain later authority gates.

## 11. Acceptance Evidence

TX-19 acceptance for this draft requires exact registry alignment, current source provenance, an explicit candidate-only facilitator boundary, preserved lifecycle and activation controls, passing focused and aggregate validators, and no new active skill or canonical claim. Acceptance establishes only that this derivative reflects the approved strategic baseline.

## 12. Change Control

This draft may be revised, split, merged, deferred, superseded, or promoted only through a controlled source-authority workflow. Skill implementation or activation requires a separate authorized transaction. Material changes to strategic facilitation, approval, permission, privacy, or host behavior require impact analysis and accountable human review.

## References

AngryOwlAI. (2026a, July 9). *Sys4AI strategic-baseline identity and execution-model decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml`.

AngryOwlAI. (2026b, July 10). *Sys4AI strategic-baseline G-08 human-approval decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml`.

Sys4AI-dev. (2026a). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

Sys4AI-dev. (2026b). *Sys4AI Phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

Sys4AI-dev. (2026c). *Sys4AI Phase 2 walking-skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

Sys4AI-dev. (2026d). *Sys4AI Phase 2 strategic-baseline addendum* [Product requirements document addendum]. `PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md`.

Sys4AI-dev. (2026e). *Sys4AI strategic-baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.

Sys4AI-dev. (2026f). *Sys4AI PRD decomposition strategy* [Decomposition strategy]. `PRDs/PRD_decomposition_strategy.md`.
