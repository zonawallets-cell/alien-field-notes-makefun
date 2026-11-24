"""Alien Field Notes: The Two Day Earth Review.

Writes exactly one line (at most 200 characters) -- an alien tourist's
review of planet Earth after a two-day visit -- to <output_dir>/entry.txt.

Pure standard library (os only). Fully deterministic: the same line,
byte for byte, on every run.
"""

import os

LINE = (
    "Two days on Earth: they set a cake on fire, make a silent wish to it, "
    "blow it out, then eat it. The cake grants nothing. 2/5 stars."
)

MAX_CHARS = 200


def validate(text):
    """Gate: 1-200 chars, UTF-8, a single line, not only whitespace."""
    if not text or not text.strip():
        raise SystemExit("line must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("line exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise SystemExit("line must not contain a newline")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    text = validate(LINE.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back what was written: the file on disk must be exactly the
    # validated line plus its trailing newline, byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != (text + "\n").encode("utf-8"):
        raise SystemExit("entry.txt on disk differs from the validated line")
    print(text)


if __name__ == "__main__":
    main()
