# Proposal: Add Edit and Stdin Body

## Why

The current `--body` flag is awkward for multi-line content: it requires shell
quoting and escaping. Reading body from stdin is more Unix-friendly — it
supports multi-line input naturally, avoids quoting issues, and follows the
convention used by tools like `git commit -F -`. Additionally, users need a
way to modify existing notes without deleting and recreating them.

## What Changes

- **BREAKING**: Change `notes add` to read body from stdin instead of `--body`
  flag. The `--body` flag is removed entirely.
- Add `notes edit <id>` command to modify an existing note's title and/or body.
  Supports `--title` (optional) and body from stdin (optional). At least one
  must be provided.

## Capabilities

### New Capabilities
None.

### Modified Capabilities
- `notes`: Modify Create Note requirement (stdin body, remove --body flag),
  add Edit Note requirement

## Impact

- Affected code: `notes/core.py`, `notes/cli.py`
- Affected tests: `tests/test_notes.py` (all add tests must be rewritten,
  new edit tests added)
- **BREAKING**: `notes add --body "..."` no longer works
