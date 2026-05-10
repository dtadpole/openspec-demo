# Design: Add List and Limit Title

## Context

The notes app currently supports creating notes via `notes add`. Notes are
stored in `./notes.json` as a flat JSON array. There is no way to view stored
notes, and titles have no length constraint.

## Goals / Non-Goals

**Goals:**
- Add a `notes list` subcommand that displays all stored notes
- Enforce a 200-character maximum on note titles at creation time

**Non-Goals:**
- Pagination or filtering (future work)
- Retroactive enforcement on existing notes with long titles

## Decisions

### List output format
Print one note per line as `<id>  <title>`. Truncate titles longer than 60
characters with `…` for display only.

Rationale: simple tabular format is easy to scan and pipe to other tools.
Alternative considered: JSON output — deferred; add a `--json` flag later if
needed.

### Title max length
Hard-coded 200-character limit enforced in `create_note()`.

Rationale: keeps validation co-located with existing empty-title check.
Alternative considered: configurable limit — unnecessary complexity for a demo
app.

### List function placement
Add `list_notes()` to `notes/core.py` alongside `create_note()`.

Rationale: both are domain operations over the notes collection.

## Risks / Trade-offs

- [Truncation hides data] → Users can inspect `notes.json` directly for full
  titles. A future `notes show <id>` command would also solve this.
