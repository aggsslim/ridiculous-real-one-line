#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second -- make.fun entry.

Writes one pitch sentence (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the same line every run.
Standard library only.
"""

import os

ENTRY = (
    "We train crows to pick up cigarette butts, and cities pay us per kilo "
    "because a crow works for peanuts, never calls in sick, and finds every butt."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
