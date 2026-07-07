# Domain Grilling With Docs Codex Compatibility Shim

Canonical skill ID: `domain-grilling-with-docs`

Canonical path: `.agents/skills/domain-grilling-with-docs`

Purpose: This file exists only so Codex skill discovery can find the Sys4AI-dev runtime skill. The canonical runtime skill, manifest, examples, templates, references, and scripts live under `.agents/skills/domain-grilling-with-docs/`.

Direct-edit warning: do not maintain behavior here. Edit `.agents/skills/domain-grilling-with-docs/SKILL.md` and `.agents/skills/domain-grilling-with-docs/skill.yaml`, then keep this shim as a pointer.

Validation command:

```bash
python3 scripts/skills/validate_skill_manifest.py --manifest .agents/skills/domain-grilling-with-docs/skill.yaml
```

When this shim is triggered, load and follow `.agents/skills/domain-grilling-with-docs/SKILL.md` as the authoritative project-fit skill instructions. Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs. `Sys4AI/` is the product scaffold, not the full development workspace.
