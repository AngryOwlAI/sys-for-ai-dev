# Portable Example

## Scenario

A project needs a sequence diagram showing how a release dashboard checks
metrics, requests approval, records an audit event, and reports the outcome.

## Source Boundary

The diagram is based on a hypothetical architecture note. In a real adaptation,
replace this paragraph with the target project's source document, code path, or
authority record.

## Example Output

```plantuml
@startuml
title Release dashboard approval sequence

actor User
participant "Release Dashboard" as Dashboard
participant "Metrics Service" as Metrics
participant "Approval Service" as Approval
database "Audit Log" as Audit

User -> Dashboard: request release status
Dashboard -> Metrics: fetch readiness metrics
Metrics --> Dashboard: readiness summary

alt release is ready
  Dashboard -> Approval: request approval
  Approval --> Dashboard: approval granted
  Dashboard -> Audit: record approval
  Dashboard --> User: show release-ready state
else release is blocked
  Dashboard -> Audit: record blocking reason
  Dashboard --> User: show blocking reason
end
@enduml
```

## Validation Notes

- The document has one matching `@startuml` and `@enduml` pair.
- The sequence diagram preserves all named participants from the scenario.
- No remote includes are used.
- Rendering validation is project-specific; run `<VALIDATION_COMMAND>` after
  adapting the template.
