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

# AGENTS.md

## Local Mission

Maintain `conversation-to-prd` as a portable PRD synthesis template grounded in
conversation context and repository evidence.

## Maintenance Rules

- Do not require a fresh interview when available context is sufficient.
- Ask only for blocking ambiguity.
- Keep external tracker behavior opt-in and explicitly configured.
- Preserve upstream MIT attribution when deriving from this template.

## Portability Requirements

The template must not assume one PRD directory, issue tracker, label vocabulary,
framework, or product domain.

## Validation Requirements

Before finalizing changes, verify that `SKILL.md`, `README.md`, and
`AGENTS.md` exist and that the skill explains use conditions, inputs, outputs,
procedure, validation, failure modes, provenance, adaptation guidance, and
third-party attribution.

## Adaptation Instructions

When adapting this skill, define local PRD location, product vocabulary,
authority/provenance requirements, tracker behavior, and validation checks.
