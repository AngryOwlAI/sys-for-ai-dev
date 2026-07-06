# Decision Grilling - sys-for-ai-dev Runtime Adaptation

Canonical skill ID: `decision-grilling`  
Canonical runtime path: `.agents/skills/decision-grilling`  
Compatibility shim path: `.codex/skills/decision-grilling/SKILL.md`  
Source import: `skills/decision-grilling` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# decision-grilling

## Purpose

Provide a reusable Socratic design-review workflow that resolves dependencies between decisions while offering a recommended answer at each step.

## When To Use

- The user asks to be grilled, challenged, or stress-tested on a plan.
- A design tree has unresolved branches or hidden assumptions.
- A decision can be clarified by either asking the user or inspecting the codebase.

## What This Skill Produces

- One question at a time.
- A recommended answer for each question.
- A progressively clarified decision tree.

## Required Files

This stored template package contains:

- `SKILL.md`: executable agent instructions.
- `README.md`: human-facing summary and adaptation notes.
- `AGENTS.md`: local maintenance rules for this template.

Target projects may add `templates/`, `scripts/`, `examples/`, or reference material when adapting the skill.

## Adaptation Summary

Replace placeholders such as `<PROJECT_ROOT>`, `<VALIDATION_COMMAND>`, `<OUTPUT_DIRECTORY>`, and any domain-specific registry, role, source, or tool names before installing this template into a project.

Preserve the reusable workflow, but add project-specific authority boundaries, commands, and stop conditions only when local evidence requires them.

## Validation Summary

A valid adaptation should satisfy these checks:

- Questions are sequential, not a questionnaire dump.
- Each question maps to a real dependency or risk.
- Recommendations are grounded in evidence or clearly marked assumptions.
