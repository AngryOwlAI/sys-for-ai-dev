# Conversation To Prd - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `conversation-to-prd`  
Canonical runtime path: `.agents/skills/conversation-to-prd`  
Compatibility shim path: `.codex/skills/conversation-to-prd/SKILL.md`  
Source import: `skills/conversation-to-prd` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# conversation-to-prd

## Purpose

Reusable workflow for synthesizing conversation context and repository evidence
into a local product requirements document.

## When To Use

Use this skill when enough context already exists to write a PRD and only
blocking ambiguities should trigger fresh questions.

## What It Produces

- Local PRD Markdown file or chat PRD.
- Problem statement, solution, user stories, implementation decisions, testing
  decisions, authority/provenance notes, out-of-scope items, and further notes.

## Required Files

- `SKILL.md`: executable workflow.
- `README.md`: human-facing summary.
- `AGENTS.md`: maintenance and adaptation rules.

## Adaptation Summary

Replace <PROJECT_ROOT> and <OUTPUT_DIRECTORY>. Add local PRD naming, issue
tracker rules, authority requirements, and validation expectations.

## Validation Summary

Confirm the PRD reflects conversation and repository evidence, marks
assumptions, identifies useful implementation and testing boundaries, and does
not invent external tracker behavior.

## Third-Party Attribution

The reusable PRD synthesis pattern preserves concepts from an MIT-licensed
upstream skill: Pocock, M. (2026). *to-prd* [AI skill]. GitHub.
https://github.com/mattpocock/skills/tree/main/skills/engineering/to-prd
