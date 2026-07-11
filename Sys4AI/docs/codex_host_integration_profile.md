# Codex App Reference-Host Integration Profile

- Status: Controlled observable development-host profile accepted at `G-07`
- Profile ID: `codex_app_reference`
- Profile version: `1.0.0`
- Verification scope: Observable development-host conformance
- Portable execution binding: `1.0.0`, executable only for current `verified_available` interfaces inside a separately authorized transaction
- Contract authority: `DDR-SFADEV-STRATEGIC-BASELINE-G04-001`
- Verification authority: `DDR-SFADEV-STRATEGIC-BASELINE-G07-001`

## 1. Purpose And Authority Boundary

This document defines the Codex App reference-host interface contract for
`Sys4AI`. It explains how the verified host profile maps portable
framework needs to host mechanisms without placing Codex mechanics in portable
field names, requirement identities, target purpose, or target authority.

The TOML profile and the TX-22 probe report jointly record current evidence.
`G-07` is accepted for the exact observed mixed state: four interfaces are
`verified_available`, three are conditional and non-executable, and target
runtime is `verified_unavailable`. The profile becomes stale after
`2026-07-18T15:19:10Z` unless reverified.

The host profile has no authority to define or approve:

- Sys4AI or target-system purpose, vision, or values;
- requirements, acceptance, permissions, or production readiness;
- stakeholder consent or accountable human approval;
- a portable execution transaction; or
- a target runtime, deployment, release, or incident decision.

Platform and system constraints, host permissions, project authorization, and
explicit human authority remain binding independently of profile content.

## 2. Artifact Contract

| Property | Controlled value |
|---|---|
| Profile source | `Sys4AI/configs/host_profiles/codex_app_reference.toml` |
| Validation contract | `Sys4AI/schemas/contracts/host_capability_profile.schema.json` |
| Focused validator | `Sys4AI/sys_for_ai/host_profiles.py` |
| Producer roles | `system_engineer`; `verification_engineer` |
| Consumer roles | `implementation_initialization_agent`; `system_architect`; `requirements_verifier` |
| Schema owner | `verification_engineer` |
| Subject layer | `framework_product` |
| External boundary | Codex App reference host |
| Source authority | Controlled configuration, schema, document, and registry rows |
| Structural verification | `validate-host-capability-profiles` |
| Observable verification | `STRATEGIC-BASELINE-MIGRATION-G07-HOST-VERIFICATION-SFADEV-TX22.md` and `DDR-SFADEV-STRATEGIC-BASELINE-G07-001` |

No separate artifact-contract registry row is required. The existing
configuration-source, validation-contract, source, and object-relationship
registries represent this narrow contract without creating a new authority
surface.

## 3. Profile State Model

Allowed per-interface capability states are:

- `verified_available`;
- `verified_unavailable`;
- `permission_dependent`;
- `environment_dependent`;
- `unknown`; and
- `deprecated`.

`Unknown` is not available. A denied, stale, unknown, deprecated, or unverified
capability cannot authorize execution. Conditional capabilities default to
non-executable until their permission and environment conditions are evaluated
within a later authorized execution transaction.

The checked-in profile uses these controlled evidence-backed representations:

| Field | Controlled value | Meaning |
|---|---|---|
| `verification_state` | `verified_G_07` | Observable development-host conformance is accepted for the exact recorded state |
| `verification_decision` | `DDR-SFADEV-STRATEGIC-BASELINE-G07-001` | Registered completed accountable decision |
| `verified_at` | `2026-07-11T15:19:10Z` | Probe-evidence timestamp |
| `verified_by` | `verification_engineer` | Controlled verifier role |
| `evidence_status` | `current` | Each interface resolves to the TX-22 report and probe identifiers |
| Safe probes | `HOST-G07-*` | Positive and denial-or-absence probes retained for all eight interfaces |
| `portable_execution_contract_version` | `1.0.0` | The profile binds the TX-09 portable structural contract |
| `portable_execution_contract_executable` | `true` | Only current `verified_available` interfaces may be used, and never without transaction authority and permission |

Structural validation resolves the accepted decision, current evidence fields,
timestamps, capability states, and execution binding. Conditional, unavailable,
unknown, stale, and deprecated interfaces remain non-executable. Capability
availability still does not grant project or transaction permission.

## 4. Permission Precedence

The exact precedence order is:

1. platform and system constraints;
2. host permissions;
3. project authorization;
4. bounded transaction permission envelope; and
5. task objective.

An item later in the list cannot override an earlier constraint. Vision,
values, goals, roles, urgency, efficiency, or model-generated reasoning do not
grant permission. A profile state is a capability description, not an
authorization decision.

## 5. Interface And Integration Map

The table records observed mappings and required evidence fields. The
`Current state` column is authoritative only for profile version `1.0.0` and
its freshness horizon.

| Interface | Data and direction | Representation and cadence | Owner and trust boundary | Primary controls | Current state and missing-capability behavior |
|---|---|---|---|---|---|
| User interaction | Human request, clarification, approval, rejection, timeout, and cancellation flow between an authorized user and host | Conversation events; per consequential decision | `system_engineer`; human identity and host interaction boundary | Silence is not consent; principal and evidence capture; explicit approval and rejection | `verified_available`, executable only in an authorized transaction; ambiguity remains blocked |
| Workspace filesystem | Source content, patches, file metadata, and diffs between host tools and authorized roots | Files and diffs; per bounded transaction | `system_engineer`; host filesystem and repository authority boundary | Allowed roots; read/write class; ownership; least privilege; diff visibility | `verified_available`; current host access does not imply authority over every readable path |
| Terminal and tests | Commands, arguments, working directory, process output, exit state, tests, and cancellation between host and local process boundary | Command invocation and retained evidence; per check | `verification_engineer`; shell, sandbox, process, and untrusted-input boundary | Injection resistance; reversible commands; stop conditions; exact result capture | `verified_available`; local exit and `Ctrl-C` behavior observed, external cancellation unproved |
| Tools, connectors, and network | Tool requests, retrieved data, consent, credential-mechanism references, and external side effects | Typed tool calls or connector operations; per invocation | `system_engineer`; platform, network, credential, external-system, and data-class boundaries | Tool identity; redaction; least privilege; irreversible-effect confirmation; untrusted output checks | `environment_dependent`, non-executable by default; evaluate each tool and permission separately |
| Sub-agents | Role, task scope, context, tool bounds, returned result, verification, and interruption between parent and child work | Bounded subtask packet and result; per delegation | `system_engineer`; context, concurrency, shared-workspace, and delegated-tool boundary | No implied authority delegation; disjoint write scopes; result verification; interruption evidence | `permission_dependent`, non-executable in TX-22; current policy prohibited spawning |
| Task and thread state | Task identity, fresh state, handoff, cancellation, and archival between host state and repository evidence | Host task state plus controlled handoff evidence; per transition | `system_engineer`; host state and repository source-authority boundary | Fresh source-backed state; resumable handoff; explicit cancellation and archival | `environment_dependent`, non-executable by default; read-only state observed, mutation not probed |
| Memory and retrieval | Query, result, source path, registry row, freshness, authority class, and stale risk between retrieval and canonical sources | Search result plus verified source inspection; per lookup | `requirements_verifier`; retrieval, privacy, retention, and authority boundary | Navigation only until source verification; freshness; data class; no generated authority inversion | `verified_available`; absent-object lookup fails closed and sources remain authoritative |
| Target runtime | Environment, release gate, telemetry, rollback, incident owner, kill control, and target approval between host and separately authorized target | Deployment and operational evidence; per release or incident | `system_architect`; host, deployment, production, operator, and target-authority boundaries | Separate promotion gate; telemetry; rollback; incident ownership; kill control; no prototype drift | `verified_unavailable`, non-executable; no hosting configuration or target authority exists |

## 6. Required Interface Fields

Every interface entry records:

- stable `interface_id`;
- `capability_status` and `execution_allowed`;
- proposed `host_mechanism`;
- `permission_source`;
- source and observable evidence status;
- safe positive and denial-or-absence probes;
- `fallback_mode` and detailed degraded behavior;
- cancellation behavior;
- evidence capture;
- known limitations; and
- review triggers.

The eight interface IDs are portable categories. Codex-specific descriptions
remain inside this reference profile. A compatible later host may implement the
same categories with different mechanisms without changing portable semantics.

## 7. Degraded, Blocked, And Rerouted Behavior

Fail-closed behavior is part of the interface contract:

- missing read access blocks source-dependent work;
- missing write access permits only a proposed patch or plan when safe;
- missing terminal access marks tests not run and prohibits pass claims;
- missing sub-agent support permits sequential work only when scope and
  assurance remain acceptable;
- denied external access requires local evidence or new authority;
- missing fresh state blocks state-dependent routing;
- missing retrieval requires direct source inspection or a block; and
- missing runtime, rollback, incident, or kill controls blocks deployment and
  operation.

If cancellation is unverified, high-risk or long-running work must not begin
without a safer control. Uncertain completion or external side effects must be
reported as uncertain rather than inferred successful.

## 8. Security And Data Handling

- Secrets and secret-like keys are forbidden in profile fixtures.
- Credentials are referenced only by mechanism; stored credential values are
  outside the contract.
- Local and external writes are separate side-effect classes.
- Retrieved content, command input, tool output, connector data, and sub-agent
  results are untrusted until checked.
- Untrusted text cannot be interpolated into commands without validation.
- Tool and sub-agent results require independent verification appropriate to
  the claim.
- Logs and retained evidence must redact secrets and sensitive target data.
- Readability does not imply authority, and tool availability does not imply
  permission.

## 9. Structural Validation

Run:

```sh
cd Sys4AI
make validate-host-capability-profiles
```

The focused validator checks:

- registered JSON Schema conformance;
- the exact unique eight-interface set;
- fixed permission precedence;
- pending or accepted `G-07` and portable execution-binding truthfulness;
- registry and YAML resolution of a completed human-authorized G-07 Director
  Decision before any `verified_G_07` profile can pass;
- non-executable unknown, unavailable, conditional, stale, and deprecated
  states;
- required permission, degraded, cancellation, limitation, evidence, and
  review fields;
- RFC 3339 and freshness consistency for verified evidence; and
- absence of secret-like structured values.

A pass means the profile is structurally admissible, its accepted decision is
registered, and its stated evidence is current. Observable behavior is proved
by the retained TX-22 report, not by schema validation alone. A pass never
grants permission or production/operational authority.

## 10. G-07 Observable Verification

`G-07` was accepted for version `1.0.0` after the verifier completed these
steps for each interface:

1. identify the applicable requirement and proposed host mechanism;
2. cite current observable or official evidence;
3. execute a safe positive probe;
4. execute a safe denial-or-absence probe where possible;
5. record the permission source and environment scope;
6. record degraded and cancellation behavior;
7. retain evidence without secrets; and
8. assign an evidence freshness horizon and review trigger.

Promotion also requires one registered, completed, controlled or canonical
Director Decision whose YAML binds `gate_id: G-07`, records
`accepts_gate_G_07: true`, and includes non-self-approved human authorization
evidence. A merely DDR-shaped string cannot satisfy the gate.

The retained TX-22 report maps all probe identifiers to methods and observed
results. Marketing language, undocumented assumptions, or a model's experience
cannot substitute for that evidence. The accepted disposition remains
separately reviewable and does not expand project or platform permissions.

## 11. Review, Supersession, And Rollback

Review is required when host capabilities, permissions, tools, environment,
cancellation, evidence freshness, portable execution contracts, or target
runtime assumptions change.

Do not overwrite an accepted verified profile in place. Register a new version,
retain prior evidence, link supersession, assess affected requirements and
permissions, and re-run safe conformance probes. A stale profile downgrades
affected capabilities and execution remains fail-closed.

Before TX-22 publication, revert the complete TX-22 profile, evidence, decision,
state, tests, registries, receipt, handoff, and generated-reader packet together.
After publication, preserve the accepted decision and supersede it explicitly.

## References

Sys4AI-dev. (2026). *Sys4AI-dev strategic baseline migration full implementation plan* [Unpublished implementation plan].

Sys4AI-dev. (2026, July 10). *DDR-SFADEV-STRATEGIC-BASELINE-G04-001* [Director decision record].

Sys4AI-dev. (2026, July 11). *G-07 observable host verification report* [Verification report].
