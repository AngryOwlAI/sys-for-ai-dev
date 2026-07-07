# Current State Baseline: Self-Hosting Memory and Continue Kernel

Status: Baseline inspection complete
Date: 2026-07-06
Scope: `Sys4AI-dev` development workspace and nested `Sys4AI/` product scaffold

## Purpose

This note records the pre-implementation baseline for the self-hosting memory and `/continue` implementation plan.

## Inspected authority and scaffold surfaces

- `PRDs/Sys4AI_phase-0_product_system_design_prd.md`
- `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`
- `Sys4AI/README.md`
- `Sys4AI/Makefile`
- `Sys4AI/sys_for_ai/cli.py`
- `Sys4AI/sys_for_ai/validators.py`
- `Sys4AI/sys_for_ai/memory.py`
- `Sys4AI/sys_for_ai/registry_io.py`
- `Sys4AI/sys_for_ai/yaml_io.py`
- `Sys4AI/sys_for_ai/jsonschema_io.py`
- `Sys4AI/registries/*.csv`
- `Sys4AI/control_records/examples/*.yaml`
- `Sys4AI/schemas/contracts/*.schema.json`

## Baseline validation

The following commands passed from the existing scaffold before implementation changes:

```bash
cd Sys4AI
make doctor
make validate
```

Observed environment:

- Python: 3.9.6 inside `Sys4AI/.venv`
- PyYAML: 6.0.3
- TOML parser: `tomli`
- jsonschema: 4.25.1

## Existing implementation shape

The product scaffold starts with a compact CLI, centralized validators, safe YAML/JSON/TOML helpers, CSV registry helpers, generated derivative validation, and a `memory.py` registry bootstrap helper.

The implementation plan requires expanding this into a typed source-first memory package and a deterministic control-loop package. The current `sys_for_ai.memory` import is used by the CLI for `bootstrap_registries`, so the package conversion must preserve that compatibility.

## Baseline gaps to address

- No typed `program_state.yaml` exists.
- No Director Decision Record contract exists.
- No operational AgentJob v0.2 contract exists.
- No memory lookup, search, status, hash, or preflight command exists.
- No generic `/continue` status, preflight, selection, packet, or finalization command exists.
- No diff-to-AgentJob write-boundary validator exists.
- Generated derivative support is validation-only, not generator-backed.
- Active `.agents` and `.codex` skill surfaces do not yet include `continue` or `source-first-memory`.

## Conclusion

The baseline is healthy. The logical next step is Phase 1: add the self-hosting boundary decision record, policy files, program state, schema, registry rows, CLI validation command, and Makefile target.
