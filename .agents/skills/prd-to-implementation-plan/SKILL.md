# Prd To Implementation Plan - sys-for-ai-dev Runtime Adaptation

Canonical skill ID: `prd-to-implementation-plan`  
Canonical runtime path: `.agents/skills/prd-to-implementation-plan`  
Compatibility shim path: `.codex/skills/prd-to-implementation-plan/SKILL.md`  
Source import: `skills/prd-to-implementation-plan` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

---
name: prd-to-implementation-plan
description: Convert a PRD, product spec, feature brief, or requirements document into a Codex-ready implementation plan and task packets.
---

# prd-to-implementation-plan

## Purpose

Transform product intent into an actionable engineering implementation plan that
Codex can execute in small, reviewable, validated tasks.

This skill produces a plan, not code, unless the user explicitly asks to
implement after planning. It maps requirements to repository context,
implementation phases, risks, validation commands, and task packets.

## When To Use

- The user asks for planning before coding.
- A PRD, product spec, issue, ticket, feature brief, RFC, or requirements
  document needs engineering breakdown.
- The output should include vertical slices, acceptance criteria, validation
  commands, or Codex-ready tasks.

Do not use this skill for direct implementation unless the user explicitly asks
to code after the plan.

## Inputs

- PRD path, pasted PRD, issue body, ticket text, selected text, or design
  document.
- Optional target output path.
- <PROJECT_ROOT> and repository instructions.
- Optional constraints: migration, deployment, compliance, accessibility,
  security, test level, release scope, or areas to avoid.

## Outputs

- Implementation plan.
- Requirement traceability matrix.
- Codex task packets with goal, context, constraints, implementation notes,
  acceptance criteria, validation, and done conditions.
- Assumptions, blockers, risks, and logical next prompt.

## Procedure

1. Locate and read the PRD or equivalent requirements input.
2. For long, vague, or multi-stakeholder inputs, use
   `templates/prd-intake-checklist.md` while extracting requirements.
3. Extract product goal, users, jobs to be done, functional requirements,
   non-functional requirements, acceptance criteria, user stories, primary
   flows, edge cases, error states, observability, rollout, migration needs,
   exclusions, and constraints.
4. Normalize vague requirements into testable statements where possible. Mark
   inferred behavior as an assumption.
5. Inspect repository context read-only: instructions, frameworks, package
   manifests, build systems, validation commands, existing patterns, related
   routes or services, schemas, migrations, fixtures, and tests.
6. Create stable requirement IDs such as `REQ-001` and `NFR-001` when the PRD
   lacks them.
7. Build a requirement map that identifies user-visible behavior, likely code
   areas, data or API impact, UI impact, test coverage, dependencies, and open
   questions.
8. Classify uncertainty as `Blocking`, `Planning assumption`, or
   `Implementation detail`.
9. Ask clarification only for blockers that prevent a credible plan. If
   progress is possible, proceed with assumptions.
10. Design the smallest maintainable implementation approach consistent with the
   repository.
11. Use `templates/implementation-plan-template.md` when writing a file or
    long-form chat plan.
12. Break the work into ordered task packets small enough for one branch or one
    draft PR where feasible.
13. Use `templates/codex-task-packet-template.md` when writing task packets.
14. Include executable validation commands only when discovered from the
    repository. If unknown, write `Discover and document the correct command
    before coding`.
15. Use `templates/review-checklist.md` to review the plan for traceability,
    task quality, validation coverage, risks, and separation between product
    questions and implementation decisions.

## Default Plan Shape

Include these sections when writing a file or long-form chat plan:

- Source PRD.
- Product summary.
- Repository context.
- Assumptions.
- Open questions.
- Requirement traceability matrix.
- Proposed technical approach.
- Implementation phases.
- Codex task packets.
- Validation plan.
- Security, privacy, and reliability notes.
- Rollout and rollback plan.
- Out of scope.
- Final review checklist.

Use `templates/implementation-plan-template.md` as the default structure unless
the target project provides a local replacement.

## Validation

- Every PRD requirement is mapped to a task or explicitly deferred.
- Every task has acceptance criteria and validation guidance.
- Risky changes have review, rollout, or rollback notes.
- Validation commands are discovered from the repository or explicitly marked
  unknown.
- The plan avoids direct coding unless implementation was requested.

## Failure Modes

- Summarizing the PRD instead of mapping it to executable work.
- Inventing repository commands or implementation details.
- Planning broad rewrites without evidence.
- Hiding product blockers as implementation assumptions.
- Creating tasks too large for review.

## Provenance

Derived from a project-specific skill and generalized as a reusable template.
Original project-specific names, paths, assumptions, and private operational
details were removed or replaced with parameters.

## Adaptation Guide

When adapting this skill to a specific project:

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when they are required.
- Preserve the reusable procedure unless local evidence shows a better
  structure.
- Document any project-specific assumptions introduced during adaptation.
