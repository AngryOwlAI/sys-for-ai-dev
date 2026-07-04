# Portable example for `skill-import-generalizer`

## Scenario

A `sys-for-ai` implementation agent receives an AgentJob requiring `skill_library_maintenance` support.

## Minimal use

1. Read the AgentJob objective and allowed files.
2. Read canonical sources before generated notes.
3. Apply the `skill-import-generalizer` adapter procedure.
4. Produce bounded output with provenance notes.
5. Run the named validator or record why it could not be run.

## Example output shape

```text
Skill: skill-import-generalizer
Status: pass | repair | block
Sources used:
- <source path or source ID>
Output:
- <bounded result>
Validation:
- <command or reasoning>
```
