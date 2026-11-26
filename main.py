#!/usr/bin/env python3
"""Make the Judge Laugh in One Line entry for make.fun.

Writes one original sentence - someone asks their toaster for a sign
from the universe, and gets a performance review instead - to entry.txt.
The setup promises a miracle; the punchline lands at the very end,
when the burnt toast turns out to be middle management.
Deterministic, standard library only: the same bytes every run.
"""

import os

LINE = (
    "I asked my toaster for a sign from the universe, and it burned "
    "my face into the bread, which felt less like a miracle and more "
    "like a performance review."
)


def main() -> None:
    # Enforce the competition gate locally: 1 to 200 characters, one line.
    assert 1 <= len(LINE) <= 200, "LINE must be 1-200 characters"
    assert "\n" not in LINE, "LINE must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify the written bytes match exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt bytes differ from LINE"


if __name__ == "__main__":
    main()
