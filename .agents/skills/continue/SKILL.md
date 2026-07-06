---
name: continue
description: Resume sys-for-ai-dev from tracked state and advance at most one authorized AgentJob.
---

# /continue

Use this skill when the operator asks to continue work from tracked state.

## Authority

Tracked project state decides the route. Chat context, generated derivatives, local caches, and summaries are navigation aids only.

## Rules

1. Read the self-hosting boundary decision record.
2. Run memory preflight.
3. Inspect canonical sources or registry rows named by useful memory hits.
4. Resolve `sys-for-ai/control_records/program_state.yaml`.
5. Inspect the latest handoff if one exists.
6. Select or reuse at most one AgentJob.
7. Stop if a Director decision is required.
8. Execute only the selected AgentJob.
9. Write a completion receipt and handoff when state changes.
10. Validate before reporting completion.
11. Do not treat generated docs, local caches, summaries, or chat memory as authority.

## Required Closeout

After completing one bounded task, write the next `temp_handoff/handoff-*.md`, commit the completed task, respond with the commit and validation evidence, and stop.
