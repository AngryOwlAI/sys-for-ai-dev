# Development Tools

- `validate_skill_catalog.py`: validates canonical bootstrap skill manifests
  and bundles using the standard library.
- `generate_host_bindings.py`: generates minimal `.agents/` and
  `.codex/` discovery bindings.

Repository-wide orchestration belongs to the `sfadev` CLI and root Makefile.
Completed name migrations and transaction-specific validators are intentionally
absent.
