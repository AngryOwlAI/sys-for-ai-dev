# Continue Loop Policy

**Status:** Draft  
**Scope:** Generic `/continue` kernel for `sys-for-ai` Phase 1

---

## Policy

`/continue` is a bounded control-loop resolver. It resumes from tracked state, inspects the latest handoff, runs source-first memory preflight, and selects at most one authorized AgentJob.

## Required sequence

1. Load `control_records/program_state.yaml`.
2. Validate program state.
3. Run memory preflight.
4. Inspect the latest handoff if one is recorded.
5. Select or reuse one AgentJob.
6. Emit an execution packet or a stop packet.
7. Validate completion evidence before updating state.
8. Write a completion receipt and handoff when the state changes.

## Stop conditions

The loop must stop when:

- no Director decision authorizes the next route;
- more than one active AgentJob exists;
- memory preflight is not usable for routing;
- a required write is outside the selected AgentJob boundary;
- a human gate is required.

## Non-goal

The Phase 1 `/continue` kernel does not provide autonomous multi-task execution. It provides deterministic routing, evidence, and transaction boundaries.
