# Phase 1 Memory System Scaffold Plan

**Status:** Draft  
**Date:** 2026-07-04  
**Scope:** Source-first memory and knowledge system initialization

---

## Objective

Create the first source-first memory scaffold for `sys-for-ai`, modeled as lightweight registries and validation commands before adding a database, vector index, wiki engine, or Obsidian sync.

---

## Initial artifacts

| Artifact | Purpose |
|---|---|
| `registries/source_registry.csv` | Canonical source objects and authority status. |
| `registries/derivative_registry.csv` | Generated or synchronized reader surfaces. |
| `registries/object_relationship_registry.csv` | Relationships among sources, derivatives, jobs, skills, and decisions. |
| `registries/skill_registry.csv` | Skill provenance and adaptation status. |
| `docs/source_authority_policy.md` | Authority hierarchy and promotion rules. |
| `docs/obsidian_derivative_policy.md` | Optional Obsidian vault rules. |
| `sys_for_ai/memory.py` | Bootstrap helper for registry files. |

---

## Bootstrap command

```bash
cd sys-for-ai
make bootstrap-memory
```

The command creates missing registry files with required headers. It does not promote generated artifacts to source authority.

---

## Validation command

```bash
cd sys-for-ai
make validate
```

The validation command checks sample AgentJob YAML, skill manifest integrity, and memory scaffold expectations.

---

## Source authority rules

1. Canonical sources outrank generated derivatives.
2. Registries identify authority, not filename vibes.
3. Obsidian vaults are derivative unless promoted through an explicit source-import workflow.
4. Generated docs must trace to source IDs.
5. Stale or orphan derivatives must be warned, regenerated, or removed.

---

## Later expansions

- Add decision registry.
- Add AgentJob registry.
- Add completion receipt ledger.
- Add generated wiki pipeline.
- Add Obsidian sync command.
- Add derivative drift validator.
- Add semantic retrieval only after source authority is stable.
