# Runtime state

Runtime state lives in the target workspace:

```text
.sys4ai/
├── workspace.yaml
├── catalog/
├── runs/<run-id>/
│   ├── transaction.yaml
│   ├── events.jsonl
│   ├── evidence/
│   └── result.yaml
├── generated/
└── cache/
```

This surface is local or externally retained evidence and is ignored by Git by
default. It is not packaged with Sys4AI and cannot become product authority by
being present in a workspace.
