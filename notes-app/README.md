# notes-app

A small notes management CLI built using **OpenSpec spec-driven development**
with **Claude Code** as the implementation agent. This repo exists primarily as
a learning artifact — to demonstrate the OpenSpec mental model end-to-end on a
real, runnable project rather than a toy snippet.

## What it does

A CLI for storing short notes in a local JSON file:

```bash
echo "milk, eggs" | notes add --title "Shopping"
notes list
echo "new body" | notes edit <id> --title "New title"
```

Notes live in `./notes.json` (gitignored). Body always comes from stdin so
multi-line content and shell pipes work naturally (`git commit -F -` style).

## Stack

- Python 3.12 (stdlib only for the application itself — no runtime deps)
- `uv` for venv + dependency management
- `pytest` 9.x for tests
- `openspec` 1.3 for the spec layer
- Claude Code as the AI coding assistant driving `/opsx:` commands

## Try it locally

```bash
git clone https://github.com/dtadpole/openspec-demo.git
cd openspec-demo/notes-app
uv venv --python 3.12
uv pip install --python .venv/bin/python pytest

# Run the CLI
echo "first thought" | .venv/bin/python -m notes.cli add --title "Hello"
.venv/bin/python -m notes.cli list

# Run the tests
.venv/bin/pytest
```

## Repository layout

```
notes-app/
├── notes/                   — application package (cli, core, storage)
├── tests/                   — pytest suite (12 tests, all passing)
├── notes.json               — runtime data file (gitignored)
├── pyproject.toml           — project + dev deps + pytest config
└── openspec/
    ├── config.yaml          — context + general/proposal/tasks/spec/design rules
    ├── specs/
    │   └── notes/spec.md    — current behavior contract (3 requirements,
    │                          14 scenarios). Source of truth.
    └── changes/
        └── archive/         — full audit trail of every change
```

## OpenSpec mental model — the short version

OpenSpec organizes work into **two folders**:

- **`openspec/specs/`** = **state**. The current contract describing what the
  system actually does. Never hand-edited — it's accumulated by archiving
  changes.
- **`openspec/changes/`** = **motion**. One folder per proposed modification,
  with proposal/design/tasks/delta artifacts. After implementation, the change
  is *archived*, which mechanically merges its delta into `specs/`.

The cycle for any modification:

```
/opsx:propose <name>   →  AI drafts 4 artifacts
                          (proposal · design · tasks · delta)
   ↓
human review           →  request edits if anything is off
   ↓
/opsx:apply            →  AI implements code + tests, ticks tasks
   ↓
human verifies         →  run tests, smoke-check behavior
   ↓
/opsx:archive          →  delta merges into specs/, change moves to archive/
```

Deltas are structured: `## ADDED Requirements`, `## MODIFIED Requirements`,
`## REMOVED Requirements`. MODIFIED is a **full replacement** of a requirement
(including all scenarios), not a diff.

## Change history (5 rounds)

| # | Change name | What it taught |
|---|---|---|
| 1 | `add-note-creation` | First `/opsx:apply` + `/opsx:archive`; `specs/` materializes from nothing |
| 2 | `add-list-and-limit-title` | `MODIFIED` semantics + the cost of a sloppy delta (List Notes silently dropped) |
| 3 | `add-list-notes-spec` | "Spec-only" change with no code changes; LLM creating an over-fragmented capability |
| 4 | `consolidate-notes-spec` | `ADDED` + `REMOVED` across two capabilities in one change; deleting a capability folder |
| 5 | `add-edit-and-stdin-body` | Breaking change with `MODIFIED` rewriting all scenarios + new `ADDED` capability; design.md catching a real bug (stdin hang on tty) |

Browse `openspec/changes/archive/` to read the proposal/design/tasks/delta of
each round — they form a complete narrative of how the spec evolved.

## What this repo is NOT

- Not a real notes app. The persistence layer is a flat JSON file.
- Not a tutorial repo for OpenSpec itself — the [official docs](https://github.com/Fission-AI/OpenSpec)
  are better for that.
- Not "complete" — many obvious features (delete, search, tags) are deliberately
  left out so the spec stays small enough to read end-to-end.

## License

MIT
