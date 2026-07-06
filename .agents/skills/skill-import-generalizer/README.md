# Skill Import Generalizer - sys-for-ai-dev Runtime Adaptation

Canonical skill ID: `skill-import-generalizer`  
Canonical runtime path: `.agents/skills/skill-import-generalizer`  
Compatibility shim path: `.codex/skills/skill-import-generalizer/SKILL.md`  
Source import: `.codex/skills/skill-import-generalizer` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

## sys-for-ai-dev Authority Rules

- Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs.
- `sys-for-ai/` is the product scaffold being developed; it is not the full development workspace.
- `.agents/skills/<skill-id>/` is the active runtime skill surface for this repository.
- `.codex/skills/<skill-id>/SKILL.md` is compatibility-only and must point back to this canonical path.
- Existing `sys-for-ai/skills/core/` files are scaffold and product-reference adapters, not the active runtime authority.
- Do not import local receipts, caches, generated `usage-metrics.txt`, or private operational state as skill source.
- Treat generated PRDs, plans, diagrams, warnings, and handoffs as derivative work until accepted by the relevant project authority.

The imported source guidance below remains valid where it does not conflict with these sys-for-ai-dev rules.

---

# Skill Import Generalizer

This skill defines the standard workflow for converting project-specific AI skills into reusable templates for this repository.

## Purpose

Use this skill when importing a skill from another project, repository, workflow, or local skill directory. The goal is to preserve the reusable method while removing project-specific assumptions.

## When To Use

- A skill should be made agnostic, portable, or reusable.
- A source skill contains hard-coded paths, project names, private terminology, or local validation commands.
- A skill should be stored under `skills/<skill-name>/` as a template.

## Output

The generalized skill folder should include:

- `SKILL.md`: executable agent instructions.
- `README.md`: human-facing overview and usage notes.
- `AGENTS.md`: local maintenance and validation rules.

Optional supporting folders may include `templates/`, `scripts/`, or `examples/` when they improve reuse.

## Adaptation Summary

Skills stored here are templates. When used inside another project, they should be adapted with project-specific paths, commands, authorities, constraints, and validation steps.

## Validation Summary

Before finalizing a generalized skill, verify that it:

- Can be understood without access to the original project.
- Contains no sensitive or private source material.
- Uses placeholders for project-specific values.
- Includes `SKILL.md`, `README.md`, and `AGENTS.md`.
- Explains how to adapt the template inside a target project.

