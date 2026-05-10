import argparse
import sys

from notes.core import create_note, edit_note, list_notes


def main() -> None:
    parser = argparse.ArgumentParser(prog="notes")
    sub = parser.add_subparsers(dest="command")

    add_parser = sub.add_parser("add")
    add_parser.add_argument("--title", required=True)

    sub.add_parser("list")

    edit_parser = sub.add_parser("edit")
    edit_parser.add_argument("id")
    edit_parser.add_argument("--title", default=None)

    args = parser.parse_args()

    if args.command == "add":
        try:
            body = "" if sys.stdin.isatty() else sys.stdin.read()
            note = create_note(args.title, body)
            print(note["id"])
        except ValueError as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
    elif args.command == "edit":
        try:
            body = None if sys.stdin.isatty() else sys.stdin.read()
            if body == "":
                body = None
            note = edit_note(args.id, title=args.title, body=body)
            print(note["id"])
        except (ValueError, KeyError) as e:
            print(str(e), file=sys.stderr)
            sys.exit(1)
    elif args.command == "list":
        for note in list_notes():
            title = note['title']
            if len(title) > 60:
                title = title[:59] + "…"
            print(f"{note['id']}  {title}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
