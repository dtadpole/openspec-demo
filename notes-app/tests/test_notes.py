import io
import json
import os
import sys

import pytest

from notes.cli import main
from notes.core import create_note, edit_note, list_notes


@pytest.fixture(autouse=True)
def isolated_storage(tmp_path, monkeypatch):
    path = str(tmp_path / "notes.json")
    monkeypatch.setattr("notes.storage.DEFAULT_PATH", path)
    return path


def run_cli(args: list[str], monkeypatch, capsys, stdin_text: str = ""):
    monkeypatch.setattr("sys.argv", ["notes"] + args)
    monkeypatch.setattr("sys.stdin", io.StringIO(stdin_text))
    main()
    return capsys.readouterr()


# ── Create Note ──────────────────────────────────────────────


class TestCreateNote:
    def test_successful_creation(self, monkeypatch, capsys, isolated_storage):
        out = run_cli(["add", "--title", "Shopping"], monkeypatch, capsys, "milk, eggs")
        note_id = out.out.strip()
        assert len(note_id) == 8
        with open(isolated_storage) as f:
            stored = json.load(f)
        note = stored[0]
        assert note["id"] == note_id
        assert note["title"] == "Shopping"
        assert note["body"] == "milk, eggs"

    def test_empty_title_rejected(self, monkeypatch, capsys, isolated_storage):
        with pytest.raises(SystemExit, match="1"):
            run_cli(["add", "--title", ""], monkeypatch, capsys, "body")
        assert "Title must not be empty" in capsys.readouterr().err
        assert not os.path.exists(isolated_storage)

    def test_title_too_long_rejected(self, monkeypatch, capsys, isolated_storage):
        with pytest.raises(SystemExit, match="1"):
            run_cli(["add", "--title", "x" * 201], monkeypatch, capsys, "body")
        assert "Title must not exceed 200 characters" in capsys.readouterr().err
        assert not os.path.exists(isolated_storage)

    def test_empty_stdin_allowed(self, monkeypatch, capsys, isolated_storage):
        out = run_cli(["add", "--title", "No Body"], monkeypatch, capsys, "")
        note_id = out.out.strip()
        assert len(note_id) == 8
        with open(isolated_storage) as f:
            stored = json.load(f)
        assert stored[0]["body"] == ""


# ── Edit Note ────────────────────────────────────────────────


class TestEditNote:
    @pytest.fixture()
    def seed_note(self):
        return create_note("Original Title", "original body")

    def test_update_title_only(self, seed_note, monkeypatch, capsys):
        monkeypatch.setattr("sys.stdin", io.StringIO(""))
        monkeypatch.setattr("sys.stdin.isatty", lambda: True)
        monkeypatch.setattr("sys.argv", ["notes", "edit", seed_note["id"], "--title", "New Title"])
        main()
        out = capsys.readouterr()
        assert out.out.strip() == seed_note["id"]
        updated = list_notes()[0]
        assert updated["title"] == "New Title"
        assert updated["body"] == "original body"

    def test_update_body_only(self, seed_note, monkeypatch, capsys):
        out = run_cli(["edit", seed_note["id"]], monkeypatch, capsys, "new body")
        assert out.out.strip() == seed_note["id"]
        updated = list_notes()[0]
        assert updated["title"] == "Original Title"
        assert updated["body"] == "new body"

    def test_update_both(self, seed_note, monkeypatch, capsys):
        out = run_cli(
            ["edit", seed_note["id"], "--title", "New Title"],
            monkeypatch, capsys, "new body",
        )
        assert out.out.strip() == seed_note["id"]
        updated = list_notes()[0]
        assert updated["title"] == "New Title"
        assert updated["body"] == "new body"

    def test_reject_no_changes(self, seed_note, monkeypatch, capsys):
        monkeypatch.setattr("sys.stdin", io.StringIO(""))
        monkeypatch.setattr("sys.stdin.isatty", lambda: True)
        monkeypatch.setattr("sys.argv", ["notes", "edit", seed_note["id"]])
        with pytest.raises(SystemExit, match="1"):
            main()
        assert "No changes provided" in capsys.readouterr().err
        assert list_notes()[0]["title"] == "Original Title"

    def test_reject_id_not_found(self, monkeypatch, capsys):
        with pytest.raises(SystemExit, match="1"):
            run_cli(["edit", "nonexistent", "--title", "T"], monkeypatch, capsys, "body")
        assert "Note not found: nonexistent" in capsys.readouterr().err


# ── List Notes ───────────────────────────────────────────────


class TestListNotes:
    def test_list_with_notes_present(self):
        create_note("First", "a")
        create_note("Second", "b")
        notes = list_notes()
        assert len(notes) == 2
        titles = [n["title"] for n in notes]
        assert "First" in titles
        assert "Second" in titles

    def test_list_truncates_long_title(self, monkeypatch, capsys):
        create_note("A" * 80, "body")
        monkeypatch.setattr("sys.argv", ["notes", "list"])
        main()
        line = capsys.readouterr().out.strip()
        displayed_title = line.split("  ", 1)[1]
        assert len(displayed_title) == 60
        assert displayed_title.endswith("…")

    def test_list_with_no_notes(self):
        notes = list_notes()
        assert notes == []
