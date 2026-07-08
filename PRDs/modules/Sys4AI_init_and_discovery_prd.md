# Sys4AI Init and Discovery PRD

**PRD module ID:** PRD-MOD-INIT-DISCOVERY
**Document status:** Decomposed draft
**Subject layer:** framework_product
**Source authority status:** derivative_draft
**Source PRDs:** PRDs/Sys4AI_phase-0_product_system_design_prd.md;PRDs/Sys4AI_phase-1_implementation_initialization_prd.md;PRDs/Sys4AI_phase-2_walking_skeleton_prd.md
**Source evidence:** PRDs/PRD_decomposition_strategy.md;implementation_plans/Sys4AI_next_scope_full_implementation_plan.md;implementation_plans/acceptance_reports/PHASE2-WALKING-SKELETON-DEMO-SFADEV-22.md;Sys4AI/registries/prd_module_registry.csv;Sys4AI/registries/requirement_trace_registry.csv
**Owns requirement prefixes:** SFA-CORE-DISCOVERY;SFA-CORE-INIT;SFA-P1-INIT-DISC;SFA-P1-INIT-FRONTDOOR
**References requirement prefixes:** PRD-MOD-ROLE-GOVERNANCE;PRD-MOD-VALIDATION-TRACEABILITY;PRD-MOD-SOURCE-FIRST-MEMORY
**Promotion status:** not_promoted
**Last updated:** 2026-07-08

> Authority notice: This document is a decomposed PRD draft generated from canonical source PRDs and walking-skeleton evidence. It is not canonical unless promoted by a Director Decision and source-authority workflow. When this draft conflicts with canonical PRDs, the canonical PRDs control.

## 1. Purpose

Define the entry path from user intent into governed discovery, requirements-discovery records, and initial PRD routing.

## 2. Source Authority Boundary

This draft derives from the Phase 0, Phase 1, and Phase 2 PRDs, the PRD decomposition strategy, the Phase 2 walking-skeleton demo acceptance evidence, and the current requirement trace registry. It does not supersede those sources. It records a proposed module boundary for review and later promotion or deferral.

## 3. Owned Requirement Scope

Intended ownership prefixes:

- `SFA-CORE-DISCOVERY`
- `SFA-CORE-INIT`
- `SFA-P1-INIT-DISC`
- `SFA-P1-INIT-FRONTDOOR`

Current trace rows observed for this draft:

- `SFA-CORE-DISCOVERY-001`
- `SFA-CORE-DISCOVERY-002`
- `SFA-CORE-DISCOVERY-003`
- `SFA-CORE-DISCOVERY-004`
- `SFA-CORE-DISCOVERY-005`
- `SFA-CORE-DISCOVERY-006`
- `SFA-CORE-DISCOVERY-007`
- `SFA-CORE-INIT-001`
- `SFA-CORE-INIT-002`
- `SFA-CORE-INIT-003`
- `SFA-CORE-INIT-004`
- `SFA-CORE-INIT-005`
- `SFA-CORE-INIT-006`
- `SFA-CORE-INIT-007`
- `SFA-CORE-INIT-008`
- `SFA-CORE-INIT-009`

## 4. Referenced Modules

This draft depends on the following module drafts for cross-cutting behavior. References are non-authoritative until a promotion decision assigns canonical ownership.

- `PRD-MOD-ROLE-GOVERNANCE`
- `PRD-MOD-VALIDATION-TRACEABILITY`
- `PRD-MOD-SOURCE-FIRST-MEMORY`

## 5. Functional Scope

- Discovery gate behavior
- init front-door behavior
- requirements discovery records
- candidate-to-PRD routing

## 6. Non-Goals

- Promote this module to canonical status.
- Supersede Phase 0, Phase 1, or Phase 2 PRDs.
- Rewrite requirement IDs or trace selectors.
- Treat generated documentation, memory hits, or wiki pages as source authority.

## 7. Traceability Requirements

- Registry row: `Sys4AI/registries/prd_module_registry.csv` records this module as `draft` and `derivative_draft`.
- Requirement trace: matching Phase 0 selectors include this module path as draft evidence where applicable.
- Source registry: this file is registered as a derivative draft source.
- Object relationships: this module traces to the decomposition strategy and derives from the source PRDs.

## 8. Validation Requirements

- `make validate-prd-modules` must pass.
- `make validate-requirement-trace` must pass.
- `make validate-registry-graph` must pass.
- `validate-check-diff` must show AJ24 changes inside the authorized packet.

## 9. Promotion Conditions

Promotion requires a Director Decision that states the module decision, canonical effect, trace updates, conflict handling, and any deferrals. The promotion decision must preserve one canonical owner per requirement family.

## 10. Open Issues

- Promotion must confirm whether discovery gate and init front door stay in one module or split after more target-system evidence.

## 11. Acceptance Evidence

AJ24 acceptance evidence is limited to draft creation, registry linkage, trace update, and validator passage. Domain truth, production readiness, and canonical authority remain out of scope.

## 12. Change Control

This draft may be revised, split, merged, deferred, or promoted only by a later controlled source-authority workflow. Until then, canonical PRDs and registered control records remain controlling.

## References

Sys4AI-dev. (2026a). *Sys4AI phase 0 product system design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

Sys4AI-dev. (2026b). *Sys4AI phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

Sys4AI-dev. (2026c). *Sys4AI phase 2 walking skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

Sys4AI-dev. (2026d). *Sys4AI PRD decomposition strategy* [Decomposition strategy]. `PRDs/PRD_decomposition_strategy.md`.
