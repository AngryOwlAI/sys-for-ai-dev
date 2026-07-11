# TX-27 Local Evidence: YAML Control And State Surface

## Conclusion

`TX-27-LOCAL-EVIDENCE-YAML-CONTROL` verifies the eleven dependency-ready YAML obligations `SFA-CORE-YAML-001` through `SFA-CORE-YAML-010` and `SFA-P0-FR-033`. Their verification states advance from `planned` to `pass`; capability remains `implemented`, coverage remains `covered`, and no waiver is used.

This packet is additive to the frozen TX-23 ledger and completed TX-24, TX-25, and TX-26 evidence. It does not execute the remaining 52 local verification obligations, change the 410 TX-25 future-work dispositions, add cross-version Python CI, obtain external evidence, accept `G-10`, or grant production, operational, stakeholder, domain, target-runtime, or permission authority.

## Authority And Baseline

- Accountable authorization: the user authorized one bounded family among the remaining 63 local verifications on 2026-07-11.
- Gate decision: `DDR-SFADEV-STRATEGIC-BASELINE-G11-004`.
- Entry commit and shared baseline: `53eaa198be20a878fb0ca52f6d5975ffe702e931`.
- Entry handoff: `HANDOFF-SFADEV-STRATEGIC-BASELINE-TX26-001`.
- Memory preflight: `MEMPREFLIGHT-TX-27-LOCAL-EVIDENCE-YAML-CONTROL-20260711T174814Z`, `PASS_WITH_WARNINGS`, zero authority inversions.
- Frozen TX-23 ledger SHA-256: `1e9e2b2a0a7bc4f589addd65b8d34642899a3f812e7ce35be6e62a2c0fcc6138`.
- Frozen TX-25 interpretation SHA-256: `9ed89d6ff5872ee2fb2b740791c268d9048e97f31eae8ff7d3b4d2d8929d5f38`.
- Subject layer: `framework_product`; development tests supply evidence and generated wiki pages remain noncanonical.

## Verification Method

The focused validator checks the exact bounded PyYAML dependency, the `fmt_yaml_control` profile, required registered control/state families, complete ownership/authority/writer/reader/contract/path metadata, safe parsing of every registered YAML record, validation against each declared JSON Schema contract, policy assignment of YAML control/state artifacts, and rejection of unsafe Python object tags. An AST check rejects unsafe PyYAML loader calls in the reference package.

The pre-acceptance check found one selected-family gap: `ctrl_skill_import_manifest` had no executable validation contract. TX-27 added `skill_import_manifest.schema.json`, registered it, and bound the existing manifest row to the contract. No canonical PRD or unrelated capability implementation changed.

## Evidence Disposition

| Requirements | Executed evidence | Disposition |
|---|---|---|
| `SFA-CORE-YAML-001`, `005`, `SFA-P0-FR-033` | Format profile, policy assignment, and 231 registered YAML control/state records | Human-readable machine-parseable YAML control/state assignment verified. |
| `SFA-CORE-YAML-002`, `006` | Registered bounded transactions, handoffs, receipts, import manifest, tracked state, and state snapshots plus policy coverage | Required control/state artifact families verified without restoring retired runtime authority. |
| `SFA-CORE-YAML-003` | Exact bounded PyYAML declaration in `pyproject.toml` | Required parser dependency verified. |
| `SFA-CORE-YAML-004`, `009` | Safe loader implementation, AST audit, malicious-tag rejection, and negative test | Unsafe object construction fails closed. |
| `SFA-CORE-YAML-007`, `008` | Complete registry metadata, executable contracts, and focused control-record validation | Registered routing, permission, boundary, state, and completion records are governed and validated before use. |
| `SFA-CORE-YAML-010` | Deterministic Configuration and Control Wiki generation and drift check | Controlled/canonical YAML rows are indexed only in a noncanonical generated reader. |

## Results And Boundaries

- Focused validator: `11/11` passed.
- Focused positive/negative unit suite: `5/5` passed.
- Registered YAML records inspected: 231 before TX-27 closeout registration; all safely parsed and contract-validated where declared.
- Verification state: `pass` increases from 31 to 42; `planned` decreases from 196 to 185.
- Remaining locally executable verification obligations: 52.
- Capability and coverage states for the eleven rows: unchanged at `implemented` and `covered`.
- Trace waiver fields: unchanged and empty.
- Accepted waivers: 0.
- `G-10`: deferred and not accepted.

These checks prove current local YAML control/state structure, governance, safe parsing, and generated indexing. They do not prove target-domain truth, runtime operations, production fitness, stakeholder consensus, external independence, or cross-version Python compatibility.

## Rollback And Supersession

Before publication, revert the complete TX-27 packet. After publication, preserve G-11-004, the eleven additive evidence rows, trace verification evidence, report, transaction, receipt, and handoff as activated history; use a new bounded transaction for any later family.

## References

AngryOwlAI. (2026, July 9). *Sys4AI-dev strategic baseline migration full implementation plan* [Implementation plan].

Sys4AI-dev. (2026a, July 11). *Strategic baseline migration evidence closure plan* [Implementation plan].

Sys4AI-dev. (2026b, July 11). *TX-26 local evidence: Python reference and package surface* [Verification report].
