# Design: Add Edit and Stdin Body

## Context

`notes add` currently takes body via `--body` flag. We are switching to stdin
and adding an `edit` command.

## Goals / Non-Goals

**Goals:**
- Read body from stdin for both `add` and `edit`
- Add `edit_note(id, title, body)` to `notes/core.py`
- Add `notes edit <id>` subcommand to CLI

**Non-Goals:**
- Interactive editing (e.g. opening $EDITOR)
- Partial body updates (stdin replaces the entire body)

## Decisions

### Stdin detection
Use `sys.stdin.isatty()` to decide whether to read body from stdin:
- If `isatty()` is True (interactive terminal, no pipe/redirect): treat as
  "no body provided" — skip `read()` entirely.
- If `isatty()` is False (piped or redirected): call `sys.stdin.read()` and
  use the result as body (may be empty string).

For `add`, no-body means empty-string body. For `edit`, no-body means body
unchanged.

Alternative considered: always read stdin unconditionally — rejected because
running `notes edit <id> --title "Foo"` in an interactive terminal would hang
waiting for EOF (Ctrl-D).

### Empty title on edit
Reject `--title ""` on edit with the same "Title must not be empty" error used
by create. This keeps validation consistent across commands.

Alternative considered: allow clearing title — rejected because it would
violate the existing Create Note invariant that titles are non-empty.
