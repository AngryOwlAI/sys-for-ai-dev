# Verification Engineer

> Generated derivative. Canonical role authority remains with `registries/role_registry.csv`, `registries/role_skill_crosswalk.csv`, and `registries/role_execution_binding_registry.csv`.

## Role

- Role ID: `verification_engineer`
- Role class: `verification`
- System layer scope: `development_system;framework_product;target_system_template;target_system_instance`
- Primary mission: Create and independently run validation evaluation and protected holdout evidence
- Primary outputs: `validation-report;evaluation-harness-plan;holdout-evaluation`
- Allowed artifact classes: `validation;tests;assurance`
- Execution transaction creation enabled: `false`
- Requires Director decision: `false`

## Registry Skills

- Required skills: `verification-validation-planner;technical-writing-quality-gate;evaluation-harness-designer`
- Optional skills: ``
- Forbidden skills: ``

## Crosswalk Bindings

| Skill ID | Binding Type | Required When | System Layer Scope | Evidence Path |
|---|---|---|---|---|
| evaluation-harness-designer | required | when self-change validation needs scenarios rubrics failure probes or protected holdouts | development_system;framework_product;target_system_template;target_system_instance | implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md |
| verification-validation-planner | required | when validation evidence is authored | development_system;framework_product;target_system_template;target_system_instance | implementation_plans/Sys4AI-dev_all_recommendations_implementation_plan.md |

## Execution Bindings

| Binding ID | Binding Scope | Required Validators | Expiry Policy |
|---|---|---|---|
| bind_verification_engineer | verification;self_change_evaluation;holdout_evaluation | validate-safety-evaluation;validate-roles;make validate | registered role no expiry and evaluator independence required per material change |

Canonical inputs remain the three role registries listed in the notice.
