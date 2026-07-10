# Sys4AI Phase 1 Implementation Initialization PRD

**Document status:** Canonical draft; `TX-06-P1-BASELINE` initialization baseline accepted
**Product name:** `Sys4AI`
**Phase:** Phase 1: Implementation initialization
**Depends on:** `PRDs/Sys4AI_phase-0_product_system_design_prd.md`
**Strategic-baseline authority:** `DDR-SFADEV-STRATEGIC-BASELINE-G03-001`
**Approval boundary:** `G-03` authorizes implementation initialization; `G-08` remains the only final vision/core-values approval gate.
**Last updated:** 2026-07-09

---

## 1. Executive summary

Phase 1 initializes the `Sys4AI` implementation repository so development can begin safely, reproducibly, and with source-first governance. Phase 1 does not finish the framework. It creates the first executable spine: Python environment, dependency policy, YAML control records, validators, skill adapters, memory registries, documentation policies, and a Docker decision record.

This revision also initializes the core file-format memory profile spine required by Phase 0: Markdown, CSV, YAML, TOML, and JSON Schema. Phase 1 adds minimal registries, examples, validators, dependency policy, and generated derivative stubs for YAML/TOML configuration-control artifacts and JSON Schema validation contracts. Phase 1 does not build a full wiki engine, does not introduce a vector database, does not make Obsidian canonical, and does not create a standalone JSON wiki by default.

This revision also initializes the discovery-gate, system-layer, self-hosting, role-governance, and skill-lifecycle obligations added to Phase 0. Phase 1 records the first executable registries, templates, validators, and control records needed to keep those concerns auditable without treating discovery candidates as approved requirements.

`TX-06-P1-BASELINE` adds the implementation requirements needed to realize the `G-03`-accepted identity, lifecycle, coordination-pattern, and operational-maturity baseline and to support the still-candidate vision and core values without approving them. It requires strategic-intent, portable-execution, runtime-actor, lifecycle, pattern, host-profile, capability-state, semantic-validation, package, self-change, and generated-derivative initialization surfaces. This transaction defines implementation obligations only; it does not create `G-04`-blocked contracts, verify `G-07` host capabilities, satisfy `G-08`, restore removed AgentJob or `/continue` runtime behavior, or claim operational completion.

The default Phase 1 environment is a local Python virtual environment. Docker is deferred unless the environment decision record identifies concrete OS-level dependencies, multi-service orchestration needs, CI parity needs, or target-runtime template needs.

---

## 2. Goals

1. Create a minimal but real Python reference implementation scaffold.
2. Add `PyYAML` and safe YAML parsing as a first dependency.
3. Provide a repo-local `.venv` setup path.
4. Add a Makefile and CLI for validation commands.
5. Create initial YAML examples and schema-like specs.
6. Add source-first memory registries and bootstrap logic.
7. Add all core skill adapter shells from `ai-skills-for-sys`.
8. Add implementation plans and task packets for the next agent pass.
9. Decide whether Docker is needed now, later, or only for generated target systems.
10. Initialize core file-format memory profiles for Markdown, CSV, YAML, TOML, and JSON Schema.
11. Add initial format-profile, configuration-source, control-record, and validation-contract registries.
12. Add TOML configuration examples and parser support.
13. Add JSON Schema validation-contract examples and executable contract validation.
14. Add generated or stub-generated Configuration and Control Wiki pages for registered YAML and TOML artifacts.
15. Add generated or stub-generated Validation Contracts Catalog pages for JSON Schema contracts.
16. Extend Makefile and CLI validation commands to cover format profiles, TOML configuration, JSON Schema contracts, and derivative trace checks.
17. Initialize a Requirements Discovery Record gate before formal USRD generation for new or substantially changed system definitions.
18. Initialize system-layer and self-hosting controls for development-system, framework-product, target-template, target-instance, and derivative-surface work.
19. Initialize controlled role governance, role-to-skill crosswalks, temporary-role policy, and role execution-binding validation.
20. Initialize core skill lifecycle statuses and governed core skill expansion workflow.
21. Initialize `/init` as the gated Sys4AI system-definition and adoption front door.
22. Initialize target vision and core-values templates, evidence, approval-state, waiver, supersession, and impact-analysis obligations.
23. Initialize a harness-neutral bounded-execution contract, independent runtime-actor representation, and portable program-state migration.
24. Initialize the accepted lifecycle and pattern baseline with explicit transition, evidence-class, maturity, promotion, and retirement validation requirements.
25. Initialize a versioned Codex reference-host capability profile without embedding host mechanics in portable semantics.
26. Initialize independent capability, evidence, approval, validation, and requirement-lifecycle states plus semantic and capability-migration validation.
27. Initialize strategic target-package content, bounded self-change controls, and deterministic noncanonical derivative indexes.

---

## 3. Non-goals

- Do not implement a production runtime service.
- Do not add a vector database.
- Do not build a full generated wiki engine.
- Do not force Docker as the default developer environment.
- Do not treat Obsidian as canonical memory.
- Do not import external skill files without local adaptation and provenance records.
- Do not implement target-domain agent systems yet.
- Do not build a production memory database.
- Do not build a full interactive wiki engine.
- Do not create a standalone JSON wiki unless a later PRD introduces general JSON source or memory artifacts.
- Do not treat generated Configuration and Control Wiki pages as canonical.
- Do not treat generated Validation Contracts Catalog pages as canonical.
- Do not support TOML writing or style-preserving TOML editing in Phase 1.
- Do not support secret-bearing YAML or TOML configuration files in Phase 1.
- Do not treat JSON Schema validation as semantic or domain acceptance.
- Do not convert all existing schema-like YAML specs in one step if doing so would destabilize the scaffold.
- Do not treat Requirements Discovery Record candidate requirements as approved or baselined requirements.
- Do not promote product-scaffold skills into active development runtime without a runtime registry decision.
- Do not implement all proposed core organizational skills in this PRD-only integration step.
- Do not treat `G-03` baseline acceptance as `G-08` approval of the candidate Sys4AI vision or core values.
- Do not create strategic-intent templates, schemas, package contracts, or concrete typed interfaces before `G-04` approves their producers, consumers, fields, approval rules, and validators.
- Do not claim Codex or compatible-host capabilities before `G-07` verification.
- Do not restore AgentJob authoring, `/continue`, the removed control loop, deleted CLI/Make targets, or removed runtime skills by implication.
- Do not represent Phase 1 requirement initialization as implemented lifecycle, production, host, package, or self-change capability.

---

## 4. Initialization requirements

### 4.1 Repository layout

`SFA-P1-INIT-REPO-001`: Add a Python scaffold under `Sys4AI/sys_for_ai/`.

`SFA-P1-INIT-REPO-002`: Add `Sys4AI/requirements.txt`, `Sys4AI/pyproject.toml`, and `Sys4AI/Makefile`.

`SFA-P1-INIT-REPO-003`: Add folders for `schemas`, `control_records`, `registries`, `skills`, `docs`, and `templates`.

`SFA-P1-INIT-REPO-004`: Preserve top-level PRDs and implementation plans outside the implementation package.

`SFA-P1-INIT-REPO-005`: Add `configs/`, `schemas/contracts/`, `docs/generated/configuration_control/`, and `docs/generated/validation_contracts/` for the initial format-profile scaffold.

### 4.2 Python environment

`SFA-P1-INIT-ENV-001`: Use a local `.venv` as the required Phase 1 development environment.

`SFA-P1-INIT-ENV-002`: Keep `.venv/`, cache files, generated local vaults, and local receipts out of source control unless explicitly promoted.

`SFA-P1-INIT-ENV-003`: Provide setup commands through the Makefile:

```bash
cd Sys4AI
make venv
make install
make doctor
```

`SFA-P1-INIT-ENV-004`: Provide direct interpreter examples:

```bash
.venv/bin/python -m sys_for_ai.cli doctor
.venv/bin/python -m sys_for_ai.cli validate
```

### 4.3 Dependencies

`SFA-P1-INIT-DEP-001`: Add `PyYAML` as the initial required dependency.

`SFA-P1-INIT-DEP-002`: Pin the dependency family conservatively enough to avoid accidental major-version breaks.

`SFA-P1-INIT-DEP-003`: Add no heavy runtime dependencies until an implementation plan justifies them.

`SFA-P1-INIT-DEP-004`: Add JSON Schema validation support through a lightweight Python dependency.

`SFA-P1-INIT-DEP-005`: Add TOML parser support consistent with the supported Python version range. If Python `>=3.10` remains supported, Phase 1 shall add a conditional `tomli` dependency for Python versions below 3.11. If the project raises its minimum Python version to `>=3.11`, Phase 1 may use standard-library `tomllib` without `tomli`.

`SFA-P1-INIT-DEP-006`: Phase 1 shall not add TOML writing, style-preserving TOML editing, vector databases, production memory services, or heavy runtime dependencies for this feature.

### 4.4 YAML records and validators

The AgentJob requirements in this subsection preserve implemented historical-compatibility evidence. They do not make AgentJob the active portable execution contract or authorize restoration of removed AgentJob-authoring or `/continue` behavior. New active execution examples and state shall use the bounded execution semantics required in Section 4.15 after their own contract transaction is approved and implemented.

`SFA-P1-INIT-YAML-001`: Preserve the existing smoke-test AgentJob YAML as a readable historical-compatibility fixture; new active execution examples shall use the approved portable bounded-execution contract.

`SFA-P1-INIT-YAML-002`: Preserve schema-like YAML specifications needed to validate historical AgentJob records and current skill manifests without treating the historical AgentJob contract as active framework execution authority.

`SFA-P1-INIT-YAML-003`: Add validators that use `yaml.safe_load`.

`SFA-P1-INIT-YAML-004`: Historical AgentJob fixture validation shall fail on missing required legacy fields, and current skill-manifest validation shall fail on malformed entries; either check shall remain distinct from portable execution capability validation.

`SFA-P1-INIT-YAML-005`: Add handoff, completion receipt, and state snapshot YAML examples that carry source-first format-profile evidence.

`SFA-P1-INIT-YAML-006`: YAML control/state examples shall parse with safe YAML loading and validate against JSON Schema contracts where contracts exist.

### 4.5 Skill import and adaptation

`SFA-P1-INIT-SKILL-001`: Add a `core_skill_manifest.yaml` listing every current core skill from `ai-skills-for-sys`.

`SFA-P1-INIT-SKILL-002`: Add adapter shell folders for each core skill.

`SFA-P1-INIT-SKILL-003`: Each adapter shall include `SKILL.md`, `README.md`, `AGENTS.md`, and `examples/portable-example.md`.

`SFA-P1-INIT-SKILL-004`: Each adapter shall record source provenance and local adaptation status.

`SFA-P1-INIT-SKILL-005`: Exact upstream content synchronization shall be done by a later explicit import task, not silently.

### 4.6 Memory scaffold

`SFA-P1-INIT-MEM-001`: Add initial CSV registries for sources, derivatives, object relationships, and skills.

`SFA-P1-INIT-MEM-002`: Add a memory bootstrap command that creates missing registries with expected headers.

`SFA-P1-INIT-MEM-003`: Add documentation for source-first authority and derivative-surface policy.

`SFA-P1-INIT-MEM-004`: Obsidian support shall be documented as optional and derivative.

`SFA-P1-INIT-MEM-005`: Add `format_profile_registry.csv` for Markdown, CSV, YAML, TOML, and JSON Schema profile rows.

`SFA-P1-INIT-MEM-006`: Add `config_source_registry.csv` for registered TOML configuration sources and later configuration formats.

`SFA-P1-INIT-MEM-007`: Add `control_record_registry.csv` for registered YAML control/state artifacts.

`SFA-P1-INIT-MEM-008`: Add `validation_contract_registry.csv` for JSON Schema contracts and later validation-contract formats.

`SFA-P1-INIT-MEM-009`: Update source and derivative registries so canonical source files and generated derivative stubs remain distinguishable.

### 4.7 Core format-profile scaffold

`SFA-P1-INIT-FORMAT-001`: Initialize the core file-format profile scaffold without promoting generated derivatives to canonical authority.

`SFA-P1-INIT-FORMAT-002`: Add TOML examples under `configs/examples/` for framework configuration and target-project configuration.

`SFA-P1-INIT-FORMAT-003`: Add JSON Schema contracts under `schemas/contracts/` for historical AgentJob compatibility, handoff, completion receipt, state snapshot, TOML configuration, and registry-row structures. The later portable execution-transaction schema shall be a distinct contract and shall not silently mutate historical AgentJob records.

`SFA-P1-INIT-FORMAT-004`: Add policy documents for format profiles, Configuration and Control Wiki behavior, and Validation Contracts Catalog behavior.

`SFA-P1-INIT-FORMAT-005`: Add generated or stub-generated Configuration and Control Wiki pages under `docs/generated/configuration_control/`.

`SFA-P1-INIT-FORMAT-006`: Add generated or stub-generated Validation Contracts Catalog pages under `docs/generated/validation_contracts/`.

`SFA-P1-INIT-FORMAT-007`: Generated wiki/catalog pages shall contain non-canonical authority notices, source trace placeholders or populated source trace, registry evidence, generator metadata, and stale/orphan status.

### 4.8 Docker decision

`SFA-P1-INIT-DOCKER-001`: Add an environment decision record that chooses `.venv` as the Phase 1 baseline.

`SFA-P1-INIT-DOCKER-002`: Defer development Docker until a trigger exists: OS-level rendering dependencies, multi-service runtime, strict CI parity, contributor environment drift, or target-runtime generation.

`SFA-P1-INIT-DOCKER-003`: Keep development environment containers separate from target-system runtime container templates.

### 4.9 Validation

`SFA-P1-INIT-VAL-001`: Add `make doctor` to check Python, PyYAML, package import, and expected folders.

`SFA-P1-INIT-VAL-002`: Add `make validate-agentjob`, `make validate-skills`, `make bootstrap-memory`, and `make validate`.

`SFA-P1-INIT-VAL-003`: Validation shall be deterministic and runnable offline after dependencies are installed.

`SFA-P1-INIT-VAL-004`: Add validation commands for format profiles, configuration sources, control records, validation contracts, TOML configuration, JSON Schema contracts, registry graph consistency, generated Configuration and Control Wiki stubs, and generated Validation Contracts Catalog stubs.

`SFA-P1-INIT-VAL-005`: Validation shall fail or warn when governed YAML, TOML, JSON Schema, or CSV artifacts are missing registry rows, reference missing validation contracts, point to missing source files, or appear as generated derivatives with canonical authority.

`SFA-P1-INIT-VAL-006`: Validation shall fail or warn when YAML or TOML examples contain secret-like keys or values according to Phase 1 security policy.

`SFA-P1-INIT-VAL-007`: Validation shall preserve the distinction between structural admissibility and semantic/domain correctness.

`SFA-P1-INIT-VAL-008`: Add a PRD requirement trace validator that checks requirement ID uniqueness and verifies that Phase 0 requirement IDs have explicit Phase 1 coverage, partial coverage, deferral, or not-applicable trace rows with semantic trace classes, justification for partial, deferred, or out-of-phase mappings, and a semantic review verdict for each non-implemented trace row.

`SFA-P1-INIT-VAL-009`: Add a dedicated `make validate-roles` target for controlled role catalogs, role-to-skill crosswalks, execution-binding constraints, generated role Markdown freshness, and role-related proposed skill references. The aggregate `make validate` target shall include `make validate-roles` so role-catalog drift is checked by default.

### 4.10 Discovery Gate Initialization

`SFA-P1-INIT-DISC-001`: Add the Requirements Discovery Record to the artifact catalog, source registry, derivative registry policy, and trace model.

`SFA-P1-INIT-DISC-002`: Add or extend a discovery-record registry that records RDR path, subject system ID, subject layer, producing execution-transaction ID, optional legacy producer AgentJob ID, authority status, candidate requirement count, open question count, downstream USRD link, validation status, source hash, and last validation timestamp.

`SFA-P1-INIT-DISC-003`: Add a bounded execution-transaction example for running `system-definition-interview-context-45` on a new target system or framework-product change. Existing AgentJob examples remain historical provenance and shall not be recommended as the active route.

`SFA-P1-INIT-DISC-004`: Add a sample completion receipt showing RDR creation, validation evidence, open issues, and recommended next route.

`SFA-P1-INIT-DISC-005`: Extend aggregate validation so discovery-record templates and registered discovery records are validated by default.

### 4.10.1 `/init` Front-Door Initialization

`SFA-P1-INIT-FRONTDOOR-001`: Add active runtime skill package `.agents/skills/init/` with `SKILL.md`, `README.md`, `AGENTS.md`, `skill.yaml`, and a portable example.

`SFA-P1-INIT-FRONTDOOR-002`: Add `.codex/skills/init/SKILL.md` as a compatibility shim that points to `.agents/skills/init/` and does not carry independent behavior.

`SFA-P1-INIT-FRONTDOOR-003`: Add `Sys4AI/skills/core/init/` as the product-scaffold reference package for future target systems.

`SFA-P1-INIT-FRONTDOOR-004`: Register `init` in the runtime skill registry, core systems engineering bundle, product core skill manifest, skill registry, core skill proposal registry, role-to-skill crosswalk, object relationship registry, source registry, and requirement trace registry.

`SFA-P1-INIT-FRONTDOOR-005`: Extend the skill-manifest validator so `init` is required by the core skill set.

`SFA-P1-INIT-FRONTDOOR-006`: Add a Current-State Baseline template for brownfield discovery and mark it as draft evidence rather than canonical authority.

`SFA-P1-INIT-FRONTDOOR-007`: Add tests that verify `/init` exists in runtime, shim, and product-scaffold surfaces; brownfield first pass is read-only; Product Requirements Document creation is gated; candidate requirement labels are preserved; and product-scaffold wording does not claim active runtime authority.

`SFA-P1-INIT-FRONTDOOR-008`: Preserve the completed `/init` Director decision, AgentJob, memory preflight receipt, completion receipt, and handoff as historical implementation evidence. Later `/init` implementation changes shall use the approved portable execution-transaction contract rather than restoring AgentJob as active framework semantics.

### 4.11 System-Layer and Self-Hosting Initialization

`SFA-P1-INIT-LAYER-001`: Add a controlled system-layer registry for `development_system`, `framework_product`, `target_system_template`, `target_system_instance`, and `derivative_surface`.

`SFA-P1-INIT-LAYER-002`: Add a self-hosting mode policy document that distinguishes `Sys4AI-dev` active runtime authority from `Sys4AI` product scaffold authority.

`SFA-P1-INIT-LAYER-003`: Add a self-hosting TOML configuration source and register it in `config_source_registry.csv`.

`SFA-P1-INIT-LAYER-004`: Add `validate-system-layers` to verify allowed layer IDs, canonical roots, derivative roots, authority mutation rules, and self-hosting constraints.

### 4.12 Role Governance Initialization

`SFA-P1-INIT-ROLE-001`: Phase 1 shall implement a controlled role registry.

`SFA-P1-INIT-ROLE-002`: Phase 1 shall implement a role-to-skill crosswalk registry.

`SFA-P1-INIT-ROLE-003`: Phase 1 shall implement role execution-binding validation.

`SFA-P1-INIT-ROLE-004`: Phase 1 shall support one-Job temporary roles with expiry, authority scope, required skills, allowed artifacts, validators, and supersession policy.

`SFA-P1-INIT-ROLE-005`: Phase 1 aggregate validation shall include role-governance checks by default.

### 4.13 Core Skill Expansion Initialization

`SFA-P1-INIT-CORESKILL-001`: Phase 1 shall extend skill registry data with lifecycle status, authority surface, provenance, role bindings, validation commands, and activation constraints.

`SFA-P1-INIT-CORESKILL-002`: Phase 1 shall add or update a skill-lifecycle validator that checks controlled statuses and rejects active-runtime use of non-active skill packages.

`SFA-P1-INIT-CORESKILL-003`: Phase 1 shall add governed proposal surfaces for core organizational skills and shall distinguish them from project-specific domain packs.

`SFA-P1-INIT-CORESKILL-004`: Phase 1 shall provide minimal scaffold or runtime packages for approved core organizational skills only through controlled execution transactions. Completed AgentJobs may remain cited as historical implementation evidence.

`SFA-P1-INIT-CORESKILL-005`: Phase 1 aggregate validation shall include skill-lifecycle checks by default after the registry/schema expansion slice creates the required data model.

### 4.14 Vision and Core-Values Initialization

The requirements in this subsection initialize controlled support for Sys4AI and target-system strategic intent. They do not approve the candidate Sys4AI vision or values, substitute model judgment for represented stakeholders, or satisfy `G-08`.

`SFA-P1-INIT-STRAT-001`: Require separate `Sys4AI/templates/governance/target-vision-statement-template.md` and `Sys4AI/templates/governance/target-core-values-template.md` governance templates that produce target-specific vision and core-values artifacts without duplicating the candidate Sys4AI product wording.

`SFA-P1-INIT-STRAT-002`: Extend Requirements Discovery Record and temp-PRD contracts with strategic-intent candidates, source evidence, inference labels, missing-stakeholder state, approval identity, inherited constraints, value conflicts, anti-values, waivers, review cadence, coordination-pattern candidates, operational maturity, autonomy, integrations, communication, monitoring, degraded mode, and promotion evidence.

`SFA-P1-INIT-STRAT-003`: Require artifact-contract, source, object-relationship, and requirement-trace rows for target vision, target core values, their approvals, active versions, supersession, waivers, and downstream consumers.

`SFA-P1-INIT-STRAT-004`: Require target-package manifests to reference strategic-intent artifact paths, vision and value IDs, content-approval states, approval evidence, source hashes, active versions, waiver references, and impact-analysis state.

`SFA-P1-INIT-STRAT-005`: Require a focused `validate-strategic-intent` validator with direct CLI and Make targets, aggregate-validation integration, structural-versus-semantic limitation language, stable-ID and state checks, source/approval evidence checks, and rejection of model self-approval or permission expansion from values.

`SFA-P1-INIT-STRAT-006`: Require greenfield and brownfield examples plus positive and negative tests for approval gates, missing stakeholders, inference labeling, waiver expiry, supersession, stale hashes, impact analysis, self-approval, and candidate content falsely represented as approved.

`SFA-P1-INIT-STRAT-007`: Require strategic-intent discovery and validation to consume a registered Codex or compatible-host capability profile where host behavior matters while failing closed on unknown or unverified capabilities.

`SFA-P1-INIT-STRAT-008`: Preserve `G-08` as the only final Sys4AI vision/core-values approval gate; `G-03`, canonical location, structural validation, implementation progress, and model authorship shall not satisfy the approved-vision or approved-values requirements.

### 4.15 Runtime Actor, Portable Execution, State, and Binding Initialization

`SFA-P1-INIT-ACTOR-001`: Add `runtime_actor` representation independently from `subject_layer` across applicable execution, role-binding, approval, trace, state, and handoff artifacts.

`SFA-P1-INIT-ACTOR-002`: Runtime-actor fields shall distinguish the acting runtime or human from the accountable approval principal, delegated role, verifier, accepter, host harness, and target runtime; no actor field shall create authority by implication.

`SFA-P1-INIT-EXEC-001`: Require a harness-neutral bounded `ExecutionTransaction` contract with transaction ID and version, objective, source requirement and decision IDs, subject system and layer, runtime actor, approval principal, permission envelope, allowed reads, allowed writes, allowed tools and external actions, forbidden actions, inputs, expected outputs, validators, stop conditions, cancellation, escalation, state, resume evidence, closeout evidence, rollback, and supersession.

`SFA-P1-INIT-EXEC-002`: The portable execution model shall represent `proposed`, `authorized`, `active`, `blocked`, `cancelled`, `completed`, `accepted`, and `superseded` states and shall retain explicit current-state, continuation, cancellation, escalation, resume, closeout, and rollback evidence.

`SFA-P1-INIT-EXEC-003`: AgentJob and `/continue` shall remain historical or optional-profile concepts only. Phase 1 shall not restore removed authoring skills, control-loop modules, CLI/Make targets, runtime tests, or active one-AgentJob execution rules without separate authorization and implementation evidence.

`SFA-P1-INIT-STATE-001`: Migrate program-state requirements toward portable fields for active execution transaction, execution profile, current-state evidence, continuation state, cancellation state, escalation state, latest closeout and handoff evidence, and explicit blocked reason while preserving legacy fields only for historical compatibility.

`SFA-P1-INIT-BIND-001`: Extend role and execution-binding requirements so every active transaction identifies authorized roles, runtime actors, approval principals, allowed artifacts, tool and data limits, delegation expiry, handoffs, validators, and escalation destinations.

`SFA-P1-INIT-BIND-002`: Role assignment, value alignment, target goals, urgency, and runtime capability shall not expand the transaction permission envelope or bypass separation-of-duties and human-approval requirements.

### 4.16 Capability, Evidence, Semantic, and Trace Initialization

`SFA-P1-INIT-STATUS-001`: Represent content approval, source authority, validation, requirement lifecycle, capability, evidence freshness, coordination pattern, operational maturity, and lifecycle state as independent controlled dimensions.

`SFA-P1-INIT-STATUS-002`: Missing, unknown, stale, contradicted, withdrawn, or unverified evidence shall not be interpreted as implemented, approved, available, or operational capability; required unknown capability shall fail closed.

`SFA-P1-INIT-CAPMIG-001`: Require `sys_for_ai/capability_migration.py` and `validate-capability-migration` to classify stale active references, distinguish historical evidence from current capability, prohibit silent restoration, and report unresolved active-surface conflicts.

`SFA-P1-INIT-SEM-001`: Require `sys_for_ai/prd_semantics.py` and `validate-prd-semantics` to check normative identity, candidate-versus-approved wording, execution-claim limits, lifecycle/pattern completeness, stale command claims, and structural-versus-semantic disclaimers without claiming domain correctness.

`SFA-P1-INIT-EVID-001`: Build a strategic-intent evidence graph linking user intent, RDR candidates, authority decisions, Phase 0 requirements, Phase 1 selectors, contracts, implementation artifacts, validators, approvals, waivers, packages, and handoff or closeout evidence through exact registered paths.

`SFA-P1-INIT-EVID-002`: Generalized trace requirements shall keep coverage, capability, evidence, approval, validation, requirement-lifecycle, freshness, and semantic-review state distinct and shall require explicit justification and review verdicts for partial, deferred, or out-of-phase mappings.

### 4.17 Lifecycle and Coordination-Pattern Initialization

`SFA-P1-INIT-LIFE-001`: Require `sys_for_ai/lifecycle_patterns.py` to represent the eight accepted lifecycle stages—Design, Develop, Implement, Test, Run, Maintain, Improve, and Retire—and their controlled transition semantics without claiming that every stage is implemented.

`SFA-P1-INIT-LIFE-002`: Require lifecycle data and validation to enforce, for every stage, entry criteria, inputs, responsible and approving roles, permission requirements, activities, outputs, test/verification/validation/evaluation evidence, exit criteria, failure and degraded behavior, allowed and rollback transitions, and monitoring or review cadence where applicable.

`SFA-P1-INIT-LIFE-003`: Require explicit allowed transitions, impact-based return paths, and evidence-bearing blocked and cancelled states; transitions shall not skip required verification, validation, evaluation, security, release, or human-approval gates.

`SFA-P1-INIT-LIFE-004`: Require test execution, requirements verification, stakeholder/system validation, and behavioral/performance evaluation to remain distinct evidence classes; Test shall be both a named stage and a cross-cutting gate after material changes.

`SFA-P1-INIT-LIFE-005`: Require evidence-driven Improve re-entry and Retire obligations for archival, data disposition, interface and authority withdrawal, shutdown, retained evidence, stakeholder notification, exceptions, and residual ownership.

`SFA-P1-INIT-LIFE-006`: Require `validate-lifecycle-and-patterns` with direct CLI and Make targets, aggregate-validation integration, valid-transition tests, rollback tests, skipped-gate failures, improvement-regression failures, and incomplete-retirement failures.

`SFA-P1-INIT-PATTERN-001`: Represent `coordination_pattern` independently from `operational_maturity` across discovery, decisions, manifests, packages, trace, and lifecycle evidence.

`SFA-P1-INIT-PATTERN-002`: Support the accepted coordination patterns `linear_workflow`, `goal_directed_autonomous_agent`, `role_based_multi_agent`, `production_orchestration`, and `hybrid`, and the accepted maturity states `concept`, `experiment`, `prototype`, `pilot`, `production_candidate`, `production_approved`, `operational`, and `retiring`, without inferring one dimension from the other.

`SFA-P1-INIT-PATTERN-003`: Require the Agentic System Pattern Decision to record subject system and layer, target problem and system type, selected and rejected patterns, drivers, tradeoffs, autonomy, roles and handoffs, interfaces and protocols, tool and data boundaries, memory/state, failure and degraded behavior, human oversight, maturity, production evidence, owner, review triggers, and supersession; the concrete typed contract remains gated by `G-04`.

`SFA-P1-INIT-PATTERN-004`: Require prototype-to-production promotion to fail closed without evaluation, security, integration, ownership, rollback, monitoring, incident response, service threshold, and accountable human approval evidence.

`SFA-P1-INIT-PATTERN-005`: Require positive and negative pattern/maturity cases, including role-based prototypes, production-orchestrated systems, hybrid systems, prototype falsely marked production-approved, missing decisions or rejected alternatives, and maturity inferred from architecture.

### 4.18 Reference-Host Profile Initialization

`SFA-P1-INIT-HOST-001`: Require `Sys4AI/sys_for_ai/host_profiles.py`, `Sys4AI/schemas/contracts/host_capability_profile.schema.json`, `Sys4AI/configs/host_profiles/codex_app_reference.toml`, and `Sys4AI/docs/codex_host_integration_profile.md` with versioned profile metadata, permission source, environment scope, evidence, degraded and cancellation behavior, known limitations, and review triggers.

`SFA-P1-INIT-HOST-002`: Require a Codex App reference-host profile covering user interaction, workspace filesystem, terminal and tests, tools/connectors/network, sub-agents, task/thread state, memory/retrieval, and target runtime with per-capability states `verified_available`, `verified_unavailable`, `permission_dependent`, `environment_dependent`, `unknown`, or `deprecated`.

`SFA-P1-INIT-HOST-003`: Require `validate-host-capability-profiles` with direct CLI and Make targets, aggregate-validation integration, evidence and freshness checks, secret absence, permission-source validation, degraded-state validation, and nonzero failure for invalid required states.

`SFA-P1-INIT-HOST-004`: Keep portable execution semantics independent from host mechanics and enforce precedence `platform and system constraints -> host permissions -> project authorization -> transaction permission envelope -> task objective`; `G-07` verification is required before host-dependent capability claims.

### 4.19 Package, Self-Change, Architecture, and Derivative Initialization

`SFA-P1-INIT-PACKAGE-001`: Extend target-system manifest requirements with strategic-intent artifact paths, vision/value IDs, content approval and evidence, source hashes, active versions, coordination pattern, operational maturity, lifecycle stage, pattern decision, host profile or host requirement, portable execution profile, waiver references, and impact-analysis state.

`SFA-P1-INIT-PACKAGE-002`: Target-package validation shall require both strategic-intent artifacts or a valid waiver, current hashes and versions, pattern and maturity evidence, lifecycle and promotion state, approval evidence, and fail-closed behavior for missing, stale, duplicate, superseded, self-approved, or operationally unsupported claims.

`SFA-P1-INIT-SELF-001`: Require bounded Meta-Agent self-change controls that stop and escalate changes to identity, purpose, values, authority, permissions, evaluator, acceptance criteria, production thresholds, or authority hierarchy and prohibit a runtime actor from accepting its own consequential change.

`SFA-P1-INIT-SELF-002`: Keep default reflection depth at one and require a separate threat model, explicit maximum depth, termination condition, least-privilege envelope, independent evaluator, protected holdout evidence, rollback, emergency stop, and accountable human approval before expansion.

`SFA-P1-INIT-ARCH-001`: Require focused implementation modules `sys_for_ai/strategic_intent.py`, `sys_for_ai/host_profiles.py`, `sys_for_ai/lifecycle_patterns.py`, `sys_for_ai/capability_migration.py`, and `sys_for_ai/prd_semantics.py` rather than unbounded growth of one validator module.

`SFA-P1-INIT-ARCH-002`: Reuse shared CSV, YAML, TOML, JSON Schema, path-resolution, hashing, and `ValidationResult` utilities and introduce no new dependency unless a focused implementation plan demonstrates need.

`SFA-P1-INIT-DERIV-001`: Generate strategic governance, lifecycle/pattern, host-profile, capability-state, package, and trace indexes deterministically from canonical or controlled sources and registries with noncanonical authority banners, exact provenance, freshness, and orphan state.

`SFA-P1-INIT-DERIV-002`: Generated derivatives shall never become requirement, approval, permission, or capability authority and shall be regenerated only after their canonical or controlled inputs change through an authorized transaction.

### 4.20 Strategic Validation Command Contract

`SFA-P1-INIT-CMD-001`: Require direct CLI entry points and focused Make targets for `validate-strategic-intent`, `validate-prd-semantics`, `validate-host-capability-profiles`, `validate-lifecycle-and-patterns`, and `validate-capability-migration`, and include every command in aggregate `make validate`.

`SFA-P1-INIT-CMD-002`: Each strategic validator shall return nonzero on failure, support machine-readable output where consistent with current CLI conventions, identify exact failing artifacts and fields, and state what its structural checks do not prove semantically or operationally.

---

## 5. Acceptance criteria

Phase 1 initialization is acceptable when:

1. `make doctor` passes inside `Sys4AI/`.
2. `make validate` passes inside `Sys4AI/`.
3. Historical AgentJob fixtures validate for compatibility without being represented as current portable execution capability.
4. The core skill manifest validates and all adapter folders exist.
5. Memory registries exist with expected headers.
6. The Docker decision record exists and distinguishes development environment from target runtime.
7. Phase 0 product requirements and Phase 1 initialization requirements are no longer mixed in one PRD.
8. `format_profile_registry.csv` exists with expected headers and rows for Markdown, CSV, YAML, TOML, and JSON Schema.
9. `config_source_registry.csv` exists with expected headers and at least one TOML example row.
10. `control_record_registry.csv` exists with expected headers and rows for historical AgentJob compatibility, handoff, completion receipt, and state snapshot examples, and the later portable execution contract remains distinct.
11. `validation_contract_registry.csv` exists with expected headers and rows for initial JSON Schema contracts.
12. `pyproject.toml` and `requirements.txt` include PyYAML, JSON Schema validation support, and TOML parsing support consistent with the selected Python version policy.
13. TOML examples parse successfully and validate against their declared JSON Schema contracts.
14. YAML control examples parse with safe YAML loading and validate against their declared JSON Schema contracts where contracts exist.
15. JSON Schema files load and pass schema checks for the selected dialect.
16. CSV registry headers pass validation.
17. Registry graph validation detects missing source paths, missing contract IDs, invalid authority classes, orphan derivatives, and generated derivatives marked as canonical.
18. Generated Configuration and Control Wiki stubs exist, contain non-canonical authority banners, and link to YAML/TOML source and registry evidence.
19. Generated Validation Contracts Catalog stubs exist, contain non-canonical authority banners, and link to JSON Schema source and registry evidence.
20. No standalone JSON wiki is created.
21. Secret-like keys in YAML/TOML examples are absent or cause validation warnings/failures according to Phase 1 policy.
22. `make validate` passes after dependencies are installed.
23. The Phase 1 portable successor transaction requirements include the new validators and generated derivative checks; legacy AgentJob packets are labeled historical.
24. The PRD requirement trace validator passes against the canonical Phase 0 PRD, Phase 1 PRD, and requirement trace registry, including semantic trace class, partial-justification, and non-implemented semantic review verdict checks.
25. `make validate-roles` exists, passes for the controlled role-catalog surface, and is included in `make validate`.
26. Requirements Discovery Record templates, registry rows, and validation commands exist before RDR artifacts can feed USRD baseline.
27. System-layer and self-hosting controls distinguish `Sys4AI-dev` development runtime authority from `Sys4AI` product scaffold authority.
28. Role registries, role-to-skill crosswalks, and temporary-role execution-binding checks are registered and validated.
29. Core skill lifecycle status and runtime-authority validation prevent scaffold or proposal skills from becoming active authority by implication.
30. Target vision and core-values initialization requirements name every required template, registry, trace, package, approval, waiver, supersession, impact-analysis, example, test, and validation surface while keeping `G-08` open.
31. Runtime actor and subject layer are represented independently, and the bounded execution contract carries explicit authorization, permission, state, stop, cancellation, escalation, resume, closeout, rollback, and supersession fields.
32. Program state and role execution bindings have explicit portable migration requirements, while AgentJob and `/continue` remain historical or optional-profile concepts and no removed runtime is claimed restored.
33. Capability, evidence, approval, validation, requirement-lifecycle, freshness, pattern, maturity, and lifecycle state remain independent and unknown required capability fails closed.
34. Lifecycle requirements cover all eight stages, full stage contracts, allowed and rollback transitions, distinct evidence classes, cross-cutting Test gates, improvement re-entry, and retirement.
35. Pattern requirements keep coordination topology independent from operational maturity, define every accepted value, require a complete decision, and fail prototype promotion closed.
36. Host-profile requirements isolate Codex-specific mappings from portable semantics and require `G-07` evidence before host-dependent capability claims.
37. Target-package and self-change requirements reject stale, missing, self-approved, permission-expanding, unevaluated, or operationally unsupported states.
38. Focused module boundaries and strategic validator CLI/Make/aggregate requirements are explicit, including nonzero failure and structural-versus-semantic limits.
39. Every Phase 0 requirement affected by `TX-03` through `TX-05` has an exact Phase 1 selector or explicit deferral trace, and `SFA-P1-INIT-VAL-008` is not used as a placeholder for strategic, lifecycle, or pattern initialization.

---

## 6. Portable Successor Transaction and Historical Packet Provenance

### 6.1 Illustrative portable successor

The following requirements-level example replaces AgentJob as the recommended active semantic route. It is not an implemented contract or execution authorization. `TX-09-EXECUTION-CONTRACT` owns the concrete schema, template, compatibility rules, and tests; a later Director Decision or equivalent authorized transaction must bind actual reads, writes, tools, permissions, validators, and acceptance.

```yaml
execution_transaction_id: TX-P1-STRATEGIC-BASELINE-IMPLEMENTATION-001
contract_status: proposed_pending_TX_09
objective: Implement one authorized Phase 1 strategic-baseline slice from exact Phase 0 and Phase 1 requirement selectors.
subject_system: Sys4AI
subject_layer: framework_product
runtime_actor: sys4ai_meta_agent_runtime
approval_principal: accountable_human_product_owner
permission_envelope: to_be_bound_by_authorized_transaction
allowed_reads:
  - PRDs/Sys4AI_phase-0_product_system_design_prd.md
  - PRDs/Sys4AI_phase-1_implementation_initialization_prd.md
  - Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G03-001.yaml
allowed_writes: []
allowed_tools: []
forbidden_actions:
  - Treat this illustrative record as executable authorization.
  - Approve the candidate Sys4AI vision or core values.
  - Create G-04-blocked contracts before their gate is accepted.
  - Claim unavailable host or runtime capability.
validators:
  - make validate
stop_conditions:
  - Required gate or permission evidence is missing.
  - The requested slice crosses its authorized transaction boundary.
cancellation_behavior: Stop safely and preserve current-state evidence.
resume_evidence: Required before continuation after interruption.
closeout_evidence: Required before a dependent transaction begins.
rollback: Defined by the authorized implementation slice.
```

### 6.2 Historical AgentJob packets

The following completed-era examples are retained verbatim as provenance for the original Phase 1 bootstrap and format-profile work. They are not recommended current execution routes and do not authorize AgentJob authoring, `/continue`, or restoration of the removed control loop.

```yaml
agentjob_id: AJ-P1-BOOTSTRAP-001
objective: Apply the Phase 1 repository overlay, create the Python virtual environment, install dependencies, and run validation.
role: implementation_initialization_agent
allowed_reads:
  - PRDs/Sys4AI_phase-0_product_system_design_prd.md
  - PRDs/Sys4AI_phase-1_implementation_initialization_prd.md
  - implementation_plans/phase-1_environment_decision_record.md
allowed_writes:
  - Sys4AI/**
  - implementation_plans/**
forbidden_actions:
  - Delete repository root license or notice files.
  - Treat generated derivatives as canonical sources.
  - Force Docker as default without updating the decision record.
expected_outputs:
  - Passing validation command receipt.
  - Updated source registry entries if files are promoted as canonical.
validators:
  - cd Sys4AI && make doctor
  - cd Sys4AI && make validate
stop_conditions:
  - Required dependency installation fails.
  - Existing repository file would be overwritten without maintainer approval.
```

```yaml
agentjob_id: AJ-P1-FORMAT-PROFILES-001
objective: Integrate core file-format memory profile requirements into the Phase 1 scaffold, including TOML configuration support, JSON Schema validation contracts, new registries, and generated derivative stubs.
role: implementation_initialization_agent
allowed_reads:
  - PRDs/Sys4AI_phase-0_product_system_design_prd.md
  - PRDs/Sys4AI_phase-1_implementation_initialization_prd.md
  - Sys4AI/**
  - implementation_plans/**
allowed_writes:
  - PRDs/Sys4AI_phase-0_product_system_design_prd.md
  - PRDs/Sys4AI_phase-1_implementation_initialization_prd.md
  - implementation_plans/**
  - Sys4AI/configs/**
  - Sys4AI/control_records/**
  - Sys4AI/schemas/**
  - Sys4AI/registries/**
  - Sys4AI/docs/**
  - Sys4AI/sys_for_ai/**
  - Sys4AI/tests/**
  - Sys4AI/requirements.txt
  - Sys4AI/pyproject.toml
  - Sys4AI/Makefile
forbidden_actions:
  - Delete repository root license or notice files.
  - Treat generated derivatives as canonical sources.
  - Create a standalone JSON wiki for JSON Schema.
  - Add vector database or production memory service dependencies.
  - Add secret-bearing TOML or YAML examples.
  - Use unsafe YAML loaders.
expected_outputs:
  - Updated Phase 0 PRD with core file-format profile requirements.
  - Updated Phase 1 PRD with implementation initialization requirements.
  - New registries for format profiles, config sources, control records, and validation contracts.
  - TOML example files and parser support.
  - JSON Schema contract files and validator support.
  - Generated Configuration and Control Wiki stubs.
  - Generated Validation Contracts Catalog stubs.
  - Passing validation command receipt.
validators:
  - cd Sys4AI && make doctor
  - cd Sys4AI && make validate
  - cd Sys4AI && make validate-roles
  - cd Sys4AI && make validate-format-profiles
  - cd Sys4AI && make validate-toml-config
  - cd Sys4AI && make validate-jsonschema-contracts
  - cd Sys4AI && make validate-registry-graph
  - cd Sys4AI && make validate-requirement-trace
  - cd Sys4AI && make validate-generated-derivatives
stop_conditions:
  - Required dependency installation fails.
  - Existing repository file would be overwritten without review.
  - Generated derivative would be marked canonical.
  - JSON wiki creation becomes necessary because requirements changed.
  - Secret-like value is discovered in a config/control example.
```

---

## 7. Baseline-Change History

| Date | Change | Rationale |
|---|---|---|
| 2026-07-09 | Added exact strategic-intent, runtime-actor, portable-execution, state, role-binding, capability/evidence, lifecycle, pattern, host-profile, package, self-change, focused-module, command, and derivative initialization requirements; migrated stale AgentJob recommendations to portable semantics while retaining historical provenance; and added exact Phase 0 trace selectors. | Implements `TX-06-P1-BASELINE` under accepted `G-03` without creating `G-04` contracts, verifying `G-07`, approving `G-08`, restoring removed runtime surfaces, or claiming implementation completion. |

## 8. References

AngryOwlAI. (2026a, July 9). *DDR-SFADEV-STRATEGIC-BASELINE-001: Sys4AI strategic-baseline identity and execution-model decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml`.

AngryOwlAI. (2026b, July 9). *DDR-SFADEV-STRATEGIC-BASELINE-G03-001: Candidate normative baseline disposition* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-G03-001.yaml`.

AngryOwlAI. (2026c, July 9). *Sys4AI-dev strategic baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.

Sys4AI-dev. (2026). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.
