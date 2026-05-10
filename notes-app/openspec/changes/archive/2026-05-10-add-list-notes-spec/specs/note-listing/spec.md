# Note Listing Spec Delta

## ADDED Requirements

### Requirement: List Notes
The system SHALL allow users to list all stored notes.

#### Scenario: List with notes present
- **GIVEN** one or more notes exist
- **WHEN** the user runs `notes list`
- **THEN** the system prints each note as `<id>  <title>`, one per line

#### Scenario: List with no notes
- **GIVEN** no notes exist
- **WHEN** the user runs `notes list`
- **THEN** the system prints nothing and exits successfully

#### Scenario: Long titles are truncated
- **GIVEN** a note exists with a title longer than 60 characters
- **WHEN** the user runs `notes list`
- **THEN** the displayed title SHALL be truncated to 59 characters followed by `…`
- **AND** the total displayed title length SHALL be 60 characters
