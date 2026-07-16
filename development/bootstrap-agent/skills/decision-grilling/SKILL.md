# Decision Grilling - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `decision-grilling`
Canonical runtime path: `development/bootstrap-agent/skills/decision-grilling`
Compatibility shim path: `.codex/skills/decision-grilling/SKILL.md`
Source import: `skills/decision-grilling` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

---
name: decision-grilling
description: Interview the user one question at a time to stress-test a plan or design until decisions are explicit.
---

# decision-grilling

## Purpose

Provide a reusable Socratic design-review workflow that resolves dependencies between decisions while offering a recommended answer at each step.

## When To Use

- The user asks to be grilled, challenged, or stress-tested on a plan.
- A design tree has unresolved branches or hidden assumptions.
- A decision can be clarified by either asking the user or inspecting the codebase.

## Inputs

- The plan, proposal, or design under review.
- Optional repository evidence, docs, or constraints.
- Any stated decision criteria or risk tolerance.

## Outputs

- One question at a time.
- A recommended answer for each question.
- A progressively clarified decision tree.

## Procedure

1. Identify the highest-leverage unresolved decision.
2. If repository inspection can answer it, inspect evidence instead of asking.
3. Ask exactly one focused question and include a recommended answer.
4. Wait for the user before moving to the next branch.
5. Track resolved decisions and revisit contradictions as they appear.
6. Stop when the plan is coherent enough to implement or the user ends the session.

## Validation

- Questions are sequential, not a questionnaire dump.
- Each question maps to a real dependency or risk.
- Recommendations are grounded in evidence or clearly marked assumptions.

## Failure Modes

- Asking broad multi-part questions that block progress.
- Ignoring codebase evidence that could answer the question.
- Letting the interview drift away from implementation-relevant decisions.

## Provenance

Derived from a project-specific skill and generalized as a reusable template. Original project-specific names, paths, assumptions, and private operational details were removed or replaced with parameters.

## Adaptation Guide

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when they are required.
- Preserve the reusable procedure unless local evidence shows a better structure.
- Document any project-specific assumptions introduced during adaptation.
