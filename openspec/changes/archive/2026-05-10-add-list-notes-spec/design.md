# Design: Add List Notes Spec

## Context

The `notes list` feature is already implemented in `notes/cli.py`. It prints
`<id>  <title>` per line and truncates titles longer than 60 characters with
`…`. Tests for the list scenarios are missing.

## Goals / Non-Goals

**Goals:**
- Add pytest tests covering all 3 list-notes scenarios

**Non-Goals:**
- Code changes — the feature is already implemented correctly

## Decisions

### Test approach
Test truncation via CLI's `main()` in-process (monkeypatch `sys.argv`, capture
stdout with `capsys`). This avoids subprocess overhead while exercising the
real CLI code path.

Alternative considered: subprocess — rejected because it can't share the
monkeypatched `DEFAULT_PATH` for storage isolation.
