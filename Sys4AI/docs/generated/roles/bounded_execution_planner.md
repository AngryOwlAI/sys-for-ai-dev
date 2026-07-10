# Bounded Execution Planner

> Generated derivative. Canonical role authority remains with `registries/role_registry.csv`, `registries/role_skill_crosswalk.csv`, and `registries/role_execution_binding_registry.csv`.

## Role

- Role ID: `bounded_execution_planner`
- Role class: `runtime_control`
- System layer scope: `development_system;framework_product;target_system_template;target_system_instance`
- Primary mission: Define portable bounded execution continuation cancellation escalation and handoff semantics
- Primary outputs: `BERA;execution-transaction-plan`
- Allowed artifact classes: `control_records;handoffs;execution_transactions`
- Execution transaction creation enabled: `true`
- Requires Director decision: `true`

## Registry Skills

- Required skills: `context-window-and-handoff-manager;baseline-change-manager`
- Optional skills: `director-decision-governor`
- Forbidden skills: ``

## Crosswalk Bindings

| Skill ID | Binding Type | Required When | System Layer Scope | Evidence Path |
|---|---|---|---|---|
| codex-usage-metrics | required | when transaction context or token accounting is needed | development_system;framework_product | Sys4AI/schemas/contracts/execution_transaction.schema.json |
| context-window-and-handoff-manager | required | when resumable handoffs or context checkpoints are needed | development_system;framework_product;target_system_template;target_system_instance | Sys4AI/schemas/contracts/execution_transaction.schema.json |

## Execution Bindings

| Binding ID | Binding Scope | Required Validators | Expiry Policy |
|---|---|---|---|
| bind_bounded_execution_planner | baseline_migration;implementation;validation;handoff_planning | make validate;validate-capability-migration | explicit transaction authorization and permission envelope required |

Canonical inputs remain the three role registries listed in the notice.
