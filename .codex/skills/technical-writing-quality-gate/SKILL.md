# Technical Writing Quality Gate Codex Compatibility Shim

Canonical skill ID: `technical-writing-quality-gate`

Canonical path: `.agents/skills/technical-writing-quality-gate`

Purpose: This file exists only so Codex skill discovery can find the sys-for-ai-dev runtime skill. The canonical runtime skill, manifest, examples, templates, references, and scripts live under `.agents/skills/technical-writing-quality-gate/`.

Direct-edit warning: do not maintain behavior here. Edit `.agents/skills/technical-writing-quality-gate/SKILL.md` and `.agents/skills/technical-writing-quality-gate/skill.yaml`, then keep this shim as a pointer.

Validation command:

```bash
python3 scripts/skills/validate_skill_manifest.py --manifest .agents/skills/technical-writing-quality-gate/skill.yaml
```

When this shim is triggered, load and follow `.agents/skills/technical-writing-quality-gate/SKILL.md` as the authoritative project-fit skill instructions. Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs. `sys-for-ai/` is the product scaffold, not the full development workspace.
