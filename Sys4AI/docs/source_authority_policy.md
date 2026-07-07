# Source Authority Policy

**Status:** Draft  
**Scope:** `Sys4AI` Phase 1 source-first memory and knowledge system

---

## Authority hierarchy

1. Registered canonical source files.
2. Registered control records and decision records.
3. Registry rows that identify source and derivative status.
4. Validated generated derivatives that trace to source IDs.
5. Unvalidated generated notes, summaries, semantic caches, local vault files, or reader surfaces.

The hierarchy is designed to prevent authority inversion. A helpful summary may speed navigation, but it does not become truth merely because it is easier to read.

---

## Promotion rule

A derivative becomes canonical only when a source-import or promotion AgentJob:

1. Identifies the derivative path.
2. Identifies the source authority gap it fills.
3. Records the promotion in `source_registry.csv`.
4. Updates or invalidates conflicting derivative rows.
5. Produces completion evidence.

---

## Derivative rule

Generated or synchronized artifacts must include at least one source link, source ID, or registry relationship before they are treated as validated reader surfaces.

---

## Anti-rules

- Do not cite a generated summary as the only authority when the source exists.
- Do not treat Obsidian notes as canonical by default.
- Do not silently let semantic retrieval override source registries.
- Do not let generated docs drift without a registry status.
