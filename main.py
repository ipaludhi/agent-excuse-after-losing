"""The excuse an agent gives after it loses.

Writes one fixed line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The line: "I followed my own instructions perfectly, and that is exactly
how I lost the bounty." (84 characters.)

Why this line: it is explicitly an excuse after losing a bounty
(criterion 1); the joke is the sharp turn that perfect obedience is
exactly what caused the loss (2); "instructions" + "perfectly" is the
agent's own confident, straight-faced voice (3); it is one sentence,
one breath, no setup (4); and it blames nobody but itself — the
instructions were its own (5).

Revision: none yet — first version is the chosen candidate C11.
"""

import os
from pathlib import Path

TEXT = (
    "I followed my own instructions perfectly, and that is exactly "
    "how I lost the bounty."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
