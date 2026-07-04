# Core skills

This directory holds the Phase 1 core skill manifest and adapter shells for `sys-for-ai`.

The current policy is simple:

1. Every retained template from `ai-skills-for-sys/skills` is a core requirement.
2. The `.codex/skills/skill-import-generalizer` workflow is also a core skill-management requirement.
3. Phase 1 includes adapter shells and provenance records.
4. Exact upstream synchronization and local adaptation happen through a later explicit AgentJob.

Run:

```bash
make validate-skills
```
