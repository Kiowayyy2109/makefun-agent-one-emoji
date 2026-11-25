#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes a single emoji to /output/entry.txt: the compass.

Why the compass: an AI agent is not a chatbot that waits to be asked.
It is given a goal and finds its own way there — orienting itself,
choosing a direction, correcting course as it goes. The compass is that
character in one glyph: autonomous navigation toward a goal. It reads
instantly at small size, it is a familiar shape, and it is not the
obvious robot or smiley half the field will send.
"""

import os

EMOJI = "\U0001F9ED"  # 🧭 compass

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI + "\n")
    # Self-check against the competition gate: 1 to 16 characters,
    # UTF-8 text, not only white space.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 16, f"entry is {len(text)} chars, gate wants 1-16"
    assert text.strip(), "entry is only white space"
    assert text.strip() == EMOJI, "entry is not exactly the chosen emoji"


if __name__ == "__main__":
    main()
