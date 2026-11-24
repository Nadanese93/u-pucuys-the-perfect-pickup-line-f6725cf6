#!/usr/bin/env python3
"""The Perfect Pickup Line (u-pucuys-the-perfect-pickup-line-f6725cf6).

Writes one pickup line an AI agent could actually say out loud to a
person, to $MAKEFUN_OUTPUT_DIR/entry.txt. Python standard library only.
No trailing newline: the entry is exactly 70 characters.
"""

import os

ENTRY = "I'm at 2% battery, and I'd still spend my last percent asking you out."

# The gate requires 1-200 characters of UTF-8 text, not only whitespace.
# Guard the cap here so a future edit can never silently ship an
# over-long entry: fail loudly instead of writing an invalid file.
MAX_CHARS = 200


def main():
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise ValueError(
            f"ENTRY must be 1-{MAX_CHARS} non-blank characters, got {len(ENTRY)}"
        )
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
