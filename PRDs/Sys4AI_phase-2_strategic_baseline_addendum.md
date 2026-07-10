# Sys4AI Phase 2 Strategic Baseline Addendum

**Document status:** Controlled Phase 2 addendum accepted for implementation under `G-06` by the accountable product-owner instruction authorizing `TX-14-PHASE2`.
**Source authority status:** controlled
**Subject system:** Sys4AI framework product
**Subject layer:** framework_product
**Phase:** Phase 2 walking skeleton
**Addendum source ID:** `SRC-PRD-P2-STRATEGIC-BASELINE-ADDENDUM`
**Controlling decision:** `DDR-SFADEV-STRATEGIC-BASELINE-001`
**Adds to:** `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`
**Effective date:** 2026-07-10
**Approval boundary:** This acceptance authorizes the Phase 2 scope in this addendum. It does not satisfy `G-08`, approve candidate vision or core-values content, expand permissions, establish domain truth, or approve production release.

> Authority notice: This addendum carries the current strategic-baseline delta for
> Phase 2. The accepted Phase 2 PRD and its draft remain unchanged historical
> evidence. Where their current-execution wording conflicts with this addendum,
> this addendum controls only the affected Phase 2 execution, strategic-intent,
> host-evidence, pattern, testing, trace, and package obligations.

## 1. Purpose and Additive Change Classification

This document is an additive controlled baseline change. It preserves the accepted
walking-skeleton objective: demonstrate a small, traceable path from target-system
intent to a non-production package. It replaces only the affected current-semantics
clauses with portable bounded execution and the strategic, host, lifecycle, pattern,
testing, and package obligations accepted by the strategic-baseline migration.

The addendum is the selected route because it is the smallest authority change that
can reconcile Phase 2 with the current framework baseline. A successor PRD is not
authorized for this migration.

## 2. Preserved Evidence and Scope of Effect

The following sources remain substantively unchanged:

- `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.
- `PRDs/drafts/Sys4AI_phase-2_walking_skeleton_prd.draft.md`.

Their pre-`TX-14` SHA-256 values are:

| Protected source | SHA-256 |
|---|---|
| Accepted Phase 2 PRD | `98567cf4f4af8ca99650a6220a78d840dae5e11195891fc808c69c4828528038` |
| Accepted Phase 2 draft | `9e290964200137329827a0164f50c2d3e97dc194fac65dd086c8b1dd7e57d84f` |

This addendum does not erase their original acceptance evidence or rewrite their
historical claims. It controls the current interpretation of these affected
requirements and tables:

| Accepted Phase 2 surface | Current controlled interpretation |
|---|---|
| `SFA-P2-WS-FLOW-001` | Retain the intent-to-package flow; use the revised artifact flow in section 4 and portable execution transactions. |
| `SFA-P2-WS-FLOW-002` | Represent current-state, continuation, handoff, cancellation, escalation, and closeout through portable controlled evidence. |
| `SFA-P2-WS-AJ-001` | Satisfy bounded task-packet intent with at least three authorized execution transactions unless an accountable decision justifies another count. Historical packet types are not required current runtime surfaces. |
| `SFA-P2-WS-TRACE-001` | Trace target intent through strategic artifacts, requirements, execution transactions, implementation, test evidence, and package outputs. |
| Artifact-flow steps 5 and 6 | Use execution transactions plus validation and closeout evidence as defined here. |
| Validation command list | Treat the original command list as packet-era acceptance evidence. Current validation is the set in section 7. |

All unaffected accepted Phase 2 requirements remain in force.

## 3. Normative Addendum Requirements

| Requirement ID | Normative requirement | Priority | Upstream authority |
|---|---|---|---|
| `SFA-P2-ADD-STRAT-001` | The walking skeleton shall create or consume a separate target vision artifact with stable target and vision IDs, candidate or approved content state, source evidence, version, hash, owner, review state, and approval-evidence or waiver reference. | Must | `SFA-P1-INIT-STRAT-001`; `SFA-P1-INIT-STRAT-004` |
| `SFA-P2-ADD-STRAT-002` | The walking skeleton shall create or consume a separate target core-values artifact with stable target and value IDs, candidate or approved content state, source evidence, decision tests, anti-values, inherited constraints, version, hash, owner, and approval-evidence or waiver reference. | Must | `SFA-P1-INIT-STRAT-001`; `SFA-P1-INIT-STRAT-004` |
| `SFA-P2-ADD-APPROVAL-001` | Candidate target vision and core-values content shall not be represented as approved without accountable non-model approval evidence; a waiver shall be explicit, scoped, time-bounded, and non-permission-expanding. | Must | `SFA-P1-INIT-STRAT-005`; `SFA-P1-INIT-STRAT-008` |
| `SFA-P2-ADD-HOST-001` | Any host-dependent walking-skeleton action shall reference a registered host-capability profile and current evidence for the required capability, permission source, limitations, degraded behavior, and cancellation behavior; unknown required capability shall fail closed. | Must | `SFA-P1-INIT-HOST-002`; `SFA-P1-INIT-HOST-003`; `SFA-P1-INIT-HOST-004` |
| `SFA-P2-ADD-PATTERN-001` | The walking skeleton shall record coordination pattern and operational maturity as independent fields and shall include a pattern decision with alternatives, autonomy, roles, interfaces, state, monitoring, failures, security, recovery, human oversight, promotion evidence, owner, review triggers, and supersession. | Must | `SFA-P1-INIT-PATTERN-001`; `SFA-P1-INIT-PATTERN-004`; `SFA-P1-INIT-PATTERN-005` |
| `SFA-P2-ADD-LIFE-001` | Within the walking-skeleton scope, Design, Develop, Implement, and Test shall each have explicit inputs, responsible and approving roles, permissions, activities, outputs, entry and exit criteria, failure behavior, rollback or return transitions, and evidence. Test execution, requirements verification, stakeholder or system validation, and behavioral or performance evaluation shall remain distinct evidence classes. | Must | `SFA-P1-INIT-LIFE-002`; `SFA-P1-INIT-LIFE-003`; `SFA-P1-INIT-LIFE-004` |
| `SFA-P2-ADD-EXEC-001` | Implementation work shall use authorized portable execution transactions that bind objective, source requirements and decisions, subject system and layer, runtime actor, approval principal, permission envelope, reads, writes, tools, external actions, validators, stop conditions, cancellation, escalation, resume, closeout, rollback, and supersession. | Must | `SFA-P1-INIT-EXEC-001`; `SFA-P1-INIT-EXEC-002` |
| `SFA-P2-ADD-STATE-001` | Every bounded transition shall preserve source-backed current-state evidence, continuation or handoff evidence, cancellation and escalation state, closeout evidence, unresolved issues, and the exact next permitted transaction. | Must | `SFA-P1-INIT-STATE-001`; `SFA-P1-INIT-EXEC-002` |
| `SFA-P2-ADD-TRACE-001` | The walking skeleton shall trace target intent, strategic-intent artifacts and approval state, pattern decision, requirements, implementation plan, execution transactions, implementation artifacts, validation evidence, package outputs, waivers, and handoff or closeout evidence through stable IDs and registered paths. | Must | `SFA-P1-INIT-EVID-001`; `SFA-P1-INIT-EVID-002` |
| `SFA-P2-ADD-PACKAGE-001` | The target package shall include or reference target vision, target core values, content-approval evidence or valid waiver, source hashes and active versions, pattern and maturity evidence, lifecycle and promotion state, host profile or host requirements, portable execution profile, impact state, requirements trace, task-packet index, and validation summary. | Must | `SFA-P1-INIT-PACKAGE-001`; `SFA-P1-INIT-PACKAGE-002` |
| `SFA-P2-ADD-SEM-001` | Every relevant validator output and validation summary shall state that structural validation does not prove strategic quality, ethical correctness, stakeholder consensus, behavioral alignment, production readiness, or domain truth. | Must | `SFA-P1-INIT-SEM-001`; `SFA-P1-INIT-VAL-007` |
| `SFA-P2-ADD-FLOW-001` | The Phase 2 walking skeleton shall follow the revised artifact flow in section 4 and shall stop rather than bypass a missing approval, required host capability, permission, evidence, or authority gate. | Must | `SFA-P1-INIT-EXEC-002`; `SFA-P1-INIT-STATUS-002` |
| `SFA-P2-ADD-SAFETY-001` | The Phase 2 result shall remain a `validated_prototype` or lower maturity state unless separate evaluation, security, integration, ownership, rollback, monitoring, incident-response, service-threshold, and accountable production-approval evidence is accepted. | Must | `SFA-P1-INIT-PATTERN-004`; `SFA-P1-INIT-STATUS-001` |

## 4. Revised Artifact Flow

The controlled Phase 2 sequence is:

1. `/init` classification of system of interest and subject layer.
2. Validated Requirements Discovery Record.
3. Target vision candidate.
4. Target core-values candidate.
5. Accountable human approval evidence or a valid waiver.
6. Agentic System Pattern Decision.
7. Controlled PRD.
8. Controlled implementation plan.
9. One or more authorized bounded execution transactions.
10. Implementation evidence and separately labeled test, verification, validation, and evaluation evidence.
11. Target-system package.
12. Validation, closeout, and next-state evidence.

The flow shall stop at any failed gate. Phase 2 may close at `validated_prototype`;
it shall not infer operational or production readiness from package creation,
test execution, validator success, or host availability.

## 5. Host and Permission Boundary

The initial reference-host evidence is the registered Codex App profile at
`Sys4AI/configs/host_profiles/codex_app_reference.toml`, together with its
registered evidence sources. A profile maps portable obligations to observed host
capabilities; it does not create framework purpose, grant permission, or override
platform, system, developer, project, or human constraints.

Precedence is:

`platform and system constraints -> host permissions -> project authorization -> transaction permission envelope -> task objective`

Values, goals, model output, generated documentation, or a successful prior run
cannot expand this order.

## 6. Trace and Authority Rules

- `SRC-PRD-P2-STRATEGIC-BASELINE-ADDENDUM` owns the requirements prefixed `SFA-P2-ADD-`.
- The accepted Phase 2 PRD remains the controlled owner of `SFA-P2-WS-` requirements.
- The Phase 0 and Phase 1 PRDs remain authoritative for their respective requirement families.
- The strategic-baseline decision controls the selected portable route and the addendum disposition.
- Requirement-trace rows for this addendum record upstream Phase 0 and Phase 1 mappings without creating duplicate Phase 0 coverage rows.
- Derivative modules do not consume this addendum until `TX-19-MODULES`; no module authority changes in `TX-14`.
- Generated readers remain noncanonical and may be refreshed only from registered sources.

## 7. Validation and Acceptance Evidence

`TX-14` acceptance requires:

- `make validate-prd-semantics`.
- `make validate-requirement-trace` and `make validate-requirement-trace-migration`.
- `make validate-registry-graph`.
- `make validate-strategic-intent`.
- `make validate-lifecycle-and-patterns`.
- `make validate-capability-migration`.
- Product and repository-root `make validate`.
- A hash and Git-diff preservation check for both protected Phase 2 sources.
- `git diff --check`.

Structural validation does not prove strategic quality, ethical correctness,
stakeholder consensus, behavioral alignment, production readiness, or domain truth.
Those claims require accountable review and additional evidence.

## 8. Acceptance Criteria

The addendum is accepted for Phase 2 implementation when all of the following hold:

1. This source is controlled, registered, indexed, and related to Phase 0, Phase 1, accepted Phase 2, the RDR, and the controlling decision.
2. Every `SFA-P2-ADD-` requirement has one registered generalized trace row.
3. The accepted Phase 2 PRD and draft retain their recorded SHA-256 values and have no Git diff.
4. New execution wording is portable and host-specific behavior remains isolated in a registered profile.
5. Target strategic intent, approval or waiver, pattern, testing, trace, and package obligations are explicit.
6. The result makes no production-readiness, operational-capability, `G-08`, or domain-truth claim.
7. The bounded `TX-14` validators pass and the handoff routes only to `TX-15-TARGET-PACKAGE`.

## 9. Non-Goals and Deferred Work

- Do not implement or modify the target package in this transaction; that belongs to `TX-15`.
- Do not implement the new walking-skeleton flow graph in this transaction; that belongs to `TX-16`.
- Do not approve the candidate Sys4AI vision or core values; that remains `G-08` work.
- Do not regenerate derivative PRD modules; that remains blocked until the later canonical approval gate.
- Do not claim production readiness or operational capability.
- Do not restore retired runtime surfaces or promote historical records to current authority.

## References

AngryOwlAI. (2026a, July 9). *Sys4AI strategic-baseline identity and execution-model decision* [Director Decision Record]. `Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml`.

AngryOwlAI. (2026b, July 9). *Sys4AI strategic-baseline migration requirements discovery record* [Requirements Discovery Record]. `Sys4AI/control_records/system_definition/strategic_baseline_migration_requirements_discovery_record.md`.

Sys4AI-dev. (2026a). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

Sys4AI-dev. (2026b). *Sys4AI Phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

Sys4AI-dev. (2026c). *Sys4AI Phase 2 walking skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

Sys4AI-dev. (2026d). *Strategic baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.
