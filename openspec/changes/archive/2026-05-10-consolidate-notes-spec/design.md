# Design: Consolidate Notes Spec

## Context

The `openspec/specs/` directory currently has two capability folders:
- `notes/` — Create Note requirement
- `note-listing/` — List Notes requirement

These should be one capability since they operate on the same domain entity.

## Goals / Non-Goals

**Goals:**
- Merge all note-related requirements under a single `notes` capability
- Remove the `note-listing` capability folder

**Non-Goals:**
- Modifying any code in `notes/`
- Modifying any tests in `tests/`

## Decisions

### Spec-only refactor
Use delta specs with ADDED (on `notes`) and REMOVED (on `note-listing`) to
let the archive sync handle the migration cleanly.

Alternative considered: manually edit main specs — rejected because it
bypasses the OpenSpec change workflow.
