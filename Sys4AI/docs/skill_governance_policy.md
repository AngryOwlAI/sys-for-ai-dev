# Skill Governance Policy

**Status:** Draft  
**Scope:** Core `Sys4AI` skills and adapter shells

---

## Skill status values

| Status | Meaning |
|---|---|
| `adapter_shell` | Local wrapper exists, exact upstream content not fully adapted yet. |
| `imported_unadapted` | Upstream content copied but not locally reviewed. |
| `adapted` | Upstream concept has been locally adapted with validators and authority boundaries. |
| `deprecated` | Skill is no longer active for the project. |

---

## Required files

Every local skill adapter shall include:

- `SKILL.md`
- `README.md`
- `AGENTS.md`
- `examples/portable-example.md`

---

## Authority boundaries

Skills provide procedures. They do not automatically override PRDs, source registries, decision records, or validators.

When skill output conflicts with source authority, the source-authority policy wins and the conflict must be recorded.

---

## Import rule

Upstream templates from `ai-skills-for-sys` must be reviewed and adapted before being marked `adapted`.
