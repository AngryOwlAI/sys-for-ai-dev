---
artifact_id: SFA-PRD-PRODUCT-BASELINE-001
artifact_type: prd
subject: sys4ai
subject_layer: framework
authority: canonical
status: active
approval: approved
implementation: partial
validation: planned
owner: system_director
supersedes: Sys4AI_phase-0_product_system_design_prd
source_trace:
  - PRDs/Sys4AI_phase-0_product_system_design_prd.md@pre-reboot-2026-07-15
  - PRDs/baselines/phase-1-initialization-baseline.md
  - PRDs/baselines/phase-2-walking-skeleton-baseline.md
  - PRDs/baselines/phase-2-strategic-addendum.md
---

# Sys4AI Product Baseline PRD

## 1. Purpose

Sys4AI shall be a host-neutral framework product and executable meta-agent
runtime for designing, building, verifying, operating, maintaining, improving,
and retiring governed AI agents and agentic systems.

This PRD defines durable product behavior. It does not define the one-time
Sys4AI-dev repository migration, which is governed by the repository reboot
PRD.

## 2. System identity and model levels

- **PB-001:** Sys4AI shall remain distinct from Sys4AI-dev, any execution host,
  every generated target framework, every target instance, and every generated
  reader or evidence surface.
- **PB-002:** The product shall represent development context D, host H,
  framework product M2, target framework M1, target instance M0, and reader or
  evidence surface R as distinct classifications.
- **PB-003:** Self-hosting shall be a relation in which trusted release N helps
  produce a separate candidate N+1; it shall not be modeled as identity among
  repository, runtime, product, target, and authority.
- **PB-004:** The product shall be installable, testable, and buildable without
  its development repository.

## 3. Product boundary and architecture

- **PB-010:** Domain semantics shall be independent of Codex, GitHub, a local
  filesystem layout, and a specific CLI.
- **PB-011:** Application services shall cover discovery, specification,
  architecture, planning, bounded execution, verification, target generation,
  operations, knowledge retrieval, and governance.
- **PB-012:** External capabilities shall be supplied through explicit ports
  for models, human approval, workspace access, files, source control, tool
  execution, state, artifact catalogs, events, clocks, secrets, and host
  capabilities.
- **PB-013:** Concrete adapters may support Codex, a standalone CLI,
  filesystems, Git, GitHub, local state, JSON Schema, YAML, and other hosts
  without changing domain authority.
- **PB-014:** Framework assets—skills, templates, role catalogs, contracts,
  policies, verification patterns, and domain-pack contracts—shall be
  versioned data, not mutable runtime state.
- **PB-015:** Mutable runtime state shall live in a target workspace under
  `.sys4ai/` or another configured external state store, never inside the
  installed source package.

## 4. Core domain invariants

- **PB-020:** Requirements shall have stable identifiers and traceable source
  authority.
- **PB-021:** Authority, lifecycle, approval, implementation, validation,
  capability, and evidence freshness shall remain independent dimensions.
- **PB-022:** Approval and implementation shall remain distinct; validation
  shall not imply operational authority.
- **PB-023:** Evidence shall support claims but shall not create permissions or
  promote itself to authority.
- **PB-024:** Generated artifacts and target systems shall not approve their own
  promotion into product authority.
- **PB-025:** Execution shall require an explicit authorization and permission
  envelope.
- **PB-026:** A material self-change shall require independent verification and
  accountable human promotion.
- **PB-027:** Target frameworks and target instances shall retain authority
  boundaries independent from Sys4AI's own authority.

## 5. Lifecycle

The controlled lifecycle is:

1. Design
2. Develop
3. Implement
4. Test
5. Run
6. Maintain
7. Improve
8. Retire

- **PB-030:** Every stage shall define entry criteria, inputs, roles,
  permissions, activities, outputs, evidence, exit criteria, failure behavior,
  allowed transitions, rollback or return behavior, and review cadence.
- **PB-031:** Testing shall be both a named stage and a cross-cutting gate.
- **PB-032:** No transition shall skip required test, verification, validation,
  evaluation, security, permission, release, or human-approval gates.
- **PB-033:** Improvement shall be evidence-driven and shall return through the
  required design, implementation, and test gates.
- **PB-034:** Retirement shall define archival, data disposition, credential
  withdrawal, authority withdrawal, and rollback limits.
- **PB-035:** Coordination patterns shall include linear workflow,
  goal-directed autonomous agent, role-based multi-agent, production
  orchestration, and hybrid.
- **PB-036:** Operational maturity shall distinguish concept, prototype,
  validated prototype, production candidate, production approved, operational,
  maintenance, and retired.

## 6. Roles, skills, and artifacts

- **PB-040:** Role types shall define mission, system-layer scope, required and
  optional skills, prohibited capabilities, outputs, and authority limits.
- **PB-041:** Development roles, framework roles, and target-project roles shall
  not be silently conflated.
- **PB-042:** Product skills shall be host-neutral, project-neutral, versioned
  independently, and free of Sys4AI-dev state assumptions.
- **PB-043:** Promotion from a development skill to a product skill shall be an
  explicit review and generalization event.
- **PB-044:** Controlled artifacts shall identify artifact type, subject,
  subject layer, authority, lifecycle status, owner, supersession, and source
  trace using a concise common metadata contract.
- **PB-045:** Each authoritative fact shall have one authority source.
  Generated indexes may provide navigation but shall not duplicate authority.

## 7. Source-first knowledge and traceability

- **PB-050:** Memory and search shall navigate to registered canonical sources;
  retrieval results shall not decide truth or permission.
- **PB-051:** Search results shall expose authority class, source path,
  validation status, freshness, and the required next inspection action.
- **PB-052:** Traceability shall link intent and requirements to exact
  implementation artifacts, validation evidence, unresolved gaps, and
  handoff/release evidence.
- **PB-053:** Missing evidence shall be represented as a gap, not inferred from
  plan text or generated summaries.

## 8. Execution and permissions

- **PB-060:** A bounded execution transaction shall identify subject, actor,
  authorization source, allowed reads and writes, tool and network permissions,
  acceptance checks, rollback, stop conditions, and resulting evidence.
- **PB-061:** The runtime shall fail closed when authority, required host
  capability, permission, or validation evidence is missing.
- **PB-062:** The product shall not execute arbitrary commands merely because a
  plan contains them; a host adapter and permission envelope must authorize the
  action.
- **PB-063:** Human approval ports shall be required for purpose changes,
  authority expansion, production promotion, safety-threshold changes, and
  acceptance of material residual risk.

## 9. Target-system generation

- **PB-070:** Sys4AI shall generate a target package with explicit governance,
  requirements, architecture, runtime, skills, contracts, tests, operations,
  and evidence layers.
- **PB-071:** A target package may represent one agent, a workflow, a
  multi-agent system, an agentic application, a reusable framework, or an
  organizational platform.
- **PB-072:** Generated target content shall remain derivative until accepted
  by the target's accountable authority.
- **PB-073:** At least one integration fixture shall prove the flow from intent
  through discovery, requirements, architecture, plan, bounded execution,
  validation, and package output.

## 10. Product CLI and host behavior

- **PB-080:** The `sys4ai` CLI shall initialize target workspaces, capture
  discovery, validate target artifacts, create implementation plans, process
  authorized transactions, generate target packages, inspect memory and trace,
  and run product-level verification.
- **PB-081:** The product CLI shall not contain Sys4AI-dev program management,
  historical migration validation, root PRD validation, development receipt
  generation, or root workflow inspection.
- **PB-082:** Codex shall be the first reference host, not the source of product
  purpose or authority.

## 11. Verification, assurance, and operations

- **PB-090:** Product contracts, assets, package behavior, lifecycle
  transitions, permissions, traceability, and self-change boundaries shall have
  deterministic positive and negative tests.
- **PB-091:** Verification, stakeholder validation, evaluation, security
  review, and production approval shall remain distinct evidence classes.
- **PB-092:** Generic assurance protocols and holdout templates may ship with
  the product; evaluations of Sys4AI-dev and transaction-numbered measurements
  shall not.
- **PB-093:** Target operations shall define monitoring, incidents, updates,
  maintenance, improvement cadence, and retirement.
- **PB-094:** No structural test result shall be described as proof of domain
  truth, stakeholder consensus, ethical correctness, production readiness, or
  operational authority.

## 12. Packaging

- **PB-100:** The distribution, Python package, and CLI names shall be
  `sys4ai`; the development repository shall remain `Sys4AI-dev`.
- **PB-101:** Permanent source modules shall use capability names rather than
  temporary phase or transaction identifiers.
- **PB-102:** Product validation shall expose install, lint, test,
  contract-validation, asset-validation, and build commands using product-local
  paths only.

## 13. Self-hosting

- **PB-110:** Stage 0 shall use a bootstrap development runtime to build the
  product.
- **PB-111:** Stage 1 shall produce a versioned, installable Sys4AI release.
- **PB-112:** Stage 2 shall use a trusted release to modify only a separate
  candidate workspace.
- **PB-113:** Stage 3 shall independently verify the candidate against the same
  invariant suite and protected holdouts.
- **PB-114:** Stage 4 shall require accountable human promotion and preserve a
  rollback release.
- **PB-115:** The candidate shall not approve its own purpose, authority,
  thresholds, safety waivers, production readiness, or deletion of rollback.

## 14. Product acceptance

The baseline is satisfied for a release only when the product:

- builds and tests independently from inside `Sys4AI/`;
- contains no development state or transaction history;
- has no dependency on a parent path or hidden development skill surface;
- generates and validates a target fixture through an installed product;
- preserves explicit authority, permission, evidence, and self-hosting
  boundaries; and
- reports unresolved semantic, stakeholder, operational, and production gaps
  without overclaiming.
