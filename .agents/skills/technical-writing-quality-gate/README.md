# Technical Writing Quality Gate - sys-for-ai-dev Runtime Adaptation

Canonical skill ID: `technical-writing-quality-gate`  
Canonical runtime path: `.agents/skills/technical-writing-quality-gate`  
Compatibility shim path: `.codex/skills/technical-writing-quality-gate/SKILL.md`  
Source import: `skills/technical-writing-quality-gate` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# technical-writing-quality-gate

## Purpose

Reusable workflow for drafting, revising, and evaluating source-grounded
technical or system prose with a `pass`, `repair`, or `block` quality gate.

## When To Use

Use this skill when a project needs claim-bearing prose to be specific,
audience-fit, and proportional to supplied source evidence. It is useful for
system descriptions, architecture summaries, release notes, research summaries,
project pages, operational documentation, and generated copy that must avoid
generic unsupported claims.

## What It Produces

- Revised or newly drafted prose when source evidence is sufficient.
- A `pass`, `repair`, or `block` gate result.
- Source-grounding notes and unsupported-claim findings.
- Validation notes and skipped-check explanations.
- Optional warning-pattern report from the bundled script.

## Required Files

- `SKILL.md`: executable workflow.
- `README.md`: human-facing summary.
- `AGENTS.md`: maintenance and adaptation rules.

## Support Files

- `references/system-writing-quality.md`: review checklist for substantial or
  public-facing technical prose.
- `scripts/technical_writing_warning_gate.py`: optional standard-library proxy
  checker for generic warning patterns.
- `examples/portable-example.md`: neutral example showing a repair gate.

## Adaptation Summary

Replace placeholders with local source authorities, document paths, validation
commands, style expectations, citation rules, output directories, and domain
constraints. Add domain-specific warning patterns only when they are supported
by local evidence and do not turn ordinary precise terms into banned words.

## Validation Summary

Confirm the skill defines use conditions, inputs, outputs, authority
boundaries, procedure, validation, failure modes, provenance, and adaptation
guidance. For project use, verify source support for claims, run the optional
warning-pattern checker when useful, and run `<VALIDATION_COMMAND>` when the
target project defines one.
