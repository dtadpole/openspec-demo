# Proposal: Consolidate Notes Spec

## Why

The previous change (add-list-notes-spec) incorrectly placed the List Notes
requirement under a separate `note-listing` capability. Conceptually, listing
notes is part of the `notes` capability — not an independent capability. This
creates unnecessary fragmentation in `openspec/specs/` with two folders for
what is logically one domain.

This is a pure spec refactor: no code changes, no test changes.

## What Changes

- Move the List Notes requirement (3 scenarios) from `note-listing` into the
  `notes` capability
- Remove the `note-listing` capability entirely

## Capabilities

### New Capabilities
None.

### Modified Capabilities
- `notes`: Adding the List Notes requirement (migrated from note-listing)
- `note-listing`: Removing all requirements (capability to be deleted)

## Impact

- Affected specs: `openspec/specs/notes/spec.md`, `openspec/specs/note-listing/`
- No code changes
- No test changes
