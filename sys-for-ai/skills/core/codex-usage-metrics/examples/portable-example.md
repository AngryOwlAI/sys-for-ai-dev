# Portable example for `codex-usage-metrics`

## Scenario

A `sys-for-ai` implementation agent receives an AgentJob requiring `runtime_session_accounting` support.

## Minimal use

1. Read the AgentJob objective and allowed files.
2. Read canonical sources before generated notes.
3. Apply the `codex-usage-metrics` adapter procedure.
4. Produce bounded output with provenance notes.
5. Run the named validator or record why it could not be run.

## Example output shape

```text
Skill: codex-usage-metrics
Status: pass | repair | block
Sources used:
- <source path or source ID>
Output:
- <bounded result>
Validation:
- <command or reasoning>
```
