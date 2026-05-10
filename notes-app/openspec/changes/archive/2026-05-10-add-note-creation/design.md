# Design: Add Note Creation

## Storage
JSON file at `./notes.json` containing a list of notes:
```json
[
  {"id": "abc123", "title": "Shopping", "body": "milk, eggs"}
]
```

Chosen because: zero dependencies, easy to inspect, fits a demo project.

## CLI
Single entry point `notes`. First subcommand:
```
notes add --title "Shopping" --body "milk, eggs"
```
Returns the new note ID on stdout.

## ID generation
Random 8-char hex string (`secrets.token_hex(4)`).

## Validation
- Title must be non-empty.
- No max length yet (deferred to a future change).
