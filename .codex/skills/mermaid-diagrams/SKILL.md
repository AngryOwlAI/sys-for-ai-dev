# Mermaid Diagrams Codex Compatibility Shim

Canonical skill ID: `mermaid-diagrams`

Canonical path: `.agents/skills/mermaid-diagrams`

Purpose: This file exists only so Codex skill discovery can find the sys-for-ai-dev runtime skill. The canonical runtime skill, manifest, examples, templates, references, and scripts live under `.agents/skills/mermaid-diagrams/`.

Direct-edit warning: do not maintain behavior here. Edit `.agents/skills/mermaid-diagrams/SKILL.md` and `.agents/skills/mermaid-diagrams/skill.yaml`, then keep this shim as a pointer.

Validation command:

```bash
python3 scripts/skills/validate_skill_manifest.py --manifest .agents/skills/mermaid-diagrams/skill.yaml
```

When this shim is triggered, load and follow `.agents/skills/mermaid-diagrams/SKILL.md` as the authoritative project-fit skill instructions. Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs. `sys-for-ai/` is the product scaffold, not the full development workspace.
