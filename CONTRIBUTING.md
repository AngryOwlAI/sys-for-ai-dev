# Contributing

Start with `PROJECT_STATUS.md`, the two active PRDs, the architecture index,
and the one active implementation plan. Classify whether a change concerns the
project control plane, bootstrap development system, portable product,
integration target, or evidence before editing.

Use the smallest authorized change and preserve these boundaries:

- project intent and requirement changes require accountable authority;
- canonical development skills live under `development/bootstrap-agent/skills/`;
- `.agents/` and `.codex/` are generated bindings;
- `Sys4AI/` cannot read or import its parent repository;
- target fixtures remain derivative and outside the product;
- ephemeral run state belongs under ignored `.sys4ai/` directories;
- generated readers and evidence cannot promote themselves.

Run the narrowest relevant check first, then the aggregate checks:

```bash
make validate-development
make validate-product
make validate-integration
make validate
git diff --check
```

Report exact commands, observed results, claim limitations, unverified scope,
and rollback. Commit, push, release, publication, and deployment are separate
actions and require explicit authorization.
