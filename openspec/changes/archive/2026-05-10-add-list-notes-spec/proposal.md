# Proposal: Add List Notes Spec

## Why

The `notes list` feature was implemented but its spec was bundled under the
`note-listing` capability with only basic scenarios. The truncation behavior
(60-char limit with ellipsis) is part of the spec but has no test coverage.
This change adds proper test coverage for all list-notes scenarios.

## What Changes

- Add tests for the List Notes requirement (3 scenarios)
- No code changes — implementation already exists

## Capabilities

### New Capabilities
None.

### Modified Capabilities
- `note-listing`: Adding test coverage for all scenarios including truncation

## Impact

- Affected code: `tests/test_notes.py` (new tests only)
