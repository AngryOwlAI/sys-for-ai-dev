# Plantuml Diagrams - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `plantuml-diagrams`  
Canonical runtime path: `.agents/skills/plantuml-diagrams`  
Compatibility shim path: `.codex/skills/plantuml-diagrams/SKILL.md`  
Source import: `skills/plantuml-diagrams` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# plantuml-diagrams

## Purpose

Reusable workflow for creating, reviewing, repairing, rendering, and validating
PlantUML diagrams as source-controlled documentation artifacts.

## When To Use

Use this skill when a project needs PlantUML or UML-as-code diagrams grounded in
source material, with clear diagram-family selection, safe include handling,
portable styling, rendered derivative checks, and explicit validation notes.

## What It Produces

- PlantUML source block or `.puml` file.
- Diagram-family rationale when selection is ambiguous.
- Include and style notes.
- Optional rendered derivative output.
- Validation summary with commands run, checks skipped, and residual risk.

## Required Files

- `SKILL.md`: executable workflow.
- `README.md`: human-facing summary.
- `AGENTS.md`: maintenance and adaptation rules.

## Adaptation Summary

Replace placeholders with local source paths, authority sources, renderer
commands, include roots, style guides, validation commands, derivative-output
paths, and publication rules. Keep PlantUML source canonical and document any
target-project assumptions about Java, Graphviz, PlantUML version, C4 support,
security policy, manifests, or visual QA.

## Validation Summary

Confirm the skill defines use conditions, inputs, outputs, output contract,
procedure, diagram-family selection, include policy, styling guidance, rendering
guidance, validation, failure modes, provenance, and adaptation guidance. For
project use, validate PlantUML syntax, include safety, family fit, source
coverage, rendered output, and derivative parity.
