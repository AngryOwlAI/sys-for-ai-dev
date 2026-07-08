# Continue Skill

Canonical skill ID: `continue`

Canonical runtime path: `.agents/skills/continue`

Compatibility shim path: `.codex/skills/continue/SKILL.md`

## Purpose

Resume `Sys4AI-dev` from tracked state and advance at most one authorized AgentJob.

## Runtime Boundary

- `.agents/skills/continue/SKILL.md` is the active development-runtime skill.
- `.codex/skills/continue/SKILL.md` is compatibility-only.
- `Sys4AI/skills/core/continue/` is a portable product-scaffold template.

The skill never uses generated docs, local caches, summaries, or chat memory as authority.

## Compatibility Note

Existing Director Decision Records remain valid historical routing evidence.
Future continuation work should prefer neutral tracked authorization language
unless a later migration explicitly renames the broader governance surface.
