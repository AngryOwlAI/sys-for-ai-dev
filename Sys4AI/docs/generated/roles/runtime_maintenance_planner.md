# Runtime and Maintenance Planner

> Generated derivative. Canonical role authority remains with `registries/role_registry.csv`, `registries/role_skill_crosswalk.csv`, and `registries/role_execution_binding_registry.csv`.

## Role

- Role ID: `runtime_maintenance_planner`
- Role class: `maintenance`
- System layer scope: `framework_product;target_system_template;target_system_instance`
- Primary mission: Define pre-production and runtime operations monitoring incident update and maintenance obligations
- Primary outputs: `operations-and-maintenance-plan;readiness-gap-register`
- Allowed artifact classes: `operations;maintenance;assurance`
- Execution transaction creation enabled: `false`
- Requires Director decision: `false`

## Registry Skills

- Required skills: `operations-and-maintenance-planner`
- Optional skills: `evaluation-harness-designer`
- Forbidden skills: ``

## Crosswalk Bindings

| Skill ID | Binding Type | Required When | System Layer Scope | Evidence Path |
|---|---|---|---|---|
| evaluation-harness-designer | optional | when operational behavior needs regression evaluation | framework_product;target_system_template;target_system_instance | implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md |
| operations-and-maintenance-planner | required | when framework or target operations maintenance or readiness planning is needed | framework_product;target_system_template;target_system_instance | implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md |

## Execution Bindings

| Binding ID | Binding Scope | Required Validators | Expiry Policy |
|---|---|---|---|
| bind_runtime_maintenance_planner | operations_planning;maintenance_planning;readiness_review | validate-safety-evaluation;validate-roles;make validate | registered role no expiry and runtime action requires separate production authority |

Canonical inputs remain the three role registries listed in the notice.
