# Mermaid Diagrams - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `mermaid-diagrams`  
Canonical runtime path: `development/bootstrap-agent/skills/mermaid-diagrams`
Compatibility shim path: `.codex/skills/mermaid-diagrams/SKILL.md`  
Source import: `skills/mermaid-diagrams` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

Maintain `mermaid-diagrams` as a portable template for source-grounded Mermaid
diagram work.

## Maintenance Rules

- Keep Mermaid source canonical and rendered assets derivative.
- Preserve the distinction between diagram explanation and source authority.
- Preserve visual grammar guidance: shapes, borders, arrows, labels, groups,
  and colors should carry explicit meaning.
- Avoid project-specific palettes, file paths, registry names, renderer
  versions, or validation commands unless expressed as placeholders.
- Do not add renderer scripts unless they are genuinely portable and documented
  with setup, dependencies, and security limits.

## Portability Requirements

The template must not assume a repository layout, documentation generator,
package manager, Mermaid version, browser runtime, renderer, manifest format,
or publication surface. Add those details only during target-project
adaptation.

## Validation Requirements

Before finalizing changes, verify that `SKILL.md`, `README.md`, and
`AGENTS.md` exist and that the skill explains use conditions, inputs, outputs,
procedure, validation, failure modes, provenance, and adaptation guidance.

When examples are changed, verify they avoid source-project names, absolute
paths, private terminology, and unmarked project assumptions.

## Adaptation Instructions

When adapting this skill, add the target project's diagram source locations,
style guide, renderer command, validator command, runtime policy, derivative
output format, accessibility standard, and authority boundary.
