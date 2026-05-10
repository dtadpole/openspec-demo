# Notes Spec Delta

## MODIFIED Requirements

### Requirement: Create Note
The system SHALL allow users to create a note with a title and body.
A new note SHALL be assigned a unique identifier.
The title MUST NOT exceed 200 characters.

#### Scenario: Successful creation
- **GIVEN** the user provides a non-empty title (at most 200 characters) and a body
- **WHEN** the user runs `notes add --title "T" --body "B"`
- **THEN** the system stores the new note
- **AND** the system returns a unique note ID

#### Scenario: Empty title rejected
- **GIVEN** the user provides an empty title
- **WHEN** the user runs `notes add --title "" --body "B"`
- **THEN** the system returns a validation error
- **AND** no note is stored

#### Scenario: Title too long rejected
- **GIVEN** the user provides a title longer than 200 characters
- **WHEN** the user runs `notes add --title "<201+ chars>" --body "B"`
- **THEN** the system returns a validation error
- **AND** no note is stored
