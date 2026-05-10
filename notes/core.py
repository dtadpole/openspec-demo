import secrets

from notes.storage import load_notes, save_notes


def list_notes() -> list[dict]:
    return load_notes()


def edit_note(note_id: str, title: str | None = None, body: str | None = None) -> dict:
    if title is not None:
        if not title.strip():
            raise ValueError("Title must not be empty")
        if len(title) > 200:
            raise ValueError("Title must not exceed 200 characters")

    if title is None and body is None:
        raise ValueError("No changes provided")

    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            if title is not None:
                note["title"] = title
            if body is not None:
                note["body"] = body
            save_notes(notes)
            return note

    raise KeyError(f"Note not found: {note_id}")


def create_note(title: str, body: str) -> dict:
    if not title.strip():
        raise ValueError("Title must not be empty")
    if len(title) > 200:
        raise ValueError("Title must not exceed 200 characters")

    note = {
        "id": secrets.token_hex(4),
        "title": title,
        "body": body,
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    return note
