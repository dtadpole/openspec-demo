# Tasks

## 1. Title length validation

- [x] 1.1 Add 200-character title limit to `create_note()` in `notes/core.py`
- [x] 1.2 Surface title-too-long error in CLI (stderr + exit 1)

## 2. List notes

- [x] 2.1 Add `list_notes()` to `notes/core.py` that returns all stored notes
- [x] 2.2 Add `notes list` subcommand to `notes/cli.py`
- [x] 2.3 Print each note as `<id>  <title>`, one per line
- [x] 2.4 Print nothing and exit 0 when no notes exist

## 3. Tests

- [x] 3.1 Test scenario: Successful creation
- [x] 3.2 Test scenario: Empty title rejected
- [x] 3.3 Test scenario: Title too long rejected
- [x] 3.4 Test scenario: List with notes present
- [x] 3.5 Test scenario: List with no notes
- [x] 3.6 Run `pytest` and confirm all tests pass
