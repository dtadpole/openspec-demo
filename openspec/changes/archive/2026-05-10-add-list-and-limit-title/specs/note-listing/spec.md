# Note Listing Spec Delta

## ADDED Requirements

### Requirement: List Notes
The system SHALL allow users to list all stored notes.

#### Scenario: List with notes present
- **GIVEN** one or more notes exist
- **WHEN** the user runs `notes list`
- **THEN** the system prints each note as `<id>  <title>`, one per line
- **AND** titles longer than 60 characters SHALL be truncated with `…`

#### Scenario: List with no notes
- **GIVEN** no notes exist
- **WHEN** the user runs `notes list`
- **THEN** the system prints nothing and exits successfully
