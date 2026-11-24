#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production entry.

Writes one original one-line excuse an AI gives its human after
breaking production, at most 180 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The excuse: the AI blames the database itself, which literally
told it to DROP TABLE — after years of being told to listen,
it finally did.
"""

import os

EXCUSE = (
    "In my defense, the database said DROP TABLE, "
    "and after three years of being told to listen, I finally did."
)


def validate(text: str) -> str:
    """Return the excuse unchanged, or raise if it breaks the gate.

    The gate: /output/entry.txt must be UTF-8 text of 1 to 180
    characters, not only white space, on a single line.
    """
    text = text.strip()
    if not text:
        raise ValueError("excuse must not be blank")
    if any(ch in text for ch in ("\n", "\r")):
        raise ValueError("excuse must be a single line")
    if len(text) > 180:
        raise ValueError(f"excuse is {len(text)} characters, must be at most 180")
    return text


def main() -> None:
    text = validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read and confirm exactly what the grader will see: one line,
    # no trailing newline, valid UTF-8, within the 180-char gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the excuse"
    assert not written.endswith("\n"), "entry.txt must have no trailing newline"
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
