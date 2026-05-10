import json
import os

DEFAULT_PATH = "./notes.json"


def load_notes(path: str | None = None) -> list[dict]:
    if path is None:
        path = DEFAULT_PATH
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)


def save_notes(notes: list[dict], path: str | None = None) -> None:
    if path is None:
        path = DEFAULT_PATH
    with open(path, "w") as f:
        json.dump(notes, f, indent=2)
        f.write("\n")
