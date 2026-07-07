# Domain Grilling With Docs - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `domain-grilling-with-docs`  
Canonical runtime path: `.agents/skills/domain-grilling-with-docs`  
Compatibility shim path: `.codex/skills/domain-grilling-with-docs/SKILL.md`  
Source import: `skills/domain-grilling-with-docs` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

---
name: domain-grilling-with-docs
description: Stress-test a plan against project language and update glossary or ADR documentation as decisions settle.
---

# domain-grilling-with-docs

## Purpose

Provide a reusable workflow for clarifying domain terminology, surfacing contradictions between plans and code, and recording stable glossary or architecture decisions.

## When To Use

- The user wants a grilling session grounded in existing docs or domain language.
- Terms are overloaded, fuzzy, or inconsistent with the project glossary.
- A decision may warrant an ADR because it is hard to reverse, surprising, and tradeoff-heavy.

## Inputs

- The plan or design under review.
- <CONTEXT_FILE> or <CONTEXT_MAP> when present.
- <ADR_DIRECTORY> when present.
- `templates/context-format.md` and `templates/adr-format.md` from this skill
  package, unless the target project provides a local replacement.
- Repository code and tests for evidence checks.

## Outputs

- Sequential questions with recommendations.
- Updated glossary/context entries when terms are resolved.
- Optional ADRs for qualifying decisions.

## Procedure

1. Discover whether the repository uses one context file or a context map with multiple bounded contexts.
2. Use `templates/context-format.md` as the default glossary format unless the
   target project has already defined a local format.
3. Use `templates/adr-format.md` as the default ADR format unless the target
   project has already defined a local format.
4. Create glossary or ADR files lazily only when there is settled content to record.
5. When the user uses a conflicting term, surface the conflict immediately.
6. Use concrete scenarios and code inspection to test boundaries between concepts.
7. Update <CONTEXT_FILE> inline when a term is resolved, keeping it free of implementation details.
8. Offer an ADR only when the decision is hard to reverse, surprising without context, and based on a real tradeoff.

## Validation

- Glossary entries define domain language, not implementation details.
- ADRs are used sparingly and explain the tradeoff.
- Code contradictions are reported with evidence.
- Questions remain one at a time.

## Failure Modes

- Turning the glossary into a spec or scratchpad.
- Creating ADRs for obvious or reversible choices.
- Accepting user terminology that contradicts existing project language without resolving it.

## Provenance

Derived from a project-specific skill and generalized as a reusable template. Original project-specific names, paths, assumptions, and private operational details were removed or replaced with parameters.

## Adaptation Guide

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when they are required.
- Preserve the reusable procedure unless local evidence shows a better structure.
- Document any project-specific assumptions introduced during adaptation.
