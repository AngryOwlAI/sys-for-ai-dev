# Technical Writing Quality Gate - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `technical-writing-quality-gate`  
Canonical runtime path: `development/bootstrap-agent/skills/technical-writing-quality-gate`
Compatibility shim path: `.codex/skills/technical-writing-quality-gate/SKILL.md`  
Source import: `skills/technical-writing-quality-gate` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

Maintain `technical-writing-quality-gate` as a portable template for
source-grounded technical prose review and repair.

## Maintenance Rules

- Preserve the distinction between source fact, inference, review signal, and
  validated claim.
- Keep the `pass`, `repair`, and `block` gate explicit.
- Keep style guidance tied to source grounding and reader understanding, not to
  cosmetic polish alone.
- Do not add project-specific repository names, absolute paths, dataset names,
  calibration values, model claims, private terminology, or validation commands
  unless they are placeholders or clearly marked adaptation examples.
- Treat warning-pattern checks as proxy evidence. They must not be described as
  proof of factual correctness, source coverage, originality, or human
  authorship.
- Keep scripts standard-library only unless a dependency is necessary,
  documented, and portable.

## Portability Requirements

The template must not assume a repository layout, publication system, package
manager, corpus, machine-learning model, writing benchmark, CI provider, or
domain authority. Add those details only during target-project adaptation.

## Validation Requirements

Before finalizing changes, verify that `SKILL.md`, `README.md`, and `AGENTS.md`
exist and that the skill explains use conditions, inputs, outputs, authority
boundaries, procedure, validation, failure modes, provenance, and adaptation
guidance.

When the script changes, run:

```sh
python3 scripts/technical_writing_warning_gate.py --help
```

When examples or references change, verify they avoid source-project names,
absolute paths, private terminology, and unmarked project assumptions.

## Adaptation Instructions

When adapting this skill, add the target project's source authority, target
document paths, citation standard, publication surface, style constraints,
domain-specific warning patterns, validation commands, and completion receipt
requirements.
