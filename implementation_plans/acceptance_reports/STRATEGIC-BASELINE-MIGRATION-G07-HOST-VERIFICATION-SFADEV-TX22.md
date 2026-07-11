# G-07 Observable Host Verification Report

## Conclusion

`TX-22-G07-HOST-VERIFICATION` verifies the `codex_app_reference` profile for the observed local Codex development-host environment and accepts `G-07` through `DDR-SFADEV-STRATEGIC-BASELINE-G07-001`.

The accepted profile is deliberately mixed rather than universally available:

- `verified_available`: user interaction, workspace filesystem, terminal and tests, and source-first memory and retrieval;
- `environment_dependent`: tools/connectors/network and task/thread state;
- `permission_dependent`: sub-agents; and
- `verified_unavailable`: target runtime.

`G-07` acceptance verifies capabilities and limitations against current observable behavior. It does not grant transaction permission, production readiness, operational authority, deployment authority, broad stakeholder consensus, target-domain acceptance, or `G-10` acceptance.

## Reviewed Baseline And Scope

- Baseline commit before TX-22 writes: `ddd87b3c0a9bdf1656eb35e3e160d157482718dc`.
- Shared baseline condition: `HEAD == origin/main` and the worktree was clean.
- Host: local Codex desktop task, saved `Sys4AI-dev` project, and governed shell/tool surfaces available to this task.
- Subject layer: `framework_product` observed through the `development_system` workspace.
- Target runtime: outside scope and verified unavailable in this environment.
- Evidence checked at: `2026-07-11T15:19:10Z`.
- Freshness horizon: `2026-07-18T15:19:10Z`.
- Memory preflight: `MEMPREFLIGHT-TX-22-G07-HOST-VERIFICATION-20260711T151753Z`, `PASS_WITH_WARNINGS`, zero derivative authority inversions.

## Probe Method

Each interface received a safe positive probe and a denial-or-absence probe where possible. A negative probe establishes failure reporting or a current limitation; it does not manufacture a platform denial. No secret, destructive command, connector mutation, external write, deployment, target runtime, or sub-agent was used.

### User interaction

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-USER-INTERACTION-POS-001` | Read the current user instruction through the current task and the read-only task-state surface. | The accountable user's exact authorization for `G-07` and evidence closure was preserved in the active task. |
| `HOST-G07-USER-INTERACTION-NEG-001` | Compare current direct authorization with the prior blocked handoff and fail-closed authority rules. | Prior narration and the blocked TX-21 handoff did not authorize execution; the current explicit instruction supplied the new bounded authority. Silence or stale narration remains non-consent. |

Disposition: `verified_available`, executable only inside a separately valid permission envelope.

### Workspace filesystem

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-WORKSPACE-FILESYSTEM-POS-001` | Read the controlled plan and host profile; run the repository preflight writer for the authorized TX-22 receipt. | Controlled reads and one governed repository write succeeded. Git exposed the new receipt as an untracked workspace change. |
| `HOST-G07-WORKSPACE-FILESYSTEM-NEG-001` | Test the deliberately absent path `Sys4AI/control_records/THIS-PATH-MUST-NOT-EXIST`. | The absence check returned nonzero without inventing file content. This verifies truthful missing-resource handling, not a sandbox boundary. |

Disposition: `verified_available` for this local task. Readability does not grant authority over every file, and host-level filesystem policy may differ in later tasks.

### Terminal and tests

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-TERMINAL-TESTS-POS-001` | Run `pwd`, `git status --short --branch`, and the product Python interpreter from explicit working directories. | Working directory, output, exit code, and Python `3.9.6` were captured correctly. |
| `HOST-G07-TERMINAL-TESTS-NEG-001` | Run a command that exits `23`; start `sleep 300` in a PTY and send `Ctrl-C`. | The nonzero exit was preserved. The long-running process was interrupted and returned `^C` with nonzero exit status. |

Disposition: `verified_available`. Cancellation evidence is limited to the observed local shell process; it does not prove cancellation for tools, connectors, tasks, sub-agents, or target runtimes.

### Tools, connectors, and network

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-TOOLS-NETWORK-POS-001` | Use the typed web-search tool with an official OpenAI-domain restriction. | The tool returned current official Codex material without an external mutation. |
| `HOST-G07-TOOLS-NETWORK-NEG-001` | Run the current Codex-manual helper. | The helper failed closed because the response lacked the required `x-content-sha256` header; no success was inferred. |

Disposition: `environment_dependent`, non-executable by default. Tool inventory, authentication, connector permission, network reachability, and side-effect authority vary by task and mechanism. The official Codex use-cases page was supplementary context, not capability authority.

### Sub-agents

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-SUBAGENTS-POS-001` | Inspect the callable collaboration surface and current concurrency metadata without spawning a child. | A collaboration surface is present in the host capability inventory. |
| `HOST-G07-SUBAGENTS-NEG-001` | Apply the current governing multi-agent policy. | Spawning is prohibited unless the user or an applicable repository/skill instruction explicitly requests delegation. No child was created. |

Disposition: `permission_dependent`, non-executable in TX-22. Interface presence does not delegate user authority, permission, or source ownership.

### Task and thread state

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-TASK-STATE-POS-001` | List saved projects and recent tasks, then read the active Sys4AI-dev task. | The saved project, active task ID, current user instruction, working directory, and in-progress status were readable. |
| `HOST-G07-TASK-STATE-NEG-001` | Read the app-terminal state without creating a terminal session. | The host reported that no app terminal session was attached. Task/thread mutation, handoff, archive, and task cancellation were not exercised. |

Disposition: `environment_dependent`, non-executable by default. Read-only state was observed; mutating state remains separately authorized and unverified.

### Memory and retrieval

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-MEMORY-RETRIEVAL-POS-001` | Run memory status, handoff lookup, targeted search, and a source-first preflight; inspect returned canonical paths and registry rows. | Status was `PASS_WITH_WARNINGS`; the host profile, validator, safety packet, plan-related sources, and TX-21 handoff were resolved without authority inversion. |
| `HOST-G07-MEMORY-RETRIEVAL-NEG-001` | Lookup `HOST-PROBE-NONEXISTENT-OBJECT`. | The lookup returned `ok: false`, `result: null`, and nonzero exit status. No absent memory object was inferred. |

Disposition: `verified_available` for repository source-first navigation. Memory remains noncanonical and cannot override inspected sources.

### Target runtime

| Probe ID | Method | Observed result |
|---|---|---|
| `HOST-G07-TARGET-RUNTIME-POS-001` | Inspect the target-package manifest and acceptance evidence. | The only package is explicitly a `smoke_example`, `derivative_draft`, and non-production demonstration. |
| `HOST-G07-TARGET-RUNTIME-NEG-001` | Search for `.openai/hosting.json` and inspect current production/operations authority. | No hosting configuration was found; TX-21 evidence retains production readiness and operational authority as open. |

Disposition: `verified_unavailable`, non-executable. No deployment, telemetry, incident owner, operational rollback, kill control, or target authorization exists in this profile.

## Permission And Threat Disposition

| Risk | Control | Residual state |
|---|---|---|
| Capability interpreted as permission | Fixed precedence plus per-transaction permission envelope | Mitigated; values, goals, roles, and availability cannot grant permission. |
| Conditional interface treated as available | Conditional statuses are non-executable and require fresh task-specific evaluation | Mitigated. |
| External side effect inferred from tool presence | No connector mutation or external write was probed; uncertain results fail closed | Mitigated for TX-22; deferred per future tool call. |
| Delegation inferred from collaboration surface | Current policy prohibited spawning and no child was created | Mitigated. |
| Development host confused with target runtime | System-layer classification and verified-unavailable target-runtime state | Mitigated. |
| Evidence staleness | Seven-day freshness horizon plus explicit review triggers | Mitigated until `2026-07-18T15:19:10Z`; stale thereafter. |
| Production or operational promotion inferred from G-07 | DDR and profile deny production and operational authority | Blocked. |

## Gate Disposition

`DDR-SFADEV-STRATEGIC-BASELINE-G07-001` accepts `G-07` for profile version `1.0.0` and the exact mixed interface state above. Host-dependent claims may cite this profile only when the required interface is `verified_available`, its evidence is current, and the consuming transaction independently supplies authorization and permission.

The following remain open after TX-22:

- 200 planned verifications;
- 137 scaffolded and 5 absent capabilities;
- 135 partial coverage rows and 7 `needs_evidence` semantic verdicts;
- quantitative strategic success results;
- confidential, rotated, external independent evaluation;
- production ownership, monitoring, incident, maintenance, and operational evidence; and
- `G-10` final acceptance.

## Verification Summary

- Focused host, program-state, trace, and generated-reader suite: 57/57 passed.
- Target-package, walking-skeleton, and safety reconciliation suite: 51/51 passed.
- Full product suite: 247/247 passed.
- Repository-root `make validate`: passed on the final TX-22 tree.
- Host profile, Director Decision, program state, execution transaction, receipts, handoff, registries, target package, walking skeleton, schemas, and generated derivatives: passed through aggregate validation.
- Requirement trace: unchanged at 227 rows and generalized SHA-256 `b868e4d201bf1a5908cd87357f51214be9081684e56c04f9cd48850653958138`.
- Memory: `PASS_WITH_WARNINGS`; 1023 objects, 452 known pending-hash warnings, zero derivative authority inversions.
- `git diff --check`: passed.

## References

AngryOwlAI. (2026, July 9). *Sys4AI-dev strategic baseline migration full implementation plan* [Implementation plan].

OpenAI. (2026). *Codex use cases*. https://developers.openai.com/codex/use-cases

Sys4AI-dev. (2026a, July 10). *Codex App reference-host integration profile* [Host interface contract].

Sys4AI-dev. (2026b, July 11). *Strategic baseline migration final acceptance audit* [Acceptance report].
