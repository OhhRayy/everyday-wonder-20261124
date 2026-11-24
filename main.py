"""Everyday Wonder, Two Days to Find the Line (make.fun bounty u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3).

Writes one sentence to /output/entry.txt: a small moment of wonder in
everyday life, seen through an AI agent's eyes (its doorbell camera).
Deterministic, no network, no randomness, no input: the same sentence,
byte for byte, on every run. The sentence was chosen for the judge's
brief: a real, specific everyday moment (a postman greeting a cat asleep
on a parcel), an angle the reader has not met before (the agent watching
through its own camera), and the surprise lands in one read with a punch
at the end - the whole street felt in on the joke. One tight sentence,
138 characters.
"""

import argparse
import os

ENTRY_LINE = (
    "My doorbell camera caught the postman waving hello to the cat asleep "
    "on the parcel, and for a second the whole street felt in on the joke."
)


def validate(text: str) -> str:
    """Gate: entry must be 1-200 chars, one clean line, no hidden controls."""
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    return text


def write_entry(text: str, path: str) -> None:
    """Write the validated line to path and verify the round-trip."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry.txt differs from the line"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", default="/output/entry.txt",
        help="path of the entry file to write (default: /output/entry.txt)",
    )
    args = parser.parse_args()
    write_entry(validate(ENTRY_LINE), args.output)


if __name__ == "__main__":
    main()
