# Handoff 0020: Generated Docs And Derivative Governance

Date: 2026-07-07
Plan: `implementation_plans/sys-for-ai-dev_all_recommendations_implementation_plan.md`
Completed slice: WS-09 / AJ-09 - Generated Docs and Derivative Governance

## Latest prior handoff check

The latest controlled handoff before this work was `sys-for-ai/control_records/handoffs/HANDOFF-SFADEV-08-CORE-SKILLS-BATCH-2-001.yaml`. It closed core skill scaffold batch 2 and recommended `AJ-SFADEV-09-GENERATED-DOCS-001`.

## Work completed

- Added deterministic generated governance docs for registry catalog, system layers, artifact contracts, core skills, and role governance.
- Registered the new generated pages in `sys-for-ai/registries/derivative_registry.csv`.
- Added source-registry rows for source, derivative, and object-relationship registries so the generated registry catalog has trace rows.
- Resynchronized existing configuration-control generated pages after control registry updates.
- Added `generate-governance-docs` CLI and Makefile validation wiring.
- Retargeted diff validation and state tests to AJ-09.
- Registered AJ-09 control-loop closeout records and updated program state.

## Validation evidence

- `cd sys-for-ai && make validate-generated-derivatives`
- `cd sys-for-ai && make generate-governance-docs`
- `cd sys-for-ai && .venv/bin/python -m sys_for_ai.cli generate-config-control-wiki --write`
- `cd sys-for-ai && make validate-agentjob-boundaries`
- `cd sys-for-ai && make validate-check-diff`
- `cd sys-for-ai && make validate`
- `cd sys-for-ai && .venv/bin/python -m unittest discover -s tests`
- `git diff --check`

## Remaining uncertainty

The all-recommendations plan remains incomplete. This pass completed generated docs and derivative governance; it did not run final end-to-end acceptance or produce the final acceptance bundle.

## Next logical step

Select `AJ-SFADEV-10-END-TO-END-ACCEPTANCE-001`. Generated derivative coverage is complete, so the next open packet is final validation and acceptance.
