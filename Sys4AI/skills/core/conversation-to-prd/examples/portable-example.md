# Portable example for `conversation-to-prd`

## Scenario

A `Sys4AI` implementation agent receives an ExecutionTransaction requiring `requirements_production` support.

## Minimal use

1. Read the ExecutionTransaction objective and allowed files.
2. Read canonical sources before generated notes.
3. Apply the `conversation-to-prd` adapter procedure.
4. Produce bounded output with provenance notes.
5. Run the named validator or record why it could not be run.

## Example output shape

```text
Skill: conversation-to-prd
Status: pass | repair | block
Sources used:
- <source path or source ID>
Output:
- <bounded result>
Validation:
- <command or reasoning>
```
