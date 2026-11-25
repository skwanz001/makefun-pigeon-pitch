"""Pigeon Pitch, One Line — entrypoint.

Writes the city pigeon's one-line elevator pitch to /output/entry.txt.
Standard library only. The pitch is a single line, 173 characters,
English, in the pigeon's own voice: the original drone, raising a
seed round — literally.
"""

import os

PITCH = (
    "Amazon spent billions teaching drones to deliver. "
    "I was born with wings, navigate by statue, and work for breadcrumbs "
    "\u2014 I'm the original drone, and I'm raising a seed round."
)


def main() -> None:
    text = " ".join(PITCH.split())
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "pitch must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "written entry does not match the pitch"


if __name__ == "__main__":
    main()
