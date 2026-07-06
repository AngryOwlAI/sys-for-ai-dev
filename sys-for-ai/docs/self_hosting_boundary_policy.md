# Self-Hosting Boundary Policy

**Status:** Draft  
**Scope:** `sys-for-ai-dev` dogfooding `sys-for-ai` Phase 1 control-loop concepts

---

## Policy

`sys-for-ai-dev` is allowed to use `sys-for-ai` concepts while building `sys-for-ai`, provided every operational record keeps these roles distinct:

- Framework system: `sys-for-ai`
- Development system: `sys-for-ai-dev`
- Target system: the system currently being changed

For this implementation, the target system is also `sys-for-ai`, so `self_hosting_mode` is true and `reflection_depth` is 1.

## Boundary rules

1. PRDs define product requirements.
2. `sys-for-ai/` is the product scaffold.
3. `.agents/skills/` is the active development runtime skill surface.
4. `.codex/skills/` is a compatibility surface.
5. `sys-for-ai/docs/generated/` is a generated reader surface.
6. `sys-for-ai/.local/` is local retrieval or receipt support.

## Anti-rules

- Do not treat a generated page as canonical by convenience.
- Do not let a local cache or chat summary authorize a code change.
- Do not collapse active development skills into product scaffold skills.
- Do not run multiple AgentJobs through one `/continue` invocation.
