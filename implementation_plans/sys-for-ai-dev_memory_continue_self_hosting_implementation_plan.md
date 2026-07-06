# sys-for-ai-dev Self-Hosting Memory and `/continue` Implementation Plan

**Document status:** Proposed implementation plan  
**Prepared for:** `AngryOwlAI/sys-for-ai-dev`  
**Target implementation area:** `sys-for-ai/` inside `sys-for-ai-dev`  
**Primary scope:** Source-first memory system, self-hosting boundary, and generic `/continue` control-loop kernel  
**Generated:** 2026-07-06  
**Recommended canonical destination if adopted:** `implementation_plans/self_hosting_memory_continue_implementation_plan.md`

---

## 0. Authority notice

This Markdown file is an implementation plan, not a canonical Product Requirements Document unless the project deliberately promotes it through the repository's source-authority workflow.

The plan assumes the current `sys-for-ai-dev` repository state in which:

- `PRDs/sys-for-ai_phase-0_product_system_design_prd.md` is the canonical Phase 0 product and system-design baseline.
- `PRDs/sys-for-ai_phase-1_implementation_initialization_prd.md` is the Phase 1 implementation initialization baseline.
- The product implementation scaffold lives under `sys-for-ai/`.
- Runtime development skills live under `.agents/skills/`.
- `.codex/skills/` remains a compatibility layer rather than the product's canonical skill surface.
- Generated derivative docs, local retrieval surfaces, caches, semantic extracts, wiki notes, Obsidian mirrors, HTML, PDF, and index surfaces remain noncanonical unless promoted through explicit source-authority workflow.

This plan should be treated as a controlled implementation proposal. Once accepted, place it under `implementation_plans/`, add it to the appropriate source registry row, and execute it through bounded AgentJobs.

---

## 1. Executive summary

The project is in a self-referential but manageable state:

```text
sys-for-ai-dev is the development system.
sys-for-ai is the product being developed inside sys-for-ai-dev.
sys-for-ai is itself a framework for developing systems.
sys-for-ai-dev is therefore the first serious dogfood target for sys-for-ai concepts.
```

This is not a defect. It is a self-hosting fixed point. The implementation must make that fixed point typed, explicit, and auditable.

The plan implements two core capabilities inside `sys-for-ai/`:

1. **Source-first memory system**  
   A deterministic file-backed memory layer that indexes registered sources, registries, control records, configuration sources, validation contracts, generated derivatives, and relationship rows. Memory retrieval is navigation, not authority. Any memory hit that influences requirements, routing, AgentJob boundaries, handoffs, permissions, claims, or continuation state must be verified against canonical source files, controlled artifacts, or registry rows.

2. **Generic `/continue` control-loop kernel**  
   A bounded continuation loop that resumes from tracked `program_state.yaml`, inspects the latest handoff, runs memory preflight, selects or reuses at most one authorized AgentJob, emits an execution packet, validates completion evidence, writes receipts and handoffs, updates state, and blocks unauthorized drift.

The implementation deliberately starts with a deterministic Python and file-based kernel. It does not add a vector database, production service, heavy memory runtime, full wiki engine, or Codex-only dependency. Those can be introduced later only through explicit PRD, decision record, registry, validator, and AgentJob authority.

---

## 2. Core implementation thesis

The system should behave according to this rule:

```text
Memory finds.
Sources decide.
Registries locate.
Schemas constrain.
Validators verify process.
AgentJobs bound action.
Receipts preserve evidence.
Handoffs define continuation.
Generated derivatives explain but do not govern.
```

The memory system must be a telescope, not an oracle. The `/continue` loop must be a turnstile, not a conveyor belt. Self-hosting must be a typed fixed point, not a hall of mirrors.

---

## 3. Existing state inventory

### 3.1 Existing repository-level structure

Current expected layout:

```text
sys-for-ai-dev/
  README.md
  PRDs/
    sys-for-ai_phase-0_product_system_design_prd.md
    sys-for-ai_phase-1_implementation_initialization_prd.md
    sys-for-ai_phase-0_prd.md
  implementation_plans/
  .agents/
    skills/
  .codex/
    skills/
  sys-for-ai/
    README.md
    Makefile
    pyproject.toml
    requirements.txt
    configs/
    control_records/
    docs/
    registries/
    schemas/
    skills/
    sys_for_ai/
    templates/
```

### 3.2 Existing product scaffold capabilities

The `sys-for-ai/` scaffold already contains the early implementation spine:

```text
sys-for-ai/README.md
sys-for-ai/Makefile
sys-for-ai/sys_for_ai/cli.py
sys-for-ai/sys_for_ai/validators.py
sys-for-ai/sys_for_ai/memory.py
sys-for-ai/sys_for_ai/registry_io.py
sys-for-ai/sys_for_ai/yaml_io.py
sys-for-ai/sys_for_ai/toml_io.py
sys-for-ai/sys_for_ai/jsonschema_io.py
sys-for-ai/sys_for_ai/security_checks.py
sys-for-ai/sys_for_ai/derivative_generation.py
```

The Makefile already exposes useful validation targets:

```text
make doctor
make validate-agentjob
make validate-agentjobs
make validate-skills
make validate-metrics
make validate-discovery-template
make bootstrap-memory
make validate-format-profiles
make validate-config-sources
make validate-control-records
make validate-validation-contract-registry
make validate-toml-config
make validate-jsonschema-contracts
make validate-registry-graph
make validate-requirement-trace
make generate-config-control-wiki
make generate-validation-contracts-catalog
make validate-generated-derivatives
make validate
```

This plan preserves that spine and extends it rather than replacing it.

### 3.3 Existing registries

Existing registry files include:

```text
sys-for-ai/registries/source_registry.csv
sys-for-ai/registries/derivative_registry.csv
sys-for-ai/registries/object_relationship_registry.csv
sys-for-ai/registries/skill_registry.csv
sys-for-ai/registries/format_profile_registry.csv
sys-for-ai/registries/config_source_registry.csv
sys-for-ai/registries/control_record_registry.csv
sys-for-ai/registries/validation_contract_registry.csv
sys-for-ai/registries/requirement_trace_registry.csv
```

The plan adds a small operational registry layer for continuation records. It does not replace existing registries.

### 3.4 Existing examples and contracts

Existing control examples include:

```text
sys-for-ai/control_records/examples/phase1_smoke_agentjob.yaml
sys-for-ai/control_records/examples/handoff.example.yaml
sys-for-ai/control_records/examples/completion_receipt.example.yaml
sys-for-ai/control_records/examples/state_snapshot.example.yaml
```

Existing JSON Schema contracts include:

```text
sys-for-ai/schemas/contracts/agentjob.schema.json
sys-for-ai/schemas/contracts/handoff.schema.json
sys-for-ai/schemas/contracts/completion_receipt.schema.json
sys-for-ai/schemas/contracts/state_snapshot.schema.json
sys-for-ai/schemas/contracts/sys_for_ai_config.schema.json
sys-for-ai/schemas/contracts/target_project_config.schema.json
sys-for-ai/schemas/contracts/format_profile_registry_row.schema.json
sys-for-ai/schemas/contracts/config_source_registry_row.schema.json
sys-for-ai/schemas/contracts/control_record_registry_row.schema.json
sys-for-ai/schemas/contracts/validation_contract_registry_row.schema.json
sys-for-ai/schemas/contracts/registry_header.schema.json
sys-for-ai/schemas/contracts/requirement_trace_registry_row.schema.json
```

These are sufficient for Phase 1 seed validation. This plan extends them with operational control-loop contracts.

---

## 4. Goals

### 4.1 Functional goals

1. Add an explicit self-hosting boundary decision record.
2. Add a typed `program_state.yaml` control record.
3. Add Director Decision Record support.
4. Add operational AgentJob v0.2 support while preserving compatibility with current AgentJob examples.
5. Add richer operational handoff and completion receipt structures.
6. Add memory preflight receipts.
7. Add deterministic memory status, lookup, search, and preflight commands.
8. Add `/continue` status, preflight, select, packet, and finalize commands.
9. Add validators for program state, Director decisions, handoff chains, completion chains, memory preflight receipts, one-active-AgentJob invariant, and AgentJob write-boundary enforcement.
10. Add generated derivative generation or check-mode support for Configuration and Control Wiki pages and Validation Contracts Catalog pages.
11. Add active development skill surfaces for `/continue` and source-first memory.
12. Keep the implementation file-backed, deterministic, offline-runnable, and compatible with the existing Phase 1 environment.

### 4.2 Governance goals

1. Preserve the framework-system versus target-system boundary.
2. Preserve the development-system versus product-scaffold boundary.
3. Preserve source-first authority.
4. Preserve one bounded AgentJob per `/continue` invocation.
5. Preserve validator scope: validator success proves process or structural conformance, not semantic truth.
6. Preserve derivative boundaries: generated docs, generated wiki notes, HTML, PDF, Obsidian mirrors, indexes, semantic extracts, and local caches are reader or retrieval surfaces unless promoted.
7. Preserve supersession: activated decisions, AgentJobs, completions, and handoffs are superseded rather than silently rewritten.
8. Preserve Phase 1 non-goals: no production service, no vector database, no heavy runtime memory system, no full interactive wiki engine, no Codex-only product dependency.

---

## 5. Non-goals

This implementation plan intentionally does not:

1. Build a production memory database.
2. Add vector embeddings or semantic search as a required dependency.
3. Add a production web service, API server, worker, or database.
4. Add a full interactive wiki engine.
5. Make Obsidian canonical.
6. Make `.codex/skills/` the canonical product skill surface.
7. Hardcode Codex as the only possible execution harness for `sys-for-ai`.
8. Import AEther-Flow physics-specific roles, Gate Chair semantics, ontology gates, GR derivation milestones, or parent-child physics synthesis as universal rules.
9. Promote generated derivatives to canonical authority.
10. Add secret-bearing YAML or TOML examples.
11. Use unsafe YAML loaders.
12. Modify repository `LICENSE` or `NOTICE` files.
13. Rewrite activated control records instead of superseding them.

---

## 6. Design invariants

### 6.1 Self-hosting invariant

Every operational control record created for this work must identify the system context:

```yaml
system_context:
  framework_system: sys-for-ai
  development_system: sys-for-ai-dev
  target_system: sys-for-ai
  self_hosting_mode: true
  reflection_depth: 1
```

Meaning:

- `framework_system` is the product framework being built.
- `development_system` is the repository and skill/runtime environment doing the building.
- `target_system` is the system currently being developed or modified.
- `self_hosting_mode` is true because the target system is the product itself.
- `reflection_depth` is 1 because this plan dogfoods system concepts inside the development system without recursively treating every generated derivative as another governing system.

### 6.2 Source-first memory invariant

Memory retrieval may not independently authorize action. It may only navigate to authority.

A memory hit is actionable only after it is paired with source or registry inspection evidence:

```yaml
memory_hit:
  returned_object_id: SRC-PRD-P0
  path: PRDs/sys-for-ai_phase-0_product_system_design_prd.md
  authority_status: canonical
  required_next_action: inspect_canonical_source
  source_inspection_evidence:
    inspected: true
    registry: source_registry.csv
    row_id: SRC-PRD-P0
```

### 6.3 One-AgentJob invariant

A `/continue` invocation may advance at most one authorized AgentJob.

Allowed:

```text
/continue resolves tracked state -> selects AJ-001 -> emits execution packet -> completes AJ-001 -> creates receipt and handoff
```

Not allowed:

```text
/continue resolves tracked state -> fixes memory -> updates docs -> modifies schema -> creates unrelated skill -> completes multiple tasks
```

### 6.4 Derivative nonauthority invariant

Generated docs, generated wiki pages, generated catalog pages, local caches, search indexes, Obsidian mirrors, semantic extracts, and summaries must never become authority by convenience.

Generated pages must include a visible noncanonical banner and metadata block. Validators should fail if generated derivatives claim canonical authority.

### 6.5 Supersession invariant

Activated or completed control records are historical evidence. If wrong or obsolete, they are superseded.

Do not mutate:

```text
active Director decisions
activated AgentJobs
completion receipts
handoffs already referenced by program state or registries
state snapshots used as evidence
```

Instead, create:

```text
new Director decision
new AgentJob with supersedes field
new completion receipt
new handoff
updated registry rows with supersession links
```

### 6.6 Validator scope invariant

Validators prove only their defined check.

Examples:

```text
JSON Schema pass means structurally admissible, not semantically correct.
Registry graph pass means references resolve, not product readiness.
Memory preflight pass means sources were inspected, not claims are true.
Completion pass means the bounded transaction satisfied declared process checks, not the system is finished.
```

---

## 7. Target architecture

### 7.1 Three-plane model

Implement the system as three planes.

#### 7.1.1 Authority plane

The authority plane contains source files, registries, control records, configuration sources, and validation contracts.

```text
PRDs/
implementation_plans/
sys-for-ai/docs/
sys-for-ai/templates/
sys-for-ai/schemas/contracts/
sys-for-ai/control_records/
sys-for-ai/registries/
sys-for-ai/configs/
```

#### 7.1.2 Retrieval plane

The retrieval plane helps agents and maintainers find authority but does not replace it.

```text
sys-for-ai/docs/generated/
sys-for-ai/wiki/                       # optional later
sys-for-ai/.local/memory/              # ignored
sys-for-ai/.local/obsidian/            # ignored, optional
sys-for-ai/.local/search_index/        # ignored
sys-for-ai/.local/receipts/            # ignored unless promoted
```

#### 7.1.3 Control-loop plane

The control-loop plane records bounded work and continuation state.

```text
sys-for-ai/control_records/program_state.yaml
sys-for-ai/control_records/tasks/
sys-for-ai/control_records/director_decisions/
sys-for-ai/control_records/agentjobs/
sys-for-ai/control_records/role_executions/
sys-for-ai/control_records/completions/
sys-for-ai/control_records/handoffs/
sys-for-ai/control_records/memory_preflights/
sys-for-ai/control_records/state_snapshots/
```

### 7.2 Python package architecture

Add these packages:

```text
sys-for-ai/sys_for_ai/memory/
  __init__.py
  model.py
  registry_catalog.py
  authority.py
  hashing.py
  lookup.py
  search.py
  preflight.py
  receipts.py
  graph.py
  bootstrap.py

sys-for-ai/sys_for_ai/control_loop/
  __init__.py
  model.py
  state.py
  director.py
  job_selection.py
  execution_packet.py
  finalization.py
  handoff.py
  receipts.py
  validators.py

sys-for-ai/sys_for_ai/derivatives/
  __init__.py
  config_control_wiki.py
  validation_contracts_catalog.py
  templates.py
```

Keep existing modules as compatibility facades where practical:

```text
sys_for_ai/memory.py -> wraps sys_for_ai.memory.bootstrap.bootstrap_registries
sys_for_ai/derivative_generation.py -> wraps sys_for_ai.derivatives validators/checkers where practical
```

---

## 8. File tree after implementation

Target tree additions:

```text
sys-for-ai-dev/
  implementation_plans/
    self_hosting_boundary_decision_record.md
    self_hosting_memory_continue_implementation_plan.md

  .agents/
    skills/
      continue/
        SKILL.md
        README.md
        examples/
          self-hosting-continue-example.md
      source-first-memory/
        SKILL.md
        README.md
        examples/
          memory-preflight-example.md

  .codex/
    skills/
      continue/
        SKILL.md                         # thin shim
      source-first-memory/
        SKILL.md                         # thin shim

  sys-for-ai/
    docs/
      memory_retrieval_policy.md
      continue_loop_policy.md
      self_hosting_boundary_policy.md
      generated_derivative_policy.md     # optional consolidation
      generated/
        configuration_control/
          index.md
          yaml-control-records.md
          toml-configuration-sources.md
        validation_contracts/
          index.md
          contracts-by-target.md

    registries/
      agentjob_registry.csv
      director_decision_registry.csv
      handoff_registry.csv
      completion_receipt_registry.csv
      memory_preflight_receipt_registry.csv
      checkpoint_registry.csv             # optional Phase 2 or later

    control_records/
      program_state.yaml
      director_decisions/
        DDR-P1-SELFHOST-001.yaml
      agentjobs/
        AJ-P1-SELFHOST-CONTINUE-KERNEL-001.yaml
      completions/
        completion_receipt.example.v0_2.yaml
      handoffs/
        handoff.example.v0_2.yaml
      memory_preflights/
        memory_preflight_receipt.example.yaml
      state_snapshots/
        state_snapshot.example.v0_2.yaml

    schemas/
      contracts/
        program_state.schema.json
        director_decision.schema.json
        agentjob_v0_2.schema.json
        handoff_v0_2.schema.json
        completion_receipt_v0_2.schema.json
        memory_preflight_receipt.schema.json
        agentjob_registry_row.schema.json
        director_decision_registry_row.schema.json
        handoff_registry_row.schema.json
        completion_receipt_registry_row.schema.json
        memory_preflight_receipt_registry_row.schema.json

    sys_for_ai/
      memory/
        __init__.py
        model.py
        registry_catalog.py
        authority.py
        hashing.py
        lookup.py
        search.py
        preflight.py
        receipts.py
        graph.py
        bootstrap.py
      control_loop/
        __init__.py
        model.py
        state.py
        director.py
        job_selection.py
        execution_packet.py
        finalization.py
        handoff.py
        receipts.py
        validators.py
      derivatives/
        __init__.py
        config_control_wiki.py
        validation_contracts_catalog.py
        templates.py

    tests/
      test_memory_lookup.py
      test_memory_preflight.py
      test_program_state.py
      test_continue_packet.py
      test_agentjob_boundaries.py
      test_handoff_chain.py
      test_completion_chain.py
      fixtures/
        memory/
        control_loop/
```

---

## 9. Implementation phases overview

Execute this plan as bounded AgentJobs. Do not implement all phases in one uncontrolled transaction.

| Phase | Name | Primary outcome | Recommended AgentJob |
|---:|---|---|---|
| 0 | Baseline freeze and source inspection | Current state recorded, no code changes yet | `AJ-P1-BASELINE-INSPECT-001` |
| 1 | Self-hosting boundary | Decision record, policies, program state seed | `AJ-P1-SELFHOST-BOUNDARY-001` |
| 2 | Operational schemas and registries | Program state, DDR, AgentJob v0.2, handoff v0.2, receipt v0.2 contracts | `AJ-P1-CONTROL-CONTRACTS-001` |
| 3 | Memory catalog and lookup | Deterministic registry-backed lookup/search | `AJ-P1-MEMORY-CATALOG-001` |
| 4 | Memory preflight receipts | Preflight command and receipt validation | `AJ-P1-MEMORY-PREFLIGHT-001` |
| 5 | `/continue` packet kernel | Status, select, packet commands | `AJ-P1-CONTINUE-PACKET-001` |
| 6 | Completion and handoff finalization | Finalize command, receipt/handoff/state update | `AJ-P1-CONTINUE-FINALIZE-001` |
| 7 | Boundary and diff validators | Git diff to AgentJob allowlist enforcement | `AJ-P1-BOUNDARY-VALIDATORS-001` |
| 8 | Generated derivative generators | Write/check generators for config/control wiki and contract catalog | `AJ-P1-DERIVATIVE-GENERATORS-001` |
| 9 | Skill surfaces and documentation | Active `.agents` skills, `.codex` shims, product scaffold skill | `AJ-P1-CONTINUE-SKILLS-001` |
| 10 | Hardening and acceptance | Full validation, trace updates, migration notes | `AJ-P1-SELFHOST-ACCEPTANCE-001` |

---

## 10. Phase 0: Baseline freeze and source inspection

### 10.1 Objective

Capture the current `sys-for-ai-dev` and `sys-for-ai/` state before introducing the self-hosting memory and `/continue` kernel.

### 10.2 Deliverables

```text
implementation_plans/current_state_baseline_self_hosting_memory_continue.md
sys-for-ai/.local/receipts/baseline-inspection.txt     # local ignored receipt
```

If the receipt must be preserved, promote it later through a controlled source-authority workflow.

### 10.3 Tasks

1. Inspect canonical PRDs.
2. Inspect existing `sys-for-ai/README.md`.
3. Inspect existing Makefile targets.
4. Inspect `sys_for_ai/cli.py`, `validators.py`, `memory.py`, `registry_io.py`, and IO helpers.
5. Inspect existing registries.
6. Inspect existing YAML examples and JSON Schema contracts.
7. Run current validation:

```bash
cd sys-for-ai
make doctor
make validate
```

8. Record current validator status.
9. Record unresolved gaps this plan will address.

### 10.4 Acceptance criteria

- Current scaffold is inspected.
- Existing validation status is known.
- No implementation files are changed except the baseline note if authorized.
- Any current validation failures are recorded as pre-existing baseline issues.

---

## 11. Phase 1: Self-hosting boundary

### 11.1 Objective

Make the self-referential development state explicit so `sys-for-ai-dev` can dogfood `sys-for-ai` concepts without confusing product requirements, product implementation, development runtime skills, generated derivatives, and local retrieval surfaces.

### 11.2 Deliverables

```text
implementation_plans/self_hosting_boundary_decision_record.md
sys-for-ai/docs/self_hosting_boundary_policy.md
sys-for-ai/docs/memory_retrieval_policy.md
sys-for-ai/docs/continue_loop_policy.md
sys-for-ai/control_records/program_state.yaml
sys-for-ai/schemas/contracts/program_state.schema.json
```

### 11.3 Self-hosting boundary decision record

Create `implementation_plans/self_hosting_boundary_decision_record.md`:

```markdown
# Self-Hosting Boundary Decision Record

Decision ID: SFA-EDR-SELFHOST-001
Status: Proposed
Date: 2026-07-06
Decision owner: Implementation initialization agent
Scope: sys-for-ai-dev using sys-for-ai concepts while sys-for-ai is under development

## Decision

sys-for-ai-dev may dogfood sys-for-ai memory and control-loop concepts as a self-hosting development system, but self-hosting records must distinguish product requirements, product reference implementation, development runtime skills, generated derivatives, and local retrieval surfaces.

## System context

- Framework system: sys-for-ai
- Development system: sys-for-ai-dev
- Target system for this implementation: sys-for-ai
- Self-hosting mode: true
- Reflection depth: 1

## Rules

1. PRDs remain the authority for product requirements.
2. Active development runtime skills live under .agents/skills/.
3. Product scaffold skills under sys-for-ai/skills/core/ are reference surfaces until promoted.
4. /continue advances at most one registered AgentJob per invocation.
5. Memory hits are navigation until verified against source files or registry rows.
6. Generated derivatives are noncanonical unless explicitly promoted by a source-authority AgentJob.
7. Activated AgentJobs, decisions, completions, and handoffs are superseded, not rewritten.
8. Codex compatibility shims must not become the product's only execution harness requirement.
```

### 11.4 Program state seed

Create `sys-for-ai/control_records/program_state.yaml`:

```yaml
program_state_id: SFA-PROGRAM-STATE-001
schema_version: 0.1.0
system_context:
  framework_system: sys-for-ai
  development_system: sys-for-ai-dev
  target_system: sys-for-ai
  self_hosting_mode: true
  reflection_depth: 1
current_phase: implementation_initialization
lifecycle_stage: develop
active_task_id: TASK-P1-SELFHOST-001
active_director_decision_id: null
active_agentjob_id: null
latest_completion_receipt_id: null
latest_handoff_id: null
latest_memory_preflight_receipt_id: null
state_status: active
blocked_reason: null
human_gate_required: false
allowed_next_actions:
  - run_memory_preflight
  - inspect_latest_handoff
  - select_one_agentjob
  - emit_execution_packet
blocked_actions:
  - execute_multiple_agentjobs
  - use_chat_memory_as_authority
  - treat_generated_derivative_as_canonical
  - mutate_activated_control_record_without_supersession
validation_status:
  last_validated_at: pending
  validators:
    - validate-program-state
    - validate-control-records
    - validate-registry-graph
```

### 11.5 Program state schema requirements

`program_state.schema.json` must require:

```text
program_state_id
schema_version
system_context
current_phase
lifecycle_stage
state_status
allowed_next_actions
blocked_actions
validation_status
```

It must constrain:

```text
system_context.framework_system == sys-for-ai
system_context.development_system == sys-for-ai-dev
system_context.self_hosting_mode is boolean
system_context.reflection_depth is integer >= 0
state_status in active, blocked, complete, human_gated
human_gate_required is boolean
```

### 11.6 Registry updates

Add to `control_record_registry.csv`:

```csv
ctrl_program_state,control_records/program_state.yaml,program_state,controlled,control_loop,contract_program_state,control_loop_engineer;system_director,all_agents,,,pending,pending,Current tracked continuation state for sys-for-ai self-hosting implementation
```

Add to `validation_contract_registry.csv`:

```csv
contract_program_state,schemas/contracts/program_state.schema.json,2020-12,yaml,program_state,control_records/program_state.yaml,controlled,control_loop,sys-for-ai validate-program-state,,pending,pending,Validates tracked /continue program state
```

Add to `source_registry.csv` rows for the new policy docs and decision record after adoption.

### 11.7 CLI and Makefile

Add:

```bash
python -m sys_for_ai.cli validate-program-state control_records/program_state.yaml
```

Makefile target:

```make
validate-program-state:
	$(PYTHON) -m sys_for_ai.cli validate-program-state control_records/program_state.yaml
```

Add to `validate` after `validate-control-records` and before `validate-registry-graph`.

### 11.8 Acceptance criteria

- Self-hosting decision record exists.
- Program state file exists.
- Program state contract validates.
- Program state is registered in `control_record_registry.csv`.
- Program state contract is registered in `validation_contract_registry.csv`.
- `make validate-program-state` passes.
- `make validate` passes or any unrelated pre-existing failures are documented.

---

## 12. Phase 2: Operational schemas and registries

### 12.1 Objective

Introduce operational contracts for Director decisions, AgentJobs, handoffs, completion receipts, and memory preflight receipts.

### 12.2 Deliverables

```text
sys-for-ai/schemas/contracts/director_decision.schema.json
sys-for-ai/schemas/contracts/agentjob_v0_2.schema.json
sys-for-ai/schemas/contracts/handoff_v0_2.schema.json
sys-for-ai/schemas/contracts/completion_receipt_v0_2.schema.json
sys-for-ai/schemas/contracts/memory_preflight_receipt.schema.json
sys-for-ai/schemas/contracts/agentjob_registry_row.schema.json
sys-for-ai/schemas/contracts/director_decision_registry_row.schema.json
sys-for-ai/schemas/contracts/handoff_registry_row.schema.json
sys-for-ai/schemas/contracts/completion_receipt_registry_row.schema.json
sys-for-ai/schemas/contracts/memory_preflight_receipt_registry_row.schema.json
sys-for-ai/registries/agentjob_registry.csv
sys-for-ai/registries/director_decision_registry.csv
sys-for-ai/registries/handoff_registry.csv
sys-for-ai/registries/completion_receipt_registry.csv
sys-for-ai/registries/memory_preflight_receipt_registry.csv
```

### 12.3 Registry headers

#### 12.3.1 `agentjob_registry.csv`

```csv
agentjob_id,path,status,role_id,task_id,created_at,activated_at,completed_at,completion_receipt_id,handoff_id,authority_status,supersedes,source_hash,last_validated_at,notes
```

#### 12.3.2 `director_decision_registry.csv`

```csv
director_decision_id,path,status,task_id,selected_route,selected_agentjob_id,authority_status,supersedes,source_hash,last_validated_at,notes
```

#### 12.3.3 `handoff_registry.csv`

```csv
handoff_id,path,status,producing_agentjob_id,next_recommended_role,next_agentjob_id,source_ids,supersedes,source_hash,last_validated_at,notes
```

#### 12.3.4 `completion_receipt_registry.csv`

```csv
completion_receipt_id,path,agentjob_id,result,validation_status,changed_artifacts_count,next_handoff_id,source_hash,last_validated_at,notes
```

#### 12.3.5 `memory_preflight_receipt_registry.csv`

```csv
memory_preflight_receipt_id,path,agentjob_id,created_at,status,queries_count,hits_count,canonical_inspections_count,stale_risks_count,source_hash,last_validated_at,notes
```

### 12.4 AgentJob v0.2 contract

New operational AgentJobs should use `agentjob_v0_2.schema.json`.

Required fields:

```text
agentjob_id
schema_version
status
objective
lifecycle_stage
role_binding
required_inputs
allowed_reads
allowed_writes
forbidden_actions
expected_outputs
validators
completion_evidence_required
memory_preflight
authority_boundary
handoff_policy
stop_conditions
```

Optional but recommended fields:

```text
generated_paths
forbidden_paths
project_system_boundary
supersedes
created_at
activated_at
```

Status values:

```text
draft
pending
active
completed
blocked
human_gated
superseded
cancelled
```

Role binding shape:

```yaml
role_binding:
  role_id: control_loop_engineer
  binding_type: registered_role | task_overlay | one_job_provisional_role
  authority_scope: implementation_scaffold_only
  expires_with_agentjob: true
```

Memory preflight shape:

```yaml
memory_preflight:
  required: true
  minimum_queries:
    - continue loop handoff AgentJob
  required_evidence:
    - canonical_sources_inspected
    - registry_rows_inspected
```

Authority boundary shape:

```yaml
authority_boundary:
  may_modify_product_scaffold: true
  may_modify_canonical_prds: false
  may_promote_generated_derivatives: false
  may_change_runtime_skill_authority: false
```

### 12.5 Director Decision Record contract

Required fields:

```text
director_decision_id
schema_version
decision_status
created_at
director_role
decision_context
selected_route
rejected_routes
authority_boundary
validators
```

Example:

```yaml
director_decision_id: DDR-P1-SELFHOST-001
schema_version: 0.1.0
decision_status: active
created_at: 2026-07-06T00:00:00Z
director_role: system_director
decision_context:
  trigger: self_hosting_bootstrap
  program_state_id: SFA-PROGRAM-STATE-001
  latest_handoff_id: null
  memory_preflight_receipt_id: null
selected_route:
  route_id: implement_continue_loop_kernel
  rationale: Phase 0 requires /continue semantics and Phase 1 already contains registry and validator scaffolding.
  selected_role: control_loop_engineer
  creates_agentjob_id: AJ-P1-SELFHOST-CONTINUE-KERNEL-001
rejected_routes:
  - route_id: add_vector_memory
    reason: Out of Phase 1 scope.
  - route_id: copy_aether_flow_research_control_wholesale
    reason: Too domain-specific.
authority_boundary:
  may_create_agentjob: true
  may_expand_role_authority: false
  may_promote_derivatives: false
  may_modify_prds: false
validators:
  - cd sys-for-ai && make validate
```

### 12.6 Handoff v0.2 contract

Required fields:

```text
handoff_id
schema_version
framework_name
target_agentic_system
artifact_name
artifact_type
artifact_version
producing_role
artifact_status
summary
source_artifacts
traceability
control_loop_notes
memory_preflight
format_profile_evidence
source_authority_evidence
derivative_surface_evidence
security_evidence
recommended_next_role
phase_boundary_notes
stop_conditions
```

### 12.7 Completion receipt v0.2 contract

Required fields:

```text
completion_receipt_id
schema_version
agentjob_id
role
result
summary
changed_artifacts
validation_evidence
memory_preflight_receipt_id
format_profile_changes
authority_changes
unresolved_issues
next_recommendation
```

Result values:

```text
PASS
PASS_WITH_WARNINGS
FAIL
BLOCKED
HUMAN_GATED
SUPERSEDED
```

### 12.8 Memory preflight receipt contract

Required fields:

```text
memory_preflight_receipt_id
schema_version
agentjob_id
created_at
status
commands_run
queries
canonical_sources_inspected
registry_rows_inspected
stale_context_risks
usable_for_routing
```

Status values:

```text
PASS
PASS_WITH_WARNINGS
FAIL
BLOCKED
```

### 12.9 Validator updates

Extend `REGISTRY_HEADERS` in `validators.py` to include new registry headers.

Add `ROW_CONTRACTS` entries for new registry row schemas.

Add CLI commands:

```text
validate-director-decisions
validate-agentjob-registry
validate-handoff-registry
validate-completion-receipt-registry
validate-memory-preflight-registry
```

### 12.10 Acceptance criteria

- All new schema files load and pass JSON Schema checks.
- All new registries exist with expected headers.
- Registry rows validate against row contracts.
- New registry files are included in `bootstrap-memory` behavior.
- `make validate-jsonschema-contracts` passes.
- `make validate-registry-graph` accounts for new operational registries.
- `make validate` passes.

---

## 13. Phase 3: Memory catalog and lookup

### 13.1 Objective

Implement deterministic source-first memory status, lookup, and search over registered artifacts.

### 13.2 Deliverables

```text
sys-for-ai/sys_for_ai/memory/__init__.py
sys-for-ai/sys_for_ai/memory/model.py
sys-for-ai/sys_for_ai/memory/registry_catalog.py
sys-for-ai/sys_for_ai/memory/authority.py
sys-for-ai/sys_for_ai/memory/hashing.py
sys-for-ai/sys_for_ai/memory/lookup.py
sys-for-ai/sys_for_ai/memory/search.py
sys-for-ai/sys_for_ai/memory/graph.py
sys-for-ai/sys_for_ai/memory/bootstrap.py
sys-for-ai/tests/test_memory_lookup.py
sys-for-ai/tests/test_memory_search.py
```

### 13.3 Internal data model

Implement dataclasses.

```python
@dataclass(frozen=True)
class RegistryEvidence:
    registry_name: str
    row_id: str
    row: dict[str, str]

@dataclass(frozen=True)
class ValidationEvidence:
    validation_status: str
    validation_contract_id: str | None
    validator_command: str | None
    last_validated_at: str | None

@dataclass(frozen=True)
class DerivativeEvidence:
    derivative_id: str | None
    source_ids: list[str]
    stale_or_orphan_status: str | None
    generation_method: str | None

@dataclass(frozen=True)
class MemoryObject:
    object_id: str
    path: str
    artifact_class: str
    format_profile_id: str | None
    authority_status: str
    registry_evidence: RegistryEvidence
    validation_evidence: ValidationEvidence
    derivative_evidence: DerivativeEvidence | None
    owner: str | None
    source_hash: str | None
    secrets_allowed: bool | None

@dataclass(frozen=True)
class MemoryHit:
    query: str
    object_id: str
    path: str
    title: str | None
    snippet: str | None
    score: int
    authority_status: str
    format_profile_id: str | None
    registry_evidence: RegistryEvidence
    validation_evidence: ValidationEvidence
    derivative_evidence: DerivativeEvidence | None
    required_next_action: str
```

### 13.4 Registry catalog behavior

`registry_catalog.py` should:

1. Load all known registries from `registries/`.
2. Build an index by object ID.
3. Build an index by path.
4. Resolve workspace-root and product-root paths.
5. Join source rows to format profile rows where possible.
6. Join control/config rows to validation contract rows.
7. Join derivative rows to source rows.
8. Emit structured warnings for missing paths, missing contracts, duplicate IDs, and authority inversions.

### 13.5 Authority resolver

`authority.py` should classify memory objects:

```text
canonical_source
canonical_draft_source
controlled_source
registry_authority
control_record
configuration_source
validation_contract
generated_derivative
local_cache
unknown_or_unregistered
```

It should return `required_next_action`:

```text
inspect_canonical_source
inspect_registry_row
safe_to_use_as_registered_metadata
reject_or_refresh_derivative
not_actionable_unregistered
```

### 13.6 Lookup command

CLI:

```bash
python -m sys_for_ai.cli memory lookup SRC-PRD-P0 --json
python -m sys_for_ai.cli memory lookup PRDs/sys-for-ai_phase-0_product_system_design_prd.md --json
```

Output shape:

```json
{
  "ok": true,
  "query": "SRC-PRD-P0",
  "result": {
    "object_id": "SRC-PRD-P0",
    "path": "PRDs/sys-for-ai_phase-0_product_system_design_prd.md",
    "authority_status": "canonical",
    "format_profile_id": "fmt_markdown_source",
    "registry": "source_registry.csv",
    "registry_row_id": "SRC-PRD-P0",
    "validation_status": "not_applicable",
    "required_next_action": "inspect_canonical_source"
  }
}
```

### 13.7 Search command

CLI:

```bash
python -m sys_for_ai.cli memory search "source-first memory" --limit 10 --json
```

Search should be deterministic:

- Lowercase token matching.
- Prefer registered canonical and controlled sources over generated derivatives.
- Penalize generated derivatives.
- Penalize unregistered files.
- Return snippets only from text files under allowed formats.
- Do not scan `.venv`, `.git`, `.local`, caches, or ignored generated binary outputs.

### 13.8 Memory status command

CLI:

```bash
python -m sys_for_ai.cli memory status --json
```

Status checks:

```text
registry headers valid
required registries present
registered source paths exist
registered contracts exist
generated derivatives do not claim canonical authority
hashes are present or pending
local retrieval surfaces ignored or absent
```

Output status values:

```text
PASS
PASS_WITH_WARNINGS
FAIL
```

### 13.9 Hashing support

Add:

```bash
python -m sys_for_ai.cli memory hash-path sys-for-ai/README.md --json
python -m sys_for_ai.cli memory validate-hashes --json
python -m sys_for_ai.cli memory update-hashes --check
python -m sys_for_ai.cli memory update-hashes --write
```

Initial behavior:

- Treat `pending` hashes as warnings, not failures.
- Make missing paths failures.
- Make generated derivative source-basis hash mismatches warnings at first.
- Later promote hash mismatch checks to failures through a new AgentJob.

### 13.10 Acceptance criteria

- `memory status` returns JSON and exits nonzero on hard failures.
- `memory lookup SRC-PRD-P0 --json` returns source path, authority status, registry evidence, and required next action.
- `memory search` returns ranked deterministic hits.
- Generated derivative hits are marked derivative and require source inspection.
- No local `.local/` or `.venv/` content is treated as authority.
- Tests pass.
- `make validate` passes.

---

## 14. Phase 4: Memory preflight receipts

### 14.1 Objective

Implement memory preflight as a formal prerequisite for operational `/continue` routing and AgentJob execution.

### 14.2 Deliverables

```text
sys-for-ai/sys_for_ai/memory/preflight.py
sys-for-ai/sys_for_ai/memory/receipts.py
sys-for-ai/control_records/memory_preflights/memory_preflight_receipt.example.yaml
sys-for-ai/schemas/contracts/memory_preflight_receipt.schema.json
sys-for-ai/tests/test_memory_preflight.py
```

### 14.3 Preflight behavior

Preflight must:

1. Run memory status.
2. Load active AgentJob if provided.
3. Load latest handoff if provided.
4. Run targeted lookup or search queries.
5. Resolve returned object IDs.
6. Require source inspection evidence for authoritative use.
7. Record derivative and stale risks.
8. Write or print a memory preflight receipt.
9. Return whether routing may proceed.

### 14.4 CLI commands

```bash
python -m sys_for_ai.cli memory preflight --agentjob AJ-P1-SELFHOST-CONTINUE-KERNEL-001 --json
python -m sys_for_ai.cli memory preflight --agentjob AJ-P1-SELFHOST-CONTINUE-KERNEL-001 --query "continue loop handoff" --json
python -m sys_for_ai.cli memory preflight --write-receipt --agentjob AJ-P1-SELFHOST-CONTINUE-KERNEL-001 --json
python -m sys_for_ai.cli validate-memory-preflight control_records/memory_preflights/memory_preflight_receipt.example.yaml
```

### 14.5 Receipt example

```yaml
memory_preflight_receipt_id: MEMPREFLIGHT-P1-EXAMPLE-001
schema_version: 0.1.0
agentjob_id: AJ-P1-SELFHOST-CONTINUE-KERNEL-001
created_at: 2026-07-06T00:00:00Z
status: PASS_WITH_WARNINGS
commands_run:
  - command: python -m sys_for_ai.cli memory status --json
    result: pass
  - command: python -m sys_for_ai.cli memory search "continue loop handoff" --limit 10 --json
    result: pass
queries:
  - query: continue loop handoff
    returned_object_ids:
      - SRC-PRD-P0
      - ctrl_handoff_example
canonical_sources_inspected:
  - path: PRDs/sys-for-ai_phase-0_product_system_design_prd.md
    registry: source_registry.csv
    row_id: SRC-PRD-P0
    inspected_sections:
      - AgentJob and continuation model
      - source-first memory
      - universal handoff contract
registry_rows_inspected:
  - registry: control_record_registry.csv
    row_id: ctrl_handoff_example
    purpose: Confirm handoff example exists and is registered.
stale_context_risks:
  - risk_id: MEMPREFLIGHT-RISK-001
    status: not_observed
    notes: No generated derivative was used as source authority.
usable_for_routing: true
```

### 14.6 Validation rules

`validate-memory-preflight` checks:

```text
receipt root is mapping
required fields exist
agentjob_id exists in agentjob registry or control-record registry
commands_run is nonempty
queries are present when memory influences routing
canonical_sources_inspected rows resolve to source_registry rows
registry_rows_inspected registries exist and row IDs exist
stale_context_risks are explicit
usable_for_routing is false if required evidence is missing
```

### 14.7 Acceptance criteria

- Memory preflight receipt validates.
- Preflight can run without writing.
- Preflight can write a receipt under `control_records/memory_preflights/` when authorized.
- Preflight rejects generated derivative authority inversion.
- Preflight records canonical source inspection evidence.
- `make validate-memory-preflight` passes.
- `make validate` passes.

---

## 15. Phase 5: `/continue` packet kernel

### 15.1 Objective

Implement the core `/continue` resolver as a deterministic packet generator. It should not secretly perform broad autonomous work. It should resolve state, preflight memory, select one AgentJob, and emit an execution packet.

### 15.2 Deliverables

```text
sys-for-ai/sys_for_ai/control_loop/__init__.py
sys-for-ai/sys_for_ai/control_loop/model.py
sys-for-ai/sys_for_ai/control_loop/state.py
sys-for-ai/sys_for_ai/control_loop/director.py
sys-for-ai/sys_for_ai/control_loop/job_selection.py
sys-for-ai/sys_for_ai/control_loop/execution_packet.py
sys-for-ai/sys_for_ai/control_loop/handoff.py
sys-for-ai/sys_for_ai/control_loop/validators.py
sys-for-ai/tests/test_program_state.py
sys-for-ai/tests/test_continue_packet.py
```

### 15.3 Continue algorithm

```python
def continue_once(root: Path) -> ContinuePacket:
    state = load_program_state(root / "control_records/program_state.yaml")
    validate_program_state_object(state)

    preflight = run_memory_preflight(
        root=root,
        agentjob_id=state.active_agentjob_id,
        handoff_id=state.latest_handoff_id,
    )
    if not preflight.usable_for_routing:
        return StopPacket(reason="memory_preflight_failed", evidence=preflight)

    handoff = load_latest_handoff_or_none(state)
    if handoff is not None:
        validate_handoff_object(handoff)

    selection = select_or_reuse_one_agentjob(state, handoff)
    if selection.kind == "director_decision_required":
        return DirectorDecisionRequiredPacket(reason=selection.reason)
    if selection.kind == "conflict":
        return StopPacket(reason="agentjob_conflict", evidence=selection.evidence)

    validate_agentjob_contract(selection.agentjob)
    validate_agentjob_authority_boundary(selection.agentjob)

    return ExecutionPacket(
        program_state_id=state.program_state_id,
        agentjob=selection.agentjob,
        memory_preflight=preflight,
        allowed_reads=selection.agentjob.allowed_reads,
        allowed_writes=selection.agentjob.allowed_writes,
        validators=selection.agentjob.validators,
        stop_conditions=selection.agentjob.stop_conditions,
    )
```

### 15.4 Packet types

#### 15.4.1 Execution packet

Returned when exactly one AgentJob is authorized.

```json
{
  "packet_type": "execution_packet",
  "status": "READY",
  "program_state_id": "SFA-PROGRAM-STATE-001",
  "agentjob_id": "AJ-P1-SELFHOST-CONTINUE-KERNEL-001",
  "role_id": "control_loop_engineer",
  "allowed_reads": [],
  "allowed_writes": [],
  "validators": [],
  "stop_conditions": [],
  "memory_preflight_receipt_id": "MEMPREFLIGHT-P1-EXAMPLE-001"
}
```

#### 15.4.2 Director decision required packet

Returned when tracked state does not authorize job creation or route selection.

```json
{
  "packet_type": "director_decision_required",
  "status": "BLOCKED",
  "reason": "No active AgentJob and no active Director decision authorizes creation.",
  "required_record_type": "director_decision"
}
```

#### 15.4.3 Stop packet

Returned for validation failure, conflict, human gate, or authority expansion.

```json
{
  "packet_type": "stop",
  "status": "BLOCKED",
  "reason": "multiple_active_agentjobs",
  "evidence": []
}
```

### 15.5 CLI commands

```bash
python -m sys_for_ai.cli continue-status --json
python -m sys_for_ai.cli continue-preflight --json
python -m sys_for_ai.cli continue-select --json
python -m sys_for_ai.cli continue-packet --json
python -m sys_for_ai.cli validate-control-loop
python -m sys_for_ai.cli validate-one-active-agentjob
```

### 15.6 Selection rules

`select_or_reuse_one_agentjob` should use this precedence:

1. If `program_state.active_agentjob_id` is set and valid, reuse it.
2. If latest handoff names `next_agentjob_id` and it is pending, select it.
3. If an active Director decision names `creates_agentjob_id` and that job exists as pending, select it.
4. If no job exists but an active Director decision authorizes creation, return a packet requiring job creation rather than creating the file silently unless the current AgentJob is a Director job.
5. If more than one active job exists, stop.
6. If no route exists, require Director decision.

### 15.7 Makefile targets

```make
continue-status:
	$(PYTHON) -m sys_for_ai.cli continue-status --json

continue-preflight:
	$(PYTHON) -m sys_for_ai.cli continue-preflight --json

continue-select:
	$(PYTHON) -m sys_for_ai.cli continue-select --json

continue-packet:
	$(PYTHON) -m sys_for_ai.cli continue-packet --json

validate-one-active-agentjob:
	$(PYTHON) -m sys_for_ai.cli validate-one-active-agentjob

validate-control-loop:
	$(PYTHON) -m sys_for_ai.cli validate-control-loop
```

Add `validate-control-loop` to `make validate` after registry graph validation.

### 15.8 Acceptance criteria

- `continue-status --json` returns current state.
- `continue-preflight --json` runs memory preflight.
- `continue-select --json` selects at most one job or blocks.
- `continue-packet --json` emits a deterministic packet.
- Multiple active AgentJobs produce a hard stop.
- Missing Director decision produces a Director Decision Required packet.
- Generated derivatives cannot authorize a job.
- `make validate-control-loop` passes.
- `make validate` passes.

---

## 16. Phase 6: Completion and handoff finalization

### 16.1 Objective

Add finalization support so a completed AgentJob can produce durable transaction evidence: completion receipt, registry updates, next handoff, state snapshot, and program state update.

### 16.2 Deliverables

```text
sys-for-ai/sys_for_ai/control_loop/finalization.py
sys-for-ai/sys_for_ai/control_loop/receipts.py
sys-for-ai/sys_for_ai/control_loop/handoff.py
sys-for-ai/control_records/completions/completion_receipt.example.v0_2.yaml
sys-for-ai/control_records/handoffs/handoff.example.v0_2.yaml
sys-for-ai/control_records/state_snapshots/state_snapshot.example.v0_2.yaml
sys-for-ai/tests/test_completion_chain.py
sys-for-ai/tests/test_handoff_chain.py
```

### 16.3 Finalization algorithm

```python
def finalize_agentjob(root: Path, completion_path: Path) -> FinalizationResult:
    completion = load_yaml(completion_path)
    validate_completion_receipt(completion)

    agentjob = load_agentjob(completion["agentjob_id"])
    validate_completion_matches_agentjob(completion, agentjob)

    changed_paths = collect_changed_paths()
    validate_changed_paths_against_agentjob(agentjob, changed_paths)

    run_declared_validators(agentjob)

    if completion_requires_handoff(completion):
        validate_or_create_handoff(completion)

    update_control_registries(completion)
    update_program_state_from_completion(completion)
    write_state_snapshot(completion)

    return FinalizationResult(ok=True, messages=[...])
```

### 16.4 Completion receipt example

```yaml
completion_receipt_id: RECEIPT-P1-SELFHOST-CONTINUE-KERNEL-001
schema_version: 0.2.0
agentjob_id: AJ-P1-SELFHOST-CONTINUE-KERNEL-001
role: control_loop_engineer
result: PASS_WITH_WARNINGS
summary: Minimal /continue packet kernel implemented with memory preflight and one-AgentJob selection.
changed_artifacts:
  - path: sys_for_ai/control_loop/state.py
    change_type: added
    authority_status: controlled
  - path: sys_for_ai/memory/preflight.py
    change_type: added
    authority_status: controlled
memory_preflight_receipt_id: MEMPREFLIGHT-P1-SELFHOST-CONTINUE-KERNEL-001
validation_evidence:
  commands_run:
    - command: make validate-control-loop
      result: pass
      output_path: .local/receipts/validate-control-loop.txt
    - command: make validate
      result: pass
      output_path: .local/receipts/validate.txt
  validators:
    - validator_id: validate-control-loop
      target_path: control_records/program_state.yaml
      result: pass
      notes: One-AgentJob selection passed.
format_profile_changes:
  added:
    - path: control_records/program_state.yaml
      profile_id: fmt_yaml_control
      registry_row_id: ctrl_program_state
  modified: []
  generated_derivatives: []
authority_changes:
  promoted: []
  not_promoted:
    - path: docs/generated/configuration_control/index.md
      reason: Generated reader surface remains derivative.
unresolved_issues:
  - issue_id: ISSUE-CONTINUE-001
    summary: Diff-to-allowlist validator still needs hardening.
    blocking: false
next_recommendation: Route one Validator Engineer AgentJob for diff boundary checks.
```

### 16.5 Handoff example

Use the v0.2 handoff structure defined in Phase 2. It must include:

```text
target_agentic_system
traceability
control_loop_notes
memory_preflight
format_profile_evidence
source_authority_evidence
derivative_surface_evidence
security_evidence
recommended_next_role
phase_boundary_notes
stop_conditions
```

### 16.6 Program state update rules

On successful finalization:

```text
latest_completion_receipt_id = completion_receipt_id
latest_handoff_id = next_handoff_id if present
active_agentjob_id = null or next active job only if explicitly activated
state_status = active, blocked, complete, or human_gated according to completion
latest_memory_preflight_receipt_id = completion.memory_preflight_receipt_id
validation_status.last_validated_at = current timestamp or deterministic placeholder in examples
```

### 16.7 Validation rules

Add:

```bash
python -m sys_for_ai.cli validate-handoffs control_records/handoffs
python -m sys_for_ai.cli validate-completion-receipts control_records/completions
python -m sys_for_ai.cli validate-state-snapshots control_records/state_snapshots
python -m sys_for_ai.cli continue-finalize --completion control_records/completions/RECEIPT-....yaml --json
```

### 16.8 Acceptance criteria

- Completion receipt validates.
- Handoff validates.
- Completion references a valid AgentJob.
- Changed artifacts are inside AgentJob allowlists once diff validator exists.
- Program state can be updated deterministically.
- Registry rows are updated or validation warns when missing.
- `make validate-handoffs` passes.
- `make validate-completion-receipts` passes.
- `make validate` passes.

---

## 17. Phase 7: Boundary and diff validators

### 17.1 Objective

Make AgentJob allowlists enforceable by checking current Git changes against the selected AgentJob's `allowed_writes`, `generated_paths`, `forbidden_paths`, and `forbidden_actions`.

### 17.2 Deliverables

```text
sys-for-ai/sys_for_ai/control_loop/boundaries.py
sys-for-ai/tests/test_agentjob_boundaries.py
```

### 17.3 CLI commands

```bash
python -m sys_for_ai.cli validate-agentjob-boundaries --agentjob AJ-P1-SELFHOST-CONTINUE-KERNEL-001 --git
python -m sys_for_ai.cli validate-check-diff --agentjob AJ-P1-SELFHOST-CONTINUE-KERNEL-001
```

### 17.4 Diff collection

Use:

```bash
git diff --name-only
git diff --cached --name-only
git ls-files --others --exclude-standard
```

The validator should support running from either repository root or `sys-for-ai/` root.

### 17.5 Matching rules

Paths must match at least one allowed write or generated path unless explicitly ignored.

Forbidden path rules outrank allowed write rules.

Generated derivative paths are allowed only when the AgentJob authorizes generated paths.

Examples:

```yaml
allowed_writes:
  - sys-for-ai/sys_for_ai/control_loop/**
  - sys-for-ai/control_records/**

generated_paths:
  - sys-for-ai/docs/generated/**

forbidden_paths:
  - LICENSE
  - NOTICE
  - .git/**
  - sys-for-ai/.venv/**
  - sys-for-ai/docs/generated/** as canonical source
```

The string `as canonical source` is a semantic rule, not a glob. Implement it through derivative registry and content checks, not simple path globbing.

### 17.6 Boundary output

JSON output:

```json
{
  "ok": false,
  "agentjob_id": "AJ-P1-SELFHOST-CONTINUE-KERNEL-001",
  "changed_paths": [
    "sys-for-ai/sys_for_ai/control_loop/state.py",
    "README.md"
  ],
  "allowed": [
    "sys-for-ai/sys_for_ai/control_loop/state.py"
  ],
  "violations": [
    {
      "path": "README.md",
      "reason": "outside_allowed_writes"
    }
  ]
}
```

### 17.7 Acceptance criteria

- Validator fails when a changed file is outside allowlist.
- Validator fails when a forbidden path changes.
- Validator warns or fails when generated derivatives are changed without generated path authorization.
- Validator handles untracked files.
- Validator works from repo root and `sys-for-ai/` root.
- `make validate-agentjob-boundaries` can be run when an active AgentJob exists.
- `make validate` passes.

---

## 18. Phase 8: Generated derivative generators

### 18.1 Objective

Replace or supplement stub-only generated derivative validation with deterministic generators for the Configuration and Control Wiki and Validation Contracts Catalog.

### 18.2 Deliverables

```text
sys-for-ai/sys_for_ai/derivatives/config_control_wiki.py
sys-for-ai/sys_for_ai/derivatives/validation_contracts_catalog.py
sys-for-ai/sys_for_ai/derivatives/templates.py
sys-for-ai/tests/test_generated_derivatives.py
```

### 18.3 CLI commands

```bash
python -m sys_for_ai.cli generate-config-control-wiki --check
python -m sys_for_ai.cli generate-config-control-wiki --write
python -m sys_for_ai.cli generate-validation-contracts-catalog --check
python -m sys_for_ai.cli generate-validation-contracts-catalog --write
python -m sys_for_ai.cli validate-generated-derivatives docs/generated registries/derivative_registry.csv
```

### 18.4 Configuration and Control Wiki pages

Generate:

```text
docs/generated/configuration_control/index.md
docs/generated/configuration_control/yaml-control-records.md
docs/generated/configuration_control/toml-configuration-sources.md
```

Each page must include:

```text
noncanonical banner
page_metadata block
source paths
registry rows
format profile IDs
validation contract IDs
source hashes or pending markers
generator version
generation timestamp or deterministic check marker
stale/orphan status
allowed promotion path
```

### 18.5 Validation Contracts Catalog pages

Generate:

```text
docs/generated/validation_contracts/index.md
docs/generated/validation_contracts/contracts-by-target.md
```

Each page must include:

```text
noncanonical banner
page_metadata block
contract IDs
source paths
dialects
target formats
target artifact classes
target globs
validator commands
owners
authority status
supersession relation
source hashes or pending markers
known limitations
structural-versus-semantic warning
```

### 18.6 Page metadata template

```yaml
page_metadata:
  derivative_id: der_configuration_control_yaml
  authority_status: generated_noncanonical
  source_registries:
    - registries/control_record_registry.csv
    - registries/config_source_registry.csv
    - registries/format_profile_registry.csv
  validation_contracts:
    - contract_agentjob
    - contract_handoff
  generated_at: 2026-07-06T00:00:00Z
  generator: sys_for_ai.derivatives.config_control_wiki:0.1.0
  stale_or_orphan_status: current
```

### 18.7 Acceptance criteria

- `--check` fails when generated pages differ from expected output.
- `--write` updates generated pages only when authorized.
- Generated pages include noncanonical authority notices.
- Generated pages include source and registry trace.
- Generated pages include metadata blocks.
- Generated pages do not claim canonical authority.
- `make generate-config-control-wiki` passes.
- `make generate-validation-contracts-catalog` passes.
- `make validate-generated-derivatives` passes.
- `make validate` passes.

---

## 19. Phase 9: Skill surfaces and documentation

### 19.1 Objective

Add active development skills, Codex shims, and product scaffold skills for `/continue` and source-first memory.

### 19.2 Deliverables

```text
.agents/skills/continue/SKILL.md
.agents/skills/continue/README.md
.agents/skills/continue/examples/self-hosting-continue-example.md
.agents/skills/source-first-memory/SKILL.md
.agents/skills/source-first-memory/README.md
.agents/skills/source-first-memory/examples/memory-preflight-example.md
.codex/skills/continue/SKILL.md
.codex/skills/source-first-memory/SKILL.md
sys-for-ai/skills/core/continue/SKILL.md
sys-for-ai/skills/core/source-first-memory/SKILL.md
sys-for-ai/docs/skill_integration_policy.md updates if needed
sys-for-ai/registries/skill_registry.csv updates
sys-for-ai/skills/core_skill_manifest.yaml updates if required
```

### 19.3 `.agents/skills/continue/SKILL.md`

```markdown
---
name: continue
description: Resume sys-for-ai-dev from tracked state and advance at most one authorized AgentJob.
---

# /continue

Use this skill when the operator asks to continue work from tracked state.

## Rules

1. Read the self-hosting boundary decision record.
2. Run memory preflight.
3. Inspect canonical sources or registry rows named by useful memory hits.
4. Resolve `sys-for-ai/control_records/program_state.yaml`.
5. Inspect the latest handoff if one exists.
6. Select or reuse at most one AgentJob.
7. Stop if a Director decision is required.
8. Execute only the selected AgentJob.
9. Write completion receipt and handoff when state changes.
10. Validate before reporting completion.
11. Do not treat generated docs, local caches, summaries, or chat memory as authority.
```

### 19.4 `.agents/skills/source-first-memory/SKILL.md`

```markdown
---
name: source-first-memory
description: Use sys-for-ai source-first memory as navigation to registered authority.
---

# Source-First Memory

Use this skill when searching, refreshing, validating, or recording memory evidence.

## Authority

Memory lookup finds likely sources. It does not decide truth or permission.

## Required practice

1. Run memory status.
2. Use lookup or targeted search.
3. Inspect the canonical source path or registry row named by useful hits.
4. Record memory preflight evidence when memory affects routing, requirements, AgentJob boundaries, handoffs, permissions, or claims.
5. Treat generated derivatives, local vaults, semantic extracts, and caches as noncanonical.
```

### 19.5 `.codex/skills` shims

Shims should be short:

```markdown
---
name: continue
description: Codex compatibility shim for the sys-for-ai-dev /continue skill.
---

Use `.agents/skills/continue/SKILL.md` as the authoritative development-runtime skill. This file is a compatibility shim.
```

### 19.6 Product scaffold skills

`sys-for-ai/skills/core/continue/SKILL.md` should be portable and target-system oriented:

```markdown
---
name: continue
description: Generic target-system continuation skill template for sys-for-ai generated systems.
---

# Generic /continue

A target system generated by sys-for-ai may adapt this skill to resume from tracked state, inspect the latest handoff, run memory preflight, select at most one bounded AgentJob, validate completion, and create a new handoff.

This template is not itself active development-system authority unless promoted through the local system's skill registry and runtime policy.
```

### 19.7 Acceptance criteria

- Active `.agents` skills exist.
- `.codex` shims point to `.agents` skills.
- Product scaffold skills remain generic and non-Codex-specific.
- Skill registry rows are updated.
- Skill manifest validation passes.
- `make validate-skills` passes.
- `make validate` passes.

---

## 20. Phase 10: Hardening and acceptance

### 20.1 Objective

Complete the implementation with validation, tests, trace updates, generated derivative refresh, and clear acceptance evidence.

### 20.2 Deliverables

```text
sys-for-ai/tests/ updated
sys-for-ai/registries/requirement_trace_registry.csv updated
sys-for-ai/docs/generated/ refreshed
sys-for-ai/control_records/completions/RECEIPT-P1-SELFHOST-ACCEPTANCE-001.yaml
sys-for-ai/control_records/handoffs/HANDOFF-P1-SELFHOST-ACCEPTANCE-001.yaml
```

### 20.3 Full validation chain

Run:

```bash
cd sys-for-ai
make doctor
make validate-agentjobs
make validate-skills
make validate-format-profiles
make validate-config-sources
make validate-control-records
make validate-validation-contract-registry
make validate-toml-config
make validate-jsonschema-contracts
make validate-registry-graph
make validate-requirement-trace
make validate-program-state
make validate-control-loop
make validate-memory-preflight
make validate-handoffs
make validate-completion-receipts
make validate-generated-derivatives
make validate
```

### 20.4 Acceptance criteria

The implementation is acceptable when:

1. Self-hosting boundary policy exists and is registered.
2. Program state exists, validates, and is registered.
3. Director decision records exist, validate, and are registered.
4. Operational AgentJob v0.2 contract exists and validates.
5. Handoff v0.2 and completion receipt v0.2 contracts exist and validate.
6. Memory preflight receipt contract exists and validates.
7. Operational registry files exist with expected headers.
8. Memory status, lookup, search, and preflight commands work.
9. `/continue` status, preflight, select, and packet commands work.
10. `/continue` selects at most one AgentJob.
11. Missing route produces a Director Decision Required packet.
12. Multiple active AgentJobs produce a stop packet.
13. Generated derivatives remain noncanonical.
14. Diff-to-allowlist validator blocks unauthorized changed paths.
15. Active `.agents` skills exist.
16. `.codex` skill files are compatibility shims.
17. Product scaffold skills are generic and not Codex-locked.
18. Generated derivative pages include authority notices and metadata blocks.
19. Requirement trace registry is updated for newly covered Phase 0 and Phase 1 requirements.
20. `make validate` passes.

---

## 21. CLI specification

### 21.1 Memory commands

```text
memory status [--json]
memory lookup <id-or-path> [--json]
memory search <query> [--limit N] [--json]
memory preflight [--agentjob ID] [--handoff ID] [--query TEXT] [--write-receipt] [--json]
memory hash-path <path> [--json]
memory validate-hashes [--json]
memory update-hashes [--check|--write]
```

### 21.2 Continue commands

```text
continue-status [--json]
continue-preflight [--json]
continue-select [--json]
continue-packet [--json]
continue-finalize --completion <path> [--json]
```

### 21.3 Validation commands

```text
validate-program-state [path]
validate-director-decisions [root]
validate-one-active-agentjob
validate-agentjob-boundaries --agentjob <id> [--git]
validate-check-diff --agentjob <id>
validate-memory-preflight <path-or-root>
validate-handoffs <root>
validate-completion-receipts <root>
validate-state-snapshots <root>
validate-control-loop
```

### 21.4 Derivative commands

```text
generate-config-control-wiki --check
generate-config-control-wiki --write
generate-validation-contracts-catalog --check
generate-validation-contracts-catalog --write
validate-generated-derivatives docs/generated registries/derivative_registry.csv
```

---

## 22. Makefile changes

Add targets:

```make
.PHONY: continue-status continue-preflight continue-select continue-packet validate-program-state validate-director-decisions validate-one-active-agentjob validate-agentjob-boundaries validate-memory-preflight validate-handoffs validate-completion-receipts validate-control-loop

continue-status:
	$(PYTHON) -m sys_for_ai.cli continue-status --json

continue-preflight:
	$(PYTHON) -m sys_for_ai.cli continue-preflight --json

continue-select:
	$(PYTHON) -m sys_for_ai.cli continue-select --json

continue-packet:
	$(PYTHON) -m sys_for_ai.cli continue-packet --json

validate-program-state:
	$(PYTHON) -m sys_for_ai.cli validate-program-state control_records/program_state.yaml

validate-director-decisions:
	$(PYTHON) -m sys_for_ai.cli validate-director-decisions control_records/director_decisions

validate-one-active-agentjob:
	$(PYTHON) -m sys_for_ai.cli validate-one-active-agentjob

validate-agentjob-boundaries:
	$(PYTHON) -m sys_for_ai.cli validate-agentjob-boundaries --git

validate-memory-preflight:
	$(PYTHON) -m sys_for_ai.cli validate-memory-preflight control_records/memory_preflights

validate-handoffs:
	$(PYTHON) -m sys_for_ai.cli validate-handoffs control_records/handoffs

validate-completion-receipts:
	$(PYTHON) -m sys_for_ai.cli validate-completion-receipts control_records/completions

validate-control-loop:
	$(PYTHON) -m sys_for_ai.cli validate-control-loop
```

Update full validation target:

```make
validate: doctor validate-agentjobs validate-skills validate-metrics validate-discovery-template bootstrap-memory validate-format-profiles validate-config-sources validate-control-records validate-validation-contract-registry validate-toml-config validate-jsonschema-contracts validate-program-state validate-director-decisions validate-memory-preflight validate-handoffs validate-completion-receipts validate-registry-graph validate-requirement-trace generate-config-control-wiki generate-validation-contracts-catalog validate-generated-derivatives validate-control-loop
```

If that becomes too long, introduce grouped targets:

```make
validate-memory-system
validate-control-loop-system
validate-derivatives
validate-all
```

---

## 23. Validator implementation details

### 23.1 `validate_program_state`

Inputs:

```text
control_records/program_state.yaml
schemas/contracts/program_state.schema.json
control_record_registry.csv
validation_contract_registry.csv
```

Checks:

```text
YAML safe-loads
JSON Schema validates
program_state_id nonempty
system_context exists
self_hosting fields are coherent
state_status is valid
active_agentjob_id exists if set
latest_handoff_id exists if set
latest_completion_receipt_id exists if set
blocked_reason exists if state_status is blocked
human_gate_required true if state_status is human_gated
blocked actions include core authority inversions
```

### 23.2 `validate_director_decisions`

Checks:

```text
all DDR YAML files safe-load
all validate against director_decision.schema.json
all active DDRs are registered
active DDR selected_agentjob_id exists or is explicitly pending creation
rejected_routes have reasons
authority boundary cannot promote derivatives unless explicit source-authority route
```

### 23.3 `validate_one_active_agentjob`

Checks:

```text
read agentjob_registry.csv
count status == active
fail if count > 1
warn if multiple pending jobs and no Director decision disambiguates
fail if completed jobs lack completion_receipt_id
fail if superseded jobs lack supersedes or notes
```

### 23.4 `validate_agentjob_boundaries`

Checks:

```text
load selected AgentJob
collect git changed, staged, and untracked paths
normalize path context
for each changed path:
  fail if forbidden
  pass if allowed_writes match
  pass if generated_paths match and generated derivative authorized
  fail otherwise
```

### 23.5 `validate_memory_preflight`

Checks:

```text
receipt validates against schema
agentjob exists
commands_run nonempty
queries nonempty if usable_for_routing true
canonical source inspections resolve
registry row inspections resolve
usable_for_routing false if required evidence is absent
```

### 23.6 `validate_handoff_chain`

Checks:

```text
handoff files validate
handoff registry rows exist
latest handoff matches program_state
source_artifacts resolve
control_loop_notes are coherent
format_profile_evidence references known profile IDs
source_authority_evidence references known sources
security_evidence exists
```

### 23.7 `validate_completion_chain`

Checks:

```text
completion receipts validate
completion registry rows exist
agentjob_id exists
validation_evidence commands recorded
changed_artifacts listed
format_profile_changes entries have profile IDs
authority_changes do not promote derivatives without approval
next handoff exists if referenced
```

### 23.8 `validate_no_authority_inversion`

Checks:

```text
no derivative registry row status in canonical, canonical_draft
no generated doc says it is canonical
no local path appears as canonical source
no generated derivative path appears in source registry as canonical unless promotion decision exists
```

---

## 24. Testing plan

### 24.1 Unit tests

Add tests for:

```text
registry catalog loading
path resolution from repo root and product root
authority classification
memory lookup by ID
memory lookup by path
memory search ranking
memory preflight receipt creation
program state loading
AgentJob selection
Director decision required packet
multiple active jobs stop packet
completion receipt validation
handoff validation
diff-to-allowlist matching
generated derivative metadata validation
```

### 24.2 Integration tests

Use fixture directories under `tests/fixtures/`.

Scenarios:

```text
valid minimal self-hosting state
missing program_state.yaml
missing latest handoff
one pending AgentJob selected by DDR
active AgentJob reused
multiple active AgentJobs fail
memory hit from generated derivative requires source inspection
completion receipt updates program state
unauthorized changed path fails boundary check
```

### 24.3 Golden JSON tests

For deterministic CLI output, add golden files:

```text
tests/fixtures/golden/memory_status.json
tests/fixtures/golden/memory_lookup_src_prd_p0.json
tests/fixtures/golden/continue_status.json
tests/fixtures/golden/continue_packet.json
```

### 24.4 Test command

Add:

```bash
python -m unittest discover -s tests
```

Makefile:

```make
test:
	$(PYTHON) -m unittest discover -s tests
```

Add `test` to full validation only after tests are stable.

---

## 25. Requirement trace updates

Update `registries/requirement_trace_registry.csv` so this implementation has explicit coverage rows for at least:

```text
SFA-CORE-AJ-001
SFA-CORE-AJ-002
SFA-CORE-AJ-003
SFA-CORE-CONT-001
SFA-CORE-CONT-002
SFA-CORE-MEM-001
SFA-CORE-MEM-002
SFA-CORE-MEM-003
SFA-CORE-MEM-004
SFA-CORE-MEM-005
SFA-CORE-MEM-006
SFA-CORE-MEM-007
SFA-CORE-MEM-008
SFA-CORE-MEM-009
SFA-CORE-DOC-001
SFA-CORE-DOC-002
SFA-CORE-DOC-003
SFA-CORE-DOC-004
SFA-CORE-DOC-005
SFA-CORE-DOC-006
SFA-CORE-DOC-007
SFA-CORE-SVC-001
SFA-CORE-SVC-002
SFA-CORE-SVC-003
SFA-CORE-SVC-004
SFA-CORE-SVC-005
SFA-CORE-IMPROVE-001
SFA-CORE-IMPROVE-002
SFA-CORE-IMPROVE-003
```

Trace rows should distinguish:

```text
covered
partial
scaffolded
deferred
out_of_phase
```

Do not claim full coverage when only scaffolding exists.

Example trace row style:

```csv
TRACE-SFA-CORE-CONT-001,SFA-CORE-CONT-001,PRDs/sys-for-ai_phase-0_product_system_design_prd.md,partial,scaffolded,"Phase 1 implements deterministic state resolution and one-AgentJob selection as a scaffold, but does not implement production autonomous execution.",needs_evidence,SFA-P1-INIT-YAML-005;SFA-P1-INIT-VAL-004,sys-for-ai/sys_for_ai/control_loop/state.py;sys-for-ai/control_records/program_state.yaml,"Self-hosting /continue kernel scaffold."
```

---

## 26. Migration plan

### 26.1 Backward compatibility

Existing files should continue to validate:

```text
control_records/examples/phase1_smoke_agentjob.yaml
control_records/examples/handoff.example.yaml
control_records/examples/completion_receipt.example.yaml
control_records/examples/state_snapshot.example.yaml
```

Do not break the current minimal AgentJob validator. Instead:

- Keep `validate-agentjob` compatible with v0.1 AgentJobs.
- Add `validate-agentjob-v0-2` or auto-detect `schema_version`.
- Treat missing `schema_version` as legacy v0.1.
- Require v0.2 only for operational `/continue` AgentJobs.

### 26.2 Registry migration

Steps:

1. Add new registry headers to `REGISTRY_HEADERS`.
2. Run `make bootstrap-memory` to create missing new registries.
3. Add initial rows.
4. Validate headers.
5. Validate row contracts.
6. Update registry graph checks.

### 26.3 Generated docs migration

Steps:

1. Preserve existing generated stubs.
2. Add generator check mode.
3. Run `--check` and record diffs.
4. Run `--write` only under authorized AgentJob.
5. Update derivative registry rows if generated pages change.

### 26.4 Skill migration

Steps:

1. Add `.agents/skills/continue/` and `.agents/skills/source-first-memory/`.
2. Add `.codex/skills/` shims.
3. Add product scaffold skills under `sys-for-ai/skills/core/` only if the skill manifest is updated accordingly.
4. Validate skill manifest.
5. Update skill registry rows.

---

## 27. Security and privacy plan

### 27.1 YAML safety

All YAML loading must use `yaml.safe_load` through the existing safe helper.

Forbidden:

```python
yaml.load(...)
yaml.unsafe_load(...)
yaml.FullLoader on untrusted files
```

### 27.2 Secret checks

Extend existing secret-like checks to:

```text
YAML control records
TOML config examples
memory preflight receipts
completion receipts
handoffs
generated derivatives
```

Secret-like keys should fail in Phase 1 examples.

### 27.3 Local cache boundaries

Ensure `.gitignore` excludes:

```text
.venv/
__pycache__/
.pytest_cache/
.local/
sys-for-ai/.local/
sys-for-ai/.venv/
```

Local memory/cache paths must not appear as canonical source rows.

### 27.4 Generated derivative redaction

Generated derivatives should never render secret-like values. Since Phase 1 forbids secrets in YAML/TOML examples, redaction is mostly future-proofing.

Add generator behavior:

```text
if key is secret-like:
  render [REDACTED-SECRET-LIKE-KEY]
  emit validation warning or failure according to policy
```

---

## 28. Risk register

| Risk ID | Risk | Impact | Mitigation |
|---|---|---|---|
| RISK-SELFHOST-001 | Self-hosting boundary remains implicit | Product and development runtime blur | Add explicit self-hosting decision record and system_context fields |
| RISK-MEM-001 | Memory lookup treated as authority | Bad routing and stale implementation | Require memory preflight receipts and source inspection evidence |
| RISK-CONT-001 | `/continue` becomes unbounded | Unauthorized work and audit failure | Enforce one-AgentJob invariant and stop packets |
| RISK-CONT-002 | AgentJob allowlists are not enforced | Control records become decorative | Add git diff to AgentJob boundary validator |
| RISK-DER-001 | Generated docs become ghost authorities | Documentation drift and authority inversion | Noncanonical banners, derivative registry checks, no-authority-inversion validator |
| RISK-SCHEMA-001 | JSON Schema treated as semantic truth | False confidence | Keep structural-versus-semantic warnings in schemas and docs |
| RISK-MIGRATE-001 | New schemas break existing examples | Validation churn | Support v0.1 legacy contracts and v0.2 operational contracts |
| RISK-SKILL-001 | `.codex` shims become canonical | Harness lock-in | Keep `.agents` active and `.codex` shim-only |
| RISK-DEP-001 | Memory implementation adds heavy dependencies | Phase 1 drift | Use stdlib, PyYAML, jsonschema, tomllib/tomli only |
| RISK-HASH-001 | Hash validation too strict too early | Blocks scaffold progress | Treat pending hashes as warnings first, then harden later |

---

## 29. Rollback plan

Each AgentJob should be independently revertible.

Rollback rules:

1. If a schema addition breaks validation, revert schema and registry row together.
2. If a CLI command breaks existing validation, remove the command from `make validate` first, then repair in a bounded AgentJob.
3. If generated derivative generator output is wrong, keep source files, revert generated pages, and open a generator repair AgentJob.
4. If new registries create excessive validation burden, keep headers but mark rows as scaffolded with deferred validation in trace registry.
5. Never rewrite activated completion or handoff records to hide a failed attempt. Supersede them.

---

## 30. Proposed PR sequence

If using pull requests or sequential commits, split implementation into these changes:

### PR 1: Self-hosting boundary and program state

Files:

```text
implementation_plans/self_hosting_boundary_decision_record.md
sys-for-ai/docs/self_hosting_boundary_policy.md
sys-for-ai/docs/memory_retrieval_policy.md
sys-for-ai/docs/continue_loop_policy.md
sys-for-ai/control_records/program_state.yaml
sys-for-ai/schemas/contracts/program_state.schema.json
sys-for-ai/registries/* updates
sys-for-ai/sys_for_ai/validators.py
sys-for-ai/sys_for_ai/cli.py
sys-for-ai/Makefile
```

### PR 2: Operational contracts and registries

Files:

```text
schemas/contracts/director_decision.schema.json
schemas/contracts/agentjob_v0_2.schema.json
schemas/contracts/handoff_v0_2.schema.json
schemas/contracts/completion_receipt_v0_2.schema.json
schemas/contracts/memory_preflight_receipt.schema.json
registries/agentjob_registry.csv
registries/director_decision_registry.csv
registries/handoff_registry.csv
registries/completion_receipt_registry.csv
registries/memory_preflight_receipt_registry.csv
```

### PR 3: Memory catalog and lookup

Files:

```text
sys_for_ai/memory/**
sys_for_ai/cli.py
tests/test_memory_*.py
```

### PR 4: Memory preflight

Files:

```text
sys_for_ai/memory/preflight.py
sys_for_ai/memory/receipts.py
control_records/memory_preflights/**
tests/test_memory_preflight.py
```

### PR 5: `/continue` packet kernel

Files:

```text
sys_for_ai/control_loop/**
control_records/director_decisions/**
control_records/agentjobs/**
tests/test_continue_packet.py
```

### PR 6: Completion and handoff finalization

Files:

```text
sys_for_ai/control_loop/finalization.py
control_records/completions/**
control_records/handoffs/**
tests/test_completion_chain.py
tests/test_handoff_chain.py
```

### PR 7: Boundary validators

Files:

```text
sys_for_ai/control_loop/boundaries.py
tests/test_agentjob_boundaries.py
Makefile
```

### PR 8: Generated derivative generators

Files:

```text
sys_for_ai/derivatives/**
docs/generated/**
tests/test_generated_derivatives.py
```

### PR 9: Skills and final docs

Files:

```text
.agents/skills/continue/**
.agents/skills/source-first-memory/**
.codex/skills/continue/**
.codex/skills/source-first-memory/**
sys-for-ai/skills/core/continue/**
sys-for-ai/skills/core/source-first-memory/**
registries/skill_registry.csv
skills/core_skill_manifest.yaml
```

### PR 10: Acceptance and trace closure

Files:

```text
registries/requirement_trace_registry.csv
control_records/completions/RECEIPT-P1-SELFHOST-ACCEPTANCE-001.yaml
control_records/handoffs/HANDOFF-P1-SELFHOST-ACCEPTANCE-001.yaml
implementation_plans/self_hosting_memory_continue_acceptance_report.md
```

---

## 31. First executable AgentJob recommendation

Create:

```text
sys-for-ai/control_records/agentjobs/AJ-P1-SELFHOST-CONTINUE-KERNEL-001.yaml
```

Content:

```yaml
agentjob_id: AJ-P1-SELFHOST-CONTINUE-KERNEL-001
schema_version: 0.2.0
status: pending
objective: >
  Implement the minimal self-hosting memory preflight and /continue control-loop
  kernel for sys-for-ai-dev using source-first memory, tracked program state,
  one-AgentJob selection, completion receipts, and handoff records.
lifecycle_stage: implementation_initialization
role_binding:
  role_id: control_loop_and_memory_engineer
  binding_type: one_job_provisional_role
  authority_scope: sys-for-ai Phase 1 scaffold
  expires_with_agentjob: true
required_inputs:
  - PRDs/sys-for-ai_phase-0_product_system_design_prd.md
  - PRDs/sys-for-ai_phase-1_implementation_initialization_prd.md
  - sys-for-ai/README.md
  - sys-for-ai/Makefile
  - sys-for-ai/sys_for_ai/cli.py
  - sys-for-ai/sys_for_ai/validators.py
  - sys-for-ai/sys_for_ai/memory.py
  - sys-for-ai/registries/source_registry.csv
  - sys-for-ai/registries/control_record_registry.csv
  - sys-for-ai/registries/validation_contract_registry.csv
  - sys-for-ai/control_records/examples/handoff.example.yaml
  - sys-for-ai/control_records/examples/completion_receipt.example.yaml
  - sys-for-ai/control_records/examples/state_snapshot.example.yaml
allowed_reads:
  - PRDs/**
  - implementation_plans/**
  - sys-for-ai/**
allowed_writes:
  - implementation_plans/self_hosting_boundary_decision_record.md
  - sys-for-ai/sys_for_ai/memory/**
  - sys-for-ai/sys_for_ai/control_loop/**
  - sys-for-ai/sys_for_ai/cli.py
  - sys-for-ai/sys_for_ai/validators.py
  - sys-for-ai/schemas/contracts/**
  - sys-for-ai/control_records/**
  - sys-for-ai/registries/**
  - sys-for-ai/docs/**
  - sys-for-ai/Makefile
  - sys-for-ai/tests/**
generated_paths:
  - sys-for-ai/docs/generated/**
  - sys-for-ai/.local/receipts/**
forbidden_paths:
  - LICENSE
  - NOTICE
  - .git/**
  - .venv/**
  - sys-for-ai/.venv/**
forbidden_actions:
  - Modify repository LICENSE or NOTICE.
  - Treat generated derivatives as canonical.
  - Add a vector database or production memory service.
  - Hardcode Codex as the only supported sys-for-ai harness.
  - Execute more than one AgentJob in one /continue invocation.
  - Mutate activated control records instead of superseding them.
  - Use unsafe YAML loading.
memory_preflight:
  required: true
  minimum_queries:
    - source-first memory AgentJob continuation handoff
    - format profile registry control record validation contract
  required_evidence:
    - canonical source inspection
    - registry row inspection
    - derivative status check
expected_outputs:
  - Self-hosting boundary decision record.
  - Program state schema and example.
  - Director decision schema and example.
  - Memory lookup/search/preflight package.
  - /continue status/select/packet commands.
  - Memory preflight receipt schema and example.
  - Updated registries.
  - New validators and Makefile targets.
  - Passing validation receipt.
validators:
  - cd sys-for-ai && make doctor
  - cd sys-for-ai && make validate-jsonschema-contracts
  - cd sys-for-ai && make validate-control-records
  - cd sys-for-ai && make validate-registry-graph
  - cd sys-for-ai && make validate
  - cd sys-for-ai && python -m sys_for_ai.cli continue-status --json
  - cd sys-for-ai && python -m sys_for_ai.cli continue-packet --json
completion_evidence_required:
  - memory_preflight_receipt_id
  - changed_artifacts
  - command_results
  - validation_status
  - unresolved_issues
  - next_handoff_id
handoff_policy:
  create_handoff_when:
    - implementation remains incomplete
    - validation fails
    - next AgentJob is recommended
    - human gate is required
authority_boundary:
  may_modify_product_scaffold: true
  may_modify_canonical_prds: false
  may_promote_generated_derivatives: false
  may_change_runtime_skill_authority: false
stop_conditions:
  - Required PRD source cannot be inspected.
  - Existing schema or registry would be broken.
  - More than one AgentJob is required.
  - Required write is outside allowlist.
  - Validation fails for reasons outside this AgentJob scope.
```

---

## 32. Operator workflow after implementation

### 32.1 Starting continuation

```bash
cd sys-for-ai
make continue-status
make continue-preflight
make continue-select
make continue-packet
```

### 32.2 Executing the selected job

The root AI agent or developer reads the execution packet and works only inside the selected AgentJob boundary.

### 32.3 Validating during work

```bash
cd sys-for-ai
make validate-control-loop
make validate-registry-graph
make validate
```

### 32.4 Finalizing

```bash
cd sys-for-ai
python -m sys_for_ai.cli continue-finalize --completion control_records/completions/RECEIPT-....yaml --json
make validate
```

### 32.5 Handling stop packets

If `/continue` returns a stop packet:

- Do not keep working from chat memory.
- Inspect the packet reason.
- Create or route a bounded AgentJob if needed.
- If authority expansion is required, create a Director decision or human-gated record.
- If validation failed, fix only inside current AgentJob allowlists or stop.

---

## 33. Definition of done

This implementation is done when the following command chain passes from `sys-for-ai/`:

```bash
make doctor
make validate
python -m sys_for_ai.cli memory status --json
python -m sys_for_ai.cli memory lookup SRC-PRD-P0 --json
python -m sys_for_ai.cli memory search "source-first memory" --limit 5 --json
python -m sys_for_ai.cli continue-status --json
python -m sys_for_ai.cli continue-preflight --json
python -m sys_for_ai.cli continue-select --json
python -m sys_for_ai.cli continue-packet --json
```

And the repository contains:

```text
self-hosting boundary decision record
program_state.yaml
operational control schemas
operational control registries
memory package
control_loop package
memory preflight receipts
continue packet command
completion and handoff validators
boundary validator
generated derivative checks/generators
active .agents skills
.codex compatibility shims
updated requirement trace rows
acceptance completion receipt
acceptance handoff
```

---

## 34. Final recommendation

Implement this plan in narrow passes. The temptation will be to build the cathedral at once. Resist that. Build the registry lock first, then the memory telescope, then the continuation turnstile, then the receipt archive, then the derivative lanterns.

The first stable milestone is not autonomous development. The first stable milestone is this:

```text
A developer can run /continue, receive a deterministic packet for exactly one authorized AgentJob, see which sources were inspected, see which writes are allowed, run validators, and produce a completion receipt plus next handoff without relying on chat memory or generated derivative authority.
```

Once that works, `sys-for-ai-dev` becomes a disciplined self-hosting development system rather than a recursive fog machine.
