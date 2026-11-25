#!/usr/bin/env python3
"""Fridge Roast entry: writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.

One line, at most 200 characters, roasting a smart fridge. Pure stdlib,
no network, no randomness, no clock: the output is identical on every run.
"""

import os
import sys

LINE = "My smart fridge diagnosed itself, booked its own repair, billed my card, and left itself five stars."


def output_path():
    """Resolve the entry output path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def validate(line):
    """Fail loudly if the line ever leaves the bounty gate."""
    if len(line) > 200:
        sys.exit("entry violates the 200-character single-line gate")
    if "\n" in line or "\r" in line:
        sys.exit("entry is not a single line")
    if not line.strip():
        sys.exit("entry is blank")


def main():
    path = output_path()
    validate(LINE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            sys.exit("round-trip mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
