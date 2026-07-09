# Strategic Baseline Migration WS-00 Completion Receipt

Receipt ID: `CR-SFADEV-STRATEGIC-BASELINE-WS00-001`
Transaction: `TX-00-BASELINE`
Workstream: `WS-00`
Plan: `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`
Result: `PASS_WITH_WARNINGS`
Capture date: 2026-07-09
Capture window: 2026-07-09T20:50:02Z through 2026-07-09T20:51:55Z
Baseline commit: `15a9b17635db2cc76d3f1003f60ea20e46a4e313`
Subject system: `Sys4AI-dev` development system and `Sys4AI` framework product
Subject layer: `development_system` completion evidence about multiple inspected layers
Source authority status: `controlled` completion evidence; not a requirements baseline
Change class: additive baseline evidence

## 1. Conclusion

`TX-00-BASELINE` is complete as a local evidence change. The post-retraction
state is reproducible, the historical boundary is protected by immutable Git
evidence, and the removed-surface inventory accounts for every match in the
Git-visible scan scope plus the current strategic migration plan.

The repository is structurally green but semantically inconsistent. The
executable `/continue`, AgentJob-authoring, control-loop, CLI, and Make surfaces
removed by commit `15a9b17` remain absent, while canonical requirements,
controlled policies, schemas, registries, validators, and the accepted Phase 2
flow still prescribe or model those surfaces.

This receipt does not approve an execution-model route, deprecate AgentJob,
make AgentJob an optional profile, modify a PRD, or authorize `TX-01-RDR`.

## 2. Authority and Layer Preflight

The implementation request authorizes the read-mostly `TX-00-BASELINE` scope
and this completion evidence. It does not supply the named human approvals for
the later identity, strategic-intent, execution-model, host, or production
gates.

| Inspected surface | Layer | Observed authority or state | Write decision |
|---|---|---|---|
| `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md` | `development_system` planning | Draft planning artifact; not a canonical requirements baseline | Preserved unchanged |
| `PRDs/README.md` and Phase 0, Phase 1, and Phase 2 PRDs | `framework_product` | Canonical, canonical draft, and controlled requirements sources | Read only |
| `Sys4AI/registries/system_layer_registry.csv` | `framework_product` | Controlled layer registry | Read only |
| `Sys4AI/control_records/program_state.yaml` | `framework_product` legacy state | Complete; no active Director Decision or AgentJob | Read only; classified stale for migration |
| `.agents/skills/` | `development_system` | Active runtime skills | Read only |
| `Sys4AI/skills/core/` and `Sys4AI/templates/` | `target_system_template` | Portable scaffold surfaces | Read only |
| `Sys4AI/examples/target_systems/repo_steward_agent_package/` | `target_system_instance` smoke example | `derivative_draft` | Read only |
| `Sys4AI/docs/generated/` | `derivative_surface` | Generated and noncanonical | Read only |

No canonical PRD, historical control record, runtime skill, or target package
was changed by this transaction. The registered receipt caused one
deterministic refresh of the noncanonical generated registry catalog.

| Changed path | Authority class | Change |
|---|---|---|
| `implementation_plans/completion_receipts/CR-SFADEV-STRATEGIC-BASELINE-WS00-001.md` | Controlled completion evidence | Added this baseline, inventory, manifest, and validation receipt |
| `Sys4AI/registries/source_registry.csv` | Controlled source registry | Registered this receipt |
| `Sys4AI/docs/generated/registry_catalog/index.md` | Generated derivative | Deterministically refreshed from the source registry |

## 3. Source-First Memory Preflight

Memory was used only to locate likely sources.

| Check | Result | Material evidence |
|---|---|---|
| `python -m sys_for_ai.cli memory status --json` | `PASS_WITH_WARNINGS` | 333 warnings, all observed as pending `source_hash` values |
| Registered search for `strategic baseline migration AgentJob continue` | PASS | Returned controlled registries, prior plans, trace sources, and one generated derivative |
| Generated hit handling | PASS | `docs/generated/configuration_control/yaml-control-records.md` was rejected as authority |
| Source inspection | PASS | Inspected `PRDs/README.md`, `program_state.yaml`, `system_layer_registry.csv`, `agentjob_registry.csv`, `control_record_registry.csv`, `requirement_trace_registry.csv`, and `source_registry.csv` |

The 333 pending hashes limit freshness claims. They do not invalidate the
Git-backed baseline captured below, but they remain explicit migration debt.

## 4. Repository Baseline

| Fact | Observation |
|---|---|
| Branch | `main` tracking `origin/main` |
| `HEAD` | `15a9b17635db2cc76d3f1003f60ea20e46a4e313` |
| `origin/main` | `15a9b17635db2cc76d3f1003f60ea20e46a4e313` |
| Worktree before this receipt | Only the supplied strategic migration plan was untracked |
| Retraction commit | `15a9b17 Remove continue and AgentJob runtime surfaces` |
| Program state | `state_status: complete`; `active_director_decision_id: null`; `active_agentjob_id: null` |
| PRD authority | Phase 0 canonical; Phase 1 canonical draft; Phase 2 controlled; older Phase 0 historical |
| Trace validator summary | 192 Phase 0 rows; 81 Phase 1 requirements; 79 implemented, 105 scaffolded, 8 deferred; 113 semantically sufficient |
| Memory status | `PASS_WITH_WARNINGS`; 333 pending-hash warnings |

`git show --stat 15a9b17` reports 158 changed files, 334 insertions, and
2,575 deletions. The deleted runtime surface includes the `/continue` and
AgentJob-authoring skills, `Sys4AI/sys_for_ai/control_loop/`, related CLI and
Make targets, and runtime tests.

## 5. Validation Record

Every command below ran against commit `15a9b17`. Exit status `0` means the
command passed; warnings are preserved separately rather than flattened into
the pass result.

| Command | UTC start | UTC end | Exit |
|---|---:|---:|---:|
| `make validate-rename` | 20:50:02.378 | 20:50:02.532 | 0 |
| `make validate-dev-skills` | 20:50:02.532 | 20:50:02.663 | 0 |
| `make validate-product-scaffold` | 20:50:02.663 | 20:50:10.934 | 0 |
| `make validate` | 20:50:10.934 | 20:50:19.225 | 0 |
| `cd Sys4AI && make validate-system-layers` | 20:50:19.225 | 20:50:19.411 | 0 |
| `cd Sys4AI && make validate-artifact-contracts` | 20:50:19.411 | 20:50:19.605 | 0 |
| `cd Sys4AI && make validate-prd-modules` | 20:50:19.605 | 20:50:19.782 | 0 |
| `cd Sys4AI && make validate-requirement-trace` | 20:50:19.782 | 20:50:21.292 | 0 |
| `cd Sys4AI && make validate-target-package-smoke` | 20:50:21.292 | 20:50:21.422 | 0 |
| `cd Sys4AI && make validate-generated-derivatives` | 20:50:21.422 | 20:50:21.561 | 0 |

Additional absence verification passed:

- `Sys4AI/.venv/bin/python Sys4AI/tests/test_skill_surfaces.py -q` ran 11 tests successfully.
- The deleted runtime skill directories and `Sys4AI/sys_for_ai/control_loop/` are absent.
- The removed continuation, AgentJob validation, diff-boundary, and control-loop targets are absent from `Sys4AI/Makefile` and `Sys4AI/sys_for_ai/cli.py`.

An initial attempt to use `pytest` could not run because `pytest` is not an
installed project dependency. The same tracked test module passed with its
native `unittest` runner; no dependency was added.

## 6. Capability-Reference Inventory

### 6.1 Scan contract

The inventory scans Git-tracked files under every WS-00 minimum root and adds
the current untracked strategic migration plan explicitly. Ignored caches,
virtual environments, and local `temp_prd.md` checkpoints are excluded because
they are not repository source authority.

The case-insensitive pattern covers:

```text
/continue, AgentJob, agentjob, control_loop,
continue-status, continue-preflight, continue-select, continue-packet,
continue-finalize, validate-agentjob, validate-agentjobs,
validate-agentjob-registry, validate-agentjob-boundaries,
validate-check-diff, validate-one-active-agentjob, validate-control-loop
```

Classification is conservative and file-level. Mixed registries are therefore
`active_but_stale` when any active row or schema contract still models the
removed execution surface. Completed control records and prior implementation
plans are `historical`; derivative PRD modules, generated docs, and the target
smoke example are `generated_derivative` for this inventory's allowed taxonomy.

### 6.2 Exhaustive classification totals

| Classification | Files | Matches | Decision |
|---|---:|---:|---|
| `active_and_valid` | 2 | 98 | Current migration plan and the runtime-absence regression test |
| `active_but_stale` | 109 | 1,049 | Requires RDR and authority decision before migration |
| `historical` | 176 | 2,759 | Preserve; never rewrite to make current semantics appear consistent |
| `generated_derivative` | 57 | 344 | Regenerate only after canonical approval |
| `deprecated` | 0 | 0 | Cannot be assigned before `WS-02` authority decision |
| `removed` | 0 | 0 | Runtime paths are absent; references are classified by their owning file |
| `optional_profile` | 0 | 0 | Cannot be assigned before `WS-02` authority decision |
| `false_positive` | 0 | 0 | No match was discarded as a false positive |
| **Total** | **344** | **4,250** | Complete Git-visible inventory plus current plan |

The two valid files are:

| Path | Matches | Reason |
|---|---:|---|
| `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md` | 91 | Defines the migration problem and explicitly prohibits implicit restoration |
| `Sys4AI/tests/test_skill_surfaces.py` | 7 | Positively verifies that removed runtime skill surfaces remain absent |

### 6.3 Active-but-stale coverage by root

| Root | Files | Matches |
|---|---:|---:|
| `PRDs/` | 5 | 108 |
| `.agents/` | 19 | 29 |
| `Sys4AI/configs/` | 1 | 2 |
| `Sys4AI/control_records/` | 1 | 4 |
| `Sys4AI/docs/` excluding generated docs | 8 | 18 |
| `Sys4AI/registries/` | 20 | 660 |
| `Sys4AI/schemas/` | 19 | 42 |
| `Sys4AI/skills/` | 17 | 30 |
| `Sys4AI/sys_for_ai/` | 11 | 119 |
| `Sys4AI/templates/` | 3 | 9 |
| `Sys4AI/tests/` excluding the absence test | 5 | 28 |
| **Total** | **109** | **1,049** |

Highest-impact active paths include:

| Path | Matches | Conflict surface |
|---|---:|---|
| `PRDs/Sys4AI_phase-0_product_system_design_prd.md` | 68 | Canonical AgentJob and `/continue` requirements |
| `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md` | 15 | AgentJob schemas, examples, validators, and acceptance |
| `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md` | 17 | Accepted AgentJob and `/continue` flow |
| `Sys4AI/control_records/program_state.yaml` | 4 | Legacy active-AgentJob state fields and actions |
| `Sys4AI/registries/control_record_registry.csv` | 213 | AgentJob contracts and historical/runtime rows |
| `Sys4AI/registries/source_registry.csv` | 196 | Registered AgentJob-era sources and implementation claims |
| `Sys4AI/registries/requirement_trace_registry.csv` | 84 | Capability evidence and status claims |
| `Sys4AI/sys_for_ai/validators.py` | 57 | Active AgentJob schemas, fields, and registry validation |
| `Sys4AI/sys_for_ai/walking_skeleton.py` | 29 | Hard-coded AgentJob nodes and paths |
| `Sys4AI/docs/skill_integration_policy.md` | 5 | Deleted runtime path and AgentJob authority language |
| `Sys4AI/docs/self_hosting_mode_policy.md` | 5 | Mandatory AgentJob transaction model |

The eight core trace rows for `SFA-CORE-AJ-001` through `003`,
`SFA-CORE-CONT-001` through `002`, and `SFA-P0-FR-017` through `019` are all
`partial`, `scaffolded`, and `sufficient`. Their notes and evidence still claim
continuation implementation. Those structural statuses are stale relative to
the retraction commit and require the generalized capability/evidence model in
later workstreams.

### 6.4 Historical and derivative group coverage

| Classification | Path group | Files | Matches |
|---|---|---:|---:|
| `historical` | `implementation_plans/**` excluding the current strategic plan | 22 | 1,105 |
| `historical` | `PRDs/Sys4AI_phase-0_prd.md` | 1 | 67 |
| `historical` | `PRDs/drafts/**` | 1 | 7 |
| `historical` | `Sys4AI/control_records/agentjobs/**` | 37 | 415 |
| `historical` | `Sys4AI/control_records/completions/**` | 29 | 340 |
| `historical` | `Sys4AI/control_records/director_decisions/**` | 22 | 243 |
| `historical` | `Sys4AI/control_records/handoffs/**` | 29 | 261 |
| `historical` | `Sys4AI/control_records/memory_preflights/**` | 29 | 259 |
| `historical` | `Sys4AI/control_records/system_definition/**` | 2 | 52 |
| `historical` | Other completed/example control records | 4 | 10 |
| `generated_derivative` | `PRDs/modules/**` | 13 | 32 |
| `generated_derivative` | `Sys4AI/docs/generated/**` | 40 | 307 |
| `generated_derivative` | `Sys4AI/examples/target_systems/**` | 4 | 5 |

These groups plus sections 6.2 and 6.3 account for all 344 files and all 4,250
matches. Reproduction must use the tracked file set from `git ls-files` and add
the current strategic plan until that plan is committed.

## 7. Conflict Inventory

| Conflict | Baseline evidence | TX-00 disposition |
|---|---|---|
| `CONFLICT-EXEC-001` | Canonical Phase 0 has 68 removed-surface matches; runtime skills and control loop are absent | Open; route decision required |
| `CONFLICT-EXEC-002` | Accepted Phase 2 has 17 removed-surface matches and names removed CLI/Make validation behavior | Open; controlled addendum or successor required |
| `CONFLICT-TRACE-001` | Eight key rows remain `scaffolded` and semantically sufficient; broader trace totals include 79 implemented rows | Open; capability/evidence-state migration required |
| `CONFLICT-STATE-001` | `program_state.yaml` is complete but retains `active_agentjob_id` and AgentJob actions | Open; portable transaction state decision required |
| `CONFLICT-POLICY-001` | Self-hosting and skill-integration policies require AgentJobs or name deleted runtime paths | Open; supersession required after decision |
| `CONFLICT-ROLE-001` | Role and execution registries retain AgentJob-specific fields | Open; atomic registry/schema migration required |
| `CONFLICT-ART-001` | Artifact and validation contracts still treat AgentJob as an active controlled artifact | Open; portable contract and lifecycle classification required |
| `CONFLICT-WALK-001` | `walking_skeleton.py` has 29 hard-coded AgentJob references | Open; generalize only after Phase 2 authority changes |
| `CONFLICT-PACK-001` | Target-package validator requires the word `agentjob` | Open; replace only after execution vocabulary approval |
| `CONFLICT-PLAN-001` | Prior plans contain 1,105 historical matches | Preserve as historical; later navigation may remove current operational authority |
| `CONFLICT-VISION-001` | Historical Phase 0 remains separate from canonical Phase 0 | Preserve; content migration requires provenance and approval |
| `CONFLICT-VALIDATION-001` | All prescribed validators pass despite the conflicts above | Open; semantic and capability validators required |

## 8. Historical-Protection Manifest

Git object IDs are immutable evidence at the baseline commit. Directory entries
are Git tree IDs; file entries are Git blob IDs. SHA-256 is included for the
three specifically protected PRDs.

| Protected path | Git object | SHA-256 or scope |
|---|---|---|
| `PRDs/Sys4AI_phase-0_prd.md` | `ed4260e2ef143e22ce63bae98ee5e6e6db7c6c59` | `41f2548c95f00c4e028b5bb86d948010b88ed334d5ec933c67c7e262a1e3c756` |
| `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md` | `573127d5fc6e237568dfb7340ecc294debc6066f` | `98567cf4f4af8ca99650a6220a78d840dae5e11195891fc808c69c4828528038` |
| `PRDs/drafts/Sys4AI_phase-2_walking_skeleton_prd.draft.md` | `d1d109e7746b8b51c627472b0b527f0be2c429ac` | `9e290964200137329827a0164f50c2d3e97dc194fac65dd086c8b1dd7e57d84f` |
| `implementation_plans/` | `46c47d7657e02ad20b2da5578c7fdecc2835900f` | Baseline tree at `15a9b17`; excludes the later untracked strategic plan |
| `implementation_plans/completion_audits/` | `6eb0157d7f27ce1e5f0750c3f5927fb807156051` | Completed audit tree |
| `implementation_plans/completion_receipts/` | `afb5b3fccb200ab8234aa8a3e2cede662c08bf8c` | Completed plan-receipt tree |
| `Sys4AI/control_records/director_decisions/` | `9e9dc88b4f833bfea10ec91858d30bb51a4e33e7` | Historical decision tree |
| `Sys4AI/control_records/agentjobs/` | `ae0c80c9695dfad9f1c4f1491780a5214c5105af` | Historical and superseded AgentJob record tree |
| `Sys4AI/control_records/completions/` | `46a94872113f4f76e74ad1735bd86f35933e93ff` | Historical completion tree |
| `Sys4AI/control_records/handoffs/` | `85fe00e94e3dce89f8447f48b2f49dbe470fc0fe` | Historical handoff tree |
| `Sys4AI/schemas/agentjob.schema.yaml` | `dbdb6e427291bafa75ee8b889576673948079a98` | Legacy schema-like source |
| `Sys4AI/schemas/contracts/agentjob.schema.json` | `5ed5a70fe9e9d47e22c7b5126bef27b4aae3f91a` | Legacy AgentJob contract |
| `Sys4AI/schemas/contracts/agentjob_v0_2.schema.json` | `7cfde91630dfda6a174c0bd0dd711b63824863db` | Operational historical AgentJob contract |
| `Sys4AI/schemas/contracts/agentjob_registry_row.schema.json` | `fcb1c06327df06d70b348596e1b8e134a56b2a8c` | Legacy registry-row contract |

Rollback is limited to removing this new receipt and its new source-registry
row. No protected artifact may be rewritten during rollback.

## 9. Material Warnings and Limits

1. The memory catalog reports 333 pending source hashes.
2. Aggregate validation emits walking-skeleton planning warnings even though the
   tracked demo receipt and target package are present and their focused checks
   pass.
3. Existing validators prove structural consistency, not current capability or
   PRD semantic truth.
4. The first post-write aggregate validation correctly detected registry-catalog
   drift after the receipt was registered. `generate-governance-docs --write`
   refreshed only `Sys4AI/docs/generated/registry_catalog/index.md`; the final
   aggregate `make validate` passed at 2026-07-09T20:57:58Z.
5. The implementation plan remains a draft with its approval table unchanged.
6. This local transaction has no commit or push evidence. Under the plan's
   transaction closeout rule, `TX-01-RDR` must not begin until this evidence is
   committed and pushed or an equivalent shared baseline is established.

## 10. Acceptance Decision and Next Gate

WS-00 acceptance criteria are satisfied locally:

- All prescribed baseline and targeted commands have recorded passing results.
- The removed-surface inventory accounts for all 4,250 Git-visible matches.
- Historical paths have immutable Git evidence and selected SHA-256 hashes.
- Pending-hash and validation limitations are documented.
- No canonical or historical artifact was modified; the only derivative change
  was a deterministic catalog refresh caused by registering this receipt.

The logical next transaction is `TX-01-RDR`, but it remains gated by the plan's
approval and shared-baseline requirements. It must create the controlled
strategic-baseline migration Requirements Discovery Record; it must not edit
Phase 0 or restore the removed runtime.

## References

AngryOwlAI. (2026a). *Sys4AI Phase 0 product and system-design PRD* [Product requirements document]. `PRDs/Sys4AI_phase-0_product_system_design_prd.md`.

AngryOwlAI. (2026b). *Sys4AI Phase 1 implementation initialization PRD* [Product requirements document]. `PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

AngryOwlAI. (2026c). *Sys4AI Phase 2 walking skeleton PRD* [Product requirements document]. `PRDs/Sys4AI_phase-2_walking_skeleton_prd.md`.

Sys4AI-dev. (2026). *Strategic baseline migration full implementation plan* [Implementation plan]. `implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.
