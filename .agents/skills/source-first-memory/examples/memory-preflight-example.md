# Memory Preflight Example

## Scenario

A continuation task needs to inspect source-first memory before selecting an AgentJob.

## Commands

```bash
cd Sys4AI
.venv/bin/python -m sys_for_ai.cli memory status --json
.venv/bin/python -m sys_for_ai.cli memory search "source-first memory continue handoff AgentJob" --json
.venv/bin/python -m sys_for_ai.cli memory preflight --agentjob AJ-P1-CONTINUE-SKILLS-001 --query "Phase 9 continue source-first-memory skills" --json
```

## Acceptable Evidence

- Registry rows inspected.
- Canonical source paths inspected.
- Any generated derivative hits labeled as noncanonical.
- Stale or missing evidence recorded as a routing risk.
