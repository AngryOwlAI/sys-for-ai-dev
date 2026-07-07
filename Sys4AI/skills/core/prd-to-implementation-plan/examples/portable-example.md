# Portable example for `prd-to-implementation-plan`

## Scenario

A `Sys4AI` implementation agent receives an AgentJob requiring `implementation_planning` support.

## Minimal use

1. Read the AgentJob objective and allowed files.
2. Read canonical sources before generated notes.
3. Apply the `prd-to-implementation-plan` adapter procedure.
4. Produce bounded output with provenance notes.
5. Run the named validator or record why it could not be run.

## Example output shape

```text
Skill: prd-to-implementation-plan
Status: pass | repair | block
Sources used:
- <source path or source ID>
Output:
- <bounded result>
Validation:
- <command or reasoning>
```
