# Obsidian Derivative Policy

**Status:** Draft  
**Scope:** Optional local Obsidian-compatible vaults

---

## Policy

Obsidian support is optional and derivative by default.

An Obsidian vault may be useful as a local reader surface, retrieval aid, or human browsing layer. It is not the canonical memory system unless specific files are promoted through a source-import workflow.

---

## Recommended local path

```text
sys-for-ai/.local/obsidian/sys-for-ai-wiki/
```

The `.local/` folder should remain ignored unless a later decision explicitly tracks generated vault content.

---

## Allowed uses

- Generated notes that summarize registered sources.
- Indexes for browsing source objects.
- Mermaid or PlantUML reader notes that link back to source diagrams.
- Local backlinks among generated wiki notes.

---

## Forbidden defaults

- Editing Obsidian notes and assuming canonical sources changed.
- Treating backlinks as source authority.
- Letting stale generated notes outrank newer source files.
- Syncing private local vault files into the repository without review.
