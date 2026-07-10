# Sys4AI Target-System Generation PRD

**PRD module ID:** PRD-MOD-TARGET-SYSTEM-GENERATION
**Document status:** Decomposed draft
**Subject layer:** framework_product
**Source authority status:** derivative_draft
**Source PRDs:** PRDs/Sys4AI_phase-0_product_system_design_prd.md;PRDs/Sys4AI_phase-1_implementation_initialization_prd.md;PRDs/Sys4AI_phase-2_walking_skeleton_prd.md;PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md
**Source evidence:** PRDs/PRD_decomposition_strategy.md;implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md;Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml;Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml;Sys4AI/registries/prd_module_registry.csv;Sys4AI/registries/requirement_trace_registry.csv
**Owns requirement prefixes:** SFA-P2-WS-FLOW;SFA-P2-WS-RDR;SFA-P2-WS-PRD;SFA-P2-WS-PLAN;SFA-P2-WS-AJ;SFA-P2-WS-PACKAGE;SFA-P0-FR-015;SFA-P0-FR-030;SFA-P1-INIT-PACKAGE;SFA-P2-ADD-PACKAGE
**References requirement prefixes:** PRD-MOD-VALIDATION-TRACEABILITY;PRD-MOD-AGENTJOB-CONTINUE;PRD-MOD-DOMAIN-PACK;PRD-MOD-INIT-DISCOVERY;PRD-MOD-INTERFACE-INTEGRATION
**Promotion status:** not_promoted
**Last updated:** 2026-07-10

> Authority notice: This TX-19-MODULES regeneration is a noncanonical decomposition of the approved Phase 0 baseline, accepted Phase 1 initialization baseline, preserved Phase 2 source, controlled Phase 2 strategic addendum, and G-08 decision. It describes target-package requirements and evidence allocation only. It does not approve a target system, verify a host, authorize execution, promote a package to production, or establish operational or domain truth.

## 1. Purpose

Define the derivative target-system generation boundary from governed discovery and implementation-ready requirements through a traceable, validated, explicitly nonproduction target package.

## 2. Source Authority Boundary

The source PRDs, target-specific controlled artifacts, accepted Director Decisions, and accountable target approvals control package content and authority. This draft does not create target intent, copy Sys4AI product intent into a target, or promote the smoke example. G-08 approves only the exact Sys4AI vision and values. Every target AI agent or target agentic system remains a separate system of interest with its own strategic intent, authority, data, approval, host, lifecycle, and operational boundary.

The stable `PRD-MOD-AGENTJOB-CONTINUE` module ID is retained for historical compatibility; its active mapped scope is bounded execution and resumability. The preserved `SFA-P2-WS-AJ` family remains historical Phase 2 trace vocabulary and does not restore AgentJob as current execution authority.

## 3. Owned Requirement Scope

Intended ownership prefixes:

- Preserved Phase 2 walking-skeleton families: `SFA-P2-WS-FLOW`, `SFA-P2-WS-RDR`, `SFA-P2-WS-PRD`, `SFA-P2-WS-PLAN`, `SFA-P2-WS-AJ`, and `SFA-P2-WS-PACKAGE`.
- Phase 0 requirements: `SFA-P0-FR-015` and `SFA-P0-FR-030`.
- Phase 1 package family: `SFA-P1-INIT-PACKAGE`.
- Phase 2 addendum package family: `SFA-P2-ADD-PACKAGE`.

These allocations cover implementation-ready SRP consumption, carried BERA/CKMSRA/SVCDA obligations, strategic-intent-aware manifests, package validation, and preserved walking-skeleton trace.

## 4. Referenced Modules

This draft depends on the following noncanonical module allocations:

- `PRD-MOD-INIT-DISCOVERY` for target intent, stakeholder evidence, candidate states, approval, waiver, and conflicts.
- `PRD-MOD-VALIDATION-TRACEABILITY` for requirement, package, approval, freshness, and semantic-limit validation.
- `PRD-MOD-AGENTJOB-CONTINUE`, the stable historical-compatibility ID whose current mapped scope is bounded execution and resumability.
- `PRD-MOD-INTERFACE-INTEGRATION` for host, tool, data, connector, external-service, and target-runtime interfaces.
- `PRD-MOD-DOMAIN-PACK` for domain-specific evidence and governance-floor constraints.

Cross-module references do not transfer ownership or authority.

## 5. Functional Scope

- Require separate target vision and target core values artifacts with stable IDs, active versions, content-approval state, accountable approval evidence, and source hashes.
- Permit omission only through a valid, explicit waiver that satisfies the strategic-intent contract; missing artifacts or a model-authored approval must fail closed.
- Require the target manifest to reference strategic artifacts, their active IDs and versions, approval or waiver evidence, hashes, and current paths.
- Require coordination pattern and operational maturity as independent fields, with a pattern decision and evidence appropriate to the target.
- Require lifecycle stage, promotion state, maintenance and retirement implications, and current impact-analysis state.
- Require a host profile or explicit host requirements, while treating unknown or unverified required capabilities as blocked rather than available.
- Require a portable execution profile and bounded task or transaction evidence without making AgentJob or `/continue` current runtime requirements.
- Preserve the governed flow from RDR to PRD to implementation plan to bounded execution evidence to implementation artifacts and package outputs.
- Require requirements trace, task-packet or transaction index, validation summary, approval or waiver evidence, and handoff or closeout evidence through stable registered paths.
- Reject stale hashes, duplicate or superseded strategic artifacts, self-approval, missing pattern evidence, unsupported operational claims, and cross-target authority or memory leakage.
- Preserve the repository-steward example as derivative, nonproduction smoke evidence only.

## 6. Non-Goals

- Approve target vision, target values, target requirements, a waiver, or production promotion through this derivative.
- Treat Sys4AI G-08 approval as approval of any target system.
- Claim G-07 host verification or assume unknown host capabilities.
- Restore AgentJob or `/continue` as current execution authority.
- Rewrite the preserved Phase 2 PRD or its historical requirement IDs.
- Promote the example package, generated evidence, or this module to canonical or operational status.
- Claim broad stakeholder consensus, autonomous capability, production readiness, operational authority, or domain truth.
- Begin TX-20 strategic generated-reader work.

## 7. Traceability Requirements

- The PRD module registry must record this file as `draft` and `derivative_draft` with the exact ownership metadata above.
- Package evidence must trace target intent, strategic artifacts, approval or waiver, pattern decision, lifecycle and promotion state, host requirements, portable execution profile, requirements, plan, implementation, validators, outputs, and closeout through stable IDs and registered paths.
- Source and relationship rows must preserve provenance to Phase 0, Phase 1, preserved Phase 2, the Phase 2 addendum, the execution-model decision, G-08, and the strategic migration plan.
- Historical `SFA-P2-WS-AJ` and AgentJob paths must remain visibly historical and cannot establish current capability.
- Cross-target strategic intent, memory, data, approvals, waivers, and evidence must remain isolated.

## 8. Validation Requirements

- `make validate-prd-modules` must confirm module metadata, noncanonical status, ownership coverage, and no duplicate active ownership.
- `make validate-target-package-smoke` must require strategic artifacts or a valid waiver, current IDs, versions and hashes, pattern and maturity evidence, lifecycle and promotion state, host requirements, portable execution profile, trace, and validation summaries.
- `make validate-strategic-intent` must reject incomplete artifacts, stale hashes, invalid waivers, and model self-approval.
- `make validate-host-capability-profiles` must fail closed on unknown required capabilities without claiming G-07.
- `make validate-lifecycle-and-patterns` must keep pattern, maturity, lifecycle, and promotion state distinct.
- `make validate-requirement-trace`, `make validate-requirement-trace-migration`, and `make validate-registry-graph` must validate exact source and evidence paths.
- `make validate-capability-migration` must preserve the historical AgentJob boundary.
- Aggregate product and repository validation must pass.
- Structural validation does not prove strategic quality, ethical correctness, stakeholder consensus, behavioral alignment, production readiness, operational capability, or domain truth.

## 9. Promotion Conditions

Promotion requires an explicit source-authority decision naming this module, its exact package scope and owned prefixes, target-instance boundary, conflict and supersession rules, review owners, validation obligations, trace migration, and unresolved limitations. Promotion of the module cannot promote any target package; each target requires its own accountable approval, host evidence, release authority, and production controls.

## 10. Open Issues

- Real-host capability evidence remains blocked on G-07.
- Production release ownership, monitoring thresholds, incident response, rollback, maintenance cadence, and data disposition remain target-specific future obligations.
- Broad stakeholder consensus and domain acceptance remain unclaimed.
- The preserved `SFA-P2-WS-AJ` vocabulary requires historical labeling wherever rendered to avoid confusing it with the portable execution profile.

## 11. Acceptance Evidence

TX-19 acceptance for this draft requires exact registry alignment, current provenance, explicit strategic-artifact and approval or waiver requirements, hashes, pattern, host, lifecycle, portable execution and trace obligations, preserved historical labeling, passing focused and aggregate validators, and no canonical, production, operational, or domain-truth promotion.

## 12. Change Control

This draft may be revised, split, merged, deferred, superseded, or promoted only through a controlled source-authority workflow. Changes to package identity, strategic-intent contracts, approval, waiver, host, pattern, lifecycle, trace, promotion, or operational boundaries require impact analysis and accountable review. Canonical PRDs and target-specific controlled sources remain controlling.

## References

AngryOwlAI. (2026a, July 9). *Sys4AI strategic-baseline identity and execution-model decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml`.

AngryOwlAI. (2026b, July 10). *Sys4AI strategic-baseline G-08 human-approval decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml`.

Sys4AI-dev. (2026a). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

Sys4AI-dev. (2026b). *Sys4AI Phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

Sys4AI-dev. (2026c). *Sys4AI Phase 2 walking-skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

Sys4AI-dev. (2026d). *Sys4AI Phase 2 strategic-baseline addendum* [Product requirements document addendum]. `PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md`.

Sys4AI-dev. (2026e). *Sys4AI strategic-baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.

Sys4AI-dev. (2026f). *Sys4AI PRD decomposition strategy* [Decomposition strategy]. `PRDs/PRD_decomposition_strategy.md`.
