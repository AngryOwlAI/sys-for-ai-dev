# Decision Grilling Context 45 Codex Compatibility Shim

Canonical skill ID: `decision-grilling-context-45`

Canonical path: `.agents/skills/decision-grilling-context-45`

Purpose: This file exists only so Codex skill discovery can find the sys-for-ai-dev runtime skill. The canonical runtime skill, manifest, examples, templates, references, and scripts live under `.agents/skills/decision-grilling-context-45/`.

Direct-edit warning: do not maintain behavior here. Edit `.agents/skills/decision-grilling-context-45/SKILL.md` and `.agents/skills/decision-grilling-context-45/skill.yaml`, then keep this shim as a pointer.

Validation command:

```bash
python3 scripts/skills/validate_skill_manifest.py --manifest .agents/skills/decision-grilling-context-45/skill.yaml
```

When this shim is triggered, load and follow `.agents/skills/decision-grilling-context-45/SKILL.md` as the authoritative project-fit skill instructions. Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs. `sys-for-ai/` is the product scaffold, not the full development workspace.
