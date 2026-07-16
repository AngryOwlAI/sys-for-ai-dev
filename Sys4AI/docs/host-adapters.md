# Host adapters

The core depends on ports for models, approvals, workspaces, files, source
control, tools, state, artifact catalogs, events, clocks, secrets, and host
capabilities. Adapters implement those mechanisms.

Capability declarations are observations, not permissions. Effective
permission is the intersection of platform constraints, host permissions,
target authorization, role authority, and the current transaction envelope.

Codex is the first reference host, but no Codex-specific path, task state, or
approval assumption is embedded in the domain kernel.
