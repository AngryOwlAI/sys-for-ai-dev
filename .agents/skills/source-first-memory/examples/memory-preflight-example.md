# Memory Preflight Example

## Scenario

A continuation task needs to inspect source-first memory before selecting an ExecutionTransaction.

## Commands

```bash
cd Sys4AI
.venv/bin/python -m sys_for_ai.cli memory status --json
.venv/bin/python -m sys_for_ai.cli memory search "source-first memory execution transaction handoff" --json
.venv/bin/python -m sys_for_ai.cli memory preflight --execution-transaction TX-EXAMPLE-MEMORY-PREFLIGHT-001 --query "portable source-first memory routing" --json
```

## Acceptable Evidence

- Registry rows inspected.
- Canonical source paths inspected.
- Any generated derivative hits labeled as noncanonical.
- Stale or missing evidence recorded as a routing risk.
