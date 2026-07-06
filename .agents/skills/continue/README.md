# Continue Skill

Canonical skill ID: `continue`

Canonical runtime path: `.agents/skills/continue`

Compatibility shim path: `.codex/skills/continue/SKILL.md`

## Purpose

Resume `sys-for-ai-dev` from tracked state and advance at most one authorized AgentJob.

## Runtime Boundary

- `.agents/skills/continue/SKILL.md` is the active development-runtime skill.
- `.codex/skills/continue/SKILL.md` is compatibility-only.
- `sys-for-ai/skills/core/continue/` is a portable product-scaffold template.

The skill never uses generated docs, local caches, summaries, or chat memory as authority.
