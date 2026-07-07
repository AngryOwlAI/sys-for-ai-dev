# Skill Import Generalizer - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `skill-import-generalizer`  
Canonical runtime path: `.agents/skills/skill-import-generalizer`  
Compatibility shim path: `.codex/skills/skill-import-generalizer/SKILL.md`  
Source import: `.codex/skills/skill-import-generalizer` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# AGENTS.md

## Local Mission

Maintain `skill-import-generalizer` as the repository's standard import protocol for converting project-specific skills into reusable templates.

## Required Files

This skill folder must contain:

- `SKILL.md`: executable import-generalization workflow.
- `README.md`: human-facing overview and usage notes.
- `AGENTS.md`: local maintenance rules.

## Maintenance Rules

- Preserve the fixed workflow sequence unless a better sequence is justified by repository evidence.
- Keep the skill project-agnostic.
- Do not add hard-coded source project paths, branch names, issue IDs, private URLs, or local-only commands.
- Use placeholders for values that must be supplied by a target project.
- Keep provenance neutral and non-sensitive.

## Validation Rules

When editing this skill, verify:

- The workflow still requires `SKILL.md`, `README.md`, and `AGENTS.md` for every generalized skill folder.
- The adaptation guide remains present.
- The sensitivity and portability checks remain explicit.
- The skill can be understood without access to any source project.

## Adaptation Rules

When adapting this skill inside a specific project:

- Replace placeholders with local paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when required.
- Document any assumptions introduced during adaptation.

