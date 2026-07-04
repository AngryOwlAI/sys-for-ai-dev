---
name: codex-usage-metrics
description: Capture Codex context, token, and rate-limit metrics into a refreshed local receipt without exporting conversation content.
adaptation_status: adapter_shell
source_repo: https://github.com/AngryOwlAI/ai-skills-for-sys
source_path: skills/codex-usage-metrics
---

# Codex Usage Metrics

## Purpose

Capture Codex context, token, and rate-limit metrics into a refreshed local receipt without exporting conversation content.

## When to use

Use this skill when a `sys-for-ai` AgentJob requires the `runtime_session_accounting` capability and the governing PRD or implementation plan authorizes skill use.

## Inputs

- Current AgentJob.
- Relevant canonical sources.
- Applicable registries.
- Any local validator commands named by the AgentJob.

## Outputs

- A bounded result appropriate to the skill family.
- Source and provenance notes.
- Validation notes or a pass/repair/block decision when applicable.
- Handoff or completion evidence when the AgentJob requires it.

## Procedure

1. Confirm the AgentJob authorizes this skill.
2. Read canonical sources before generated derivatives.
3. Apply the upstream skill procedure after local adaptation is completed.
4. Preserve source provenance and document assumptions.
5. Run or name validators before completion.

## Local authority boundaries

- This adapter does not override PRDs, source registries, decision records, or validators.
- Generated notes are derivative unless promoted through source authority.
- Upstream skill text must be reviewed before this adapter is marked `adapted`.

## Validation

Run:

```bash
cd sys-for-ai && make validate-skills
```

## Known failure modes

- Using the skill without an authorized AgentJob.
- Treating upstream placeholders as local facts.
- Producing output that is not traceable to canonical sources.
- Marking the adapter as fully adapted before local review.
