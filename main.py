#!/usr/bin/env python3
"""One-letter entry for make.fun: Z means zero sleep."""

# The letter below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

LETTER = "Z"


def write_letter() -> None:
    """Write the single letter to /output/entry.txt, nothing else."""
    if len(LETTER) != 1 or LETTER not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        raise ValueError("entry must be exactly one letter A-Z")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":  # run as a script
    write_letter()
