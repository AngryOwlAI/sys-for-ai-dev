# Changelog

## Unreleased — repository reboot

- Separate the project-control, bootstrap-development, product, integration,
  and evidence planes.
- Establish the one-way dependency rule from development to product to target.
- Replace historical planning clutter with one active change PRD and one active
  implementation plan.
- Relocate canonical development skills into `development/` and generate host
  bindings.
- Normalize the product distribution, package, and CLI name to `sys4ai`.
- Add a host-neutral domain kernel, application services, explicit ports,
  bounded adapters, target generation, runtime state, memory, traceability, and
  assurance validation.
- Add the repository-specific `sfadev` development CLI and keep product and
  development commands independent.
- Remove development state, transaction history, and generated readers from
  the product boundary.
- Add independent development, product, integration, source-copy, and
  installed-wheel validation.

The frozen source baseline is tag `pre-reboot-2026-07-15` at commit
`5a6aaf7652661e094cdfa40be55a380e9bc0cd8c`.
