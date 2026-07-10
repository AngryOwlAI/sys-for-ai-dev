# Sys4AI Role Governance PRD

**PRD module ID:** PRD-MOD-ROLE-GOVERNANCE
**Document status:** Decomposed draft
**Subject layer:** framework_product
**Source authority status:** derivative_draft
**Source PRDs:** PRDs/Sys4AI_phase-0_product_system_design_prd.md;PRDs/Sys4AI_phase-1_implementation_initialization_prd.md;PRDs/Sys4AI_phase-2_walking_skeleton_prd.md;PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md
**Source evidence:** PRDs/PRD_decomposition_strategy.md;implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md;Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml;Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml;Sys4AI/registries/prd_module_registry.csv;Sys4AI/registries/requirement_trace_registry.csv
**Owns requirement prefixes:** SFA-CORE-ROLE;SFA-CORE-ART;SFA-P0-FR-007;SFA-P0-FR-010;SFA-P0-FR-011;SFA-P0-FR-020;SFA-P0-FR-021;SFA-P1-INIT-ROLE;SFA-P1-INIT-BIND
**References requirement prefixes:** PRD-MOD-SKILL-LIFECYCLE;PRD-MOD-INIT-DISCOVERY;PRD-MOD-VALIDATION-TRACEABILITY
**Promotion status:** not_promoted
**Last updated:** 2026-07-10

> Authority notice: This TX-19-MODULES regeneration is a noncanonical decomposition of the approved Phase 0 baseline, accepted Phase 1 initialization baseline, preserved Phase 2 source, controlled Phase 2 strategic addendum, and G-08 decision. It allocates derivative ownership for review and navigation only. It does not supersede a source PRD, approve a role assignment, grant permission, verify a host capability, or authorize production operation.

## 1. Purpose

Define the derivative role-governance boundary for role catalogs, artifact producers and consumers, execution bindings, delegation, handoffs, decisions, evaluation independence, and acceptance duties.

## 2. Source Authority Boundary

The source PRDs and accepted Director Decisions control all normative role, authority, approval, and permission requirements. This draft summarizes and allocates those requirements without rewriting them as independent authority. G-08 approves the exact Sys4AI vision and core values, but those values do not grant permissions or collapse separation of duties. G-07 host verification, production readiness, operational authority, broad stakeholder consensus, and domain truth remain outside this module.

## 3. Owned Requirement Scope

Intended ownership prefixes:

- `SFA-CORE-ROLE`
- `SFA-CORE-ART`
- `SFA-P0-FR-007`
- `SFA-P0-FR-010`
- `SFA-P0-FR-011`
- `SFA-P0-FR-020`
- `SFA-P0-FR-021`
- `SFA-P1-INIT-ROLE`
- `SFA-P1-INIT-BIND`

These families cover explicit role inputs, outputs, responsibilities, and exit criteria; conditional specialist-sub-agent prompts; universal handoffs; Director Decisions for unresolved authority-sensitive routing; completion receipts; controlled role registries; role-to-skill crosswalks; execution bindings; delegation expiry; and permission-envelope constraints.

## 4. Referenced Modules

This draft depends on the following noncanonical module allocations:

- `PRD-MOD-SKILL-LIFECYCLE` for governed skill status and activation.
- `PRD-MOD-INIT-DISCOVERY` for stakeholder elicitation, candidate state, approval, waiver, and conflict discovery.
- `PRD-MOD-VALIDATION-TRACEABILITY` for role, binding, approval-evidence, and separation-of-duties validation.

Cross-module references do not transfer requirement ownership or authority.

## 5. Functional Scope

- Assign strategic-intent facilitator duties without giving the facilitator approval authority.
- Assign a strategic-intent custodian to preserve stable IDs, versions, source hashes, approval state, and supersession history.
- Assign independent verifier and accountable human approver duties.
- Assign impact analyst duties before material changes to identity, vision, values, authority, permissions, architecture, lifecycle, or operational posture.
- Assign evaluator and acceptance duties so a proposer cannot be the sole evaluator or approver of a material self-change.
- Define artifact producer, consumer, reviewer, and handoff responsibilities.
- Require every active execution binding to identify authorized roles, runtime actors, approval principals, artifacts, tool and data limits, delegation expiry, validators, handoffs, and escalation destinations.
- Keep role assignment, values, goals, urgency, and apparent runtime capability from expanding the permission envelope.
- Treat specialist sub-agent creation as conditional on explicit authorization and verified host support; this draft makes no G-07 claim.
- Preserve Director Decision and completion-receipt obligations for authority-sensitive routing and bounded work.

## 6. Non-Goals

- Promote this module or any referenced module to canonical status.
- Approve a person, model, role, or runtime actor for a specific transaction.
- Let a facilitator, proposer, model, or evaluator self-approve purpose, values, permissions, evaluation criteria, or acceptance.
- Treat G-08 as G-07 host verification, production promotion, operational authority, or broad stakeholder consensus.
- Restore retired AgentJob or `/continue` runtime surfaces.
- Treat generated documentation, memory hits, or module summaries as source authority.

## 7. Traceability Requirements

- The PRD module registry must record this file as `draft` and `derivative_draft` with the exact ownership prefixes above.
- Source and relationship rows must preserve provenance to Phase 0, Phase 1, preserved Phase 2, the Phase 2 addendum, the execution-model decision, G-08, and the strategic migration plan.
- Requirement-trace evidence must distinguish requirement lifecycle, approval, authority, capability, validation, evidence freshness, and semantic-review state.
- Role and binding evidence must name the responsible actor, applicable permission envelope, required approvals, independent checks, and handoff or closeout evidence.
- Historical role and AgentJob evidence may remain readable for provenance but cannot establish current authority or capability.

## 8. Validation Requirements

- `make validate-prd-modules` must confirm registry metadata, noncanonical status, ownership coverage, and no duplicate active ownership.
- `make validate-roles` must validate role catalogs, role-to-skill crosswalks, execution bindings, delegation constraints, and proposed-skill references.
- `make validate-requirement-trace` and `make validate-requirement-trace-migration` must preserve exact requirement allocation and independent state dimensions.
- `make validate-registry-graph` must validate source, decision, artifact, module, and relationship links.
- `make validate-safety-evaluation` must continue to reject self-approval and evaluator-independence failures.
- Aggregate product and repository validation must pass.
- Passing structural checks do not prove role fitness, ethical correctness, stakeholder consensus, host support, production readiness, operational capability, or domain truth.

## 9. Promotion Conditions

Promotion requires an explicit source-authority decision naming the module, exact authority scope, owned prefixes, conflict rules, role reviewers, trace updates, supersession effect, and unresolved limitations. Promotion must preserve one active owner per requirement family and may not weaken human-reserved approvals, permission limits, evaluator independence, or historical evidence.

## 10. Open Issues

- Whether artifact-contract allocation should remain within role governance or become a separate module remains a future decomposition decision.
- Real-host evidence for specialist sub-agent mechanics remains blocked on G-07.
- Broad stakeholder representation, confidential independent holdouts, quantitative vision-success thresholds, and production role assignments remain future evidence obligations.

## 11. Acceptance Evidence

TX-19 acceptance for this draft requires exact registry alignment, current source provenance, explicit facilitator/custodian/verifier/approver/impact-analyst/evaluator/acceptance duties, preserved separation of duties, passing focused and aggregate validators, and no canonical or operational promotion. Acceptance establishes only that this derivative reflects the approved strategic baseline.

## 12. Change Control

This draft may be revised, split, merged, deferred, superseded, or promoted only through a controlled source-authority workflow. Material changes to role authority, approval, permission, evaluation, or acceptance boundaries require impact analysis and accountable human review. Canonical PRDs and accepted Director Decisions remain controlling.

## References

AngryOwlAI. (2026a, July 9). *Sys4AI strategic-baseline identity and execution-model decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml`.

AngryOwlAI. (2026b, July 10). *Sys4AI strategic-baseline G-08 human-approval decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml`.

Sys4AI-dev. (2026a). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

Sys4AI-dev. (2026b). *Sys4AI Phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

Sys4AI-dev. (2026c). *Sys4AI Phase 2 walking-skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

Sys4AI-dev. (2026d). *Sys4AI Phase 2 strategic-baseline addendum* [Product requirements document addendum]. `PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md`.

Sys4AI-dev. (2026e). *Sys4AI strategic-baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.

Sys4AI-dev. (2026f). *Sys4AI PRD decomposition strategy* [Decomposition strategy]. `PRDs/PRD_decomposition_strategy.md`.
