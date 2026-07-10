# Sys4AI Interface and Integration PRD

**PRD module ID:** PRD-MOD-INTERFACE-INTEGRATION
**Document status:** Regenerated decomposed draft
**Subject layer:** framework_product
**Source authority status:** derivative_draft
**Source PRDs:** PRDs/Sys4AI_phase-0_product_system_design_prd.md;PRDs/Sys4AI_phase-1_implementation_initialization_prd.md;PRDs/Sys4AI_phase-2_walking_skeleton_prd.md;PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md
**Source evidence:** Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml;PRDs/PRD_decomposition_strategy.md;implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md;Sys4AI/registries/prd_module_registry.csv;Sys4AI/registries/requirement_trace_registry.csv
**Owns requirement prefixes:** SFA-CORE-SVC;SFA-P0-FR-016;SFA-P1-INIT-HOST;SFA-P2-ADD-HOST
**References requirement prefixes:** PRD-MOD-AGENTJOB-CONTINUE;PRD-MOD-SOURCE-FIRST-MEMORY;PRD-MOD-ROLE-GOVERNANCE;PRD-MOD-TARGET-SYSTEM-GENERATION;PRD-MOD-SECURITY-SAFETY-ASSURANCE
**Promotion status:** not_promoted
**Regeneration transaction:** TX-19-MODULES
**Last updated:** 2026-07-10

> Authority notice: This document is a noncanonical derivative draft regenerated from the approved Phase 0 baseline, accepted Phase 1 initialization baseline, preserved Phase 2 PRD, controlled Phase 2 strategic addendum, and accepted G-08 decision. It allocates interface review scope but does not create an independent interface authority, verify a host capability, expand permissions, supersede a source PRD, or satisfy production acceptance. The registered canonical and controlled sources govern every conflict.

## 1. Purpose

Allocate the `host_harness_integration` boundary and define the evidence expected for actual host, model, tool, data, external-service, connector, sub-agent, user-interface, memory/state, and target-runtime contracts.

## 2. Source Authority Boundary

The approved Phase 0 PRD controls the target-harness boundary and source/version-control requirements. The accepted Phase 1 PRD controls reference-host profile initialization and host-evidence states. The preserved Phase 2 PRD remains historical requirement evidence; the controlled Phase 2 strategic addendum requires host-dependent actions to resolve through a registered profile with current permission, limitation, degraded-mode, and cancellation evidence. `DDR-SFADEV-STRATEGIC-BASELINE-G08-001` approves strategic content only and explicitly leaves G-07 host verification open.

This module summarizes and allocates those obligations for TX-19 review. It cannot turn a reference profile, configuration file, observed local behavior, or successful structural validation into verified host capability.

## 3. Owned Requirement Scope

Intended ownership prefixes:

- `SFA-CORE-SVC`
- `SFA-P0-FR-016`
- `SFA-P1-INIT-HOST`
- `SFA-P2-ADD-HOST`

This is intended allocation metadata only. Requirement wording and evidence state remain controlled by the source PRDs, host-profile records, and requirement-trace registry.

## 4. Referenced Modules

This draft depends on the following module drafts for cross-cutting behavior. References are non-authoritative until a promotion decision assigns canonical ownership.

- `PRD-MOD-AGENTJOB-CONTINUE` as the historical mapping to bounded execution, cancellation, and resume-operation semantics
- `PRD-MOD-SOURCE-FIRST-MEMORY`
- `PRD-MOD-ROLE-GOVERNANCE`
- `PRD-MOD-TARGET-SYSTEM-GENERATION`
- `PRD-MOD-SECURITY-SAFETY-ASSURANCE`

## 5. Functional Scope

- Maintain an interface inventory that distinguishes the framework product, Meta-Agent Runtime, host harness, target-system template, target-system instance, and derivative surfaces.
- Require every applicable target system to declare whether it is an agentic AI software harness and to define its LLM/model, tool, state, memory, policy, and user-interface boundaries or record a justified not-applicable disposition.
- Define actual contracts for host interaction, models, tools, local and external data, each external service, networked connectors, sub-agents, task or thread state, memory/retrieval, and the target runtime.
- For each interface, record a stable ID, parties and direction, purpose, endpoint or invocation mechanism, protocol and data schema, authentication and permission source, environment scope, data classification, provenance, rate or resource limits, timeouts, version, owner, monitoring, failure and degraded behavior, cancellation, rollback or compensation, evidence freshness, review triggers, and supersession.
- Keep portable execution semantics independent from host mechanics. Apply precedence `platform and system constraints -> host permissions -> project authorization -> transaction permission envelope -> task objective`.
- Require unknown, stale, permission-dependent, environment-dependent, contradicted, or unavailable required host capability to fail closed rather than be inferred from goals, values, local configuration, or model behavior.
- Require source/version-control, registry trace, hashes where practical, validation evidence, and rollback or migration evidence for controlled interface definitions and their generated summaries.
- Keep sub-agent creation, connector use, data egress, external-service calls, target-runtime mutation, and other side effects independently permissioned and bounded by the active transaction.
- Preserve G-07 as a separate observable-host verification gate. TX-19 documentation may state requirements and known limitations but cannot mark host capabilities verified.

## 6. Non-Goals

- Promote this module to canonical status.
- Supersede Phase 0, Phase 1, or Phase 2 PRDs.
- Rewrite requirement IDs or trace selectors.
- Treat generated documentation, memory hits, or wiki pages as source authority.
- Treat a host profile schema pass, reference configuration, local tool presence, or successful smoke test as G-07 acceptance.
- Grant connector, network, sub-agent, data, tool, target-runtime, or production permission from the approved values or task objective.
- Claim production readiness, operational authority, broad host conformance, or service reliability without accepted evidence and accountable approval.

## 7. Traceability Requirements

- Registry row: `Sys4AI/registries/prd_module_registry.csv` records this module as `draft` and `derivative_draft`.
- Requirement trace: matching source requirements retain independent capability, verification, freshness, approval, and semantic-review states; this module path is derivative evidence only.
- Source registry: this file is registered as a derivative draft source.
- Object relationships: this module traces to the decomposition strategy and TX-19 plan, derives from all four source PRDs, and references the G-08 decision without changing it.
- Host-dependent claims must resolve to registered capability-profile evidence rather than this module or a generated summary.

## 8. Validation Requirements

- `make validate-prd-modules` must pass.
- `make validate-host-capability-profiles` must pass without interpreting structural success as G-07 verification.
- `make validate-prd-semantics` must pass.
- `make validate-requirement-trace` must pass.
- `make validate-registry-graph` must pass.
- `make validate-capability-migration` and `make validate-generated-derivatives` must pass.
- Negative probes must reject unknown required capability, missing or stale evidence, invalid permission sources, absent degraded/cancellation behavior, secret-bearing examples, derivative authority inversion, and unsupported G-07 or production claims.
- Passing structural validation does not prove end-to-end integration, host conformance, availability, performance, safety, production readiness, operational authority, or domain truth.

## 9. Promotion Conditions

Promotion requires a later source-authority decision that states the module decision, canonical effect, interface ownership, host-evidence impact, trace migration, permission review, validation, rollback, and supersession. It must preserve one canonical owner per requirement family and cannot infer promotion from TX-19 regeneration.

## 10. Open Issues

- G-07 observable verification remains open for the reference host; per-capability evidence must be collected and accepted separately.
- Concrete target-runtime, connector, external-service, data-retention, performance, service-level, and incident-response contracts remain target- and deployment-specific.
- Production permissions, operational ownership, and cross-system data agreements remain outside TX-19.

## 11. Acceptance Evidence

TX-19 acceptance evidence for this module is limited to accurate derivative allocation, approved-baseline provenance, complete WS-14 interface categories, explicit G-07 separation, noncanonical status, and validator passage. It does not verify a host, authorize an external action, satisfy G-07 or G-10, establish production readiness, grant operational authority, or prove domain truth.

## 12. Change Control

This draft may be revised, split, merged, deferred, replaced, or promoted only through a bounded source-authority workflow with interface-impact, permission, validation, rollback, receipt, and handoff evidence. Changes to approved vision or values require accountable human supersession of the G-08 decision. Until then, the registered source PRDs, host profiles, decisions, and trace records control.

## References

AngryOwlAI. (2026a). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

AngryOwlAI. (2026b). *Sys4AI Phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

AngryOwlAI. (2026c). *Sys4AI Phase 2 walking skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

AngryOwlAI. (2026d). *Sys4AI Phase 2 strategic baseline addendum* [Product requirements document addendum]. `PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md`.

AngryOwlAI. (2026e). *DDR-SFADEV-STRATEGIC-BASELINE-G08-001: Strategic vision and core-values approval* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml`.

AngryOwlAI. (2026f). *Sys4AI strategic baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.

AngryOwlAI. (2026g). *Sys4AI PRD decomposition strategy* [Decomposition strategy]. `PRDs/PRD_decomposition_strategy.md`.
