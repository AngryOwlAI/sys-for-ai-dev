# Roles guide

Sys4AI roles describe responsibility and bounded decision rights. They are not
personas with intrinsic permission. A runtime actor may perform a role only
when the target's accountable authority, host constraints, and current
transaction all permit the action.

The canonical role catalog defines twenty active role types across intent,
requirements, architecture, domain review, protection review, documentation,
execution planning, knowledge, implementation, verification, operations,
maintenance, improvement, and retirement. The catalog intentionally omits
temporary development roles and compatibility aliases.

Important separations:

- `system_director` governs intent and accountable decisions; it does not
  implement by default.
- `requirements_manager` governs stable requirement identity and change.
- `system_architect` defines boundaries and interfaces; verification remains
  independent.
- `documentation_librarian` governs controlled documents and configuration; it
  is not a general operator.
- `runtime_maintenance_planner` covers operations, maintenance, improvement,
  and retirement planning; execution still requires bounded authorization.
- `verification_engineer` records evidence against named claims and cannot
  convert a structural pass into target acceptance.
- `software_engineer` implements accepted work but cannot self-approve a
  material change.

See `contracts/catalogs/role-types.yaml` for authority and
`contracts/schemas/role.schema.json` for structure.
