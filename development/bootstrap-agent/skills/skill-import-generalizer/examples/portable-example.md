# Portable example for `skill-import-generalizer`

## Scenario

A `Sys4AI-dev` implementation agent receives a task to import a skill from
another local repository into the root development-system runtime layer.

## Minimal use

1. Read the task objective and allowed files.
2. Read root PRDs, implementation plans, source registries, validators, and
   git-tracked project files before generated notes.
3. Treat `Sys4AI/` as the product scaffold, not the full development
   workspace.
4. Adapt the source skill into `development/bootstrap-agent/skills/<skill-id>/`.
5. Add a thin `.codex/skills/<skill-id>/SKILL.md` compatibility shim.
6. Run the root skill validator and record any skipped checks.

## Example output shape

```text
Skill: skill-import-generalizer
Status: pass | repair | block
Canonical runtime path:
- development/bootstrap-agent/skills/<skill-id>
Compatibility shim:
- .codex/skills/<skill-id>/SKILL.md
Sources used:
- <source path or source ID>
Validation:
- python3 development/tools/validate_skill_catalog.py --root .
```
