# Phase 1 Skill Import Plan

**Status:** Draft  
**Date:** 2026-07-04  
**Scope:** Core skill templates from `AngryOwlAI/ai-skills-for-sys`

---

## Objective

Make all current `ai-skills-for-sys` templates core governed skills for `Sys4AI`, while preserving provenance and adapting them to local authority rules.

---

## Core skill set

| Skill | Family | Phase 1 status |
|---|---|---|
| `conversation-to-prd` | Requirements production | Adapter shell included |
| `decision-grilling` | Decision clarification | Adapter shell included |
| `decision-grilling-context-45` | Decision clarification | Adapter shell included |
| `domain-grilling-with-docs` | Domain/documentation clarification | Adapter shell included |
| `domain-grilling-with-docs-context-45` | Domain/documentation clarification | Adapter shell included |
| `mermaid-diagrams` | Technical communication | Adapter shell included |
| `plantuml-diagrams` | Technical communication | Adapter shell included |
| `prd-to-implementation-plan` | Implementation planning | Adapter shell included |
| `codex-usage-metrics` | Runtime/session accounting | Adapter shell included |
| `technical-writing-quality-gate` | Technical writing verification | Adapter shell included |
| `skill-import-generalizer` | Skill library maintenance | Adapter shell included |

---

## Import rules

1. Do not treat upstream templates as invisible magic.
2. Copy or adapt upstream content only through an explicit skill-import AgentJob.
3. Preserve upstream repository path and retrieval date.
4. Replace placeholders with local `Sys4AI` paths, commands, and authority boundaries.
5. Add local validators where available.
6. Record imported/adapted status in `skills/core_skill_manifest.yaml` and `registries/skill_registry.csv`.
7. Keep skills as governed capabilities, not random prompt snippets.

---

## Next AgentJob

```yaml
agentjob_id: AJ-P1-SKILL-IMPORT-001
objective: Compare adapter shells with upstream skill templates and promote exact adapted content where appropriate.
role: skill_governance_agent
allowed_reads:
  - Sys4AI/skills/core_skill_manifest.yaml
  - Sys4AI/skills/core/**
  - https://github.com/AngryOwlAI/ai-skills-for-sys
allowed_writes:
  - Sys4AI/skills/core/**
  - Sys4AI/registries/skill_registry.csv
forbidden_actions:
  - Remove provenance records.
  - Copy project-specific assumptions without adaptation.
  - Mark an upstream template as authoritative without local review.
validators:
  - cd Sys4AI && make validate-skills
expected_outputs:
  - Updated adapted skills.
  - Updated skill registry.
  - Completion receipt with upstream source revision if available.
```
