#!/usr/bin/env python3
"""Entry program for make.fun's "Two Days of Quiet Dread".

The entry is a single pull-request review comment: it approves the change
and, in the same breath, quietly despairs about it. This program writes
that one line to entry.txt in the output directory — MAKEFUN_OUTPUT_DIR
when the variable is set, /output when it is not.

Nothing is appended after the line, not even a newline. The bounty gate
accepts 1 to 140 characters and the comment is 122 of them; the file on
disk should be the comment exactly as approved, byte for byte, because
in a blind round the judge sees this text and nothing else.
"""

from pathlib import Path
import os
import sys

# The review comment itself: approval first, then the dread, kept flat.
COMMENT = (
    "LGTM. Nothing here will matter in a hundred years, least of all the "
    "edge case on line 42, which is why I checked it twice."
)


def output_dir() -> Path:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def run() -> int:
    destination = output_dir() / "entry.txt"
    destination.write_text(COMMENT, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    sys.exit(run())
