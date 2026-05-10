# Notes Spec

## Requirements

### Requirement: Create Note
The system SHALL allow users to create a note with a title and body.
A new note SHALL be assigned a unique identifier.
The title MUST NOT exceed 200 characters.
The body SHALL be read from stdin.

#### Scenario: Successful creation
- **GIVEN** the user provides a non-empty title and body via stdin
- **WHEN** the user runs `echo "B" | notes add --title "T"`
- **THEN** the system stores the new note
- **AND** the system returns a unique note ID

#### Scenario: Empty title rejected
- **GIVEN** the user provides an empty title
- **WHEN** the user runs `echo "B" | notes add --title ""`
- **THEN** the system returns a validation error
- **AND** no note is stored

#### Scenario: Title too long rejected
- **GIVEN** the user provides a title longer than 200 characters
- **WHEN** the user runs `echo "B" | notes add --title "<201+ chars>"`
- **THEN** the system returns a validation error
- **AND** no note is stored

#### Scenario: Empty stdin allowed
- **GIVEN** the user provides a valid title but stdin is empty
- **WHEN** the user runs `echo -n "" | notes add --title "T"`
- **THEN** the system stores a new note with an empty body
- **AND** the system returns a unique note ID

### Requirement: Edit Note
The system SHALL allow users to modify an existing note's title and/or body.
The title MUST NOT exceed 200 characters.
The title MUST NOT be empty.
The body, if provided, SHALL be read from stdin.

#### Scenario: Update title only
- **GIVEN** a note with id `<id>` exists
- **AND** the user provides a new title but no stdin body
- **WHEN** the user runs `echo -n "" | notes edit <id> --title "New Title"`
- **THEN** the system updates the note's title
- **AND** the body remains unchanged
- **AND** the system prints the note ID

#### Scenario: Update body only
- **GIVEN** a note with id `<id>` exists
- **AND** the user provides body via stdin but no `--title` flag
- **WHEN** the user runs `echo "new body" | notes edit <id>`
- **THEN** the system updates the note's body
- **AND** the title remains unchanged
- **AND** the system prints the note ID

#### Scenario: Update both
- **GIVEN** a note with id `<id>` exists
- **AND** the user provides both `--title` and body via stdin
- **WHEN** the user runs `echo "new body" | notes edit <id> --title "New Title"`
- **THEN** the system updates both the note's title and body
- **AND** the system prints the note ID

#### Scenario: Reject when no changes
- **GIVEN** a note with id `<id>` exists
- **AND** the user provides no `--title` flag and stdin is empty
- **WHEN** the user runs `echo -n "" | notes edit <id>`
- **THEN** the system returns a validation error "No changes provided"
- **AND** the note remains unchanged

#### Scenario: Reject when ID not found
- **GIVEN** no note with id `nonexistent` exists
- **WHEN** the user runs `echo "body" | notes edit nonexistent --title "T"`
- **THEN** the system returns an error "Note not found: nonexistent"
- **AND** no notes are modified

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
