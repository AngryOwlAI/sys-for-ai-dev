# Getting started

## Install and inspect

```bash
python -m pip install -e '.[dev]'
sys4ai doctor
sys4ai contracts
sys4ai assets
```

## Generate a target package

```bash
sys4ai generate /tmp/sample-target \
  --system-id sample-target \
  --name "Sample Target" \
  --intent "Demonstrate governed target generation"
sys4ai validate /tmp/sample-target
```

Generation creates a complete derivative package and local `.sys4ai/` runtime
workspace. It does not approve requirements, execute a target runtime, or claim
production readiness.

## Continue lifecycle work

```bash
sys4ai discover /tmp/sample-target \
  --intent "Clarify stakeholder intent and boundaries"
sys4ai plan /tmp/sample-target
sys4ai memory search /tmp/sample-target authority
sys4ai trace /tmp/sample-target
```

Use `sys4ai execute` only with a transaction conforming to
`contracts/schemas/execution-transaction.schema.json`. The command checks
authorization and records a run for a permitted host; it does not invoke
arbitrary tools itself.
