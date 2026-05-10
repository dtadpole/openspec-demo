# Proposal: Add Note Creation

## Why
Users need a way to capture thoughts as text notes. This is the most basic
building block of the app — without it, nothing else (search, edit, delete)
makes sense.

## What Changes
- Introduce a Note concept (id, title, body)
- Add a way to create a new note via CLI command `notes add`
- Notes are stored on disk in a simple JSON file

## Impact
- Affected specs: `notes` (new capability)
- Affected code: new `notes/` Python package, new CLI entry point
