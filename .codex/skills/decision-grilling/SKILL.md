# Decision Grilling Codex Compatibility Shim

Canonical skill ID: `decision-grilling`

Canonical path: `.agents/skills/decision-grilling`

Purpose: This file exists only so Codex skill discovery can find the Sys4AI-dev runtime skill. The canonical runtime skill, manifest, examples, templates, references, and scripts live under `.agents/skills/decision-grilling/`.

Direct-edit warning: do not maintain behavior here. Edit `.agents/skills/decision-grilling/SKILL.md` and `.agents/skills/decision-grilling/skill.yaml`, then keep this shim as a pointer.

Validation command:

```bash
python3 scripts/skills/validate_skill_manifest.py --manifest .agents/skills/decision-grilling/skill.yaml
```

When this shim is triggered, load and follow `.agents/skills/decision-grilling/SKILL.md` as the authoritative project-fit skill instructions. Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs. `Sys4AI/` is the product scaffold, not the full development workspace.
