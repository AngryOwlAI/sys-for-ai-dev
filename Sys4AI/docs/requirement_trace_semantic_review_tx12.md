# TX-12 Requirement Trace Semantic Review

## Authority and scope

`TX-12-TRACE-DATA` migrated and reviewed every row in `registries/requirement_trace_registry.csv`. The accountable review role is `requirements_verifier`; the review date is `2026-07-10`. This report records review evidence and does not begin or satisfy `TX-13-VALIDATORS`.

All 214 rows remain active required Phase 0 framework obligations. Conditional behavior inside a requirement does not make the trace row an optional host profile. Coverage records mapping completeness and does not imply implementation, verification, or operational capability.

## Baseline and rollback evidence

- TX-11 legacy rows: 214.
- TX-11 legacy SHA-256: `95e59cf5befc4f9fd29d857d1f609a4c0d2c321c1b3adf1efca1a69cdb01b28c`.
- TX-12 generalized SHA-256: `b76dd57a8e5be11703213e57661690d7219e3a62eec9971fea633328e9003f97`.
- Compatibility fields reconstruct the exact TX-11 CSV bytes, header, row order, trace IDs, requirement IDs, evidence paths, justifications, verdicts, selectors, and notes.
- Rollback is atomic: restore the full legacy CSV together with the transaction packet; do not mix the v2 header with legacy rows or the legacy header with v2 rows.

## Review method

1. Preserve every stable trace ID, requirement ID, legacy field, selector, evidence path, and row order.
2. Set lifecycle to `active` and applicability to `required` because every row maps a current canonical Phase 0 obligation.
3. Preserve coverage independently from capability.
4. Retain legacy `implemented` as current `implemented` only when an exact non-generated implementation artifact is identifiable; otherwise demote it to `scaffolded` and record `needs_evidence`.
5. Retain truthful scaffolded classifications and classify deferred capability as `absent`.
6. Use `pass` only when an exact current test or strategic-baseline receipt is named; otherwise use reviewed state `planned`.
7. Treat resolved canonical sources as current mapping evidence. Existing paths alone do not prove an operational capability.
8. Treat every AgentJob, `/continue`, removed control-loop, and older self-hosting execution reference as historical compatibility evidence only.
9. Assign no `operational` status because the repository contains no deployment and current operational evidence meeting the v2 contract.

## State counts

| Dimension | Counts |
|---|---|
| `requirement_lifecycle` | `active`=214 |
| `applicability_status` | `required`=214 |
| `coverage_status` | `covered`=79, `partial`=135 |
| `capability_status` | `absent`=5, `implemented`=72, `scaffolded`=137 |
| `verification_status` | `pass`=14, `planned`=200 |
| `evidence_status` | `current`=214 |
| `semantic_review_verdict` | `needs_evidence`=7, `sufficient`=207 |

- Rows retaining retired-runtime compatibility evidence: 32.
- Rows claiming operational capability: 0.
- Rows left with provisional lifecycle, applicability, verification, evidence, or semantic-review state: 0.

## Explicit evidence gaps

The following seven legacy `implemented` rows had mapping evidence but no exact current implementation artifact. They are deliberately `scaffolded`, `planned`, and `needs_evidence` rather than being mechanically promoted:

- `TRACE-SFA-CORE-ID-001` / `SFA-CORE-ID-001`
- `TRACE-SFA-CORE-ID-002` / `SFA-CORE-ID-002`
- `TRACE-SFA-CORE-ID-003` / `SFA-CORE-ID-003`
- `TRACE-SFA-P0-FR-001` / `SFA-P0-FR-001`
- `TRACE-SFA-P0-FR-002` / `SFA-P0-FR-002`
- `TRACE-SFA-P0-FR-003` / `SFA-P0-FR-003`
- `TRACE-SFA-P0-FR-004` / `SFA-P0-FR-004`

## Row-by-row accountable review

Exact implementation artifacts, validation evidence, preserved source evidence, and compatibility fields are stored in the generalized trace row. Counts below make missing evidence explicit without duplicating path lists into a second authority surface.

| Trace ID | Requirement | Coverage | Capability | Verification | Verdict | Implementation paths | Validation paths | Legacy runtime evidence |
|---|---|---|---|---|---|---:|---:|---|
| `TRACE-SFA-CORE-ID-001` | `SFA-CORE-ID-001` | `covered` | `scaffolded` | `planned` | `needs_evidence` | 0 | 0 | no |
| `TRACE-SFA-CORE-ID-002` | `SFA-CORE-ID-002` | `covered` | `scaffolded` | `planned` | `needs_evidence` | 0 | 0 | no |
| `TRACE-SFA-CORE-ID-003` | `SFA-CORE-ID-003` | `covered` | `scaffolded` | `planned` | `needs_evidence` | 0 | 0 | no |
| `TRACE-SFA-CORE-ID-004` | `SFA-CORE-ID-004` | `partial` | `scaffolded` | `pass` | `sufficient` | 2 | 2 | no |
| `TRACE-SFA-CORE-ID-005` | `SFA-CORE-ID-005` | `partial` | `scaffolded` | `pass` | `sufficient` | 4 | 2 | no |
| `TRACE-SFA-CORE-ID-006` | `SFA-CORE-ID-006` | `partial` | `scaffolded` | `pass` | `sufficient` | 4 | 1 | no |
| `TRACE-SFA-CORE-ID-007` | `SFA-CORE-ID-007` | `partial` | `scaffolded` | `pass` | `sufficient` | 4 | 3 | no |
| `TRACE-SFA-CORE-VISION-001` | `SFA-CORE-VISION-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-VISION-002` | `SFA-CORE-VISION-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | no |
| `TRACE-SFA-CORE-VISION-003` | `SFA-CORE-VISION-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | no |
| `TRACE-SFA-CORE-VALUES-001` | `SFA-CORE-VALUES-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-VALUES-002` | `SFA-CORE-VALUES-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 3 | 0 | no |
| `TRACE-SFA-CORE-VALUES-003` | `SFA-CORE-VALUES-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | no |
| `TRACE-SFA-CORE-VALUES-004` | `SFA-CORE-VALUES-004` | `partial` | `scaffolded` | `pass` | `sufficient` | 6 | 2 | no |
| `TRACE-SFA-CORE-VALUES-005` | `SFA-CORE-VALUES-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 3 | 0 | no |
| `TRACE-SFA-P0-FR-001` | `SFA-P0-FR-001` | `covered` | `scaffolded` | `planned` | `needs_evidence` | 0 | 0 | no |
| `TRACE-SFA-P0-FR-002` | `SFA-P0-FR-002` | `covered` | `scaffolded` | `planned` | `needs_evidence` | 0 | 0 | no |
| `TRACE-SFA-P0-FR-003` | `SFA-P0-FR-003` | `covered` | `scaffolded` | `planned` | `needs_evidence` | 0 | 0 | no |
| `TRACE-SFA-P0-FR-004` | `SFA-P0-FR-004` | `covered` | `scaffolded` | `planned` | `needs_evidence` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-001` | `SFA-CORE-LIFE-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-002` | `SFA-CORE-LIFE-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-003` | `SFA-CORE-LIFE-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-004` | `SFA-CORE-LIFE-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-005` | `SFA-CORE-LIFE-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-006` | `SFA-CORE-LIFE-006` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-007` | `SFA-CORE-LIFE-007` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LIFE-008` | `SFA-CORE-LIFE-008` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-PATTERN-001` | `SFA-CORE-PATTERN-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-PATTERN-002` | `SFA-CORE-PATTERN-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-PATTERN-003` | `SFA-CORE-PATTERN-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-PATTERN-004` | `SFA-CORE-PATTERN-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-PATTERN-005` | `SFA-CORE-PATTERN-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-P0-FR-014` | `SFA-P0-FR-014` | `partial` | `absent` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-P0-FR-015` | `SFA-P0-FR-015` | `partial` | `absent` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-P0-NFR-007` | `SFA-P0-NFR-007` | `partial` | `absent` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-P0-NFR-008` | `SFA-P0-NFR-008` | `partial` | `absent` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-P0-NFR-012` | `SFA-P0-NFR-012` | `partial` | `absent` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-ART-001` | `SFA-CORE-ART-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | no |
| `TRACE-SFA-CORE-ROLE-001` | `SFA-CORE-ROLE-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | no |
| `TRACE-SFA-P0-FR-005` | `SFA-P0-FR-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | no |
| `TRACE-SFA-P0-FR-007` | `SFA-P0-FR-007` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | no |
| `TRACE-SFA-CORE-TRACE-001` | `SFA-CORE-TRACE-001` | `covered` | `implemented` | `pass` | `sufficient` | 4 | 2 | historical only |
| `TRACE-SFA-P0-FR-008` | `SFA-P0-FR-008` | `covered` | `implemented` | `pass` | `sufficient` | 3 | 2 | historical only |
| `TRACE-SFA-P0-NFR-003` | `SFA-P0-NFR-003` | `covered` | `implemented` | `pass` | `sufficient` | 3 | 2 | no |
| `TRACE-SFA-P0-NFR-006` | `SFA-P0-NFR-006` | `covered` | `implemented` | `pass` | `sufficient` | 3 | 2 | no |
| `TRACE-SFA-P0-NFR-013` | `SFA-P0-NFR-013` | `covered` | `implemented` | `pass` | `sufficient` | 3 | 2 | no |
| `TRACE-SFA-CORE-AJ-001` | `SFA-CORE-AJ-001` | `partial` | `scaffolded` | `pass` | `sufficient` | 2 | 2 | no |
| `TRACE-SFA-CORE-AJ-002` | `SFA-CORE-AJ-002` | `partial` | `scaffolded` | `pass` | `sufficient` | 2 | 2 | no |
| `TRACE-SFA-CORE-AJ-003` | `SFA-CORE-AJ-003` | `partial` | `scaffolded` | `pass` | `sufficient` | 4 | 2 | no |
| `TRACE-SFA-CORE-CONT-001` | `SFA-CORE-CONT-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 1 | 0 | historical only |
| `TRACE-SFA-CORE-CONT-002` | `SFA-CORE-CONT-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 1 | 0 | historical only |
| `TRACE-SFA-P0-FR-017` | `SFA-P0-FR-017` | `partial` | `scaffolded` | `pass` | `sufficient` | 3 | 2 | no |
| `TRACE-SFA-P0-FR-018` | `SFA-P0-FR-018` | `partial` | `scaffolded` | `planned` | `sufficient` | 7 | 0 | historical only |
| `TRACE-SFA-P0-FR-019` | `SFA-P0-FR-019` | `partial` | `scaffolded` | `planned` | `sufficient` | 1 | 0 | historical only |
| `TRACE-SFA-P0-FR-020` | `SFA-P0-FR-020` | `partial` | `scaffolded` | `planned` | `sufficient` | 7 | 0 | historical only |
| `TRACE-SFA-P0-FR-021` | `SFA-P0-FR-021` | `partial` | `scaffolded` | `planned` | `sufficient` | 7 | 0 | historical only |
| `TRACE-SFA-P0-NFR-010` | `SFA-P0-NFR-010` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-PY-001` | `SFA-CORE-PY-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-PY-002` | `SFA-CORE-PY-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-PY-003` | `SFA-CORE-PY-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-NFR-015` | `SFA-P0-NFR-015` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-001` | `SFA-CORE-YAML-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-002` | `SFA-CORE-YAML-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-003` | `SFA-CORE-YAML-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-004` | `SFA-CORE-YAML-004` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-005` | `SFA-CORE-YAML-005` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-006` | `SFA-CORE-YAML-006` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-007` | `SFA-CORE-YAML-007` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-008` | `SFA-CORE-YAML-008` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-009` | `SFA-CORE-YAML-009` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-YAML-010` | `SFA-CORE-YAML-010` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-033` | `SFA-P0-FR-033` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-FORMAT-001` | `SFA-CORE-FORMAT-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-FORMAT-002` | `SFA-CORE-FORMAT-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-FORMAT-003` | `SFA-CORE-FORMAT-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-FORMAT-004` | `SFA-CORE-FORMAT-004` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-FORMAT-005` | `SFA-CORE-FORMAT-005` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-FORMAT-006` | `SFA-CORE-FORMAT-006` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-031` | `SFA-P0-FR-031` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-032` | `SFA-P0-FR-032` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-045` | `SFA-P0-FR-045` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-NFR-014` | `SFA-P0-NFR-014` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CSV-001` | `SFA-CORE-CSV-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CSV-002` | `SFA-CORE-CSV-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CSV-003` | `SFA-CORE-CSV-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CSV-004` | `SFA-CORE-CSV-004` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CSV-005` | `SFA-CORE-CSV-005` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-MD-001` | `SFA-CORE-MD-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-MD-002` | `SFA-CORE-MD-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-MD-003` | `SFA-CORE-MD-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-036` | `SFA-P0-FR-036` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-TOML-001` | `SFA-CORE-TOML-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-TOML-002` | `SFA-CORE-TOML-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-TOML-003` | `SFA-CORE-TOML-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-TOML-004` | `SFA-CORE-TOML-004` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-TOML-005` | `SFA-CORE-TOML-005` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-TOML-006` | `SFA-CORE-TOML-006` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-TOML-007` | `SFA-CORE-TOML-007` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-034` | `SFA-P0-FR-034` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-043` | `SFA-P0-FR-043` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-JSONSCHEMA-001` | `SFA-CORE-JSONSCHEMA-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-JSONSCHEMA-002` | `SFA-CORE-JSONSCHEMA-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-JSONSCHEMA-003` | `SFA-CORE-JSONSCHEMA-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-JSONSCHEMA-004` | `SFA-CORE-JSONSCHEMA-004` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-JSONSCHEMA-005` | `SFA-CORE-JSONSCHEMA-005` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-JSONSCHEMA-006` | `SFA-CORE-JSONSCHEMA-006` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-JSONSCHEMA-007` | `SFA-CORE-JSONSCHEMA-007` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-035` | `SFA-P0-FR-035` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-039` | `SFA-P0-FR-039` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-042` | `SFA-P0-FR-042` | `covered` | `implemented` | `planned` | `sufficient` | 2 | 0 | historical only |
| `TRACE-SFA-CORE-CCWIKI-001` | `SFA-CORE-CCWIKI-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CCWIKI-002` | `SFA-CORE-CCWIKI-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CCWIKI-003` | `SFA-CORE-CCWIKI-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CCWIKI-004` | `SFA-CORE-CCWIKI-004` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-CCWIKI-005` | `SFA-CORE-CCWIKI-005` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-VCCAT-001` | `SFA-CORE-VCCAT-001` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-VCCAT-002` | `SFA-CORE-VCCAT-002` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-VCCAT-003` | `SFA-CORE-VCCAT-003` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-VCCAT-004` | `SFA-CORE-VCCAT-004` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-VCCAT-005` | `SFA-CORE-VCCAT-005` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-037` | `SFA-P0-FR-037` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-038` | `SFA-P0-FR-038` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-FR-044` | `SFA-P0-FR-044` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-P0-NFR-017` | `SFA-P0-NFR-017` | `covered` | `implemented` | `planned` | `sufficient` | 1 | 0 | no |
| `TRACE-SFA-CORE-SKILL-001` | `SFA-CORE-SKILL-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-SKILL-002` | `SFA-CORE-SKILL-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-SKILL-003` | `SFA-CORE-SKILL-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-SKILL-004` | `SFA-CORE-SKILL-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-SKILL-005` | `SFA-CORE-SKILL-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-FR-010` | `SFA-P0-FR-010` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-FR-012` | `SFA-P0-FR-012` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-FR-013` | `SFA-P0-FR-013` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-DOC-001` | `SFA-CORE-DOC-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-DOC-002` | `SFA-CORE-DOC-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-DOC-003` | `SFA-CORE-DOC-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-DOC-004` | `SFA-CORE-DOC-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-DOC-005` | `SFA-CORE-DOC-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-DOC-006` | `SFA-CORE-DOC-006` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-DOC-007` | `SFA-CORE-DOC-007` | `partial` | `scaffolded` | `planned` | `sufficient` | 5 | 0 | historical only |
| `TRACE-SFA-CORE-MEM-001` | `SFA-CORE-MEM-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-002` | `SFA-CORE-MEM-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-003` | `SFA-CORE-MEM-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-004` | `SFA-CORE-MEM-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-005` | `SFA-CORE-MEM-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-006` | `SFA-CORE-MEM-006` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-007` | `SFA-CORE-MEM-007` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-008` | `SFA-CORE-MEM-008` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-MEM-009` | `SFA-CORE-MEM-009` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-OBS-001` | `SFA-CORE-OBS-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-OBS-002` | `SFA-CORE-OBS-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-OBS-003` | `SFA-CORE-OBS-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-SVC-001` | `SFA-CORE-SVC-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-SVC-002` | `SFA-CORE-SVC-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-SVC-003` | `SFA-CORE-SVC-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-SVC-004` | `SFA-CORE-SVC-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-SVC-005` | `SFA-CORE-SVC-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-022` | `SFA-P0-FR-022` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-023` | `SFA-P0-FR-023` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-024` | `SFA-P0-FR-024` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-025` | `SFA-P0-FR-025` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-026` | `SFA-P0-FR-026` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-027` | `SFA-P0-FR-027` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-028` | `SFA-P0-FR-028` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-029` | `SFA-P0-FR-029` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-030` | `SFA-P0-FR-030` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-040` | `SFA-P0-FR-040` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-FR-041` | `SFA-P0-FR-041` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-NFR-009` | `SFA-P0-NFR-009` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-NFR-011` | `SFA-P0-NFR-011` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-P0-NFR-016` | `SFA-P0-NFR-016` | `partial` | `scaffolded` | `planned` | `sufficient` | 11 | 0 | no |
| `TRACE-SFA-CORE-IMPROVE-001` | `SFA-CORE-IMPROVE-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-IMPROVE-002` | `SFA-CORE-IMPROVE-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-IMPROVE-003` | `SFA-CORE-IMPROVE-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-FR-006` | `SFA-P0-FR-006` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-FR-009` | `SFA-P0-FR-009` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-FR-011` | `SFA-P0-FR-011` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-FR-016` | `SFA-P0-FR-016` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-NFR-001` | `SFA-P0-NFR-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-NFR-002` | `SFA-P0-NFR-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-NFR-004` | `SFA-P0-NFR-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-P0-NFR-005` | `SFA-P0-NFR-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 4 | 0 | historical only |
| `TRACE-SFA-CORE-ROLE-002` | `SFA-CORE-ROLE-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-ROLE-003` | `SFA-CORE-ROLE-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-ROLE-004` | `SFA-CORE-ROLE-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-ROLE-005` | `SFA-CORE-ROLE-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LAYER-001` | `SFA-CORE-LAYER-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LAYER-002` | `SFA-CORE-LAYER-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LAYER-003` | `SFA-CORE-LAYER-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LAYER-004` | `SFA-CORE-LAYER-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-LAYER-005` | `SFA-CORE-LAYER-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SELFHOST-001` | `SFA-CORE-SELFHOST-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SELFHOST-002` | `SFA-CORE-SELFHOST-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SELFHOST-003` | `SFA-CORE-SELFHOST-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SELFHOST-004` | `SFA-CORE-SELFHOST-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-DISCOVERY-001` | `SFA-CORE-DISCOVERY-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-DISCOVERY-002` | `SFA-CORE-DISCOVERY-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-DISCOVERY-003` | `SFA-CORE-DISCOVERY-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-DISCOVERY-004` | `SFA-CORE-DISCOVERY-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-DISCOVERY-005` | `SFA-CORE-DISCOVERY-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 3 | 0 | no |
| `TRACE-SFA-CORE-DISCOVERY-006` | `SFA-CORE-DISCOVERY-006` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-DISCOVERY-007` | `SFA-CORE-DISCOVERY-007` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SKILL-006` | `SFA-CORE-SKILL-006` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SKILL-007` | `SFA-CORE-SKILL-007` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SKILL-008` | `SFA-CORE-SKILL-008` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-SKILL-009` | `SFA-CORE-SKILL-009` | `partial` | `scaffolded` | `planned` | `sufficient` | 0 | 0 | no |
| `TRACE-SFA-CORE-INIT-001` | `SFA-CORE-INIT-001` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-INIT-002` | `SFA-CORE-INIT-002` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-INIT-003` | `SFA-CORE-INIT-003` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-INIT-004` | `SFA-CORE-INIT-004` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-INIT-005` | `SFA-CORE-INIT-005` | `partial` | `scaffolded` | `planned` | `sufficient` | 3 | 0 | no |
| `TRACE-SFA-CORE-INIT-006` | `SFA-CORE-INIT-006` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-INIT-007` | `SFA-CORE-INIT-007` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-INIT-008` | `SFA-CORE-INIT-008` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | no |
| `TRACE-SFA-CORE-INIT-009` | `SFA-CORE-INIT-009` | `partial` | `scaffolded` | `planned` | `sufficient` | 2 | 0 | historical only |

## Conclusion

Every row has an accountable owner, date, and verdict. The migration is reversible and does not overstate operational capability. The 200 `planned` verification rows and seven `needs_evidence` mappings are explicit obligations for later evidence and validator work; they are not silently treated as pass.
