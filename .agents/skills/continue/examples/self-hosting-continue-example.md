# Self-Hosting Continue Example

## Scenario

The operator asks to continue the self-hosting implementation plan.

## Procedure

1. Read the latest `temp_handoff/handoff-*.md`.
2. Inspect `sys-for-ai/control_records/program_state.yaml`.
3. Run:

   ```bash
   cd sys-for-ai
   .venv/bin/python -m sys_for_ai.cli continue-status --json
   .venv/bin/python -m sys_for_ai.cli continue-preflight --json
   .venv/bin/python -m sys_for_ai.cli continue-select --json
   .venv/bin/python -m sys_for_ai.cli continue-packet --json
   ```

4. Work only inside the selected AgentJob boundary.
5. Run validators named by the AgentJob.
6. Write the next `temp_handoff/handoff-*.md`.
7. Commit and report the completed phase.
