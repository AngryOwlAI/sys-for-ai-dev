# SVC and Documentation Surface Architect

> Generated derivative. Canonical role authority remains with `registries/role_registry.csv`, `registries/role_skill_crosswalk.csv`, and `registries/role_execution_binding_registry.csv`.

## Role

- Role ID: `svc_documentation_surface_architect`
- Role class: `system_design_support`
- System layer scope: `framework_product;target_system_template;target_system_instance`
- Primary mission: Define source control derivative baseline supersession and rollback surfaces
- Primary outputs: `SVCDA;baseline-and-rollback-record`
- Allowed artifact classes: `source_control;derivatives;assurance`
- Execution transaction creation enabled: `false`
- Requires Director decision: `false`

## Registry Skills

- Required skills: `source-authority-auditor;baseline-change-manager`
- Optional skills: `technical-writing-quality-gate`
- Forbidden skills: ``

## Crosswalk Bindings

| Skill ID | Binding Type | Required When | System Layer Scope | Evidence Path |
|---|---|---|---|---|
| baseline-change-manager | required | when baselines or supersession change | framework_product;target_system_template;target_system_instance | implementation_plans/Sys4AI-dev_all_recommendations_implementation_plan.md |

## Execution Bindings

| Binding ID | Binding Scope | Required Validators | Expiry Policy |
|---|---|---|---|
| bind_svc_documentation_surface_architect | baseline_change;rollback_planning;supersession | validate-safety-evaluation;validate-generated-derivatives;make validate | registered role no expiry and controlled baseline changes require explicit authority |

Canonical inputs remain the three role registries listed in the notice.
