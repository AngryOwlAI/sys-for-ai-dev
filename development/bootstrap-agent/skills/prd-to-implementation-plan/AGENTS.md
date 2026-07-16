# Prd To Implementation Plan - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `prd-to-implementation-plan`  
Canonical runtime path: `development/bootstrap-agent/skills/prd-to-implementation-plan`
Compatibility shim path: `.codex/skills/prd-to-implementation-plan/SKILL.md`  
Source import: `skills/prd-to-implementation-plan` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# AGENTS.md

## Local Mission

Maintain `prd-to-implementation-plan` as a practical bridge from product intent
to reviewable Codex engineering packets.

## Maintenance Rules

- Keep planning separate from direct implementation.
- Preserve traceability from requirements to tasks.
- Require repository inspection before naming commands or affected files.
- Avoid project-specific output paths unless expressed as placeholders.
- Keep reusable planning templates under `templates/` portable and synchronized
  with `SKILL.md`.

## Portability Requirements

The template must not assume a framework, package manager, issue tracker, or
file layout. Add local conventions only during adaptation.

## Validation Requirements

Before finalizing changes, verify that `SKILL.md`, `README.md`, and
`AGENTS.md` exist and that the skill explains use conditions, inputs, outputs,
procedure, validation, failure modes, provenance, and adaptation guidance.

## Adaptation Instructions

When adapting this skill, add the target project's PRD format, planning output
directory, known validators, release constraints, and review checklist.
