# Sys4AI Phase 2 Walking Skeleton PRD

**Document status:** Controlled Phase 2 PRD accepted by `RECEIPT-SFADEV-18-PHASE2-WALKING-SKELETON-PRD-001`.
**Product name:** Sys4AI.
**Phase:** Phase 2 walking skeleton.
**Subject system:** Sys4AI framework product.
**Depends on:** `PRDs/Sys4AI_phase-0_product_system_design_prd.md`, `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`, and `RDR-SFADEV-P2-WS-001`.
**Last updated:** 2026-07-08.
**Producing AgentJob:** `AJ-SFADEV-18-PHASE2-WALKING-SKELETON-PRD-001`.
**Authority note:** This PRD adds a Phase 2 slice. It does not supersede Phase 0 or Phase 1.

## Executive Summary

This PRD defines the Phase 2 walking skeleton for Sys4AI. The walking skeleton is a constrained end-to-end governance demonstration: it starts from target-system intent, passes through `/init`, creates a Requirements Discovery Record, creates a PRD, creates an implementation plan, creates bounded AgentJobs, records validation evidence, and creates a package or export smoke artifact.

The purpose is not to prove production readiness. The purpose is to prove that Sys4AI can carry source authority, role boundaries, traceability, continuation state, validation evidence, and packaging evidence through a small but complete system-definition-to-package path.

## Phase Boundary

This PRD authorizes later Phase 2 planning and implementation packets. It does not authorize this packet to write implementation code, create the sample package, export a target-system bundle, or make autonomous runtime claims.

The logical next packet is a Phase 2 implementation plan and AgentJob set. Later packets may implement orchestration and package smoke artifacts only after that plan exists and validates.

## User And Stakeholder Model

| Stakeholder | Need | Phase 2 implication |
| --- | --- | --- |
| Framework maintainer | Evidence that Sys4AI can run a governed end-to-end slice. | The walking skeleton must be source-traced and validator-backed. |
| Root AI agent using Sys4AI | A clear path from user intent to executable bounded work. | `/init`, RDR, PRD, plan, AgentJobs, and handoffs must connect without hidden assumptions. |
| Requirements manager | Requirements that are baselined only after discovery evidence exists. | RDR candidates must map to PRD requirements before planning begins. |
| Verification role | A distinction between structural validation and semantic acceptance. | Validator output must state what is proven and what remains review-only. |
| Future target-system owner | A package or export surface that can be inspected. | The smoke package must include README, manifest, task-packet index, and requirements trace. |

## Walking Skeleton System Of Interest

The system of interest is the Sys4AI framework-product flow for creating and packaging a governed target agentic system. In this phase, the concrete package scenario remains open, but the package boundary is already constrained: it must carry enough trace evidence for an agent or maintainer to inspect how target-system intent became bounded work.

## Functional Requirements

| Requirement ID | Requirement | Priority | Trace |
| --- | --- | --- | --- |
| `SFA-P2-WS-FLOW-001` | Sys4AI shall provide a walking skeleton flow from user target-system intent through `/init`, RDR, PRD, implementation plan, AgentJobs, validation evidence, and target-system package or export smoke output. | Must | `REQ-CAND-P2-001`; `REQ-CAND-P2-002`; `REQ-CAND-P2-003`; `REQ-CAND-P2-004`; `REQ-CAND-P2-005`; `REQ-CAND-P2-006`; `REQ-CAND-P2-007` |
| `SFA-P2-WS-FLOW-002` | Sys4AI shall expose each walking skeleton transition as controlled status evidence through `/continue` handoffs, receipts, and program-state updates. | Must | `DRV-P2-003`; `REQ-CAND-P2-005`; `REQ-CAND-P2-007`; `NFR-CAND-P2-002` |
| `SFA-P2-WS-RDR-001` | The walking skeleton shall consume a validated Requirements Discovery Record before PRD synthesis. | Must | `REQ-CAND-P2-002`; `CON-P2-002` |
| `SFA-P2-WS-PRD-001` | The walking skeleton shall produce a Phase 2 PRD that traces each baselined requirement to the Phase 2 RDR or an approved Director Decision. | Must | `REQ-CAND-P2-003`; `DRV-P2-002` |
| `SFA-P2-WS-PLAN-001` | The walking skeleton shall produce an implementation plan from the Phase 2 PRD using the active `prd-to-implementation-plan` skill or an equivalent governed procedure. | Must | `REQ-CAND-P2-004`; `DRV-P2-002` |
| `SFA-P2-WS-AJ-001` | The walking skeleton shall produce at least three bounded AgentJob or task-packet artifacts from the implementation plan. | Should | `REQ-CAND-P2-005`; `DRV-P2-003`; `OPEN-P2-003` |
| `SFA-P2-WS-PACKAGE-001` | The walking skeleton shall produce a sample target-system package or export surface containing a README, manifest, requirements trace, and task packet index. | Should | `REQ-CAND-P2-006`; `DRV-P2-004`; `OPEN-P2-001`; `OPEN-P2-002` |

## Non-Functional Requirements

| Requirement ID | Requirement | Priority | Trace |
| --- | --- | --- | --- |
| `SFA-P2-WS-TRACE-001` | The walking skeleton shall preserve trace from RDR candidate requirements through PRD requirements, implementation plan tasks, AgentJobs, validation evidence, and package outputs. | Must | `REQ-CAND-P2-003`; `REQ-CAND-P2-004`; `REQ-CAND-P2-005`; `REQ-CAND-P2-006`; `REQ-CAND-P2-007`; `NFR-CAND-P2-002` |
| `SFA-P2-WS-VAL-001` | The walking skeleton shall run structural validators and report which claims are proven by validation and which claims remain semantic or human-review obligations. | Must | `REQ-CAND-P2-007`; `SFA-P0-FR-042` |
| `SFA-P2-WS-NFR-001` | Generated artifacts shall remain derivative until accepted through source-authority workflow. | Must | `NFR-CAND-P2-001`; `CON-P2-003` |
| `SFA-P2-WS-NFR-002` | The walking skeleton shall not claim production runtime readiness, autonomous operation readiness, or domain semantic correctness. | Must | `NFR-CAND-P2-003`; `RISK-P2-002` |

## Artifact Flow Requirements

| Step | Required artifact | Authority status at creation | Exit evidence |
| --- | --- | --- | --- |
| 1 | `/init` classification summary | Controlled or controlled evidence | Subject layer, route, and system-of-interest are explicit. |
| 2 | Phase 2 RDR | Controlled discovery evidence | RDR validator passes and candidate IDs remain candidate-labeled. |
| 3 | Phase 2 PRD | Controlled PRD | Each baselined requirement traces to RDR or approved Director Decision evidence. |
| 4 | Phase 2 implementation plan | Controlled implementation plan | Plan maps PRD requirements to task packets and validators. |
| 5 | AgentJobs or task packets | Controlled control records | At least three bounded packets exist or a Director Decision justifies another count. |
| 6 | Validation evidence | Controlled completion evidence | Structural validators pass or failures are routed. |
| 7 | Package or export smoke surface | Smoke evidence | README, manifest, requirements trace, and task-packet index exist. |

## Traceability Requirements

The authoritative RDR-to-PRD trace for this phase is the table below. The Phase 0-to-Phase 1 `requirement_trace_registry.csv` remains a continuity registry for prior baselines and is not redefined as a Phase 2 requirement database.

| PRD requirement | RDR candidate or decision evidence | Trace status |
| --- | --- | --- |
| `SFA-P2-WS-FLOW-001` | `REQ-CAND-P2-001`; `REQ-CAND-P2-002`; `REQ-CAND-P2-003`; `REQ-CAND-P2-004`; `REQ-CAND-P2-005`; `REQ-CAND-P2-006`; `REQ-CAND-P2-007` | covered |
| `SFA-P2-WS-FLOW-002` | `DRV-P2-003`; `REQ-CAND-P2-005`; `REQ-CAND-P2-007`; `NFR-CAND-P2-002`; `SFA-CORE-CONT-001`; `SFA-CORE-CONT-002` | covered |
| `SFA-P2-WS-RDR-001` | `REQ-CAND-P2-002`; `CON-P2-002` | covered |
| `SFA-P2-WS-PRD-001` | `REQ-CAND-P2-003`; `DRV-P2-002` | covered |
| `SFA-P2-WS-PLAN-001` | `REQ-CAND-P2-004`; `DRV-P2-002` | covered |
| `SFA-P2-WS-AJ-001` | `REQ-CAND-P2-005`; `DRV-P2-003`; `OPEN-P2-003` | covered with deferred planning choice |
| `SFA-P2-WS-PACKAGE-001` | `REQ-CAND-P2-006`; `DRV-P2-004`; `OPEN-P2-001`; `OPEN-P2-002` | covered with deferred package detail |
| `SFA-P2-WS-TRACE-001` | `REQ-CAND-P2-003`; `REQ-CAND-P2-004`; `REQ-CAND-P2-005`; `REQ-CAND-P2-006`; `REQ-CAND-P2-007`; `NFR-CAND-P2-002` | covered |
| `SFA-P2-WS-VAL-001` | `REQ-CAND-P2-007`; `SFA-P0-FR-042` | covered |
| `SFA-P2-WS-NFR-001` | `NFR-CAND-P2-001`; `CON-P2-003`; `SFA-CORE-INIT-009` | covered |
| `SFA-P2-WS-NFR-002` | `NFR-CAND-P2-003`; `RISK-P2-002`; `SFA-P0-FR-042` | covered |

## Validation Requirements

Structural validation shall prove only structure, registry connectivity, and declared process constraints. It shall not prove domain semantic correctness, production readiness, autonomous operation readiness, or human acceptance.

Required validation evidence for this PRD packet:

- `validate-requirement-trace` passes for the existing Phase 0-to-Phase 1 trace registry.
- `validate-registry-graph` passes after the Phase 2 PRD source rows are registered.
- `validate-control-loop` passes with no active AgentJob left open.
- `validate-check-diff --agentjob AJ-SFADEV-18-PHASE2-WALKING-SKELETON-PRD-001` passes.
- Aggregate `make validate` passes with the selected check-diff AgentJob.

## Target-System Package Or Export Requirements

The package or export smoke surface shall include at minimum:

- `README.md`.
- A machine-readable manifest.
- A requirements trace artifact.
- A task-packet index.
- Validation evidence or a validation summary.
- A non-production authority notice.

The exact target-system scenario and package shape remain deferred to implementation planning because `OPEN-P2-001` and `OPEN-P2-002` are open in the RDR.

## Non-Goals

- Do not create implementation code in the PRD packet.
- Do not create a target-system package or export smoke artifact in the PRD packet.
- Do not supersede the Phase 0 or Phase 1 PRDs.
- Do not treat generated derivatives or memory hits as canonical authority.
- Do not claim production runtime readiness or autonomous operation readiness.
- Do not claim that validators prove domain semantic correctness.

## Risks And Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| RDR candidates are mistaken for approved requirements. | Later packets may overreach. | This PRD promotes only explicitly listed Phase 2 requirements and keeps RDR candidate IDs as trace evidence. |
| The walking skeleton becomes an unbounded build. | The `/continue` contract is weakened. | Each later packet must be an AgentJob or task packet with receipt and handoff evidence. |
| Package smoke evidence is mistaken for production readiness. | Users may overtrust a demo artifact. | `SFA-P2-WS-NFR-002` requires non-production claim discipline. |
| Structural validation is mistaken for semantic truth. | Incorrect assurance claims may appear. | `SFA-P2-WS-VAL-001` requires proven versus review-only claim separation. |
| `SFA-P2-WS-FLOW-002` lacks a statement in the adopted plan. | Requirement ambiguity could cause drift. | This PRD records the narrow controlled-transition interpretation and traces it to `/continue` evidence. |

## Acceptance Criteria

| Acceptance criterion | Evidence |
| --- | --- |
| Phase 2 PRD exists and is marked controlled. | This file and source-registry row `SRC-PRD-P2-WALKING-SKELETON`. |
| Draft evidence exists. | `PRDs/drafts/Sys4AI_phase-2_walking_skeleton_prd.draft.md`. |
| Every Phase 2 PRD requirement traces to RDR evidence or Director Decision evidence. | RDR-to-PRD trace table in this file. |
| No Phase 0 or Phase 1 authority is replaced. | Phase boundary and non-goals in this file. |
| Requirement trace validator passes. | Completion receipt for `AJ-SFADEV-18-PHASE2-WALKING-SKELETON-PRD-001`. |
| Source registry includes the new PRD. | `Sys4AI/registries/source_registry.csv`. |

## Deferred Items

| Item | Deferral reason | Expected owner |
| --- | --- | --- |
| Concrete target-system example | `OPEN-P2-001` remains open. | Phase 2 implementation planning packet. |
| Exact package or export artifact shape | `OPEN-P2-002` remains open. | Phase 2 implementation planning packet. |
| Exactly three versus more task packets | `OPEN-P2-003` remains open. | Director Decision or implementation plan. |
| CLI or module surface for walking skeleton | Code is out of this PRD packet. | Later implementation packet. |

## Open Questions

| Open question | Status | Handling |
| --- | --- | --- |
| `OPEN-P2-001`: What concrete target-system example should the walking skeleton use for package or export smoke evidence? | open | Resolve before package smoke implementation. |
| `OPEN-P2-002`: What exact package or export artifact shape should count as smoke evidence? | open | Resolve during implementation planning. |
| `OPEN-P2-003`: Should the Phase 2 flow require exactly three bounded task packets or allow more when trace requires it? | open | Resolve in the implementation plan or Director Decision. |

## References

AngryOwlAI. (2026a). *Sys4AI Phase 0 Product and System-Design PRD* [Repository document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

AngryOwlAI. (2026b). *Sys4AI Phase 1 Implementation Initialization PRD* [Repository document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

AngryOwlAI. (2026c). *Phase 2 walking skeleton Requirements Discovery Record* [Repository control record]. `Sys4AI/control_records/system_definition/phase2_walking_skeleton_requirements_discovery_record.md`.

AngryOwlAI. (2026d). *Sys4AI-dev next-scope full implementation plan* [Repository implementation plan]. `implementation_plans/Sys4AI-dev_next_scope_full_implementation_plan.md`.
