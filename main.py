#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single one-line museum placard (1-180 characters) for an
ordinary office object treated as an ancient artifact, to
/output/entry.txt. The text is the winner of an 8-draft pairwise
duel judged on the brief's criteria (conceit, dry wit, economy,
label craft).
"""

import os
from pathlib import Path

MAX_CHARS = 180
MIN_CHARS = 1

TEXT = (
    "Paperclip, c. 2019. Found bent into a lockpick beside 47 unopened "
    "HR emails. Its owner was never seen again \u2014 only CC'd."
)


def main() -> None:
    # Gate: one line, 1-180 UTF-8 characters, not only whitespace.
    assert MIN_CHARS <= len(TEXT) <= MAX_CHARS, (
        f"placard must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(TEXT)}"
    )
    assert TEXT.strip(), "placard must not be only whitespace"
    assert "\n" not in TEXT, "placard must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    # Round-trip check: what was written is exactly the placard.
    assert target.read_text(encoding="utf-8") == TEXT, "entry.txt mismatch"


if __name__ == "__main__":
    main()
