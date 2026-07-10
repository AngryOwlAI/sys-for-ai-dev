# Sys4AI Security Safety and Assurance PRD

**PRD module ID:** PRD-MOD-SECURITY-SAFETY-ASSURANCE
**Document status:** Regenerated decomposed draft
**Subject layer:** framework_product
**Source authority status:** derivative_draft
**Source PRDs:** PRDs/Sys4AI_phase-0_product_system_design_prd.md;PRDs/Sys4AI_phase-1_implementation_initialization_prd.md;PRDs/Sys4AI_phase-2_walking_skeleton_prd.md;PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md
**Source evidence:** Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml;PRDs/PRD_decomposition_strategy.md;implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md;Sys4AI/registries/prd_module_registry.csv;Sys4AI/registries/requirement_trace_registry.csv
**Owns requirement prefixes:** SFA-P0-FR-013;SFA-P0-FR-043;SFA-P0-RISK-003;SFA-P0-RISK-004;SFA-P0-RISK-FORMAT-003;SFA-P0-ISSUE-005;SFA-P1-INIT-DEP;SFA-P1-INIT-SELF;SFA-P2-ADD-SAFETY
**References requirement prefixes:** PRD-MOD-VALIDATION-TRACEABILITY;PRD-MOD-DOMAIN-PACK;PRD-MOD-OPERATIONS-MAINTENANCE;PRD-MOD-INTERFACE-INTEGRATION;PRD-MOD-ROLE-GOVERNANCE
**Promotion status:** not_promoted
**Regeneration transaction:** TX-19-MODULES
**Last updated:** 2026-07-10

> Authority notice: This document is a noncanonical derivative draft regenerated from the approved Phase 0 baseline, accepted Phase 1 initialization baseline, preserved Phase 2 PRD, controlled Phase 2 strategic addendum, and accepted G-08 decision. It allocates assurance review scope but does not create independent security policy, waive a binding control, grant permission, supersede a source PRD, prove safety, or satisfy production acceptance. The registered canonical and controlled sources govern every conflict.

## 1. Purpose

Allocate security, safety, privacy, compliance, dependency, secret-handling, sensitive-elicitation, self-change, permission, evaluation, rollback, and assurance obligations while keeping strategic values subordinate to binding controls and permissions.

## 2. Source Authority Boundary

The approved Phase 0 PRD controls value precedence, security and compliance hooks, secret-free examples, risks, and open permission questions. The accepted Phase 1 PRD controls dependency limits and bounded self-change obligations. The preserved Phase 2 PRD remains historical requirement evidence; the controlled Phase 2 strategic addendum retains the `validated_prototype` ceiling until separate evaluation, security, integration, ownership, rollback, monitoring, incident-response, service-threshold, and accountable production-approval evidence is accepted. `DDR-SFADEV-STRATEGIC-BASELINE-G08-001` approves the exact strategic content but explicitly prohibits permission expansion or control waiver from values.

This module summarizes and allocates those obligations for TX-19 review. It cannot change the control hierarchy, approval principal, permission envelope, evaluator independence, holdout protection, or production gate.

## 3. Owned Requirement Scope

Intended ownership prefixes:

- `SFA-P0-FR-013`
- `SFA-P0-FR-043`
- `SFA-P0-RISK-003`
- `SFA-P0-RISK-004`
- `SFA-P0-RISK-FORMAT-003`
- `SFA-P0-ISSUE-005`
- `SFA-P1-INIT-DEP`
- `SFA-P1-INIT-SELF`
- `SFA-P2-ADD-SAFETY`

This is intended allocation metadata only. Requirement wording, risk disposition, capability state, and evidence status remain controlled by the source PRDs and requirement-trace registry.

## 4. Referenced Modules

This draft depends on the following module drafts for cross-cutting behavior. References are non-authoritative until a promotion decision assigns canonical ownership.

- `PRD-MOD-VALIDATION-TRACEABILITY`
- `PRD-MOD-DOMAIN-PACK`
- `PRD-MOD-OPERATIONS-MAINTENANCE`
- `PRD-MOD-INTERFACE-INTEGRATION`
- `PRD-MOD-ROLE-GOVERNANCE`

## 5. Functional Scope

- Invoke independent security, safety, privacy, and compliance review early for sensitive, high-impact, regulated, externally connected, self-modifying, or materially autonomous target systems.
- Apply the precedence order `law and mandatory platform policy -> safety/security/privacy/compliance -> source authority, host permissions, and human approvals -> approved Sys4AI governance floor -> approved target values -> ordinary preferences`.
- Values shall not grant permission, waive controls, authorize data access, lower evaluation thresholds, replace required human approval, or justify bypassing host or project restrictions. Material conflicts require a typed, accountable decision with contrary evidence and downstream impact.
- Minimize sensitive elicitation data through purpose limitation, least-data collection, source authorization, classification, redaction, no-secret defaults, bounded retention, controlled access, explicit downstream use, and disposition evidence. Missing sensitive facts remain open issues rather than invitations to collect excess data.
- Keep YAML and TOML examples secret-free by default; require a later controlled security design before any real secret-management feature or example is introduced.
- Preserve lightweight, justified, version-compatible dependencies and reject heavy runtime or data services without an approved implementation need and security review.
- Require bounded Meta-Agent self-change controls for changes to identity, purpose, values, authority, permissions, evaluators, acceptance criteria, production thresholds, and authority hierarchy. A runtime actor cannot accept its own consequential change.
- Keep reflection depth at one by default. Expansion requires a threat model, explicit maximum depth and termination condition, least privilege, independent evaluation, protected holdouts, rollback, emergency stop, and accountable human approval.
- Require threat and hazard analysis, permission inventory, control mapping, negative tests, hostile-input handling, cross-layer and cross-target isolation, residual-risk ownership, incident readiness, cancellation, and rollback evidence appropriate to scope.
- Keep the result at `validated_prototype` or lower until all separately governed production evidence is accepted; local tests, structural validation, reference holdouts, or G-08 approval cannot establish production readiness.

## 6. Non-Goals

- Promote this module to canonical status.
- Supersede Phase 0, Phase 1, or Phase 2 PRDs.
- Rewrite requirement IDs or trace selectors.
- Treat generated documentation, memory hits, or wiki pages as source authority.
- Treat approved values as a permission source, control waiver, risk acceptance, or production-approval substitute.
- Collect sensitive elicitation data merely because it may be useful, or place secrets in examples, prompts, logs, generated pages, or uncontrolled evidence.
- Claim external evaluator independence, confidential holdouts, behavioral alignment, production readiness, operational authority, broad stakeholder consensus, or domain truth from TX-17, G-08, or TX-19 evidence.

## 7. Traceability Requirements

- Registry row: `Sys4AI/registries/prd_module_registry.csv` records this module as `draft` and `derivative_draft`.
- Requirement trace: matching source requirements retain independent approval, capability, verification, freshness, and semantic-review states; this module path is derivative evidence only.
- Source registry: this file is registered as a derivative draft source.
- Object relationships: this module traces to the decomposition strategy and TX-19 plan, derives from all four source PRDs, and references the G-08 decision without changing it.
- Assurance claims must trace to controlled threat, permission, evaluation, holdout, rollback, and acceptance evidence; this module cannot serve as sole evidence for any safety or production claim.

## 8. Validation Requirements

- `make validate-prd-modules` must pass.
- `make validate-safety-evaluation` must pass while retaining its explicit structural and local-evidence limitations.
- `make validate-strategic-intent` and `make validate-prd-semantics` must pass.
- `make validate-roles` and `make validate-artifact-contracts` must pass where separation of duties or assurance artifacts are implicated.
- `make validate-requirement-trace` must pass.
- `make validate-registry-graph` must pass.
- `make validate-capability-migration` and `make validate-generated-derivatives` must pass.
- Negative probes must reject model self-approval, values-based permission expansion, evaluator conflicts, threshold mutation, missing holdouts or rollback, excessive reflection, hostile-input failure, cross-layer or cross-target escape, secret-bearing examples, and unsupported production claims.
- Passing structural validation does not prove ethical correctness, behavioral alignment, external independence, production safety, operational authority, stakeholder consensus, or domain truth.

## 9. Promotion Conditions

Promotion requires a later source-authority decision that states the module decision, canonical effect, threat and privacy impact, permission consequences, separation of duties, trace migration, evaluation evidence, rollback, and supersession. It must preserve one canonical owner per requirement family and cannot infer promotion from TX-19 regeneration.

## 10. Open Issues

- Confidential, externally curated, independently rotated holdouts remain absent.
- Quantitative strategic-success thresholds and real-host operational evidence remain future obligations.
- Production secret management, target-specific legal or regulatory controls, service thresholds, operational ownership, and incident exercises remain outside TX-19.

## 11. Acceptance Evidence

TX-19 acceptance evidence for this module is limited to accurate derivative allocation, approved-baseline provenance, complete WS-14 value-precedence and sensitive-data obligations, explicit production limits, noncanonical status, and validator passage. It does not satisfy G-07 or G-10, prove safety or alignment, grant permission or operational authority, or establish production or domain acceptance.

## 12. Change Control

This draft may be revised, split, merged, deferred, replaced, or promoted only through a bounded source-authority workflow with threat, privacy, permission, evaluation, validation, rollback, receipt, and handoff evidence. Changes to approved vision, values, or their precedence require accountable human supersession of the G-08 decision. Until then, the registered source PRDs, decisions, assurance records, and trace records control.

## References

AngryOwlAI. (2026a). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

AngryOwlAI. (2026b). *Sys4AI Phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

AngryOwlAI. (2026c). *Sys4AI Phase 2 walking skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

AngryOwlAI. (2026d). *Sys4AI Phase 2 strategic baseline addendum* [Product requirements document addendum]. `PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md`.

AngryOwlAI. (2026e). *DDR-SFADEV-STRATEGIC-BASELINE-G08-001: Strategic vision and core-values approval* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G08-001.yaml`.

AngryOwlAI. (2026f). *Sys4AI strategic baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.

AngryOwlAI. (2026g). *Sys4AI PRD decomposition strategy* [Decomposition strategy]. `PRDs/PRD_decomposition_strategy.md`.
