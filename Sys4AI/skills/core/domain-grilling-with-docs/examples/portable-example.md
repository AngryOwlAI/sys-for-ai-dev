# Portable example for `domain-grilling-with-docs`

## Scenario

A `Sys4AI` implementation agent receives an ExecutionTransaction requiring `domain_documentation_clarification` support.

## Minimal use

1. Read the ExecutionTransaction objective and allowed files.
2. Read canonical sources before generated notes.
3. Apply the `domain-grilling-with-docs` adapter procedure.
4. Produce bounded output with provenance notes.
5. Run the named validator or record why it could not be run.

## Example output shape

```text
Skill: domain-grilling-with-docs
Status: pass | repair | block
Sources used:
- <source path or source ID>
Output:
- <bounded result>
Validation:
- <command or reasoning>
```
