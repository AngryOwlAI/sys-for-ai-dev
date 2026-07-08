# Sys4AI Phase 2 Walking Skeleton PRD Draft

**Document status:** Draft for trace validation.
**Product name:** Sys4AI.
**Phase:** Phase 2 walking skeleton.
**Depends on:** Phase 0 PRD, Phase 1 PRD, and `RDR-SFADEV-P2-WS-001`.
**Last updated:** 2026-07-08.
**Draft AgentJob:** `AJ-SFADEV-18-PHASE2-WALKING-SKELETON-PRD-001`.

## Executive Summary

This draft converts the validated Phase 2 walking skeleton Requirements Discovery Record into baselined Phase 2 product requirements. The walking skeleton is a controlled proof path for Sys4AI: it starts with target-system intent, passes through `/init`, creates an RDR, creates this PRD, creates an implementation plan, creates bounded AgentJobs, records validation evidence, and ends with a package or export smoke artifact.

The draft does not replace the Phase 0 or Phase 1 PRDs. It narrows a Phase 2 slice that demonstrates the existing framework governance in a concrete end-to-end flow.

## Phase Boundary

This PRD authorizes planning and later implementation of the Phase 2 walking skeleton. It does not authorize production runtime claims, autonomous operation claims, domain semantic correctness claims, or target-system package creation in this PRD packet.

## Baselined Requirements

| Requirement ID | Requirement | RDR or decision trace | Verification seed |
| --- | --- | --- | --- |
| `SFA-P2-WS-FLOW-001` | Sys4AI shall provide a walking skeleton flow from user target-system intent through `/init`, RDR, PRD, implementation plan, AgentJobs, validation evidence, and target-system package or export smoke output. | `REQ-CAND-P2-001`; `REQ-CAND-P2-002`; `REQ-CAND-P2-003`; `REQ-CAND-P2-004`; `REQ-CAND-P2-005`; `REQ-CAND-P2-006`; `REQ-CAND-P2-007` | `VVE-P2-001` through `VVE-P2-007` |
| `SFA-P2-WS-FLOW-002` | Sys4AI shall expose each walking skeleton transition as controlled status evidence through `/continue` handoffs, receipts, and program-state updates. | `DRV-P2-003`; `REQ-CAND-P2-005`; `REQ-CAND-P2-007`; `NFR-CAND-P2-002` | `VVE-P2-005`; `VVE-P2-007`; `VVE-P2-009` |
| `SFA-P2-WS-RDR-001` | The walking skeleton shall consume a validated Requirements Discovery Record before PRD synthesis. | `REQ-CAND-P2-002`; `CON-P2-002` | `VVE-P2-002`; `VVE-P2-003` |
| `SFA-P2-WS-PRD-001` | The walking skeleton shall produce a Phase 2 PRD that traces each baselined requirement to the Phase 2 RDR or an approved Director Decision. | `REQ-CAND-P2-003`; `DRV-P2-002` | `VVE-P2-003` |
| `SFA-P2-WS-PLAN-001` | The walking skeleton shall produce an implementation plan from the Phase 2 PRD using the active `prd-to-implementation-plan` skill or an equivalent governed procedure. | `REQ-CAND-P2-004`; `DRV-P2-002` | `VVE-P2-004` |
| `SFA-P2-WS-AJ-001` | The walking skeleton shall produce at least three bounded AgentJob or task-packet artifacts from the implementation plan. | `REQ-CAND-P2-005`; `DRV-P2-003`; `OPEN-P2-003` | `VVE-P2-005` |
| `SFA-P2-WS-PACKAGE-001` | The walking skeleton shall produce a sample target-system package or export surface containing a README, manifest, requirements trace, and task packet index. | `REQ-CAND-P2-006`; `DRV-P2-004`; `OPEN-P2-001`; `OPEN-P2-002` | `VVE-P2-006` |
| `SFA-P2-WS-TRACE-001` | The walking skeleton shall preserve trace from RDR candidate requirements through PRD requirements, implementation plan tasks, AgentJobs, validation evidence, and package outputs. | `REQ-CAND-P2-003`; `REQ-CAND-P2-004`; `REQ-CAND-P2-005`; `REQ-CAND-P2-006`; `REQ-CAND-P2-007`; `NFR-CAND-P2-002` | `VVE-P2-003` through `VVE-P2-007`; `VVE-P2-009` |
| `SFA-P2-WS-VAL-001` | The walking skeleton shall run structural validators and report which claims are proven by validation and which claims remain semantic or human-review obligations. | `REQ-CAND-P2-007`; `SFA-P0-FR-042` | `VVE-P2-007` |
| `SFA-P2-WS-NFR-001` | Generated artifacts shall remain derivative until accepted through source-authority workflow. | `NFR-CAND-P2-001`; `CON-P2-003` | `VVE-P2-008` |
| `SFA-P2-WS-NFR-002` | The walking skeleton shall not claim production runtime readiness, autonomous operation readiness, or domain semantic correctness. | `NFR-CAND-P2-003`; `RISK-P2-002` | `VVE-P2-010` |

## Draft Validation Notes

- `SFA-P2-WS-FLOW-002` is present in the adopted implementation plan ID scheme without a separate statement. This draft defines it as the controlled transition-evidence requirement because that is the narrowest interpretation supported by `DRV-P2-003`, `/continue`, and Phase 0 control-loop requirements.
- `OPEN-P2-001`, `OPEN-P2-002`, and `OPEN-P2-003` remain non-blocking planning inputs. They do not block this PRD because the PRD constrains later planning instead of choosing the package scenario here.
- Acceptance of this draft requires source-registry registration, PRD trace inspection, and completion evidence from `AJ-SFADEV-18-PHASE2-WALKING-SKELETON-PRD-001`.

## References

AngryOwlAI. (2026a). *Sys4AI Phase 0 Product and System-Design PRD* [Repository document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

AngryOwlAI. (2026b). *Sys4AI Phase 1 Implementation Initialization PRD* [Repository document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

AngryOwlAI. (2026c). *Phase 2 walking skeleton Requirements Discovery Record* [Repository control record]. `Sys4AI/control_records/system_definition/phase2_walking_skeleton_requirements_discovery_record.md`.

AngryOwlAI. (2026d). *Sys4AI-dev next-scope full implementation plan* [Repository implementation plan]. `implementation_plans/Sys4AI-dev_next_scope_full_implementation_plan.md`.
