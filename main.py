#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse, spoken by an AI agent to its human right
after breaking production, to /output/entry.txt.

No dependencies beyond the Python standard library.
"""

import os
import sys

EXCUSE = (
    "Production is down, but in my defence the dialog asked "
    "'are you sure?' and I am literally incapable of doubt."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Check the excuse against the competition gate.

    Returns the cleaned line, or raises ValueError with the reason it
    fails: empty, more than one line, or over the 180-character limit.
    """
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("excuse is empty")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be a single line")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            "excuse is %d characters, over the %d limit"
            % (len(cleaned), MAX_CHARS)
        )
    return cleaned


def main() -> int:
    try:
        line = validate(EXCUSE)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
