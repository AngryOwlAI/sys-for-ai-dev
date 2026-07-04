# Phase 1 Validation Plan

**Status:** Draft  
**Date:** 2026-07-04  
**Scope:** Initial local validation for `sys-for-ai`

---

## Validation philosophy

Phase 1 validation should be small, deterministic, local, and source-aware. It should prove that the repository has a working Python spine and that the first YAML, skill, and memory artifacts follow the declared contracts.

---

## Commands

| Command | Purpose |
|---|---|
| `make doctor` | Check Python, PyYAML, package import, and expected folders. |
| `make validate-agentjob` | Validate sample AgentJob control record. |
| `make validate-skills` | Validate the core skill manifest and adapter folders. |
| `make bootstrap-memory` | Create missing memory registries with expected headers. |
| `make validate` | Run all Phase 1 checks. |

---

## Acceptance checks

1. Python imports `yaml` successfully.
2. `sys_for_ai` imports successfully.
3. Sample AgentJob YAML has all required fields.
4. Core skill manifest lists all required skill IDs.
5. Every manifest skill has a local adapter folder.
6. Every adapter folder has `SKILL.md`, `README.md`, `AGENTS.md`, and an example.
7. Required registry files exist with headers.

---

## Known limitations

- The AgentJob validator is structural, not semantically complete.
- The skill validator checks adapter presence and manifest shape, not full workflow quality.
- Registry validation checks file existence and headers, not full authority graph consistency.
- No CI workflow is included yet.
