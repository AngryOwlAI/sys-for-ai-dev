# Prd To Implementation Plan - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `prd-to-implementation-plan`  
Canonical runtime path: `.agents/skills/prd-to-implementation-plan`  
Compatibility shim path: `.codex/skills/prd-to-implementation-plan/SKILL.md`  
Source import: `skills/prd-to-implementation-plan` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

## Sys4AI-dev Authority Rules

- Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs.
- `Sys4AI/` is the product scaffold being developed; it is not the full development workspace.
- `.agents/skills/<skill-id>/` is the active runtime skill surface for this repository.
- `.codex/skills/<skill-id>/SKILL.md` is compatibility-only and must point back to this canonical path.
- Existing `Sys4AI/skills/core/` files are scaffold and product-reference adapters, not the active runtime authority.
- Do not import local receipts, caches, generated `usage-metrics.txt`, or private operational state as skill source.
- Treat generated PRDs, plans, diagrams, warnings, and handoffs as derivative work until accepted by the relevant project authority.

The imported source guidance below remains valid where it does not conflict with these Sys4AI-dev rules.

---

# prd-to-implementation-plan

## Purpose

Reusable workflow for converting PRDs, specs, issues, or feature briefs into
engineering implementation plans and Codex-ready task packets.

## When To Use

Use this skill when requirements need traceability, repository grounding,
implementation phases, acceptance criteria, validation commands, and reviewable
task slices.

## What It Produces

- Implementation plan.
- Requirement traceability matrix.
- Codex task packets.
- Assumptions, blockers, risks, validation plan, and next prompt.

## Required Files

- `SKILL.md`: executable workflow.
- `README.md`: human-facing summary.
- `AGENTS.md`: maintenance and adaptation rules.
- `templates/prd-intake-checklist.md`: requirement extraction checklist.
- `templates/implementation-plan-template.md`: default long-form plan shape.
- `templates/codex-task-packet-template.md`: default task packet shape.
- `templates/review-checklist.md`: final planning quality checklist.

## Adaptation Summary

Replace project placeholders with local output paths, repository conventions,
planning templates, and validation commands. Add domain-specific constraints
only when they affect implementation or validation.

## Validation Summary

Confirm each requirement maps to a task or explicit deferral, tasks include
acceptance criteria and validation guidance, and commands are discovered rather
than invented.
