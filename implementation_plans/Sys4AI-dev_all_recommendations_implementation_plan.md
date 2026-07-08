# Sys4AI-dev Implementation Plan: Full Integration of Discovery Gate, Self-Hosting Governance, Role Validation, Runtime Skill Reconciliation, and Core Skill Expansion

**Plan ID:** `SFADEV-IMPL-PLAN-ALL-RECS-001`
**Status:** Draft for maintainer review
**Prepared for repository:** `AngryOwlAI/Sys4AI-dev`
**Prepared date:** 2026-07-07
**Primary subject system:** `Sys4AI-dev` development workspace
**Framework product under development:** `Sys4AI`
**Plan scope:** Implement all recommendations from the system review, including PRD integration, discovery-gate lifecycle changes, self-hosting boundaries, role governance, runtime skill reconciliation, skill lifecycle governance, new core skills, validators, registries, documentation, and acceptance evidence.

---

## 0. Executive Summary

This implementation plan converts the review recommendations into a concrete, staged roadmap for `Sys4AI-dev`.

The central problem is not that the repository lacks architecture. It already has PRDs, a product scaffold, validators, registries, control records, AgentJob semantics, `/continue` semantics, source-first memory, generated derivative policies, and a core skill inventory. The current problem is that several of the most important ideas exist but are not yet fully binding across the PRDs, registries, validators, runtime skill layer, and implementation workflow.

The highest-priority change is to make `system-definition-interview-context-45` the mandatory front-door discovery gate for any new or substantially changed system definition. That gate must produce a governed Requirements Discovery Record before USRD generation begins. The second highest-priority change is to make system-layer classification explicit everywhere, so the development workspace, framework product, future target-system templates, actual target systems, and derivative reader surfaces cannot be confused. The third priority is to implement the missing `validate-roles` requirement already called for by the Phase 1 PRD. The fourth priority is to reconcile the active `.agents` runtime skill registry with the product-scaffold skill manifest, especially for `continue` and `source-first-memory`.

The plan is organized into workstreams that can be executed as bounded AgentJobs. Each workstream specifies files to add or modify, exact registry and schema changes, validator requirements, CLI and Makefile targets, acceptance criteria, risks, and completion evidence.

The implementation should proceed in the following order:

1. Baseline and sync preflight.
2. PRD integration for discovery gate, RDR, self-hosting, system layers, role validation, and core skill lifecycle.
3. Registry and schema expansion.
4. Discovery gate implementation.
5. Role governance and `validate-roles` implementation.
6. Runtime skill reconciliation for `continue` and `source-first-memory`.
7. Skill lifecycle governance.
8. New core skill scaffolds and active runtime manifests.
9. System-layer classifier and self-hosting policy implementation.
10. Artifact-contract governance and traceability engine.
11. Director decision, verification/validation, assurance, authority audit, baseline change, operations, ontology, and domain-pack router skill integration.
12. Generated documentation and derivative validation.
13. Full validation and acceptance evidence.

The plan intentionally avoids creating project-specific domain skills. It only adds core organizational skills that belong to the framework and development system regardless of future project domain.

---

## 1. Terminology and Layer Model

### 1.1 Required System Layers

All implementation work must distinguish these layers:

| Layer ID | Layer Name | Meaning | Example Roots | Authority Notes |
|---|---|---|---|---|
| `development_system` | `Sys4AI-dev` | The current development workspace and active operating layer used to build `Sys4AI`. | repository root, `.agents/`, `.codex/`, root `Makefile`, root scripts | Active runtime authority for development. |
| `framework_product` | `Sys4AI` | The product framework being developed. | `Sys4AI/`, `PRDs/`, `implementation_plans/` | Product scaffold and reference implementation. |
| `target_system_template` | Future generated system template | Generic templates, patterns, contracts, and examples used by `Sys4AI` to create future target systems. | `Sys4AI/templates/`, some `Sys4AI/skills/core/` content | Template authority only when explicitly classified. |
| `target_system_instance` | A concrete future target system | A system produced or managed by `Sys4AI`. | future generated repo or package | Project-specific authority; must not mutate core framework authority without escalation. |
| `derivative_surface` | Generated reader surface or cache | Generated wikis, catalogs, Obsidian mirrors, PDFs, HTML, diagrams, summaries, semantic caches. | `docs/generated/`, optional vaults, generated indexes | Non-canonical by default. Must trace to source. |

### 1.2 Required Fields for Controlled Artifacts

Every new controlled artifact introduced by this plan should include these fields when structurally appropriate:

```yaml
subject_system_id: <stable system ID>
subject_system_name: <human-readable system name>
subject_layer: development_system | framework_product | target_system_template | target_system_instance | derivative_surface
authority_scope: <what this artifact may govern>
source_authority_status: canonical | controlled | derivative_draft | generated_derivative | scaffold_reference | deprecated
producer_agentjob_id: <AgentJob ID or null>
producer_role_id: <role ID or null>
source_trace:
  - <source path, registry ID, user statement ID, decision ID, or evidence ID>
validation_status: pass | warn | fail | not_run
supersedes: <prior artifact ID or empty>
```

### 1.3 Non-Negotiable Authority Rule

Generated derivative surfaces must never authorize changes to PRDs, registries, control records, role catalogs, skill manifests, validation contracts, or source files unless the content has been promoted through an explicit source-authority workflow.

---

## 2. Implementation Principles

1. **Source-first, always.** Any memory, generated doc, skill output, or summary that affects requirements, routing, claims, AgentJob boundaries, handoffs, or permissions must trace to canonical sources or controlled registry rows.
2. **Discovery before requirements.** The system must not jump from a vague user prompt into PRD generation. It must first produce a Requirements Discovery Record unless a Director Decision Record waives the gate.
3. **System layer before mutation.** The agent must know which system layer it is acting on before modifying anything.
4. **Controlled roles before role execution.** Roles must be machine-readable, validateable, and bound to allowed skills and artifact authorities.
5. **One AgentJob at a time.** Any implementation work should remain bounded by AgentJob contracts, completion receipts, validators, and handoffs.
6. **Runtime and scaffold are different.** `.agents/skills/` is the active runtime surface for `Sys4AI-dev`; `Sys4AI/skills/core/` is the product scaffold/reference surface unless promoted.
7. **Validators prove scope-limited facts.** Schema and process validation prove structural admissibility and process conformance, not domain truth, safety, or business acceptance.
8. **Supersede rather than silently rewrite.** Activated control records, decisions, handoffs, and completion receipts should be superseded rather than historically rewritten.
9. **Core skills must remain domain-neutral.** Project-specific domain packs can be added later, but this plan only adds core framework and development-system capabilities.
10. **Every recommendation must land in at least one authority surface.** A recommendation is not implemented until it is reflected in PRDs, registry/schema structures, runtime skill surfaces, validators, documentation, and acceptance evidence as applicable.

### 2.1 Mandatory `/continue` Execution Protocol

This plan must be implemented through the active `/continue` skill, not by manually walking multiple workstreams in a single chat turn. For any remaining, resumed, corrective, or follow-on implementation task, the agent must use `/continue` to start from tracked state and let the repository select or constrain the next bounded task.

Required sequence:

1. Invoke `/continue` before starting implementation work.
2. Read the self-hosting boundary decision record, run memory preflight, resolve `Sys4AI/control_records/program_state.yaml`, and inspect the latest handoff.
3. Select or reuse at most one authorized AgentJob.
4. Execute only that selected AgentJob. Do not batch multiple plan tasks into one continuation.
5. On completion, write the required completion receipt, the controlled handoff record when applicable, the required `temp_handoff/handoff-*.md` markdown handoff, and any related registry, program-state, generated-derivative, memory-preflight, or Director-decision files required by the selected AgentJob.
6. Run the validators named by the AgentJob and any aggregate validation required by the handoff.
7. Commit the completed task as its own bounded checkpoint.
8. Push the completed commit to the configured upstream before starting the next plan task. If the branch is ahead of upstream or the push has not happened, report that the next task is waiting on `git push` evidence and stop.

The in-chat closeout after each completed task must state:

- The selected AgentJob or controlled task ID.
- What was done.
- Which handoff markdown file and related controlled files were created or updated.
- Which validators ran and whether they passed.
- The commit hash, push status, remaining uncertainty, and logical next step.

This rule preserves the one-AgentJob invariant, makes handoffs inspectable, and prevents a later task from starting before the previous task is both checkpointed and published.

---

## 3. Recommendation-to-Workstream Trace Matrix

| Recommendation | Workstream | Primary Files | Required Validators | Acceptance Evidence |
|---|---|---|---|---|
| Make `system-definition-interview-context-45` the mandatory first discovery gate | WS-01, WS-03 | Phase 0 PRD, Phase 1 PRD, RDR template, discovery registry | `validate-discovery-record`, `validate-requirement-trace`, `validate-registry-graph` | RDR artifact catalog entry, PRD requirements, sample AgentJob and receipt |
| Add Requirements Discovery Record before USRD | WS-01, WS-03 | Phase 0 PRD, artifact catalog, `templates/system_definition/` | `validate-discovery-record` | RDR template registered and validated |
| Add system-layer and self-hosting boundary | WS-01, WS-08 | PRDs, `self_hosting_mode_policy.md`, system layer registry, config TOML | `validate-toml-config`, `validate-registry-graph`, new `validate-system-layers` | system layer config, registry rows, policy doc |
| Implement missing `validate-roles` | WS-04 | role registries, role schemas, CLI, Makefile | `make validate-roles`, aggregate `make validate` | passing validator output and completion receipt |
| Reconcile active runtime skills for `continue` and `source-first-memory` | WS-05 | `.agents/skill_registry/SKILL_REGISTRY.yaml`, `.agents/skills/continue`, `.agents/skills/source-first-memory` | `make validate-dev-skills`, `make validate-skills` | active runtime entries and skill manifests |
| Add strict skill lifecycle vocabulary | WS-06 | PRDs, skill registries, schemas, validators | `validate-dev-skills`, `validate-skills`, new lifecycle checks | lifecycle statuses enforced |
| Add new core skills | WS-07 through WS-13 | `.agents/skills/*`, `Sys4AI/skills/core/*`, registries | `validate-dev-skills`, `validate-skills`, role validation | all new core skill manifests pass |
| Add artifact-contract governance | WS-09 | artifact contract registry, schemas, validator, skill | `validate-artifact-contracts` | artifact contract registry passes |
| Add traceability engine | WS-10 | trace registry extensions, trace skill, validators | `validate-requirement-trace`, new `validate-traceability-graph` | trace gap report and validator pass |
| Add Director decision governance | WS-11 | decision skill, decision schemas/registry | `validate-director-decisions` | sample Director Decision Record validates |
| Add verification, assurance, threat, and evaluation core skills | WS-12 | skill folders, templates, registries | skill validators, artifact validators | validated skill packages and templates |
| Add baseline change, operations, ontology, domain-pack router skills | WS-13 | skill folders, templates, registries | skill validators, artifact validators | validated skill packages and templates |
| Update generated docs and derivative validation | WS-14 | docs generated pages, derivative registry | generated derivative validators | docs regenerate/check cleanly |
| End-to-end acceptance | WS-15 | completion receipts, handoffs, design readiness report | root `make validate` | final acceptance packet |

---

## 4. Workstream Overview

### WS-00: Baseline, Sync, and Safety Preflight

**Purpose:** Ensure the implementation begins from a known repository state and does not accidentally overwrite active work.

**Inputs:**

- Existing `PRDs/`
- Existing `Sys4AI/`
- Existing `.agents/`
- Existing `.codex/`
- Existing control records and registries

**Outputs:**

- Baseline completion receipt
- Optional branch or checkpoint note
- Initial validation transcript

**Recommended commands:**

```bash
make validate-dev-skills
make validate-product-scaffold
make validate
cd Sys4AI && make validate
```

**Required checks:**

1. Confirm current branch and latest commit.
2. Confirm root `make validate` behavior.
3. Confirm `Sys4AI/Makefile` aggregate validation behavior.
4. Confirm `.agents/skill_registry/SKILL_REGISTRY.yaml` content.
5. Confirm `Sys4AI/skills/core_skill_manifest.yaml` content.
6. Confirm `system-definition-interview-context-45` runtime skill exists.
7. Confirm RDR template exists and passes current validator.
8. Confirm no local uncommitted work would be overwritten.

**Completion evidence:**

```yaml
completion_receipt_id: CR-WS00-BASELINE-001
agentjob_id: AJ-SFADEV-WS00-BASELINE-001
result: pass | warn | fail
commands_run:
  - make validate-dev-skills
  - make validate-product-scaffold
  - make validate
changed_artifacts: []
open_issues: []
```

---

## 5. WS-01: PRD Integration for Discovery Gate, RDR, System Layers, Self-Hosting, Role Governance, and Skill Lifecycle

### 5.1 Purpose

Update canonical PRDs so the recommendations become binding product and initialization requirements rather than advisory notes.

### 5.2 Files to Modify

```text
PRDs/Sys4AI_phase-0_product_system_design_prd.md
PRDs/Sys4AI_phase-1_implementation_initialization_prd.md
Sys4AI/registries/requirement_trace_registry.csv
```

Potential supporting files:

```text
implementation_plans/phase-1_discovery_gate_and_self_hosting_plan.md
implementation_plans/phase-1_role_governance_plan.md
implementation_plans/phase-1_core_skill_expansion_plan.md
```

### 5.3 Phase 0 PRD Additions

Add or update these sections.

#### 5.3.1 System Layer and Self-Hosting Boundary

Recommended insertion location: after Definitions or immediately before Phase Boundary.

```md
### System Layer and Self-Hosting Boundary

`SFA-CORE-LAYER-001`: Every controlled artifact, AgentJob, handoff, role invocation, skill invocation, validation receipt, and generated derivative shall declare its subject layer: `development_system`, `framework_product`, `target_system_template`, `target_system_instance`, or `derivative_surface`.

`SFA-CORE-LAYER-002`: Work on `Sys4AI-dev` shall be treated as self-hosting development-system work. It may use `Sys4AI` patterns, but it shall not treat product-scaffold artifacts as active runtime authority unless they are explicitly promoted.

`SFA-CORE-LAYER-003`: Work on `Sys4AI` shall distinguish framework-product requirements from future target-system requirements.

`SFA-CORE-LAYER-004`: Work on a future generated target system shall not mutate core `Sys4AI` framework authority unless routed through a framework-improvement AgentJob and Director decision.

`SFA-CORE-LAYER-005`: Generated derivatives shall never authorize changes to canonical sources, registries, control records, validation contracts, role catalogs, or skill manifests without a promotion workflow.
```

#### 5.3.2 System Definition Discovery Gate

Recommended insertion location: before the System Design phase pipeline.

```md
### System Definition Discovery Gate

`SFA-CORE-DISCOVERY-001`: Every new or substantially changed target-system definition shall begin with a System Definition Discovery pass using `system-definition-interview-context-45`, unless a Director Decision Record explicitly waives or substitutes the discovery gate.

`SFA-CORE-DISCOVERY-002`: The System Definition Discovery pass shall produce a Requirements Discovery Record before USRD generation.

`SFA-CORE-DISCOVERY-003`: A USRD shall not be baselined unless it traces to a Requirements Discovery Record or to a Director Decision Record explaining why discovery was waived.

`SFA-CORE-DISCOVERY-004`: Candidate requirements from discovery shall remain candidate requirements until promoted through the requirements authority workflow.

`SFA-CORE-DISCOVERY-005`: The discovery gate shall capture system layer, mission need, problem statement, desired outcome, value case, system-of-interest, stakeholders, boundaries, as-is state when applicable, to-be state, operational scenarios, candidate requirements, quality attributes, architecture drivers, interface candidates, V&V seeds, evidence, assumptions, risks, constraints, open questions, and downstream routing recommendation.

`SFA-CORE-DISCOVERY-006`: The discovery gate shall inspect available repository or document evidence before asking questions that existing source evidence can answer.

`SFA-CORE-DISCOVERY-007`: The discovery gate shall ask focused questions and shall not automatically create a PRD until questioning is complete and the user or Director explicitly approves PRD synthesis.
```

#### 5.3.3 RDR Artifact Catalog Entry

Add this before USRD in the artifact catalog:

```md
| RDR / `requirements-discovery-record.md` | Captures initial system intent, mission, stakeholders, boundaries, scenarios, candidate requirements, evidence, risks, assumptions, constraints, open questions, and downstream routing before formal requirements generation. | System Developer / User Wants Elicitor using `system-definition-interview-context-45` | USRD author, Requirements Manager, System Director |
```

#### 5.3.4 Pipeline Update

Add RDR between initial user intent and USRD:

```text
User intent -> System Director layer classification -> System Definition Discovery Gate -> RDR -> USRD -> SRD -> ARD -> TRP -> RSRD -> RARD -> SRP
```

#### 5.3.5 Role Requirements

Add:

```md
`SFA-CORE-ROLE-002`: The System Developer / User Wants Elicitor role shall use `system-definition-interview-context-45` as its default discovery skill for new or substantially changed system definitions.

`SFA-CORE-ROLE-003`: The controlled role catalog shall include a role-to-skill crosswalk that maps every core and support role to required, optional, and forbidden skills.

`SFA-CORE-ROLE-004`: Any temporary role created for one AgentJob shall declare expiry, authority scope, required skills, allowed artifacts, validation obligations, and supersession behavior.

`SFA-CORE-ROLE-005`: Runtime role execution shall validate role binding before an AgentJob may be selected or executed.
```

#### 5.3.6 Skill Lifecycle Requirements

Add:

```md
`SFA-CORE-SKILL-006`: Every core skill shall declare lifecycle status using controlled vocabulary: `proposed`, `imported_unadapted`, `adapter_shell`, `adapted_runtime_active`, `product_scaffold_reference`, `deprecated`, `superseded`, or `blocked`.

`SFA-CORE-SKILL-007`: A skill shall not be used as active runtime authority unless its runtime registry entry is `adapted_runtime_active` or an equivalent active status approved by the skill governance policy.

`SFA-CORE-SKILL-008`: Product-scaffold skills shall not be treated as active development-runtime skills unless also listed in the active runtime skill registry.

`SFA-CORE-SKILL-009`: Core organizational skills may be added to the framework through controlled skill proposal, manifest, role-binding, validation, and provenance workflows. Project-specific domain skills shall be added through domain packs rather than core skill expansion.
```

#### 5.3.7 Self-Hosting Requirements

Add:

```md
`SFA-CORE-SELFHOST-001`: `Sys4AI-dev` shall define a self-hosting mode for cases where the development workspace uses `Sys4AI` concepts to improve `Sys4AI`.

`SFA-CORE-SELFHOST-002`: Self-hosting mode shall require explicit system-layer classification before any artifact, registry, validator, skill, or role rule is changed.

`SFA-CORE-SELFHOST-003`: Self-hosting improvements shall be routed through AgentJobs, Director decisions where needed, validation receipts, handoffs, and source-first memory preflight.

`SFA-CORE-SELFHOST-004`: Self-hosting mode shall prohibit generated derivative surfaces from authorizing changes to PRDs, role catalogs, skill manifests, control records, validators, validation contracts, or registries.
```

### 5.4 Phase 1 PRD Additions

Add a new section after Memory Scaffold or before Validation.

#### 5.4.1 Discovery Gate Initialization Requirements

```md
### Discovery Gate Initialization

`SFA-P1-INIT-DISC-001`: Add the Requirements Discovery Record to the artifact catalog, source registry, derivative registry policy, and trace model.

`SFA-P1-INIT-DISC-002`: Add or extend a discovery-record registry that records RDR path, subject system ID, subject layer, producer AgentJob, authority status, candidate requirement count, open question count, downstream USRD link, validation status, source hash, and last validation timestamp.

`SFA-P1-INIT-DISC-003`: Add a sample AgentJob for running `system-definition-interview-context-45` on a new target system or framework-product change.

`SFA-P1-INIT-DISC-004`: Add a sample completion receipt showing RDR creation, validation evidence, open issues, and recommended next route.

`SFA-P1-INIT-DISC-005`: Extend aggregate validation so discovery-record templates and registered discovery records are validated by default.
```

#### 5.4.2 System-Layer and Self-Hosting Initialization Requirements

```md
### System-Layer and Self-Hosting Initialization

`SFA-P1-INIT-LAYER-001`: Add a controlled system-layer registry for `development_system`, `framework_product`, `target_system_template`, `target_system_instance`, and `derivative_surface`.

`SFA-P1-INIT-LAYER-002`: Add a self-hosting mode policy document that distinguishes `Sys4AI-dev` active runtime authority from `Sys4AI` product scaffold authority.

`SFA-P1-INIT-LAYER-003`: Add a self-hosting TOML configuration source and register it in `config_source_registry.csv`.

`SFA-P1-INIT-LAYER-004`: Add `validate-system-layers` to verify allowed layer IDs, canonical roots, derivative roots, authority mutation rules, and self-hosting constraints.
```

#### 5.4.3 Role Governance Initialization Requirements

```md
### Role Governance Initialization

`SFA-P1-INIT-ROLE-001`: Phase 1 shall implement a controlled role registry.

`SFA-P1-INIT-ROLE-002`: Phase 1 shall implement a role-to-skill crosswalk registry.

`SFA-P1-INIT-ROLE-003`: Phase 1 shall implement role execution-binding validation.

`SFA-P1-INIT-ROLE-004`: `make validate-roles` shall fail when a role references a missing skill, a skill references an unknown role, a generated role page is stale, an AgentJob binds to a role without declared authority, or a role is missing required skill bindings.

`SFA-P1-INIT-ROLE-005`: Aggregate `make validate` shall include `make validate-roles`.
```

#### 5.4.4 Core Skill Expansion Initialization Requirements

```md
### Core Skill Expansion Initialization

`SFA-P1-INIT-CORESKILL-001`: Add governed skill proposals and active runtime manifests for new core organizational skills approved by the Phase 0 skill lifecycle policy.

`SFA-P1-INIT-CORESKILL-002`: New core skills shall be domain-neutral and shall not include project-specific domain rules except through a domain-pack router.

`SFA-P1-INIT-CORESKILL-003`: Each new core skill shall include `SKILL.md`, `README.md`, `AGENTS.md`, `skill.yaml`, and `examples/portable-example.md` in the active runtime skill root when activated.

`SFA-P1-INIT-CORESKILL-004`: Product-scaffold adapter surfaces shall be added under `Sys4AI/skills/core/<skill-id>/` for each active core skill.

`SFA-P1-INIT-CORESKILL-005`: Skill validators shall enforce lifecycle status, provenance, role posture, dependency declarations, authority boundaries, and validation classes.
```

### 5.5 Requirement Trace Updates

Update:

```text
Sys4AI/registries/requirement_trace_registry.csv
```

For each new Phase 0 requirement, add a trace row with one of:

- `coverage_status=covered` if Phase 1 adds direct implementation.
- `coverage_status=partial` if Phase 1 adds scaffold or validation hooks.
- `coverage_status=deferred` if implementation belongs to a later phase.
- `coverage_status=not_applicable` only with strong justification.

Every partial, deferred, or out-of-phase row must include `semantic_justification` and `semantic_review_verdict`.

### 5.6 Validators

Run:

```bash
cd Sys4AI
make validate-requirement-trace
make validate-discovery-template
make validate
```

### 5.7 Acceptance Criteria

- Phase 0 PRD contains system layer requirements.
- Phase 0 PRD contains self-hosting requirements.
- Phase 0 PRD contains discovery gate requirements.
- Phase 0 PRD lists RDR in artifact catalog before USRD.
- Phase 0 pipeline shows RDR before USRD.
- Phase 0 role requirements bind User Wants Elicitor to `system-definition-interview-context-45`.
- Phase 0 skill requirements include lifecycle vocabulary.
- Phase 1 PRD contains discovery, layer, role, and core skill initialization requirements.
- Requirement trace registry covers every new Phase 0 requirement.
- Existing Phase 0/Phase 1 requirement ID uniqueness remains valid.

---

## 6. WS-02: Registry and Schema Expansion

### 6.1 Purpose

Add the structured registry and schema foundations needed for the remaining workstreams.

### 6.2 Files to Add

```text
Sys4AI/registries/system_layer_registry.csv
Sys4AI/registries/discovery_record_registry.csv
Sys4AI/registries/role_registry.csv
Sys4AI/registries/role_skill_crosswalk.csv
Sys4AI/registries/role_execution_binding_registry.csv
Sys4AI/registries/artifact_contract_registry.csv
Sys4AI/registries/core_skill_proposal_registry.csv
Sys4AI/registries/skill_lifecycle_status_registry.csv

Sys4AI/schemas/contracts/system_layer_registry_row.schema.json
Sys4AI/schemas/contracts/discovery_record_registry_row.schema.json
Sys4AI/schemas/contracts/role_registry_row.schema.json
Sys4AI/schemas/contracts/role_skill_crosswalk_row.schema.json
Sys4AI/schemas/contracts/role_execution_binding_registry_row.schema.json
Sys4AI/schemas/contracts/artifact_contract_registry_row.schema.json
Sys4AI/schemas/contracts/core_skill_proposal_registry_row.schema.json
Sys4AI/schemas/contracts/skill_lifecycle_status_registry_row.schema.json
```

### 6.3 Validator Header Updates

Modify:

```text
Sys4AI/sys_for_ai/validators.py
```

Add expected headers to `REGISTRY_HEADERS`.

#### 6.3.1 `system_layer_registry.csv`

```csv
layer_id,layer_name,layer_type,canonical_roots,mutable_roots,derivative_roots,authority_notes,requires_director_decision_for_mutation,default_validators,owner,source_hash,last_validated_at,notes
```

Seed rows:

```csv
development_system,Sys4AI-dev,development_system,".;.agents;.codex;scripts;PRDs;implementation_plans",".;.agents;.codex;scripts;PRDs;implementation_plans","docs/generated;.local",Active development workspace authority,true,"make validate-dev-skills;make validate-product-scaffold",system_director,,,
framework_product,Sys4AI,framework_product,"Sys4AI;PRDs;implementation_plans","Sys4AI;PRDs;implementation_plans","Sys4AI/docs/generated",Product framework scaffold authority,true,"cd Sys4AI && make validate",system_director,,,
target_system_template,Target system template,target_system_template,"Sys4AI/templates;Sys4AI/skills/core","Sys4AI/templates;Sys4AI/skills/core","Sys4AI/docs/generated",Template authority only,true,"cd Sys4AI && make validate",system_architect,,,
target_system_instance,Concrete target system,target_system_instance,"<future-target-root>","<future-target-root>","<future-target-root>/docs/generated",Project-specific authority,true,"<target-system validators>",system_director,,,
derivative_surface,Generated derivative surface,derivative_surface,"docs/generated;Sys4AI/docs/generated","","docs/generated;Sys4AI/docs/generated",Non-canonical by default,true,"validate-generated-derivatives",documentation_librarian,,,
```

#### 6.3.2 `discovery_record_registry.csv`

```csv
discovery_record_id,path,subject_system_id,subject_layer,status,producer_agentjob_id,source_authority_status,candidate_requirement_count,open_question_count,downstream_usrd_path,validation_status,source_hash,last_validated_at,notes
```

#### 6.3.3 `role_registry.csv`

```csv
role_id,role_name,role_class,system_layer_scope,primary_mission,required_skills,optional_skills,forbidden_skills,primary_outputs,allowed_artifact_classes,may_create_agentjobs,requires_director_decision,authority_status,owner,supersedes,source_hash,last_validated_at,notes
```

Seed rows must include at minimum:

```text
system_director
user_wants_elicitor
existing_system_analyst
requirements_manager
system_architect
technical_requirements_engineer
reconciliation_analyst
reconciled_architecture_architect
final_system_requirements_packager
requirements_verifier
domain_specialist
security_safety_privacy_compliance_reviewer
documentation_librarian
runtime_maintenance_planner
control_loop_agentjob_planner
context_memory_knowledge_architect
svc_documentation_surface_architect
implementation_initialization_agent
verification_engineer
software_engineer
system_engineer
system_analyst
```

Role IDs should use snake case. Display names can match PRD role names.

#### 6.3.4 `role_skill_crosswalk.csv`

```csv
crosswalk_id,role_id,skill_id,binding_type,required_when,system_layer_scope,invocation_policy,authority_status,evidence_path,source_hash,last_validated_at,notes
```

`binding_type` values:

```text
required
optional
forbidden
conditional
recommended
```

#### 6.3.5 `role_execution_binding_registry.csv`

```csv
binding_id,role_id,allowed_agentjob_types,allowed_reads,allowed_writes,forbidden_actions,required_validators,completion_evidence,expiry_policy,authority_status,owner,supersedes,source_hash,last_validated_at,notes
```

#### 6.3.6 `artifact_contract_registry.csv`

```csv
artifact_contract_id,artifact_type,canonical_filename_or_pattern,producer_role_ids,consumer_role_ids,system_layer_scope,authority_default,required_sections,validation_contract_id,registry_required,derivative_surfaces,promotion_rule,source_hash,last_validated_at,notes
```

Seed artifacts:

```text
RDR
USRD
ESAR
SRD
ARD
TRP
RSRD
RARD
SRP
CLRA
CKMSRA
SVCDA
AgentJob
DirectorDecision
Handoff
CompletionReceipt
MemoryPreflightReceipt
RoleRegistry
SkillManifest
ValidationContract
GeneratedConfigurationControlWiki
GeneratedValidationContractsCatalog
```

#### 6.3.7 `core_skill_proposal_registry.csv`

```csv
proposal_id,skill_id,skill_family,priority,status,core_or_project_specific,required_by_roles,source_rationale,target_runtime_path,product_scaffold_path,validator_plan,owner,source_hash,last_validated_at,notes
```

`status` values:

```text
proposed
approved_for_scaffold
scaffolded
active
blocked
deferred
superseded
```

#### 6.3.8 `skill_lifecycle_status_registry.csv`

```csv
status_id,status_name,may_execute_runtime,may_be_used_as_authority,requires_provenance,requires_manifest,requires_skill_md,requires_validator,allowed_roots,notes
```

Seed statuses:

```text
proposed
imported_unadapted
adapter_shell
adapted_runtime_active
product_scaffold_reference
deprecated
superseded
blocked
```

### 6.4 Contract Schema Requirements

Each row schema should enforce:

- Required ID field.
- Non-empty path when applicable.
- Controlled enum fields.
- No absolute paths.
- No generated derivative marked canonical.
- Valid system layer IDs where applicable.
- Valid lifecycle status values where applicable.

### 6.5 Registry Graph Updates

Modify registry graph validation to check:

1. Every `role_id` in role-skill crosswalk exists in `role_registry.csv`.
2. Every `skill_id` in role-skill crosswalk exists in active runtime registry or product scaffold manifest depending on `system_layer_scope`.
3. Every role execution binding references a known role.
4. Every artifact contract references known producer and consumer roles.
5. Every discovery record path exists.
6. Every discovery record subject layer exists in system layer registry.
7. Every core skill proposal has `core_or_project_specific=core` for this plan.
8. Every skill lifecycle status referenced by a registry row exists in `skill_lifecycle_status_registry.csv`.

### 6.6 CLI Additions

Modify:

```text
Sys4AI/sys_for_ai/cli.py
```

Add commands:

```bash
validate-system-layers
validate-discovery-records
validate-roles
validate-artifact-contracts
validate-core-skill-proposals
validate-skill-lifecycle
```

### 6.7 Makefile Additions

Modify:

```text
Sys4AI/Makefile
```

Add phony targets:

```make
validate-system-layers:
	$(PYTHON) -m sys_for_ai.cli validate-system-layers registries/system_layer_registry.csv

validate-discovery-records:
	$(PYTHON) -m sys_for_ai.cli validate-discovery-records registries/discovery_record_registry.csv

validate-roles:
	$(PYTHON) -m sys_for_ai.cli validate-roles

validate-artifact-contracts:
	$(PYTHON) -m sys_for_ai.cli validate-artifact-contracts registries/artifact_contract_registry.csv

validate-core-skill-proposals:
	$(PYTHON) -m sys_for_ai.cli validate-core-skill-proposals registries/core_skill_proposal_registry.csv

validate-skill-lifecycle:
	$(PYTHON) -m sys_for_ai.cli validate-skill-lifecycle registries/skill_lifecycle_status_registry.csv
```

Include all in aggregate `validate`.

### 6.8 Acceptance Criteria

- All new registry files exist with exact headers.
- All row schemas exist and pass JSON Schema checks.
- CLI exposes new validation commands.
- Makefile exposes new validation targets.
- Aggregate `make validate` includes new targets.
- Registry graph detects broken role, skill, artifact, layer, and lifecycle references.

---

## 7. WS-03: Discovery Gate Implementation

### 7.1 Purpose

Make `system-definition-interview-context-45` the operational first gate for new or substantially changed system definitions.

### 7.2 Files to Modify

```text
.agents/skills/system-definition-interview-context-45/SKILL.md
.agents/skills/system-definition-interview-context-45/README.md
.agents/skills/system-definition-interview-context-45/AGENTS.md
.agents/skills/system-definition-interview-context-45/skill.yaml
Sys4AI/skills/core/system-definition-interview-context-45/SKILL.md
Sys4AI/skills/core/system-definition-interview-context-45/README.md
Sys4AI/skills/core/system-definition-interview-context-45/AGENTS.md
Sys4AI/templates/system_definition/requirements-discovery-record-template.md
Sys4AI/schemas/discovery_record.schema.yaml
Sys4AI/sys_for_ai/discovery.py
Sys4AI/sys_for_ai/cli.py
Sys4AI/Makefile
Sys4AI/registries/discovery_record_registry.csv
Sys4AI/registries/artifact_contract_registry.csv
Sys4AI/registries/source_registry.csv
Sys4AI/registries/control_record_registry.csv
```

### 7.3 Skill Procedure Changes

Update `system-definition-interview-context-45` to explicitly say:

1. It is the default front-door discovery gate for new or substantially changed system definitions.
2. It must first classify the subject layer or route to `system-layer-classifier` when available.
3. It must produce or update `requirements-discovery-record.md` before any USRD, PRD, SRD, ARD, TRP, or SRP generation.
4. It must preserve candidate requirement labels.
5. It must not create a PRD automatically.
6. It must explicitly ask for PRD creation only after discovery is coherent enough.
7. It must create a completion record or handoff recommendation when used inside AgentJob flow.

### 7.4 RDR Template Changes

Add these fields to the RDR template header:

```md
**Subject system ID:** <system ID>
**Subject layer:** development_system / framework_product / target_system_template / target_system_instance / derivative_surface
**Discovery gate:** system-definition-interview-context-45
**Producer AgentJob:** <AgentJob ID or Director decision ID>
**Discovery registry row:** <discovery_record_registry.csv row ID>
**Downstream artifact status:** no USRD yet / USRD proposed / USRD created / discovery waived
```

Add a new section near the top:

```md
## System Layer Classification

| Field | Value | Evidence | Open Issues |
|---|---|---|---|
| Subject layer | <layer> | <source> | <OPEN-*> |
| Active authority root | <path or registry> | <source> | <OPEN-*> |
| Product scaffold involved? | yes / no / unknown | <source> | <OPEN-*> |
| Target-system instance involved? | yes / no / unknown | <source> | <OPEN-*> |
| Derivative surfaces involved? | yes / no / unknown | <source> | <OPEN-*> |
```

Add a discovery gate exit checklist:

```md
## Discovery Gate Exit Checklist

| Check | Status | Evidence | Blocking Issues |
|---|---|---|---|
| Subject layer classified | pass / warn / fail | <evidence> | <OPEN-*> |
| Mission need captured or marked missing | pass / warn / fail | <evidence> | <OPEN-*> |
| Problem statement captured or marked missing | pass / warn / fail | <evidence> | <OPEN-*> |
| System-of-interest identified | pass / warn / fail | <evidence> | <OPEN-*> |
| Stakeholders identified | pass / warn / fail | <evidence> | <OPEN-*> |
| Boundaries captured | pass / warn / fail | <evidence> | <OPEN-*> |
| Candidate requirements remain candidate-labeled | pass / warn / fail | <evidence> | <OPEN-*> |
| Evidence register populated | pass / warn / fail | <evidence> | <OPEN-*> |
| Open questions routed | pass / warn / fail | <evidence> | <OPEN-*> |
| Next route recommended | pass / warn / fail | <evidence> | <OPEN-*> |
```

### 7.5 Discovery Validator Enhancements

Modify `Sys4AI/sys_for_ai/discovery.py`:

Add checks for:

- Header contains subject layer.
- Subject layer is one of allowed values.
- Discovery gate marker exists.
- Authority notice still marks RDR as not canonical.
- Discovery gate exit checklist exists.
- Candidate requirements remain `REQ-CAND-*` or `NFR-CAND-*`.
- No unguarded baseline requirement IDs appear.
- Evidence Register section exists and has at least one non-placeholder row for registered discovery records.
- Open Questions section exists.
- Downstream Routing Recommendation section exists.

Add a registry-level validator:

```python
def validate_discovery_records(registry_path: str | Path = "registries/discovery_record_registry.csv") -> ValidationResult:
    ...
```

Expected behavior:

1. Validate registry rows against JSON Schema.
2. Resolve every RDR path.
3. Run `validate_discovery_record` on every path.
4. Verify subject layer is known.
5. Verify source hash if populated.
6. Verify `candidate_requirement_count` and `open_question_count` are numeric strings.
7. Warn if downstream USRD path is set but missing.

### 7.6 Sample AgentJob

Add:

```text
Sys4AI/control_records/agentjobs/AJ-P1-DISCOVERY-GATE-SMOKE-001.yaml
```

Example:

```yaml
schema_version: "0.2.0"
agentjob_id: AJ-P1-DISCOVERY-GATE-SMOKE-001
objective: Run the System Definition Discovery Gate on a sample framework-product change and produce a Requirements Discovery Record.
role: user_wants_elicitor
subject_system_id: Sys4AI
subject_layer: framework_product
allowed_reads:
  - PRDs/**
  - Sys4AI/templates/system_definition/**
  - .agents/skills/system-definition-interview-context-45/**
allowed_writes:
  - Sys4AI/control_records/system_definition/**
  - Sys4AI/registries/discovery_record_registry.csv
forbidden_actions:
  - Create a baselined USRD automatically.
  - Treat candidate requirements as approved requirements.
  - Treat generated derivatives as canonical.
required_inputs:
  - User or Director-provided system change request.
expected_outputs:
  - requirements-discovery-record.md
  - discovery_record_registry.csv row
validators:
  - python -m sys_for_ai.cli validate-discovery-record <path>
  - python -m sys_for_ai.cli validate-discovery-records registries/discovery_record_registry.csv
completion_evidence:
  - RDR path
  - validation status
  - open issue count
stop_conditions:
  - Subject layer cannot be classified.
  - Existing source evidence conflicts with user request.
  - User asks to skip discovery without Director Decision Record.
```

### 7.7 Acceptance Criteria

- `system-definition-interview-context-45` states it is the default discovery gate.
- RDR template includes system layer classification and exit checklist.
- Discovery validator enforces new required sections.
- Discovery registry exists and validates.
- Sample AgentJob exists and validates.
- Aggregate validation includes registered discovery records.

---

## 8. WS-04: Role Governance and `validate-roles`

### 8.1 Purpose

Implement the missing controlled role validation layer. This workstream closes a direct gap between Phase 1 PRD expectations and implementation.

### 8.2 Files to Add or Modify

```text
Sys4AI/registries/role_registry.csv
Sys4AI/registries/role_skill_crosswalk.csv
Sys4AI/registries/role_execution_binding_registry.csv
Sys4AI/schemas/contracts/role_registry_row.schema.json
Sys4AI/schemas/contracts/role_skill_crosswalk_row.schema.json
Sys4AI/schemas/contracts/role_execution_binding_registry_row.schema.json
Sys4AI/sys_for_ai/roles.py
Sys4AI/sys_for_ai/role_validators.py
Sys4AI/sys_for_ai/cli.py
Sys4AI/sys_for_ai/validators.py
Sys4AI/Makefile
Sys4AI/docs/generated/roles/README.md
Sys4AI/docs/generated/roles/<role-id>.md
Sys4AI/registries/derivative_registry.csv
```

### 8.3 Role Classes

Use this controlled vocabulary:

```text
framework_governance
system_design_core
system_design_support
implementation
verification
maintenance
runtime_control
temporary_agentjob_role
project_specific
```

### 8.4 Seed Role Registry

Seed rows should include the roles from the Phase 0 PRD and runtime aliases used by skill manifests.

| Role ID | Display Name | Role Class | Notes |
|---|---|---|---|
| `system_director` | System Director | `framework_governance` | Orchestrates phases, gates, handoffs, artifact governance. |
| `user_wants_elicitor` | System Developer / User Wants Elicitor | `system_design_core` | Uses discovery gate. |
| `existing_system_analyst` | Existing System Analyst | `system_design_support` | Brownfield/current-state analysis. |
| `requirements_manager` | System Manager / Requirements Manager | `system_design_core` | Converts user wants to system requirements. |
| `system_architect` | System Architect | `system_design_core` | Architecture drivers, views, ADRs. |
| `technical_requirements_engineer` | System Engineer / Technical Requirements Engineer | `system_design_core` | Technical requirements, allocation, verification. |
| `reconciliation_analyst` | System Analyst / Reconciliation Analyst | `system_design_core` | Reconciles user intent and technical obligations. |
| `reconciled_architecture_architect` | Reconciled Architecture Architect | `system_design_core` | Updates architecture after reconciliation. |
| `final_system_requirements_packager` | Final System Requirements Packager | `system_design_core` | Produces SRP. |
| `requirements_verifier` | Requirements Verifier / Consistency Auditor | `verification` | Checks consistency and traceability. |
| `domain_specialist` | Domain Specialist | `system_design_support` | Domain-specific validation hook. |
| `security_safety_privacy_compliance_reviewer` | Security, Safety, Privacy, and Compliance Reviewer | `verification` | Risk and control review. |
| `documentation_librarian` | Documentation Librarian / Configuration Controller | `framework_governance` | Artifact index, IDs, derivative policy. |
| `runtime_maintenance_planner` | Runtime and Maintenance Planner | `maintenance` | Ops and lifecycle requirements. |
| `control_loop_agentjob_planner` | Control Loop and AgentJob Planner | `runtime_control` | `/continue`, AgentJob schema, handoff semantics. |
| `context_memory_knowledge_architect` | Context, Memory, and Knowledge Architect | `system_design_support` | Source-first memory, retrieval, registry rules. |
| `svc_documentation_surface_architect` | SVC and Documentation Surface Architect | `system_design_support` | Source/version-control and derivative surfaces. |
| `implementation_initialization_agent` | Implementation Initialization Agent | `implementation` | Phase 1 repo bootstrap. |
| `verification_engineer` | Verification Engineer | `verification` | Validator/evidence focus. |
| `software_engineer` | Software Engineer | `implementation` | Code changes and implementation tasks. |
| `system_engineer` | System Engineer | `system_design_core` | Compatibility role posture used by current skill manifests. |
| `system_analyst` | System Analyst | `system_design_core` | Compatibility role posture used by current skill manifests. |

### 8.5 Role-to-Skill Crosswalk Seed Rules

Minimum required bindings:

| Role ID | Required Skills | Optional Skills |
|---|---|---|
| `user_wants_elicitor` | `system-definition-interview-context-45` | `conversation-to-prd`, `decision-grilling-context-45` |
| `requirements_manager` | `conversation-to-prd`, `technical-writing-quality-gate` | `decision-grilling`, `traceability-matrix-engine` |
| `system_architect` | `decision-grilling`, `mermaid-diagrams` or `plantuml-diagrams` | `artifact-contract-governance`, `interface-and-integration-discovery` |
| `technical_requirements_engineer` | `prd-to-implementation-plan`, `verification-validation-planner` | `agentjob-task-packet-author` |
| `requirements_verifier` | `technical-writing-quality-gate`, `traceability-matrix-engine` | `verification-validation-planner` |
| `documentation_librarian` | `source-authority-auditor`, `skill-import-generalizer` | `technical-writing-quality-gate` |
| `control_loop_agentjob_planner` | `continue`, `agentjob-task-packet-author`, `context-window-and-handoff-manager` | `director-decision-governor` |
| `context_memory_knowledge_architect` | `source-first-memory`, `source-authority-auditor` | `artifact-contract-governance` |
| `runtime_maintenance_planner` | `operations-and-maintenance-planner` | `evaluation-harness-designer` |
| `security_safety_privacy_compliance_reviewer` | `threat-model-and-permission-scope`, `assurance-case-builder` | `verification-validation-planner` |
| `system_director` | `director-decision-governor`, `system-layer-classifier`, `baseline-change-manager` | `source-first-memory` |

Some of the optional/required skills are added later by this plan. During intermediate phases, their crosswalk rows can be marked `conditional` or `approved_for_scaffold` until the skill exists.

### 8.6 Role Validator Design

Create:

```text
Sys4AI/sys_for_ai/role_validators.py
```

Required functions:

```python
def validate_role_registry(path: str | Path = "registries/role_registry.csv") -> ValidationResult: ...
def validate_role_skill_crosswalk(path: str | Path = "registries/role_skill_crosswalk.csv") -> ValidationResult: ...
def validate_role_execution_bindings(path: str | Path = "registries/role_execution_binding_registry.csv") -> ValidationResult: ...
def validate_role_graph() -> ValidationResult: ...
def validate_generated_role_docs(docs_root: str | Path = "docs/generated/roles") -> ValidationResult: ...
def validate_roles() -> ValidationResult: ...
```

Validation logic:

1. Validate row schemas.
2. Role IDs must be unique.
3. Role classes must be in controlled vocabulary.
4. System layer scopes must use allowed layer IDs or semicolon-separated allowed layer IDs.
5. Required skills must exist in active runtime registry or approved product scaffold, based on role scope.
6. Optional skills must exist or be listed as approved proposals.
7. Forbidden skills must not appear as required or optional for the same role.
8. Every active core skill must have at least one role binding unless explicitly exempt.
9. Every AgentJob role binding must reference a known role or approved temporary role.
10. Temporary roles must include expiry policy.
11. Generated role Markdown must be derivative and fresh relative to registry source hash where practical.

### 8.7 CLI and Makefile

Add:

```bash
python -m sys_for_ai.cli validate-roles
```

Add to aggregate validation.

### 8.8 Generated Role Docs

Add generator later or stub-generated docs now:

```text
Sys4AI/docs/generated/roles/README.md
Sys4AI/docs/generated/roles/system_director.md
...
```

Each page must include:

```md
> Generated derivative. Canonical role authority remains with `registries/role_registry.csv`, `registries/role_skill_crosswalk.csv`, and `registries/role_execution_binding_registry.csv`.
```

### 8.9 Acceptance Criteria

- `make validate-roles` exists.
- Aggregate `make validate` includes role validation.
- Role registry validates.
- Role-to-skill crosswalk validates.
- Role execution binding registry validates.
- Unknown roles fail validation.
- Unknown required skills fail validation unless marked as approved proposals during scaffold transition.
- Generated role docs are marked derivative.

---

## 9. WS-05: Runtime Skill Registry Reconciliation for `continue` and `source-first-memory`

### 9.1 Purpose

Remove ambiguity between active runtime skills and product-scaffold skills.

### 9.2 Current Issue

The product scaffold expects `continue` and `source-first-memory` as core skills. The active development runtime registry must either activate them or explicitly state that they are product-scaffold-only. The recommended path is to make both active runtime skills because self-hosting safely depends on them.

### 9.3 Files to Add or Modify

```text
.agents/skill_registry/SKILL_REGISTRY.yaml
.agents/skills/continue/SKILL.md
.agents/skills/continue/README.md
.agents/skills/continue/AGENTS.md
.agents/skills/continue/skill.yaml
.agents/skills/continue/examples/portable-example.md
.agents/skills/source-first-memory/SKILL.md
.agents/skills/source-first-memory/README.md
.agents/skills/source-first-memory/AGENTS.md
.agents/skills/source-first-memory/skill.yaml
.agents/skills/source-first-memory/examples/portable-example.md
.codex/skills/continue/SKILL.md
.codex/skills/source-first-memory/SKILL.md
Sys4AI/skills/core/continue/*
Sys4AI/skills/core/source-first-memory/*
Sys4AI/skills/core_skill_manifest.yaml
Sys4AI/registries/skill_registry.csv
```

### 9.4 Active Runtime Registry Entries

Add to `.agents/skill_registry/SKILL_REGISTRY.yaml`:

```yaml
  - skill_id: continue
    canonical_path: .agents/skills/continue
    status: active
    lifecycle_status: adapted_runtime_active
    manifest_path: .agents/skills/continue/skill.yaml
    required_by_roles:
      - system_director
      - control_loop_agentjob_planner
      - system_engineer
      - software_engineer
    required_skills:
      - source-first-memory
    optional_skills:
      - director-decision-governor
      - context-window-and-handoff-manager
    python_requirements: null
    scripts: []
    compatibility_shims:
      - .codex/skills/continue/SKILL.md
    migration_phase: adapted_runtime_active

  - skill_id: source-first-memory
    canonical_path: .agents/skills/source-first-memory
    status: active
    lifecycle_status: adapted_runtime_active
    manifest_path: .agents/skills/source-first-memory/skill.yaml
    required_by_roles:
      - system_director
      - context_memory_knowledge_architect
      - documentation_librarian
      - system_engineer
      - software_engineer
    required_skills: []
    optional_skills:
      - source-authority-auditor
    python_requirements: null
    scripts: []
    compatibility_shims:
      - .codex/skills/source-first-memory/SKILL.md
    migration_phase: adapted_runtime_active
```

If the existing root skill manifest validator does not allow `lifecycle_status`, either update the validator or omit the field from the root registry and store lifecycle in a separate registry. Preferred: update validator to allow lifecycle status.

### 9.5 `continue` Runtime Skill Behavior

`continue` must implement the development-system safe continuation pattern:

1. Inspect current program state.
2. Inspect latest handoff.
3. Run source-first memory preflight.
4. Select at most one authorized active AgentJob.
5. Emit execution packet.
6. Enforce allowed reads/writes and forbidden actions.
7. Run validators.
8. Produce completion receipt.
9. Produce or update handoff.
10. Refuse to continue if state is blocked, human-gated, or ambiguous.

### 9.6 `source-first-memory` Runtime Skill Behavior

`source-first-memory` must require:

1. Retrieval results include source path or registry row.
2. Structured artifacts include authority status.
3. Generated derivative results include source trace.
4. Memory hits that affect requirements, routing, claims, AgentJob boundaries, or handoffs are checked against canonical sources or registries.
5. Stale, orphaned, or unregistered derivative content is not actionable authority.

### 9.7 Codex Shims

Each shim should be minimal:

```md
# Compatibility Shim: continue

This shim points to the canonical runtime skill at `.agents/skills/continue/SKILL.md`.
```

### 9.8 Acceptance Criteria

- `.agents/skills/continue/skill.yaml` passes root skill validator.
- `.agents/skills/source-first-memory/skill.yaml` passes root skill validator.
- `.agents/skill_registry/SKILL_REGISTRY.yaml` includes both skills.
- `.codex/skills` shims exist.
- Product scaffold manifest and runtime registry no longer conflict.
- Root `make validate-dev-skills` passes.
- Product scaffold `make validate-skills` passes.

---

## 10. WS-06: Skill Lifecycle Governance

### 10.1 Purpose

Make skill status unambiguous across imported skills, active runtime skills, and product-scaffold reference skills.

### 10.2 Controlled Lifecycle Vocabulary

Use these statuses:

| Status | Runtime executable? | May be authoritative? | Meaning |
|---|---:|---:|---|
| `proposed` | No | No | Candidate skill not yet scaffolded. |
| `imported_unadapted` | No | No | Imported source exists but not adapted. |
| `adapter_shell` | Usually no | No | Local shell exists but full adaptation pending. |
| `adapted_runtime_active` | Yes | Yes, within declared authority | Active runtime skill. |
| `product_scaffold_reference` | No, unless copied/adapted | No for dev runtime | Product scaffold/reference skill. |
| `deprecated` | No or limited | No new use | Replaced or discouraged. |
| `superseded` | No | No | Replaced by another skill. |
| `blocked` | No | No | Cannot be used due to safety, validity, or authority issue. |

### 10.3 Files to Modify

```text
.agents/skill_registry/SKILL_REGISTRY.yaml
.agents/skills/*/skill.yaml
Sys4AI/skills/core_skill_manifest.yaml
Sys4AI/registries/skill_registry.csv
Sys4AI/registries/skill_lifecycle_status_registry.csv
scripts/skills/validate_skill_manifest.py
Sys4AI/sys_for_ai/validators.py
```

### 10.4 Validator Rules

Root skill validator should enforce:

1. If registry entry status is `active`, lifecycle must be `adapted_runtime_active` or equivalent.
2. If lifecycle is `adapter_shell`, the skill cannot be listed as mandatory runtime authority unless explicitly exempted.
3. If lifecycle is `product_scaffold_reference`, path should be under `Sys4AI/skills/core` or equivalent scaffold root.
4. Deprecated, superseded, and blocked skills cannot be required by active roles.
5. Every skill must declare provenance and local authority boundary.
6. Compatibility shims must not be canonical.

### 10.5 Migration Strategy

1. Add `skill_lifecycle_status_registry.csv` first.
2. Update validators to accept both old and new fields during transition.
3. Add lifecycle fields to root registry entries.
4. Add lifecycle fields to product scaffold manifest or map `adaptation_status` to lifecycle status.
5. Run validators.
6. Remove transitional compatibility only in a later cleanup phase.

### 10.6 Acceptance Criteria

- Lifecycle registry exists.
- Validators check lifecycle statuses.
- Runtime active skills have active lifecycle.
- Product scaffold skills are not mistaken for runtime authority.
- Deprecated or blocked skills cannot be required by active roles.

---

## 11. WS-07: New Core Skill Scaffolds, Registry Proposals, and Activation Policy

### 11.1 Purpose

Add all recommended new core organizational skills as governed skills. These are not project-specific domain skills; they are reusable framework capabilities.

### 11.2 New Core Skills

| Priority | Skill ID | Family | Purpose |
|---:|---|---|---|
| 1 | `role-catalog-governance` | role_governance | Maintain role registry, role-to-skill crosswalk, and execution bindings. |
| 2 | `system-layer-classifier` | system_layer_governance | Classify development/framework/template/target/derivative layer before work. |
| 3 | `artifact-contract-governance` | artifact_governance | Define and validate artifact contracts. |
| 4 | `traceability-matrix-engine` | traceability_governance | Maintain trace from discovery through validation and maintenance. |
| 5 | `director-decision-governor` | decision_governance | Create, validate, supersede, and apply Director Decision Records. |
| 6 | `verification-validation-planner` | verification_planning | Convert requirements into V&V plans, matrices, and evidence obligations. |
| 7 | `source-authority-auditor` | source_authority | Audit canonical sources, derivatives, stale docs, and authority inversions. |
| 8 | `context-window-and-handoff-manager` | context_handoff | Generalize context checkpoint and resumable handoff behavior. |
| 9 | `threat-model-and-permission-scope` | safety_security_privacy | Identify permissions, autonomy boundaries, tool/data risks, and controls. |
| 10 | `evaluation-harness-designer` | evaluation_design | Design eval scenarios, rubrics, regression checks, and failure probes. |
| 11 | `baseline-change-manager` | change_control | Manage baselines, supersession, migrations, rollback, and change evidence. |
| 12 | `agentjob-task-packet-author` | agentjob_authoring | Convert implementation plans into bounded AgentJobs and task packets. |
| 13 | `operations-and-maintenance-planner` | operations_maintenance | Define monitoring, incidents, updates, evaluation cadence, and maintenance. |
| 14 | `project-ontology-and-glossary` | ontology_glossary | Maintain controlled vocabulary, ontology, and term decisions. |
| 15 | `domain-pack-router` | domain_routing | Detect when project-specific domain packs are needed and route accordingly. |
| 16 | `requirements-discovery-governor` | discovery_governance | Govern RDR creation and discovery-to-USRD transition. May be wrapper around existing discovery skill. |
| 17 | `interface-and-integration-discovery` | interface_discovery | Identify external systems, interfaces, data flows, owners, and integration risks. |
| 18 | `assurance-case-builder` | assurance_case | Build claims/evidence/argument structure for high-impact systems. |

### 11.3 Activation Strategy

Use a two-stage activation model:

1. **Scaffold stage:** Add proposal registry rows, product scaffold adapters, and optional `.agents` inactive manifests.
2. **Runtime active stage:** Promote selected skills to active runtime once `SKILL.md`, `skill.yaml`, role bindings, examples, and validators are in place.

Because the user requested implementing all recommendations, this plan activates all core skills with at least a minimal governed runtime package. Deeper automation scripts can be added later, but every skill must have enough procedure, inputs, outputs, failure modes, authority rules, and validation guidance to be usable by an agent.

### 11.4 Files to Add for Each Skill

For each skill ID `<skill-id>`:

```text
.agents/skills/<skill-id>/SKILL.md
.agents/skills/<skill-id>/README.md
.agents/skills/<skill-id>/AGENTS.md
.agents/skills/<skill-id>/skill.yaml
.agents/skills/<skill-id>/examples/portable-example.md
.codex/skills/<skill-id>/SKILL.md
Sys4AI/skills/core/<skill-id>/SKILL.md
Sys4AI/skills/core/<skill-id>/README.md
Sys4AI/skills/core/<skill-id>/AGENTS.md
Sys4AI/skills/core/<skill-id>/examples/portable-example.md
```

### 11.5 Common Runtime Skill Manifest Pattern

Every new `.agents/skills/<skill-id>/skill.yaml` should include:

```yaml
skill_id: <skill-id>
version: 0.1.0
status: active
canonical_path: .agents/skills/<skill-id>
summary: <one sentence>
scope:
  system_agnostic: true
  target_system_types:
    - agentic_ai_software_harness
    - framework_development
    - documentation_governed_system
    - source_first_system
domain_emphasis:
  - systems_engineering
  - software_engineering
  - ai_systems
required_role_posture:
  - system_analyst
  - system_engineer
  - software_engineer
activation:
  triggers:
    - <trigger>
inputs:
  required:
    - <input>
  optional:
    - <input>
outputs:
  primary:
    - <output>
  evidence:
    - <evidence>
dependencies:
  required_skills: []
  optional_skills: []
  python: null
authority:
  may_read:
    - PRDs/**
    - Sys4AI/**
  may_write: []
  may_not:
    - Treat generated derivatives as canonical.
    - Mutate controlled artifacts without AgentJob authority.
validation:
  commands: []
  contextual_validation_rationale: <why command validation is contextual or which validator applies>
  validator_classes:
    - process_validation
    - trace_validation
handoff:
  requires_completion_receipt: true
  evidence:
    - changed artifacts or no-change decision
    - validation status
    - unresolved issues
```

### 11.6 Registry Updates

Update:

```text
.agents/skill_registry/SKILL_REGISTRY.yaml
Sys4AI/skills/core_skill_manifest.yaml
Sys4AI/registries/skill_registry.csv
Sys4AI/registries/core_skill_proposal_registry.csv
Sys4AI/registries/role_skill_crosswalk.csv
```

### 11.7 Acceptance Criteria

- Every recommended core skill has a proposal row.
- Every recommended core skill has an active runtime skill package or an explicitly justified staged activation row.
- Every active runtime skill passes root skill validation.
- Every active runtime skill has a product scaffold adapter.
- Every active runtime skill has role bindings.
- No new skill is project-specific domain logic.
- Domain-specific behavior is routed through `domain-pack-router` only.

---

## 12. WS-08: `system-layer-classifier` and Self-Hosting Mode

### 12.1 Purpose

Implement a core skill and policy layer that prevents confusion between `Sys4AI-dev`, `Sys4AI`, future target-system templates, future target-system instances, and generated derivatives.

### 12.2 Files to Add or Modify

```text
.agents/skills/system-layer-classifier/*
Sys4AI/skills/core/system-layer-classifier/*
Sys4AI/docs/self_hosting_mode_policy.md
Sys4AI/configs/self_hosting_mode.toml
Sys4AI/registries/system_layer_registry.csv
Sys4AI/registries/config_source_registry.csv
Sys4AI/schemas/contracts/self_hosting_mode.schema.json
Sys4AI/sys_for_ai/system_layers.py
Sys4AI/sys_for_ai/cli.py
Sys4AI/Makefile
```

### 12.3 Self-Hosting Policy Document

Create:

```text
Sys4AI/docs/self_hosting_mode_policy.md
```

Required sections:

1. Purpose and scope.
2. Layer definitions.
3. Active runtime versus product scaffold.
4. Authority hierarchy.
5. Required system-layer classification fields.
6. When Director Decision is required.
7. Forbidden mutations.
8. Generated derivative limitations.
9. AgentJob implications.
10. Validation commands.
11. Examples.
12. Failure modes.

### 12.4 Self-Hosting TOML

Create:

```toml
[system_layers]
development_system = "Sys4AI-dev"
framework_product = "Sys4AI"
target_system_template = "future-target-system-template"
derivative_surface = "generated-derivative-surface"

[self_hosting]
enabled = true
requires_layer_classification = true
requires_director_decision_for_authority_expansion = true
generated_derivatives_can_authorize_changes = false
product_scaffold_is_runtime_authority = false

[authority_roots]
development_system_runtime = [".agents/skills", ".agents/skill_registry", "scripts", "PRDs", "implementation_plans"]
product_scaffold = ["Sys4AI"]
derivative_roots = ["docs/generated", "Sys4AI/docs/generated"]

[validation]
required_commands = [
  "make validate-dev-skills",
  "cd Sys4AI && make validate-system-layers",
  "cd Sys4AI && make validate"
]
```

Register it in `config_source_registry.csv`.

### 12.5 `system-layer-classifier` Skill Outputs

The skill should produce:

```yaml
system_layer_classification_id: SLC-<date>-<nnn>
subject_system_id: <id>
subject_system_name: <name>
subject_layer: development_system | framework_product | target_system_template | target_system_instance | derivative_surface
work_type: discovery | requirements | architecture | implementation | validation | improvement | maintenance | documentation | runtime_control
canonical_authorities:
  - <path or registry row>
allowed_mutations:
  - <path glob>
forbidden_mutations:
  - <path glob or action>
requires_director_decision: true | false
required_next_gate: discovery_gate | role_validation | director_decision | source_memory_preflight | none
evidence:
  - <source path, user statement, registry row>
open_issues:
  - <issue>
```

### 12.6 Validator

Create:

```python
def validate_system_layers(path: str | Path = "registries/system_layer_registry.csv") -> ValidationResult: ...
def validate_self_hosting_config(path: str | Path = "configs/self_hosting_mode.toml") -> ValidationResult: ...
```

Checks:

- All required layer IDs exist.
- Layer roots are relative paths or explicit placeholders.
- Derivative layer cannot have canonical mutation rights.
- `product_scaffold_is_runtime_authority` must be false unless a Director decision exists.
- Required validation commands are non-empty.
- System layer registry and self-hosting TOML agree on layer IDs.

### 12.7 Acceptance Criteria

- Self-hosting policy exists.
- Self-hosting TOML exists and is registered.
- `validate-system-layers` passes.
- System layer classifier skill exists and validates.
- AgentJob templates include subject layer fields.
- Discovery gate uses system layer classification.

---

## 13. WS-09: Artifact Contract Governance

### 13.1 Purpose

Make artifact structures controlled, inspectable, and validateable.

### 13.2 Files to Add or Modify

```text
.agents/skills/artifact-contract-governance/*
Sys4AI/skills/core/artifact-contract-governance/*
Sys4AI/registries/artifact_contract_registry.csv
Sys4AI/schemas/contracts/artifact_contract_registry_row.schema.json
Sys4AI/sys_for_ai/artifact_contracts.py
Sys4AI/sys_for_ai/cli.py
Sys4AI/Makefile
Sys4AI/templates/artifacts/*
```

### 13.3 Artifact Contract Registry Seed Rows

Create rows for:

| Artifact Type | Default Authority | Registry Required | Notes |
|---|---|---:|---|
| RDR | derivative_draft | yes | Discovery evidence before USRD. |
| USRD | controlled_source | yes | User wants source. |
| ESAR | controlled_source | conditional | Brownfield/current-state. |
| SRD | controlled_source | yes | System requirements. |
| ARD | controlled_source | yes | Architecture requirements. |
| TRP | controlled_source | yes | Implementable technical requirements. |
| RSRD | controlled_source | yes | Reconciled system requirements. |
| RARD | controlled_source | yes | Reconciled architecture. |
| SRP | canonical_package | yes | Implementation-ready package. |
| CLRA | controlled_source | conditional | Control loop annex. |
| CKMSRA | controlled_source | conditional | Memory annex. |
| SVCDA | controlled_source | conditional | Source/version-control annex. |
| AgentJob | control_record | yes | Bounded execution. |
| DirectorDecision | control_record | yes | Routing/authority decision. |
| Handoff | control_record | yes | Continuation handoff. |
| CompletionReceipt | control_record | yes | Completion evidence. |
| MemoryPreflightReceipt | control_record | yes | Memory source verification. |

### 13.4 Validator Behavior

`validate-artifact-contracts` should:

1. Validate row schema.
2. Ensure producer roles exist.
3. Ensure consumer roles exist.
4. Ensure validation contract ID exists when specified.
5. Ensure required sections are not empty for major artifacts.
6. Ensure derivative surfaces are not default canonical.
7. Ensure RDR is not canonical.
8. Ensure SRP requires traceability and implementation readiness sections.

### 13.5 Skill Behavior

`artifact-contract-governance` should guide agents to:

1. Determine artifact type.
2. Load artifact contract registry.
3. Check producer/consumer roles.
4. Check required sections.
5. Check authority class.
6. Check validation contract.
7. Decide whether the artifact can be promoted.
8. Emit repair tasks if missing sections or authority mismatch exist.

### 13.6 Acceptance Criteria

- Artifact contract registry exists and validates.
- RDR, USRD, SRD, ARD, TRP, RSRD, RARD, SRP, CLRA, CKMSRA, SVCDA are represented.
- Control record artifact types are represented.
- Validator catches RDR marked canonical.
- Validator catches unknown producer role.

---

## 14. WS-10: Traceability Matrix Engine

### 14.1 Purpose

Provide a core skill and validation support for maintaining traceability from discovery evidence through requirements, architecture, implementation tasks, validation evidence, maintenance decisions, and improvement loops.

### 14.2 Files to Add or Modify

```text
.agents/skills/traceability-matrix-engine/*
Sys4AI/skills/core/traceability-matrix-engine/*
Sys4AI/registries/requirement_trace_registry.csv
Sys4AI/registries/object_relationship_registry.csv
Sys4AI/registries/artifact_contract_registry.csv
Sys4AI/sys_for_ai/traceability.py
Sys4AI/sys_for_ai/cli.py
Sys4AI/Makefile
Sys4AI/templates/traceability/traceability-ledger-template.md
```

### 14.3 Trace Objects

The trace engine should handle:

```text
user statement -> RDR need
RDR need -> candidate requirement
candidate requirement -> USRD want
USRD want -> SRD requirement
SRD requirement -> ARD driver/view/decision
SRD/ARD -> TRP technical requirement
TRP -> RSRD/RARD reconciliation item
RSRD/RARD -> SRP final requirement
SRP requirement -> implementation task packet
implementation task packet -> AgentJob
AgentJob -> changed artifact
changed artifact -> completion receipt
completion receipt -> validation evidence
validation evidence -> maintenance decision or improvement signal
```

### 14.4 Trace Registry Extension

Existing `requirement_trace_registry.csv` handles Phase 0 to Phase 1 coverage. Do not break it. Add either:

1. A new `traceability_edge_registry.csv`, or
2. Extend `object_relationship_registry.csv` for trace edges.

Recommended new file:

```text
Sys4AI/registries/traceability_edge_registry.csv
```

Header:

```csv
trace_edge_id,source_object_id,source_object_type,target_object_id,target_object_type,trace_relation,evidence_path,authority_status,validation_status,source_hash,last_validated_at,notes
```

Relations:

```text
satisfies
derives_from
refines
allocates_to
verified_by
implemented_by
supersedes
blocks
mitigates
uses_evidence
routes_to
```

### 14.5 Validator

Add:

```bash
make validate-traceability-graph
```

Checks:

- Edge IDs unique.
- Relation is in controlled vocabulary.
- Evidence path exists.
- Source and target object IDs are non-empty.
- No edge points from derivative to canonical promotion without promotion evidence.
- Every final SRP requirement traces back to user intent or explicit Director decision.
- Every AgentJob traces to SRP, implementation plan, issue, or Director decision.

### 14.6 Skill Behavior

`traceability-matrix-engine` should:

1. Load relevant artifacts and registries.
2. Identify traceable IDs.
3. Create missing trace edges as candidate rows.
4. Detect orphan requirements.
5. Detect implementation tasks without requirements.
6. Detect validation evidence without requirement target.
7. Emit trace gap report.

### 14.7 Acceptance Criteria

- Traceability edge registry exists.
- Validator catches missing evidence path.
- Validator catches orphan SRP requirement where possible.
- Skill package exists and validates.
- Existing requirement trace validation continues to pass.

---

## 15. WS-11: Director Decision Governance

### 15.1 Purpose

Create a core skill for Director Decision Records, since Director decisions are required for routing, role selection, authority expansion, task creation, and job creation when tracked state does not already determine the route.

### 15.2 Files to Add or Modify

```text
.agents/skills/director-decision-governor/*
Sys4AI/skills/core/director-decision-governor/*
Sys4AI/control_records/director_decisions/*.yaml
Sys4AI/registries/director_decision_registry.csv
Sys4AI/schemas/contracts/director_decision.schema.json
Sys4AI/sys_for_ai/control_loop.py
Sys4AI/sys_for_ai/validators.py
```

### 15.3 Decision Record Template

Create:

```text
Sys4AI/templates/control_records/director_decision_template.yaml
```

Required fields:

```yaml
schema_version: "0.2.0"
director_decision_id: DDR-<YYYYMMDD>-<NNN>
subject_system_id: <id>
subject_layer: <layer>
decision_type: routing | role_selection | authority_expansion | task_creation | agentjob_creation | waiver | promotion | supersession
status: proposed | active | superseded | rejected
context:
  problem: <text>
  triggering_event: <text>
  current_state: <text>
alternatives:
  - id: ALT-001
    description: <text>
    benefits: <text>
    risks: <text>
selected_alternative: ALT-001
rationale: <text>
authority_change:
  expands_authority: true | false
  allowed_reads: []
  allowed_writes: []
  forbidden_actions: []
source_trace: []
validators_required: []
supersedes: ""
completion_evidence_required: []
```

### 15.4 Skill Behavior

`director-decision-governor` should:

1. Detect when a Director Decision is required.
2. Identify decision type.
3. Gather source evidence.
4. List alternatives.
5. Select or recommend alternative.
6. Declare authority change.
7. Record validation obligations.
8. Register decision.
9. Supersede prior decision when needed.

### 15.5 Acceptance Criteria

- Skill exists and validates.
- Decision template exists.
- Validator catches missing alternatives.
- Validator catches authority expansion without forbidden actions and validators.
- Registry row exists for sample decision.

---

## 16. WS-12: Verification, Assurance, Threat, and Evaluation Core Skills

### 16.1 Purpose

Add core skills that transform requirements and architecture into evidence obligations, safety/security/privacy scope, assurance claims, and evaluation harness plans.

### 16.2 Skills in This Workstream

```text
verification-validation-planner
assurance-case-builder
threat-model-and-permission-scope
evaluation-harness-designer
```

### 16.3 Shared Design Rule

These skills must distinguish:

- Structural validation.
- Process validation.
- Domain validation.
- User acceptance.
- Safety/security assurance.
- Production readiness.

They must never claim that a passing schema validator proves domain truth or safety.

### 16.4 `verification-validation-planner`

**Inputs:** RDR, USRD, SRD, ARD, TRP, SRP, artifact contracts.
**Outputs:**

```text
verification_matrix.md
validation_plan.md
acceptance_criteria_register.csv
evidence_obligation_map.csv
```

**Procedure:**

1. Extract requirements and candidate requirements.
2. Classify each as functional, quality, interface, data, security, privacy, safety, operational, or governance.
3. Assign verification method: inspection, analysis, demonstration, test, review, simulation, formal proof, domain expert review, red-team review, eval harness.
4. Define acceptance criteria.
5. Define evidence obligation.
6. Mark unverifiable requirements as open issues.
7. Emit validation plan.

### 16.5 `assurance-case-builder`

**Inputs:** Requirements, risk register, threat model, validation plan.
**Outputs:**

```text
assurance_case.md
claim_evidence_registry.csv
risk_control_matrix.csv
residual_risk_register.md
```

**Procedure:**

1. Identify top-level claims.
2. Decompose claims into subclaims.
3. Map evidence.
4. Record assumptions.
5. Record defeaters and residual risks.
6. Mark unsupported claims.
7. Route to domain/security/safety review where needed.

### 16.6 `threat-model-and-permission-scope`

**Inputs:** ARD, tool permissions, data access, user roles, deployment context.
**Outputs:**

```text
threat_model.md
permission_scope_matrix.csv
data_handling_register.csv
unsafe_action_register.md
```

**Procedure:**

1. Identify assets.
2. Identify actors and trust boundaries.
3. Identify tools and external actions.
4. Identify data classes.
5. Identify autonomy levels.
6. Identify misuse/abuse cases.
7. Map controls and evidence.
8. Define forbidden actions for AgentJobs.

### 16.7 `evaluation-harness-designer`

**Inputs:** Requirements, scenarios, quality attributes, known failure modes.
**Outputs:**

```text
evaluation_plan.md
scenario_eval_registry.csv
rubric.md
regression_suite_plan.md
```

**Procedure:**

1. Identify behavior to evaluate.
2. Create scenario set.
3. Define expected outputs or rubrics.
4. Define regression cases.
5. Define evaluation cadence.
6. Define failure thresholds.
7. Map evals to requirements and risks.

### 16.8 Acceptance Criteria

- All four skill packages exist and validate.
- Each skill has role bindings.
- Each skill has artifact contract rows for outputs.
- No skill treats validator success as domain truth.
- Security/safety/privacy reviewer role has required bindings to threat and assurance skills.

---

## 17. WS-13: Baseline Change, AgentJob Authoring, Operations, Ontology, Domain Routing, Interface Discovery, and Context Handoff Skills

### 17.1 Purpose

Add remaining core system-management skills needed for long-term maintainability and agentic execution.

### 17.2 Skills in This Workstream

```text
baseline-change-manager
agentjob-task-packet-author
operations-and-maintenance-planner
project-ontology-and-glossary
domain-pack-router
interface-and-integration-discovery
context-window-and-handoff-manager
source-authority-auditor
requirements-discovery-governor
```

### 17.3 `baseline-change-manager`

**Outputs:**

```text
baseline_change_record.yaml
supersession_map.csv
migration_evidence.md
rollback_plan.md
```

**Core rules:**

- Do not silently rewrite activated controls.
- Supersede when correcting baselines.
- Require migration evidence when schema or registry changes affect existing artifacts.
- Require rollback plan for significant authority changes.

### 17.4 `agentjob-task-packet-author`

**Outputs:**

```text
agentjob.yaml
task_packet.md
expected_completion_receipt.yaml
handoff_template.yaml
```

**Core rules:**

- Every AgentJob needs objective, role binding, allowed reads, allowed writes, forbidden actions, required inputs, expected outputs, validators, completion evidence, and stop conditions.
- AgentJob must include subject layer.
- AgentJob cannot expand authority without Director Decision.

### 17.5 `operations-and-maintenance-planner`

**Outputs:**

```text
operations_requirements.md
maintenance_plan.md
monitoring_observability_plan.md
incident_response_requirements.md
```

**Core rules:**

- Define runtime monitoring expectations.
- Define eval cadence.
- Define update policy.
- Define incident categories.
- Define maintenance ownership.

### 17.6 `project-ontology-and-glossary`

**Outputs:**

```text
glossary.md
ontology_registry.csv
term_decision_records.md
synonym_map.csv
```

**Core rules:**

- Define terms before using them as requirements authority.
- Record ambiguous terms as open issues.
- Link term decisions to artifacts and source evidence.

### 17.7 `domain-pack-router`

**Outputs:**

```text
domain_trigger_report.md
recommended_domain_packs.yaml
domain_specialist_routing_decision.yaml
```

**Core rules:**

- Router is core.
- Domain packs are project-specific.
- Router can recommend but not invent domain-specific authority.
- Domain Specialist or Director must approve domain-specific constraints.

### 17.8 `interface-and-integration-discovery`

**Outputs:**

```text
interface_candidate_register.csv
external_systems_register.csv
data_flow_context.md
integration_risk_register.md
```

**Core rules:**

- Identify external actors, systems, APIs, tools, files, data flows, commands, events, owners, and failure modes.
- Mark unknown owners and protocols as open issues.
- Feed ARD and TRP.

### 17.9 `context-window-and-handoff-manager`

**Outputs:**

```text
context_checkpoint.yaml
handoff.yaml
temp_state_summary.md
resume_instruction.md
```

**Core rules:**

- Generalize the 45 percent context checkpoint pattern.
- Do not overwrite active checkpoint without confirmation or supersession rule.
- Always include last question/answer or last action/result when checkpointing an interview or execution flow.
- Must route through completion receipt and handoff when under AgentJob control.

### 17.10 `source-authority-auditor`

**Outputs:**

```text
source_authority_audit.md
stale_derivative_report.md
orphan_derivative_report.md
authority_inversion_findings.md
```

**Core rules:**

- Canonical sources outrank generated summaries.
- Stale derivatives cannot be used as authority.
- Missing registry rows are audit findings.
- Authority inversion is a blocking finding for gated changes.

### 17.11 `requirements-discovery-governor`

This may be a wrapper skill rather than a separate execution skill.

**Outputs:**

```text
discovery_gate_decision.yaml
discovery_completion_receipt.yaml
discovery_to_usrd_handoff.md
```

**Core rules:**

- Ensure RDR exists before USRD.
- Ensure discovery waiver is recorded if skipped.
- Ensure candidate requirements remain candidates.
- Ensure next route is explicit.

### 17.12 Acceptance Criteria

- Every skill has active runtime package and product scaffold adapter.
- Every skill has role bindings.
- Every skill has output artifact contracts where applicable.
- Every skill validates with root skill validator.
- No skill introduces project-specific domain content.

---

## 18. WS-14: Generated Documentation and Derivative Surface Updates

### 18.1 Purpose

Ensure new registries, roles, artifact contracts, system layers, discovery records, and skill lifecycle states are documented as derivative reader surfaces without becoming canonical.

### 18.2 Files to Add or Modify

```text
Sys4AI/docs/generated/configuration_control/*
Sys4AI/docs/generated/validation_contracts/*
Sys4AI/docs/generated/roles/*
Sys4AI/docs/generated/artifact_contracts/*
Sys4AI/docs/generated/system_layers/*
Sys4AI/docs/generated/core_skills/*
Sys4AI/registries/derivative_registry.csv
Sys4AI/sys_for_ai/derivatives.py
Sys4AI/sys_for_ai/derivative_generation.py
Sys4AI/Makefile
```

### 18.3 Required Derivative Pages

Add generated or stub-generated pages for:

1. System layer registry.
2. Self-hosting mode config.
3. Discovery record registry.
4. Role registry.
5. Role-to-skill crosswalk.
6. Role execution bindings.
7. Artifact contract registry.
8. Core skill proposals.
9. Skill lifecycle statuses.
10. New validation contracts.

### 18.4 Required Banner

Every generated page must include:

```md
> Generated derivative. Canonical authority remains with the registered source files, registries, validation contracts, and control records named on this page. Do not hand-edit this page as source authority.
```

### 18.5 Validator Updates

`validate-generated-derivatives` should catch:

- Generated page missing authority banner.
- Generated page missing source path.
- Generated page missing registry evidence.
- Generated page claims canonical authority.
- Generated page stale relative to source hash where practical.
- Derivative registry missing page row.

### 18.6 Acceptance Criteria

- Derivative registry includes all generated pages.
- Generated pages are non-canonical.
- Validation catches missing banner.
- Aggregate validation passes.

---

## 19. WS-15: End-to-End Acceptance and Release Bundle

### 19.1 Purpose

Prove the full recommendation set has landed across PRDs, registries, schemas, skills, validators, docs, and control records.

### 19.2 Required Commands

Run from repository root:

```bash
make validate-dev-skills
make validate-product-scaffold
make validate
```

Run from product scaffold:

```bash
cd Sys4AI
make doctor
make validate-discovery-template
make validate-system-layers
make validate-discovery-records
make validate-roles
make validate-artifact-contracts
make validate-core-skill-proposals
make validate-skill-lifecycle
make validate-format-profiles
make validate-config-sources
make validate-control-records
make validate-program-state
make validate-agentjob-registry
make validate-director-decision-registry
make validate-handoff-registry
make validate-completion-receipt-registry
make validate-memory-preflight-registry
make validate-handoffs
make validate-completion-receipts
make validate-state-snapshots
make validate-memory-preflight
make validate-validation-contract-registry
make validate-toml-config
make validate-jsonschema-contracts
make validate-registry-graph
make validate-check-diff
make validate-one-active-agentjob
make validate-control-loop
make validate-requirement-trace
make generate-config-control-wiki
make generate-validation-contracts-catalog
make validate-generated-derivatives
make validate
```

### 19.3 Acceptance Packet

Create:

```text
implementation_plans/completion_receipts/CR-SFADEV-ALL-RECS-IMPLEMENTED-001.md
```

Required sections:

1. Summary.
2. PRD changes.
3. Registry changes.
4. Schema changes.
5. Skill changes.
6. Validator changes.
7. Documentation changes.
8. Commands run.
9. Validation results.
10. Open issues.
11. Deferred items.
12. Known limitations.
13. Maintainer approval checklist.

### 19.4 Definition of Done

The implementation is complete when:

- Phase 0 PRD contains all new core requirements.
- Phase 1 PRD contains all new initialization requirements.
- RDR is first-class and appears before USRD in pipeline.
- `system-definition-interview-context-45` is mandatory default discovery gate.
- System-layer classification exists and validates.
- Self-hosting mode policy and config exist and validate.
- `validate-roles` exists and is part of aggregate validation.
- Role registries exist and validate.
- `continue` and `source-first-memory` are reconciled between active runtime and product scaffold.
- Skill lifecycle governance exists and validates.
- All recommended new core skills exist and validate.
- Artifact contract governance exists and validates.
- Traceability graph support exists and validates.
- Director decision governance exists and validates.
- Verification, assurance, threat, evaluation, baseline, AgentJob, ops, ontology, domain router, interface, context handoff, source audit, and discovery governor skills exist and validate.
- Generated docs are derivative and validated.
- Root `make validate` passes.
- Product scaffold `make validate` passes.
- Completion receipt records exactly what changed and what remains open.

---

## 20. Detailed AgentJob Backlog

The following AgentJobs provide a bounded execution sequence. They must be implemented one by one using `/continue` from tracked state. Each completed AgentJob requires completion evidence, a handoff markdown file, related controlled closeout files, an in-chat completion report, a commit, and `git push` evidence before the next AgentJob begins.

### AJ-00: Baseline Validation

```yaml
agentjob_id: AJ-SFADEV-00-BASELINE-VALIDATION-001
objective: Capture current validation baseline before implementing recommendations.
role: system_director
subject_system_id: Sys4AI-dev
subject_layer: development_system
allowed_reads:
  - "**"
allowed_writes:
  - implementation_plans/completion_receipts/**
forbidden_actions:
  - Modify PRDs or source files.
expected_outputs:
  - Baseline validation receipt.
validators:
  - make validate-dev-skills
  - make validate-product-scaffold
  - make validate
stop_conditions:
  - Repository has uncommitted work that could be overwritten.
```

### AJ-01: PRD Integration

```yaml
agentjob_id: AJ-SFADEV-01-PRD-INTEGRATION-001
objective: Add discovery gate, RDR, system layer, self-hosting, role governance, and skill lifecycle requirements to PRDs.
role: system_engineer
subject_system_id: Sys4AI
subject_layer: framework_product
allowed_reads:
  - PRDs/**
  - Sys4AI/templates/system_definition/**
  - .agents/skills/system-definition-interview-context-45/**
allowed_writes:
  - PRDs/Sys4AI_phase-0_product_system_design_prd.md
  - PRDs/Sys4AI_phase-1_implementation_initialization_prd.md
  - Sys4AI/registries/requirement_trace_registry.csv
forbidden_actions:
  - Remove existing Phase 0 to Phase 1 boundary.
  - Mark RDR as canonical requirements baseline.
expected_outputs:
  - Updated PRDs.
  - Updated requirement trace registry.
validators:
  - cd Sys4AI && make validate-requirement-trace
stop_conditions:
  - New requirement IDs collide.
```

### AJ-02: Registry and Schema Expansion

```yaml
agentjob_id: AJ-SFADEV-02-REGISTRY-SCHEMA-EXPANSION-001
objective: Add registries and row schemas for system layers, discovery records, roles, artifact contracts, core skill proposals, and skill lifecycle statuses.
role: implementation_initialization_agent
subject_system_id: Sys4AI
subject_layer: framework_product
allowed_reads:
  - Sys4AI/registries/**
  - Sys4AI/schemas/contracts/**
  - Sys4AI/sys_for_ai/**
allowed_writes:
  - Sys4AI/registries/**
  - Sys4AI/schemas/contracts/**
  - Sys4AI/sys_for_ai/validators.py
  - Sys4AI/sys_for_ai/cli.py
  - Sys4AI/Makefile
forbidden_actions:
  - Remove existing registry headers.
  - Break existing validation commands.
expected_outputs:
  - New registries.
  - New row schemas.
  - New CLI validators.
  - New Makefile targets.
validators:
  - cd Sys4AI && make validate-jsonschema-contracts
  - cd Sys4AI && make validate-registry-graph
  - cd Sys4AI && make validate
stop_conditions:
  - Existing aggregate validation breaks without repair path.
```

### AJ-03: Discovery Gate Implementation

```yaml
agentjob_id: AJ-SFADEV-03-DISCOVERY-GATE-001
objective: Integrate Requirements Discovery Record and `system-definition-interview-context-45` as operational discovery gate.
role: user_wants_elicitor
subject_system_id: Sys4AI
subject_layer: framework_product
allowed_reads:
  - .agents/skills/system-definition-interview-context-45/**
  - Sys4AI/templates/system_definition/**
  - Sys4AI/sys_for_ai/discovery.py
allowed_writes:
  - .agents/skills/system-definition-interview-context-45/**
  - Sys4AI/skills/core/system-definition-interview-context-45/**
  - Sys4AI/templates/system_definition/**
  - Sys4AI/sys_for_ai/discovery.py
  - Sys4AI/registries/discovery_record_registry.csv
forbidden_actions:
  - Automatically create PRD without explicit approval.
  - Promote candidate requirements.
expected_outputs:
  - Updated skill docs.
  - Updated RDR template.
  - Enhanced discovery validator.
validators:
  - make validate-dev-skills
  - cd Sys4AI && make validate-discovery-template
  - cd Sys4AI && make validate-discovery-records
stop_conditions:
  - RDR authority becomes canonical by accident.
```

### AJ-04: Role Governance

```yaml
agentjob_id: AJ-SFADEV-04-ROLE-GOVERNANCE-001
objective: Implement role registries, role-to-skill crosswalk, role execution bindings, role validators, CLI command, and Makefile target.
role: implementation_initialization_agent
subject_system_id: Sys4AI
subject_layer: framework_product
allowed_reads:
  - PRDs/**
  - .agents/skill_registry/SKILL_REGISTRY.yaml
  - Sys4AI/skills/core_skill_manifest.yaml
  - Sys4AI/registries/**
allowed_writes:
  - Sys4AI/registries/role_registry.csv
  - Sys4AI/registries/role_skill_crosswalk.csv
  - Sys4AI/registries/role_execution_binding_registry.csv
  - Sys4AI/schemas/contracts/role*.schema.json
  - Sys4AI/sys_for_ai/roles.py
  - Sys4AI/sys_for_ai/role_validators.py
  - Sys4AI/sys_for_ai/cli.py
  - Sys4AI/Makefile
forbidden_actions:
  - Treat generated role docs as canonical.
expected_outputs:
  - `make validate-roles`.
  - Aggregate validation includes role validation.
validators:
  - cd Sys4AI && make validate-roles
  - cd Sys4AI && make validate
stop_conditions:
  - Existing skills cannot be mapped to roles.
```

### AJ-05: Runtime Skill Reconciliation

```yaml
agentjob_id: AJ-SFADEV-05-RUNTIME-SKILL-RECONCILIATION-001
objective: Activate or explicitly classify `continue` and `source-first-memory` across runtime and scaffold skill registries.
role: documentation_librarian
subject_system_id: Sys4AI-dev
subject_layer: development_system
allowed_reads:
  - .agents/skill_registry/SKILL_REGISTRY.yaml
  - .agents/skills/**
  - Sys4AI/skills/core_skill_manifest.yaml
  - Sys4AI/registries/skill_registry.csv
allowed_writes:
  - .agents/skill_registry/SKILL_REGISTRY.yaml
  - .agents/skills/continue/**
  - .agents/skills/source-first-memory/**
  - .codex/skills/continue/**
  - .codex/skills/source-first-memory/**
  - Sys4AI/skills/core/continue/**
  - Sys4AI/skills/core/source-first-memory/**
  - Sys4AI/registries/skill_registry.csv
forbidden_actions:
  - Mark skill active without SKILL.md and skill.yaml.
expected_outputs:
  - Active runtime skill entries.
  - Product scaffold sync.
validators:
  - make validate-dev-skills
  - cd Sys4AI && make validate-skills
stop_conditions:
  - Runtime and scaffold authority cannot be reconciled.
```

### AJ-06: Skill Lifecycle Governance

```yaml
agentjob_id: AJ-SFADEV-06-SKILL-LIFECYCLE-001
objective: Add controlled skill lifecycle vocabulary and validation.
role: documentation_librarian
subject_system_id: Sys4AI-dev
subject_layer: development_system
allowed_reads:
  - .agents/skill_registry/SKILL_REGISTRY.yaml
  - .agents/skills/**
  - Sys4AI/skills/core_skill_manifest.yaml
  - Sys4AI/registries/**
  - scripts/skills/validate_skill_manifest.py
allowed_writes:
  - .agents/skill_registry/SKILL_REGISTRY.yaml
  - .agents/skills/*/skill.yaml
  - Sys4AI/registries/skill_lifecycle_status_registry.csv
  - Sys4AI/skills/core_skill_manifest.yaml
  - scripts/skills/validate_skill_manifest.py
  - Sys4AI/sys_for_ai/validators.py
forbidden_actions:
  - Make adapter shells runtime-authoritative without approval.
expected_outputs:
  - Lifecycle statuses enforced.
validators:
  - make validate-dev-skills
  - cd Sys4AI && make validate-skill-lifecycle
  - cd Sys4AI && make validate
stop_conditions:
  - Validator change breaks existing skill manifests without migration path.
```

### AJ-07: Core Skill Scaffold Batch 1

```yaml
agentjob_id: AJ-SFADEV-07-CORE-SKILLS-BATCH-1-001
objective: Add high-priority core skills for role governance, system layers, artifacts, traceability, director decisions, source authority, and context handoff.
role: implementation_initialization_agent
subject_system_id: Sys4AI-dev
subject_layer: development_system
allowed_reads:
  - .agents/skills/**
  - Sys4AI/skills/core/**
  - .agents/skill_registry/SKILL_REGISTRY.yaml
allowed_writes:
  - .agents/skills/role-catalog-governance/**
  - .agents/skills/system-layer-classifier/**
  - .agents/skills/artifact-contract-governance/**
  - .agents/skills/traceability-matrix-engine/**
  - .agents/skills/director-decision-governor/**
  - .agents/skills/source-authority-auditor/**
  - .agents/skills/context-window-and-handoff-manager/**
  - .codex/skills/**
  - Sys4AI/skills/core/**
  - .agents/skill_registry/SKILL_REGISTRY.yaml
  - Sys4AI/skills/core_skill_manifest.yaml
  - Sys4AI/registries/skill_registry.csv
  - Sys4AI/registries/core_skill_proposal_registry.csv
forbidden_actions:
  - Add project-specific domain constraints as core.
expected_outputs:
  - Seven new validated core skills.
validators:
  - make validate-dev-skills
  - cd Sys4AI && make validate-skills
  - cd Sys4AI && make validate-core-skill-proposals
stop_conditions:
  - Any new skill lacks required manifest or authority rules.
```

### AJ-08: Core Skill Scaffold Batch 2

```yaml
agentjob_id: AJ-SFADEV-08-CORE-SKILLS-BATCH-2-001
objective: Add verification, assurance, threat, evaluation, baseline, AgentJob authoring, operations, ontology, domain routing, interface discovery, and discovery governance skills.
role: implementation_initialization_agent
subject_system_id: Sys4AI-dev
subject_layer: development_system
allowed_reads:
  - .agents/skills/**
  - Sys4AI/skills/core/**
allowed_writes:
  - .agents/skills/verification-validation-planner/**
  - .agents/skills/assurance-case-builder/**
  - .agents/skills/threat-model-and-permission-scope/**
  - .agents/skills/evaluation-harness-designer/**
  - .agents/skills/baseline-change-manager/**
  - .agents/skills/agentjob-task-packet-author/**
  - .agents/skills/operations-and-maintenance-planner/**
  - .agents/skills/project-ontology-and-glossary/**
  - .agents/skills/domain-pack-router/**
  - .agents/skills/interface-and-integration-discovery/**
  - .agents/skills/requirements-discovery-governor/**
  - .codex/skills/**
  - Sys4AI/skills/core/**
  - .agents/skill_registry/SKILL_REGISTRY.yaml
  - Sys4AI/skills/core_skill_manifest.yaml
  - Sys4AI/registries/skill_registry.csv
  - Sys4AI/registries/core_skill_proposal_registry.csv
forbidden_actions:
  - Include project-specific domain-pack contents.
expected_outputs:
  - Eleven additional validated core skills.
validators:
  - make validate-dev-skills
  - cd Sys4AI && make validate-skills
  - cd Sys4AI && make validate-core-skill-proposals
stop_conditions:
  - Any new skill lacks required manifest or authority rules.
```

### AJ-09: Generated Docs and Derivative Governance

```yaml
agentjob_id: AJ-SFADEV-09-GENERATED-DOCS-001
objective: Generate or stub generated derivative docs for new registries, roles, artifact contracts, layers, and core skills.
role: documentation_librarian
subject_system_id: Sys4AI
subject_layer: framework_product
allowed_reads:
  - Sys4AI/registries/**
  - Sys4AI/docs/generated/**
  - Sys4AI/sys_for_ai/derivatives.py
allowed_writes:
  - Sys4AI/docs/generated/**
  - Sys4AI/registries/derivative_registry.csv
  - Sys4AI/sys_for_ai/derivatives.py
  - Sys4AI/sys_for_ai/derivative_generation.py
forbidden_actions:
  - Mark generated docs canonical.
expected_outputs:
  - Generated or stub-generated docs.
  - Derivative registry rows.
validators:
  - cd Sys4AI && make validate-generated-derivatives
  - cd Sys4AI && make validate
stop_conditions:
  - Generated page lacks source trace.
```

### AJ-10: End-to-End Acceptance

```yaml
agentjob_id: AJ-SFADEV-10-END-TO-END-ACCEPTANCE-001
objective: Run full validation and produce final acceptance packet.
role: requirements_verifier
subject_system_id: Sys4AI-dev
subject_layer: development_system
allowed_reads:
  - "**"
allowed_writes:
  - implementation_plans/completion_receipts/**
  - Sys4AI/control_records/completions/**
  - Sys4AI/control_records/handoffs/**
forbidden_actions:
  - Change source files to force validation pass without recording changes.
expected_outputs:
  - Final acceptance receipt.
  - Open issue list.
  - Deferred item list.
validators:
  - make validate
  - cd Sys4AI && make validate
stop_conditions:
  - Validation fails without documented repair path.
```

---

## 21. Exact File Tree Delta

This section lists the expected new or modified file areas. It is not exhaustive down to every generated page, but it captures the intended shape.

```text
PRDs/
  Sys4AI_phase-0_product_system_design_prd.md        # modify
  Sys4AI_phase-1_implementation_initialization_prd.md # modify

implementation_plans/
  Sys4AI-dev_all_recommendations_implementation_plan.md # this plan
  phase-1_discovery_gate_and_self_hosting_plan.md            # optional split-out
  phase-1_role_governance_plan.md                            # optional split-out
  phase-1_core_skill_expansion_plan.md                       # optional split-out
  completion_receipts/
    CR-WS00-BASELINE-001.md
    CR-SFADEV-ALL-RECS-IMPLEMENTED-001.md

.agents/
  skill_registry/
    SKILL_REGISTRY.yaml                                  # modify
  skills/
    continue/                                           # add or promote
    source-first-memory/                                # add or promote
    role-catalog-governance/                            # add
    system-layer-classifier/                            # add
    artifact-contract-governance/                       # add
    traceability-matrix-engine/                         # add
    director-decision-governor/                         # add
    verification-validation-planner/                    # add
    source-authority-auditor/                           # add
    context-window-and-handoff-manager/                 # add
    threat-model-and-permission-scope/                  # add
    evaluation-harness-designer/                        # add
    baseline-change-manager/                            # add
    agentjob-task-packet-author/                        # add
    operations-and-maintenance-planner/                 # add
    project-ontology-and-glossary/                      # add
    domain-pack-router/                                 # add
    interface-and-integration-discovery/                # add
    assurance-case-builder/                             # add
    requirements-discovery-governor/                    # add

.codex/
  skills/
    <new-skill-id>/SKILL.md                             # add shims

scripts/
  skills/
    validate_skill_manifest.py                          # modify

Sys4AI/
  Makefile                                              # modify
  configs/
    self_hosting_mode.toml                              # add
  control_records/
    agentjobs/
      AJ-P1-DISCOVERY-GATE-SMOKE-001.yaml               # add
      AJ-SFADEV-*.yaml                                  # optional add from backlog
    completions/
      completion_receipt.discovery_gate.example.yaml     # add
    handoffs/
      handoff.discovery_gate.example.yaml                # add
  docs/
    self_hosting_mode_policy.md                         # add
    generated/
      roles/                                            # add
      artifact_contracts/                               # add
      system_layers/                                    # add
      core_skills/                                      # add
  registries/
    system_layer_registry.csv                           # add
    discovery_record_registry.csv                       # add
    role_registry.csv                                   # add
    role_skill_crosswalk.csv                            # add
    role_execution_binding_registry.csv                 # add
    artifact_contract_registry.csv                      # add
    core_skill_proposal_registry.csv                    # add
    skill_lifecycle_status_registry.csv                 # add
    traceability_edge_registry.csv                      # optional/add recommended
    requirement_trace_registry.csv                      # modify
    skill_registry.csv                                  # modify
    derivative_registry.csv                             # modify
    config_source_registry.csv                          # modify
    source_registry.csv                                 # modify
  schemas/
    contracts/
      system_layer_registry_row.schema.json             # add
      discovery_record_registry_row.schema.json         # add
      role_registry_row.schema.json                     # add
      role_skill_crosswalk_row.schema.json              # add
      role_execution_binding_registry_row.schema.json   # add
      artifact_contract_registry_row.schema.json        # add
      core_skill_proposal_registry_row.schema.json      # add
      skill_lifecycle_status_registry_row.schema.json   # add
      self_hosting_mode.schema.json                     # add if TOML normalized validation uses JSON Schema
      traceability_edge_registry_row.schema.json        # add if traceability edge registry added
  skills/
    core/
      <new-skill-id>/                                  # add product scaffold adapters
    core_skill_manifest.yaml                            # modify
  sys_for_ai/
    artifact_contracts.py                               # add
    discovery.py                                        # modify
    role_validators.py                                  # add
    roles.py                                            # add
    system_layers.py                                    # add
    traceability.py                                     # add
    validators.py                                       # modify
    cli.py                                             # modify
    derivatives.py                                      # modify
    derivative_generation.py                            # modify
  templates/
    system_definition/
      requirements-discovery-record-template.md         # modify
    control_records/
      director_decision_template.yaml                   # add
    artifacts/                                          # add
    traceability/                                       # add
```

---

## 22. Risk Register

| Risk ID | Risk | Impact | Likelihood | Mitigation | Owner |
|---|---|---:|---:|---|---|
| RISK-001 | PRD requirement IDs collide or trace rows become incomplete. | High | Medium | Run `validate-requirement-trace` after every PRD edit. | System Engineer |
| RISK-002 | Role validator breaks current skill manifests because role aliases differ. | High | Medium | Seed compatibility roles `system_analyst`, `system_engineer`, `software_engineer`; map to PRD roles. | Role Governance Agent |
| RISK-003 | New skill lifecycle fields break root validator. | Medium | Medium | Implement transitional validator support before adding fields everywhere. | Software Engineer |
| RISK-004 | Too many new skills are added as hollow shells. | Medium | High | Each skill must include purpose, triggers, inputs, outputs, procedure, authority, validation, failure modes, and example. | Documentation Librarian |
| RISK-005 | Product scaffold and active runtime registries drift. | High | Medium | Add cross-registry validation between `.agents` and `Sys4AI/skills/core_skill_manifest.yaml`. | Skill Governance Agent |
| RISK-006 | Generated role or skill docs become treated as canonical. | High | Medium | Authority banners and derivative validation. | Documentation Librarian |
| RISK-007 | Discovery gate slows simple changes. | Medium | Medium | Allow Director Decision waiver for trivial changes with recorded rationale. | System Director |
| RISK-008 | Self-hosting policy over-constrains development. | Medium | Medium | Allow controlled authority expansion through Director Decision. | System Director |
| RISK-009 | Traceability graph becomes too heavy for Phase 1. | Medium | Medium | Start with registry rows and basic validator; deeper graph analysis can be incremental. | Requirements Verifier |
| RISK-010 | Core/domain boundary blurs in new skills. | High | Medium | Domain-pack-router must route domain-specific logic; core skills stay domain-neutral. | Domain Specialist |
| RISK-011 | Validator success is misread as product correctness. | High | Medium | Skill docs and PRDs must repeat scoped validation rule. | Verification Engineer |
| RISK-012 | New registries create maintenance burden. | Medium | High | Generate derivative docs and validation receipts; keep schemas simple. | Documentation Librarian |
| RISK-013 | AgentJob boundary validators block legitimate multi-file changes. | Medium | Medium | Use Director Decision for authorized boundary expansion. | Control Loop Planner |
| RISK-014 | RDR is accidentally treated as approved requirements. | High | Medium | Discovery validator forbids unguarded baseline language and requires candidate IDs. | User Wants Elicitor |
| RISK-015 | New Makefile targets rely on missing dependencies. | Medium | Low | Keep validators stdlib where possible; use existing JSON Schema dependency already in Phase 1. | Software Engineer |

---

## 23. Open Issues and Maintainer Decisions

| Issue ID | Question | Why It Matters | Recommended Decision |
|---|---|---|---|
| OPEN-001 | Should all 18 new core skills become active runtime skills immediately, or should some remain approved scaffold? | Active runtime expansion increases validation load. | Activate all with minimal governed package because user requested implementing all recommendations; add deeper scripts later. |
| OPEN-002 | Should `requirements-discovery-governor` be a separate skill or a policy wrapper around `system-definition-interview-context-45`? | Avoid redundant skill surface. | Add as a lightweight governance skill that wraps discovery gate compliance. |
| OPEN-003 | Should `traceability_edge_registry.csv` be added now or should object relationships be reused? | New registry adds overhead, but trace graph becomes clearer. | Add it now because traceability is central and deserves a dedicated contract. |
| OPEN-004 | Should lifecycle status live in skill manifests or only registries? | Avoid duplicative data. | Store authoritative lifecycle in registries; allow skill manifests to include matching lifecycle for readability. Validator checks consistency where present. |
| OPEN-005 | Should generated role docs be implemented as full generator or stubs first? | Full generator takes more code. | Stub-generated pages with source trace and derivative banner now; full generator later. |
| OPEN-006 | Should RDR registry be a source registry extension or its own registry? | Avoid registry proliferation. | Create dedicated registry because discovery gate is central and has unique fields. |
| OPEN-007 | Should self-hosting TOML use JSON Schema validation via normalized dict? | Keeps config validation consistent. | Yes. Use existing TOML parser and JSON Schema validation approach. |
| OPEN-008 | Should root `.agents` validation understand product scaffold skills? | Cross-layer validation reduces drift. | Add a dedicated crosswalk check later; for now validate both layers separately plus reconciled registry rows. |

---

## 24. Validation Strategy

### 24.1 Validation Layers

| Layer | Validator | Purpose |
|---|---|---|
| Root runtime skill layer | `make validate-dev-skills` | Validates `.agents` skill manifests, registry, bundles, domain packs. |
| Product scaffold | `cd Sys4AI && make validate` | Validates product scaffold registries, contracts, control records, generated docs. |
| PRD trace | `make validate-requirement-trace` | Validates requirement ID uniqueness and Phase 0 to Phase 1 coverage. |
| Discovery | `validate-discovery-record`, `validate-discovery-records` | Validates RDR template and registered RDRs. |
| Roles | `validate-roles` | Validates role registry, crosswalk, execution bindings, generated role docs. |
| System layers | `validate-system-layers` | Validates layer registry and self-hosting config. |
| Skill lifecycle | `validate-skill-lifecycle` | Validates lifecycle vocabulary and skill status consistency. |
| Artifact contracts | `validate-artifact-contracts` | Validates artifact contract registry. |
| Traceability graph | `validate-traceability-graph` | Validates trace edge registry and evidence paths. |
| Generated derivatives | `validate-generated-derivatives` | Ensures derivatives remain non-canonical and sourced. |

### 24.2 Failure Policy

Validation failures must be categorized:

```text
blocker: cannot proceed until fixed
repair: can proceed only inside current AgentJob if allowed writes include fix paths
warning: may proceed with recorded issue
informational: no action needed
```

### 24.3 Completion Receipts

Every AgentJob should produce a completion receipt with:

- AgentJob ID.
- Role ID.
- Subject system layer.
- Changed artifacts.
- Validators run.
- Validation status.
- Open issues.
- Next recommended AgentJob.
- Handoff ID.

---

## 25. Rollout Strategy

### 25.1 Recommended Branching

Use one branch for the full integration or split by workstream:

```text
feature/discovery-selfhost-role-governance
feature/core-skill-expansion
feature/artifact-trace-governance
```

If using one branch, commit by workstream.

Continuation rule: every commit in the sequence must come from one selected `/continue` AgentJob. After each commit, push to the configured upstream and stop. The next workstream may begin only after the pushed commit is visible from repository evidence and the next `/continue` invocation selects a new authorized task.

### 25.2 Commit Sequence

Recommended commits:

1. `docs(prd): add discovery gate, RDR, system layers, self-hosting requirements`
2. `feat(registry): add system layer, discovery, role, artifact, lifecycle registries`
3. `feat(discovery): enforce RDR gate and registered discovery records`
4. `feat(roles): add role governance and validate-roles`
5. `feat(skills): activate continue and source-first-memory runtime skills`
6. `feat(skills): add skill lifecycle governance`
7. `feat(skills): add core governance skill batch one`
8. `feat(skills): add core governance skill batch two`
9. `feat(system): add self-hosting policy and layer classifier`
10. `feat(artifacts): add artifact contracts and traceability edge validation`
11. `docs(generated): add derivative pages for new registries and skills`
12. `test(validate): pass full root and product scaffold validation`

### 25.3 Migration Rules

- Do not remove current registry rows unless superseded.
- Add new fields in backward-compatible ways where possible.
- Keep transitional validator support for old skill metadata until all manifests are migrated.
- Any change to activated control records should use supersession.
- Generated derivatives should be regenerated or marked stale, never silently trusted.

---

## 26. Implementation Details for New Core Skills

This section gives each new skill a minimum viable content contract.

### 26.1 `role-catalog-governance`

**Activation triggers:**

- User asks to add, modify, validate, or explain system roles.
- PRD role model changes.
- AgentJob references unknown role.
- Skill registry references unknown role.

**Required inputs:**

- Role registry.
- Role-skill crosswalk.
- Role execution binding registry.
- Active runtime skill registry.
- Product scaffold skill manifest.

**Outputs:**

- Role registry repair recommendations.
- Role-to-skill crosswalk updates.
- Validation receipt.

**Failure modes:**

- Treating prose role catalog as authority over controlled registry.
- Allowing unknown roles in AgentJobs.
- Binding required skill that does not exist.

### 26.2 `system-layer-classifier`

**Activation triggers:**

- Work begins on a new artifact or AgentJob.
- User request refers to “the system” ambiguously.
- Work could affect `Sys4AI-dev`, `Sys4AI`, or target-system templates.

**Required inputs:**

- User request.
- Current repo context.
- System layer registry.
- Self-hosting policy.

**Outputs:**

- System layer classification YAML.
- Required next gate.

**Failure modes:**

- Treating product scaffold as runtime authority.
- Applying target-system changes to framework PRDs.
- Treating generated docs as canonical.

### 26.3 `artifact-contract-governance`

**Activation triggers:**

- New artifact type is introduced.
- Artifact fails validation.
- Agent needs to create USRD/SRD/ARD/TRP/SRP or annex.

**Outputs:**

- Artifact contract row.
- Artifact template update.
- Contract validation receipt.

**Failure modes:**

- Creating artifacts with no producer/consumer role.
- Missing required sections.
- Incorrect authority class.

### 26.4 `traceability-matrix-engine`

**Activation triggers:**

- Requirements, architecture, implementation, or validation artifacts change.
- Trace gaps detected.
- PRD requirement trace changes.

**Outputs:**

- Trace edge rows.
- Trace gap report.
- Orphan requirement report.

**Failure modes:**

- Creating implementation tasks without source requirement.
- Treating inferred trace as confirmed.
- Losing trace during reconciliation.

### 26.5 `director-decision-governor`

**Activation triggers:**

- Routing is ambiguous.
- Authority expansion is requested.
- Discovery gate waiver is requested.
- Role selection is not determined.
- AgentJob creation is not already authorized.

**Outputs:**

- Director Decision Record.
- Decision registry row.
- Supersession map if applicable.

**Failure modes:**

- Authority expansion without explicit record.
- Alternatives omitted.
- Decision not tied to source evidence.

### 26.6 `verification-validation-planner`

**Activation triggers:**

- Requirements baseline changes.
- TRP or SRP is being prepared.
- Acceptance criteria missing.

**Outputs:**

- Verification matrix.
- Validation plan.
- Evidence map.

**Failure modes:**

- Verification method too vague.
- Validator success treated as acceptance.
- Requirement lacks acceptance criterion.

### 26.7 `source-authority-auditor`

**Activation triggers:**

- Memory hit affects requirements/routing/claims.
- Generated docs are used.
- Registry graph validation fails.

**Outputs:**

- Authority audit report.
- Stale derivative report.
- Orphan derivative report.

**Failure modes:**

- Citing generated derivative as source.
- Ignoring stale hash.
- Unregistered source used as canonical.

### 26.8 `context-window-and-handoff-manager`

**Activation triggers:**

- Context threshold reached.
- User asks for handoff.
- Long-running interview or implementation session.

**Outputs:**

- Context checkpoint.
- Handoff.
- Resume instruction.

**Failure modes:**

- Overwriting checkpoint without confirmation.
- Omitting last action or last answer.
- Continuing when context metrics unavailable.

### 26.9 `threat-model-and-permission-scope`

**Activation triggers:**

- Target system uses tools, external actions, private data, autonomous loops, model outputs, or users.

**Outputs:**

- Threat model.
- Permission matrix.
- Data handling register.
- Unsafe action register.

**Failure modes:**

- Treating low-risk defaults as universal.
- Omitting external action risks.
- Missing data classification.

### 26.10 `evaluation-harness-designer`

**Activation triggers:**

- Need to evaluate agent behavior.
- Requirements need measurable acceptance.
- Regression risk exists.

**Outputs:**

- Evaluation plan.
- Scenario eval registry.
- Rubric.
- Regression suite plan.

**Failure modes:**

- Eval cases not traced to requirements.
- Rubric too subjective.
- No failure thresholds.

### 26.11 `baseline-change-manager`

**Activation triggers:**

- PRD, registry, schema, role, skill, or control artifact baseline changes.
- Supersession needed.
- Rollback/migration required.

**Outputs:**

- Baseline change record.
- Supersession map.
- Migration evidence.
- Rollback plan.

**Failure modes:**

- Silent mutation.
- Missing migration evidence.
- Rollback impossible.

### 26.12 `agentjob-task-packet-author`

**Activation triggers:**

- Implementation plan must become bounded AgentJobs.
- `/continue` needs next job.

**Outputs:**

- AgentJob YAML.
- Task packet.
- Expected completion receipt.
- Handoff template.

**Failure modes:**

- AgentJob too broad.
- Allowed writes too wide.
- Validators missing.

### 26.13 `operations-and-maintenance-planner`

**Activation triggers:**

- Target system must run over time.
- Maintenance, monitoring, update, or incident requirements are needed.

**Outputs:**

- Operations requirements.
- Maintenance plan.
- Monitoring plan.
- Incident response requirements.

**Failure modes:**

- No owner or cadence.
- No incident response.
- No regression/eval schedule.

### 26.14 `project-ontology-and-glossary`

**Activation triggers:**

- Terms are ambiguous.
- Domain language appears.
- Role/artifact names conflict.

**Outputs:**

- Glossary.
- Ontology registry.
- Term decision records.
- Synonym map.

**Failure modes:**

- Ambiguous terms become requirements.
- Synonyms split traceability.
- Project-specific terms pollute core vocabulary.

### 26.15 `domain-pack-router`

**Activation triggers:**

- Specialized domain appears.
- Domain Specialist needed.
- Domain-specific skill pack may be required.

**Outputs:**

- Domain trigger report.
- Recommended domain packs.
- Domain specialist routing decision.

**Failure modes:**

- Router invents domain rules.
- Domain-specific content enters core.
- Domain risk ignored.

### 26.16 `interface-and-integration-discovery`

**Activation triggers:**

- System interacts with tools, APIs, users, files, external services, models, state stores, or repositories.

**Outputs:**

- Interface candidate register.
- External systems register.
- Data flow context.
- Integration risk register.

**Failure modes:**

- Tool boundary omitted.
- Owner unknown but not flagged.
- Interface not traced to scenario.

### 26.17 `assurance-case-builder`

**Activation triggers:**

- High-impact system.
- Safety/security/privacy claims.
- Need to justify readiness.

**Outputs:**

- Assurance case.
- Claim evidence registry.
- Risk control matrix.
- Residual risk register.

**Failure modes:**

- Unsupported claim.
- Evidence mismatch.
- Residual risk hidden.

### 26.18 `requirements-discovery-governor`

**Activation triggers:**

- Discovery gate starts or completes.
- User asks to skip discovery.
- RDR transitions to USRD.

**Outputs:**

- Discovery gate decision.
- Discovery completion receipt.
- Discovery-to-USRD handoff.

**Failure modes:**

- PRD created without discovery or waiver.
- Candidate requirements promoted too early.
- Open questions lost.

---

## 27. Maintainer Review Checklist

Before implementation starts:

- [ ] Approve system-layer IDs.
- [ ] Approve RDR as first artifact before USRD.
- [ ] Approve `system-definition-interview-context-45` as default discovery gate.
- [ ] Approve self-hosting mode requirements.
- [ ] Approve role registry headers.
- [ ] Approve role-to-skill crosswalk strategy.
- [ ] Approve skill lifecycle vocabulary.
- [ ] Approve activation of `continue` and `source-first-memory` in `.agents` runtime.
- [ ] Approve adding all recommended new core skills as runtime-active minimal governed skills.
- [ ] Approve traceability edge registry.
- [ ] Approve generated derivative doc expansion.

Before final acceptance:

- [ ] Root `make validate-dev-skills` passes.
- [ ] Product scaffold `make validate` passes.
- [ ] `validate-roles` passes.
- [ ] `validate-system-layers` passes.
- [ ] `validate-discovery-records` passes.
- [ ] `validate-artifact-contracts` passes.
- [ ] `validate-skill-lifecycle` passes.
- [ ] All new skill manifests pass.
- [ ] No generated derivative claims canonical authority.
- [ ] Completion receipt records changed files and validators.

---

## 28. Suggested Immediate Next Step

The first implementation AgentJob should be:

```yaml
agentjob_id: AJ-SFADEV-01-PRD-INTEGRATION-001
objective: Add discovery gate, Requirements Discovery Record, system layer, self-hosting, role governance, and skill lifecycle requirements to the Phase 0 and Phase 1 PRDs.
role: system_engineer
subject_system_id: Sys4AI
subject_layer: framework_product
```

This should happen before writing validators or adding new skills, because the PRDs are the authority surface. After that, implement registries and validators, then runtime skills.

---

## 29. Summary

This plan turns the project’s recursive bootstrapping challenge into an explicit self-hosting architecture.

The implementation result should be a development system where:

- The agent always knows which system layer it is working on.
- New systems begin with structured discovery, not premature PRD generation.
- The Requirements Discovery Record becomes the bridge from conversation to formal artifacts.
- Roles are controlled data, not only prose.
- Skills have lifecycle status and authority boundaries.
- `continue` and `source-first-memory` are active runtime capabilities.
- Core organizational skills are available for every future target system.
- Generated documentation remains useful but non-authoritative.
- Traceability, validation, decisions, baselines, and handoffs become inspectable.

In short: `Sys4AI-dev` becomes a governed system for developing `Sys4AI`, and `Sys4AI` becomes a governed system for developing future systems.
