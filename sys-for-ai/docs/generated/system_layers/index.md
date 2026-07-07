> **Generated derivative notice**
>
> This page is a generated reader surface. It is not canonical. Canonical authority remains with the linked source files, registry rows, and validation contracts. Do not hand-edit this page as source authority.

```yaml
page_metadata:
  derivative_id: der_system_layers_index
  authority_status: generated_noncanonical
  derivative_type: governance_system_layers_page
  source_registries:
    - registries/system_layer_registry.csv
    - registries/derivative_registry.csv
  validation_contracts:
    - contract_system_layer_registry_row
  generated_at: 2026-07-06T00:00:00Z
  generator: sys_for_ai.derivative_generation.governance_generated_docs:0.1.0
  stale_or_orphan_status: current
  source_hashes:
    - pending
```

# System Layers

This generated page summarizes registered system layers and their authority boundaries.

## Registry Trace

| derivative_id | path | source_ids | generation_method | status |
| --- | --- | --- | --- | --- |
| der_system_layers_index | docs/generated/system_layers/index.md | SRC-REG-SYSTEM-LAYERS;SRC-DERIVATIVE-GENERATION | sys_for_ai.derivative_generation.governance_generated_docs:0.1.0 | generated_derivative |

## Layer Rows

| layer_id | layer_type | canonical_roots | derivative_roots | requires_decision | default_validators | owner |
| --- | --- | --- | --- | --- | --- | --- |
| development_system | development_system | .;.agents;.codex;scripts;PRDs;implementation_plans | docs/generated;.local | true | make validate-dev-skills;make validate-product-scaffold | system_director |
| framework_product | framework_product | sys-for-ai;PRDs;implementation_plans | sys-for-ai/docs/generated | true | cd sys-for-ai && make validate | system_director |
| target_system_template | target_system_template | sys-for-ai/templates;sys-for-ai/skills/core | sys-for-ai/docs/generated | true | cd sys-for-ai && make validate | system_architect |
| target_system_instance | target_system_instance | <future-target-root> | <future-target-root>/docs/generated | true | <target-system validators> | system_director |
| derivative_surface | derivative_surface | docs/generated;sys-for-ai/docs/generated | docs/generated;sys-for-ai/docs/generated | true | validate-generated-derivatives | documentation_librarian |

## Boundary Note

Generated derivative surfaces remain noncanonical unless explicitly promoted by a source-authority decision.

## Allowed Promotion Path

Promotion requires an explicit source-authority decision, registry update, and validation evidence. This generated page is not promoted by generation.
