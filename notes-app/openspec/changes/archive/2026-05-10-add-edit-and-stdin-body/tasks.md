# Tasks

## 1. Refactor add to use stdin

- [x] 1.1 Remove `--body` parameter from `add` subcommand in `notes/cli.py`
- [x] 1.2 Read body from `sys.stdin.read()` in the `add` handler
- [x] 1.3 Update `create_note()` call to pass stdin body

## 2. Implement edit command

- [x] 2.1 Add `edit_note(note_id, title, body)` to `notes/core.py`
- [x] 2.2 Add `notes edit <id>` subcommand with optional `--title` flag
- [x] 2.3 Read body from stdin in the `edit` handler; empty stdin means no body change
- [x] 2.4 Reject when no `--title` and stdin is empty ("No changes provided")
- [x] 2.5 Reject when note ID not found ("Note not found: <id>")

## 3. Tests

- [x] 3.1 Test scenario: Successful creation (stdin body)
- [x] 3.2 Test scenario: Empty title rejected (stdin body)
- [x] 3.3 Test scenario: Title too long rejected (stdin body)
- [x] 3.4 Test scenario: Empty stdin allowed
- [x] 3.5 Test scenario: Update title only
- [x] 3.6 Test scenario: Update body only
- [x] 3.7 Test scenario: Update both
- [x] 3.8 Test scenario: Reject when no changes
- [x] 3.9 Test scenario: Reject when ID not found
- [x] 3.10 Run `.venv/bin/pytest` and confirm all tests pass
