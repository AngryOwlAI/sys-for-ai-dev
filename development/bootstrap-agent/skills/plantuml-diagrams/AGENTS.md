# Plantuml Diagrams - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `plantuml-diagrams`  
Canonical runtime path: `development/bootstrap-agent/skills/plantuml-diagrams`
Compatibility shim path: `.codex/skills/plantuml-diagrams/SKILL.md`  
Source import: `skills/plantuml-diagrams` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

Maintain `plantuml-diagrams` as a portable template for source-grounded
PlantUML diagram work.

## Maintenance Rules

- Keep PlantUML source canonical and rendered assets derivative.
- Preserve the distinction between diagram explanation and source authority.
- Preserve diagram-family selection guidance for sequence, class, activity,
  state, use case, component, deployment, object, timing, mindmap, WBS, Gantt,
  and C4-style diagrams.
- Preserve conservative include handling. Remote includes, decorative icon
  packages, and third-party macros must be target-project adaptation points, not
  template defaults.
- Avoid project-specific palettes, file paths, renderer versions, vendored
  include roots, package names, validation commands, or private terminology
  unless expressed as placeholders.
- Do not add renderer scripts unless they are portable and documented with
  setup, dependencies, expected runtime, security limits, and validation scope.

## Portability Requirements

The template must not assume a repository layout, documentation generator,
package manager, operating system, Java distribution, PlantUML jar location,
Graphviz installation, C4 include path, manifest format, or publication surface.
Add those details only during target-project adaptation.

## Validation Requirements

Before finalizing changes, verify that `SKILL.md`, `README.md`, and `AGENTS.md`
exist and that the skill explains use conditions, inputs, outputs, procedure,
validation, failure modes, provenance, and adaptation guidance.

When examples are changed, verify they avoid source-project names, absolute
paths, private terminology, unapproved remote includes, and unmarked project
assumptions.

## Adaptation Instructions

When adapting this skill, add the target project's PlantUML source locations,
renderer command, Java and Graphviz expectations, include policy, C4 support,
style guide, validator command, derivative output format, accessibility
standard, manifest or source-hash policy, and authority boundary.
