# sys-for-ai Phase 1 Implementation Initialization PRD

**Document status:** Draft baseline  
**Product name:** `sys-for-ai`  
**Phase:** Phase 1: Implementation initialization  
**Depends on:** `PRDs/sys-for-ai_phase-0_product_system_design_prd.md`  
**Last updated:** 2026-07-04

---

## 1. Executive summary

Phase 1 initializes the `sys-for-ai` implementation repository so development can begin safely, reproducibly, and with source-first governance. Phase 1 does not finish the framework. It creates the first executable spine: Python environment, dependency policy, YAML control records, validators, skill adapters, memory registries, documentation policies, and a Docker decision record.

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

---

## 3. Non-goals

- Do not implement a production runtime service.
- Do not add a vector database.
- Do not build a full generated wiki engine.
- Do not force Docker as the default developer environment.
- Do not treat Obsidian as canonical memory.
- Do not import external skill files without local adaptation and provenance records.
- Do not implement target-domain agent systems yet.

---

## 4. Initialization requirements

### 4.1 Repository layout

`SFA-P1-INIT-REPO-001`: Add a Python scaffold under `sys-for-ai/sys_for_ai/`.

`SFA-P1-INIT-REPO-002`: Add `sys-for-ai/requirements.txt`, `sys-for-ai/pyproject.toml`, and `sys-for-ai/Makefile`.

`SFA-P1-INIT-REPO-003`: Add folders for `schemas`, `control_records`, `registries`, `skills`, `docs`, and `templates`.

`SFA-P1-INIT-REPO-004`: Preserve top-level PRDs and implementation plans outside the implementation package.

### 4.2 Python environment

`SFA-P1-INIT-ENV-001`: Use a local `.venv` as the required Phase 1 development environment.

`SFA-P1-INIT-ENV-002`: Keep `.venv/`, cache files, generated local vaults, and local receipts out of source control unless explicitly promoted.

`SFA-P1-INIT-ENV-003`: Provide setup commands through the Makefile:

```bash
cd sys-for-ai
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

### 4.4 YAML records and validators

`SFA-P1-INIT-YAML-001`: Create a smoke-test AgentJob YAML file.

`SFA-P1-INIT-YAML-002`: Create schema-like YAML specifications for AgentJobs and skills.

`SFA-P1-INIT-YAML-003`: Add validators that use `yaml.safe_load`.

`SFA-P1-INIT-YAML-004`: The validation command shall fail on missing required AgentJob fields or malformed skill manifest entries.

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

### 4.7 Docker decision

`SFA-P1-INIT-DOCKER-001`: Add an environment decision record that chooses `.venv` as the Phase 1 baseline.

`SFA-P1-INIT-DOCKER-002`: Defer development Docker until a trigger exists: OS-level rendering dependencies, multi-service runtime, strict CI parity, contributor environment drift, or target-runtime generation.

`SFA-P1-INIT-DOCKER-003`: Keep development environment containers separate from target-system runtime container templates.

### 4.8 Validation

`SFA-P1-INIT-VAL-001`: Add `make doctor` to check Python, PyYAML, package import, and expected folders.

`SFA-P1-INIT-VAL-002`: Add `make validate-agentjob`, `make validate-skills`, `make bootstrap-memory`, and `make validate`.

`SFA-P1-INIT-VAL-003`: Validation shall be deterministic and runnable offline after dependencies are installed.

---

## 5. Acceptance criteria

Phase 1 initialization is acceptable when:

1. `make doctor` passes inside `sys-for-ai/`.
2. `make validate` passes inside `sys-for-ai/`.
3. The sample AgentJob YAML validates.
4. The core skill manifest validates and all adapter folders exist.
5. Memory registries exist with expected headers.
6. The Docker decision record exists and distinguishes development environment from target runtime.
7. Phase 0 product requirements and Phase 1 initialization requirements are no longer mixed in one PRD.

---

## 6. Recommended next AgentJob

```yaml
agentjob_id: AJ-P1-BOOTSTRAP-001
objective: Apply the Phase 1 repository overlay, create the Python virtual environment, install dependencies, and run validation.
role: implementation_initialization_agent
allowed_reads:
  - PRDs/sys-for-ai_phase-0_product_system_design_prd.md
  - PRDs/sys-for-ai_phase-1_implementation_initialization_prd.md
  - implementation_plans/phase-1_environment_decision_record.md
allowed_writes:
  - sys-for-ai/**
  - implementation_plans/**
forbidden_actions:
  - Delete repository root license or notice files.
  - Treat generated derivatives as canonical sources.
  - Force Docker as default without updating the decision record.
expected_outputs:
  - Passing validation command receipt.
  - Updated source registry entries if files are promoted as canonical.
validators:
  - cd sys-for-ai && make doctor
  - cd sys-for-ai && make validate
stop_conditions:
  - Required dependency installation fails.
  - Existing repository file would be overwritten without maintainer approval.
```
