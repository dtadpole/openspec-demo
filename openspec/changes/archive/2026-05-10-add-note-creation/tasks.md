# Tasks

## 1. Storage
- [x] 1.1 Create `notes/storage.py` with `load_notes()` and `save_notes()`
- [x] 1.2 Default file path is `./notes.json`, created if missing

## 2. Note creation
- [x] 2.1 Create `notes/core.py` with `create_note(title, body) -> dict`
- [x] 2.2 Generate 8-char hex ID
- [x] 2.3 Reject empty title with a clear error

## 3. CLI
- [x] 3.1 Create `notes/cli.py` with argparse-based `notes add` subcommand
- [x] 3.2 Print the new note ID on success
- [x] 3.3 Print error to stderr and exit 1 on validation failure
