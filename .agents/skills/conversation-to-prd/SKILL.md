# Conversation To Prd - sys-for-ai-dev Runtime Adaptation

Canonical skill ID: `conversation-to-prd`  
Canonical runtime path: `.agents/skills/conversation-to-prd`  
Compatibility shim path: `.codex/skills/conversation-to-prd/SKILL.md`  
Source import: `skills/conversation-to-prd` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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
name: conversation-to-prd
description: Synthesize conversation context and repository evidence into a local product requirements document without a fresh interview unless a blocking ambiguity remains.
---

# conversation-to-prd

## Purpose

Turn the current conversation, repository evidence, and known constraints into a
local product requirements document.

Do not interview the user by default. Use what has already been discussed, then
ask only when a missing answer would make the PRD materially wrong.

## When To Use

- The user asks to turn the current conversation into a PRD.
- A feature, workflow, design, or implementation direction has enough context
  to document product requirements.
- The project needs a local planning artifact before implementation.

Do not publish to an external issue tracker unless that tracker and label
vocabulary are explicitly configured or the user asks for it.

## Inputs

- Current conversation context.
- <PROJECT_ROOT> and relevant repository evidence.
- <OUTPUT_DIRECTORY> for local PRDs.
- Optional target filename or feature slug.
- Optional external tracker configuration.

## Outputs

- Local PRD Markdown file or chat PRD.
- Problem statement, solution, user stories, implementation decisions, testing
  decisions, authority/provenance notes, out-of-scope items, and further notes.
- Open questions only when they are material.

## Procedure

1. Explore the repository enough to understand current state, existing
   vocabulary, relevant architecture, and constraints.
2. Identify the highest useful implementation and testing boundary. Prefer
   existing routes, modules, scripts, validators, quality gates, APIs, schemas,
   or components.
3. Add new boundaries only when needed and keep their count low.
4. If the boundary is uncertain and the user is present, ask one concise
   question before writing.
5. Write the PRD using the template below.
6. Save it under <OUTPUT_DIRECTORY>/<short-slug>.md unless the user provides
   another local path.
7. Publish externally only when explicitly configured or requested.

## PRD Template

```md
# <Feature Name> PRD

## Problem Statement

The problem from the user's perspective.

## Solution

The solution from the user's perspective.

## User Stories

1. As an <actor>, I want <feature>, so that <benefit>.

## Implementation Decisions

- Modules, surfaces, or boundaries to build or modify.
- Interfaces or content boundaries that need to change.
- Technical clarifications from the conversation.
- Architectural decisions.
- Schema, manifest, route, API, or data contracts.
- Specific interactions.

## Testing Decisions

- External behavior that matters.
- Routes, scripts, validators, or quality gates to test.
- Prior art for similar tests.
- What should not be tested because it is implementation detail.

## Authority And Provenance

- Source materials the feature depends on.
- Claim-status or source-authority requirements.
- Reader-facing notices or provenance links required.

## Out Of Scope

Things this PRD deliberately does not include.

## Further Notes

Additional context, risks, or follow-up questions.
```

## Validation

- The PRD reflects conversation context and repository evidence.
- Assumptions are marked rather than presented as facts.
- The implementation boundary is useful but not over-prescriptive.
- Testing decisions name observable behavior and discovered project checks.
- External tracker publication is not invented.

## Failure Modes

- Restarting the interview despite enough context.
- Embedding brittle file paths or code snippets without need.
- Over-specifying implementation before repository evidence supports it.
- Publishing to an unconfigured external tracker.
- Hiding blocking ambiguity.

## Provenance

Derived from a project-specific skill and generalized as a reusable template.
Original project-specific names, paths, assumptions, and private operational
details were removed or replaced with parameters.

This template also preserves the reusable conversation-to-PRD pattern from an
MIT-licensed upstream skill concept: Pocock, M. (2026). *to-prd* [AI skill].
GitHub. https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd

## Adaptation Guide

When adapting this skill to a specific project:

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when they are required.
- Preserve the reusable procedure unless local evidence shows a better
  structure.
- Document any project-specific assumptions introduced during adaptation.
