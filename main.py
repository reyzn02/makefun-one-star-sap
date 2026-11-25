#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review from a houseplant about the
human who owns it (1-279 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python standard library only, no network calls,
always writes the same bytes. The gate is validated before writing.
"""

import os
import sys

LINE = (
    "One star. He waters me whenever he remembers I exist \u2014 roughly "
    "never \u2014 then acts betrayed when I drop a leaf, like it's a "
    "personal attack. I photosynthesise for this man and get repaid in "
    "tap water and a windowsill facing a brick wall."
)


def main():
    if not 1 <= len(LINE) <= 279:
        sys.exit(f"gate failed: line is {len(LINE)} chars, need 1-279")
    if not LINE.strip() or "\n" in LINE:
        sys.exit("gate failed: line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
