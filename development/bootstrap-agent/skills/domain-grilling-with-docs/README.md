# Domain Grilling With Docs - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `domain-grilling-with-docs`  
Canonical runtime path: `development/bootstrap-agent/skills/domain-grilling-with-docs`
Compatibility shim path: `.codex/skills/domain-grilling-with-docs/SKILL.md`  
Source import: `skills/domain-grilling-with-docs` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

## Sys4AI-dev Authority Rules

- Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs.
- `Sys4AI/` is the product scaffold being developed; it is not the full development workspace.
- `development/bootstrap-agent/skills/<skill-id>/` is the active runtime skill surface for this repository.
- `.codex/skills/<skill-id>/SKILL.md` is compatibility-only and must point back to this canonical path.
- Existing `Sys4AI/assets/skills/` files are scaffold and product-reference adapters, not the active runtime authority.
- Do not import local receipts, caches, generated `usage-metrics.txt`, or private operational state as skill source.
- Treat generated PRDs, plans, diagrams, warnings, and handoffs as derivative work until accepted by the relevant project authority.

The imported source guidance below remains valid where it does not conflict with these Sys4AI-dev rules.

---

# domain-grilling-with-docs

## Purpose

Provide a reusable workflow for clarifying domain terminology, surfacing contradictions between plans and code, and recording stable glossary or architecture decisions.

## When To Use

- The user wants a grilling session grounded in existing docs or domain language.
- Terms are overloaded, fuzzy, or inconsistent with the project glossary.
- A decision may warrant an ADR because it is hard to reverse, surprising, and tradeoff-heavy.

## What This Skill Produces

- Sequential questions with recommendations.
- Updated glossary/context entries when terms are resolved.
- Optional ADRs for qualifying decisions.

## Required Files

This stored template package contains:

- `SKILL.md`: executable agent instructions.
- `README.md`: human-facing summary and adaptation notes.
- `AGENTS.md`: local maintenance rules for this template.
- `templates/context-format.md`: portable glossary/context format guidance.
- `templates/adr-format.md`: portable ADR format and qualification guidance.

Target projects may add `templates/`, `scripts/`, `examples/`, or reference material when adapting the skill.

## Adaptation Summary

Replace placeholders such as `<PROJECT_ROOT>`, `<VALIDATION_COMMAND>`, `<OUTPUT_DIRECTORY>`, and any domain-specific registry, role, source, or tool names before installing this template into a project.

Preserve the reusable workflow, but add project-specific authority boundaries, commands, and stop conditions only when local evidence requires them.

## Validation Summary

A valid adaptation should satisfy these checks:

- Glossary entries define domain language, not implementation details.
- ADRs are used sparingly and explain the tradeoff.
- Code contradictions are reported with evidence.
- Questions remain one at a time.
