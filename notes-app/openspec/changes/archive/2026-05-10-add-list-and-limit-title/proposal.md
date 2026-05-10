# Proposal: Add List and Limit Title

## Why

Users can create notes but have no way to see what notes exist. A `notes list`
command is the natural complement to `notes add`. Additionally, the previous
change deferred title-length validation — unbounded titles can break display
formatting, so a max-length constraint should be added now.

## What Changes

- Add a `notes list` CLI subcommand that prints all stored notes
- Enforce a maximum title length (200 characters) when creating a note

## Capabilities

### New Capabilities
- `note-listing`: List all stored notes via the CLI

### Modified Capabilities
- `notes`: Add title-length validation to the Create Note requirement

## Impact

- Affected code: `notes/core.py` (new validation), `notes/cli.py` (new subcommand)
- No new dependencies
