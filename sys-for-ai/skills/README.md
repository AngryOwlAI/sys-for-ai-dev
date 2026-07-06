# Core skills

This directory holds the Phase 1 core skill manifest and adapter shells for `sys-for-ai`.
The active development-system runtime skills for this repository live at the
workspace root under `.agents/skills/`.

The current policy is simple:

1. Every retained template from `ai-skills-for-sys/skills` is a core product-reference requirement.
2. The `.codex/skills/skill-import-generalizer` workflow is also a core skill-management requirement.
3. Phase 1 includes product scaffold adapter shells and provenance records.
4. Root `.agents/skills` is the canonical runtime surface for `sys-for-ai-dev`.
5. Exact upstream synchronization and local adaptation happen through a later explicit AgentJob unless root project authority supersedes this scaffold.

Run:

```bash
make validate-skills
```
