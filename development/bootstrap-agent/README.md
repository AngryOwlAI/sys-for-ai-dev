# Bootstrap Agent

This is the canonical stage-0 development runtime.

- `skills/` contains executable development skill sources.
- `skill-catalog/` contains their controlled catalog and bundles.
- `profiles/` contains development-only operating profiles.
- `policies/` records bootstrap authority and promotion constraints.
- `host-adapters/` describes development-host bindings.

The `.agents/` and `.codex/` directories at the repository root are
generated discovery bindings. Edit canonical files here and run:

    python3 development/tools/generate_host_bindings.py --root .

Development skills are not copied into the product. A product skill under
`Sys4AI/assets/skills/` requires explicit generalization and independent
validation.
