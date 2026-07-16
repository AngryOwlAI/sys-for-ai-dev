# Context Format Template

Use this template when a target project needs a portable glossary or domain
language file. Adapt the filename, context name, and term list to the target
project. Do not treat this file as an implementation spec.

## Default Location

- Single-context project: `<PROJECT_ROOT>/<CONTEXT_FILE>`
- Multi-context project: `<PROJECT_ROOT>/<CONTEXT_MAP>` plus one
  `<CONTEXT_FILE>` per context

Create files lazily. If no settled term exists yet, do not create an empty
glossary file only to satisfy the workflow.

## Single-Context Structure

```md
# <Context Name>

<One or two sentences describing what this context represents and why the
language matters.>

## Language

**<Canonical Term>**:
<One or two sentences defining what the term is.>
_Avoid_: <ambiguous synonym>, <deprecated synonym>

**<Another Canonical Term>**:
<One or two sentences defining the term.>
_Avoid_: <ambiguous synonym>
```

## Multi-Context Map Structure

```md
# Context Map

## Contexts

- [<Context A>](./<path-to-context-a>/<CONTEXT_FILE>) - <short purpose>
- [<Context B>](./<path-to-context-b>/<CONTEXT_FILE>) - <short purpose>

## Relationships

- **<Context A> -> <Context B>**: <how concepts, events, records, or ownership
  boundaries relate>
```

## Rules

- Choose one canonical term when multiple terms compete.
- Keep definitions tight: define what the concept is, not implementation steps.
- Include only domain-specific language. General programming concepts do not
  belong here unless the target project gives them special domain meaning.
- Record avoided terms only when they reduce ambiguity for future readers.
- Add subheadings only when natural clusters make the glossary easier to scan.
- If existing code or docs contradict the proposed term, resolve the
  contradiction before writing the entry.
