# TX-29 Local Evidence: CSV Registry Governance

## Conclusion

`TX-29-LOCAL-EVIDENCE-CSV-REGISTRY` verifies exactly `SFA-CORE-CSV-001` through `SFA-CORE-CSV-005`. Their verification states advance from `planned` to `pass`; capability remains `implemented`, coverage remains `covered`, semantic review remains `sufficient`, and no waiver is used.

The packet does not execute any of the remaining 37 local obligations, obtain external evidence, add cross-version Python CI, accept `G-10`, or grant production, operational, stakeholder, domain, target-runtime, or permission authority.

## Authority And Baseline

- Accountable authorization: the user explicitly authorized the earliest remaining five-row CSV-registry family on 2026-07-11.
- Gate decision: `DDR-SFADEV-STRATEGIC-BASELINE-G11-006`.
- Entry commit and shared baseline: `2de9d847ba4763cc876141b301d0babcb2a7ab5a`.
- Entry handoff: `HANDOFF-SFADEV-STRATEGIC-BASELINE-TX28-001`.
- Memory preflight: `MEMPREFLIGHT-TX-29-LOCAL-EVIDENCE-CSV-REGISTRY-20260711T195006Z`, `PASS_WITH_WARNINGS`, zero authority inversions.
- Frozen TX-23 ledger SHA-256: `1e9e2b2a0a7bc4f589addd65b8d34642899a3f812e7ce35be6e62a2c0fcc6138`.
- Frozen TX-25 interpretation SHA-256: `9ed89d6ff5872ee2fb2b740791c268d9048e97f31eae8ff7d3b4d2d8929d5f38`.
- Subject layer: `framework_product`; generated registry catalog pages remain noncanonical derivatives.

## Verification Method

The focused validator reads every CSV through the standard strict parser, rejects malformed row widths and duplicate headers, and validates every live registry against `registry_definition_registry.csv`. Each definition declares purpose, owner, authority status, expected header, row-ID field, validation method, promotion rule, source hash state, and review metadata. The same surface rejects missing registry definitions, duplicate or blank stable IDs, missing source or derivative files, missing validation contracts, orphan derivative source references, stale populated hashes, invalid registry authority classes, and authority/promotion inconsistencies.

The registry-definition contract supports both `core` and `project_specific` scope. A project-specific CSV cannot enter the governed registry root without a definition row and the same strict validation. A generated derivative registry must use explicit `generated_derivative` authority and `generated_derivative_no_promotion`; all current live registries are controlled `registry_authority` artifacts.

## Evidence Disposition

| Requirement | Executed evidence | Disposition |
|---|---|---|
| `SFA-CORE-CSV-001` | Strict reader plus 27 governed live CSV registries | CSV is verified for registries, ledgers, relationship maps, provenance rows, and memory tables. |
| `SFA-CORE-CSV-002` | Expected headers, stable row-ID fields, strict malformed-row rejection, duplicate-ID negatives | Stable deterministic structure and identity pass. |
| `SFA-CORE-CSV-003` | Registry graph and populated-hash checks with missing-contract, orphan-derivative, and stale-hash negatives | Required cross-registry failure classes fail closed. |
| `SFA-CORE-CSV-004` | Registry authority and promotion-rule contract | Registry sources remain controlled; derivative registries cannot self-promote. |
| `SFA-CORE-CSV-005` | Registry-definition row contract and unregistered project-registry negative | Core and project-specific registries require complete governed metadata. |

## Results And Boundaries

- Focused validator: `5/5` requirements passed.
- Focused positive/negative suite: `9/9` tests passed.
- Full product suite: `288/288` tests passed.
- Product and repository-root `make validate`: passed.
- Verification state: `pass` increases from 52 to 57; `planned` decreases from 175 to 170.
- Local evidence registry: 37 accepted rows total; 37 local verification obligations remain.
- Capability and coverage remain `implemented` and `covered`.
- Trace waiver fields remain empty; accepted waivers remain 0.
- `G-10` remains deferred and not accepted.
- Final memory status: `PASS_WITH_WARNINGS`; 1,157 objects, 518 known warnings, zero derivative authority inversions.

These checks prove current local CSV registry structure, metadata, graph integrity, authority classification, deterministic validation, and project-extension control. They do not prove external truth, target-runtime operations, production fitness, stakeholder consensus, cross-version Python compatibility, or any later Markdown, TOML, JSON Schema, or generated-reader family.

## Rollback And Supersession

Before publication, revert the complete TX-29 packet. After publication, preserve G-11-006, the five additive evidence rows, trace verification evidence, report, transaction, receipt, and handoff as activated history; use a new bounded transaction for any later family.

## References

AngryOwlAI. (2026, July 9). *Sys4AI-dev strategic baseline migration full implementation plan* [Implementation plan].

Sys4AI-dev. (2026a, July 11). *Strategic baseline migration evidence closure plan* [Implementation plan].

Sys4AI-dev. (2026b, July 11). *TX-28 local evidence: Core format governance and memory inspectability* [Verification report].
