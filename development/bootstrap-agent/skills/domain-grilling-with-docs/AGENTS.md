# Domain Grilling With Docs - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `domain-grilling-with-docs`  
Canonical runtime path: `development/bootstrap-agent/skills/domain-grilling-with-docs`
Compatibility shim path: `.codex/skills/domain-grilling-with-docs/SKILL.md`  
Source import: `skills/domain-grilling-with-docs` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# AGENTS.md

## Local Mission

Maintain `domain-grilling-with-docs` as a reusable template skill. It should define the portable capability without depending on the source project that inspired it.

## Maintenance Rules

- Keep `SKILL.md`, `README.md`, and `AGENTS.md` synchronized when the workflow changes.
- Keep template files under `templates/` portable and synchronized with the
  procedure in `SKILL.md`.
- Preserve placeholders for project-specific paths, commands, authorities, registries, tools, and output directories.
- Do not add secrets, private URLs, absolute local paths, branch names, task IDs, or organization-specific operational state.
- Add scripts, templates, or examples only when they are portable and documented.
- Keep instructions specific enough for a future agent to execute after adaptation.

## Portability Requirements

- Use parameters such as `<PROJECT_ROOT>`, `<VALIDATION_COMMAND>`, `<OUTPUT_DIRECTORY>`, and `<PROJECT_AUTHORITY>` for target-specific values.
- Explain any required external tool or API as an adaptation dependency.
- Keep generated artifacts non-authoritative unless the target project explicitly defines them as authority.

## Validation Requirements

Before finalizing changes to this template, check that:

- The skill can be understood without access to the source project.
- Required inputs and expected outputs are explicit.
- The validation and failure modes still match the procedure.
- No hard-coded local source paths or private project names remain.

## Adaptation Instructions

When adapting this template into a target project, replace placeholders, add project-specific commands, document new assumptions, and run the target project's own validation before relying on the adapted skill.
