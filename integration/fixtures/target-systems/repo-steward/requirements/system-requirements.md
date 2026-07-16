# System Requirements

- The built-in fixture transaction uses a read-only filesystem adapter.
- File content is not copied into the execution receipt; only size and SHA-256
  are retained.
- Runtime evidence remains under ignored `.sys4ai/` state.
- No network, external write, source-control mutation, or tool execution is
  enabled by the fixture.
