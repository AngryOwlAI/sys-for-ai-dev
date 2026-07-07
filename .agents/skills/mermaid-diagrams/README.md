# Mermaid Diagrams - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `mermaid-diagrams`  
Canonical runtime path: `.agents/skills/mermaid-diagrams`  
Compatibility shim path: `.codex/skills/mermaid-diagrams/SKILL.md`  
Source import: `skills/mermaid-diagrams` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# mermaid-diagrams

## Purpose

Reusable workflow for creating, reviewing, rendering, and validating Mermaid
diagrams as source-controlled documentation artifacts.

## When To Use

Use this skill when a project needs Mermaid diagrams with source grounding,
explicit visual grammar, stable IDs, portable styling, rendered derivative
checks, and clear claim boundaries.

## What It Produces

- Mermaid source block or `.mmd` file.
- Stable diagram ID when required.
- Visual grammar summary.
- Optional rendered derivative output.
- Validation summary with commands run and checks skipped.

## Required Files

- `SKILL.md`: executable workflow.
- `README.md`: human-facing summary.
- `AGENTS.md`: maintenance and adaptation rules.

## Adaptation Summary

Replace placeholders with local diagram paths, project authority sources,
style guides, renderer commands, validation commands, and publication rules.
Keep Mermaid source canonical and document any project-specific renderer,
runtime, registry, or manifest assumptions.

## Validation Summary

Confirm the skill defines use conditions, inputs, outputs, diagram grammar,
rendering guidance, validation, failure modes, provenance, and adaptation
guidance. For project use, validate Mermaid syntax, derivative parity, runtime
policy, accessibility, and visual readability.
