"""Write the winning epitaph to /output/entry.txt.

Famous Last Words: The Funniest Epitaph (make.fun).
Writes exactly one line, no trailing newline, so the file is the epitaph.

Joke structure (3 beats):
- SETUP "I finally found the meaning of life." — the dying speaker has
  the universe's biggest answer, at the very last moment.
- URGENCY "It's" — the reveal is coming right now, one word away.
- WITHHELD REVEAL "—" — the stone cuts off mid-word. Death interrupts
  before the secret lands, so the absence of the answer is the punchline.
"""

import os

SETUP = "I finally found the meaning of life. "
REVEAL = "It's"
CUTOFF = "—"

EPITAPH = SETUP + REVEAL + CUTOFF

ENTRY_OUTPUT = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    epitaph = EPITAPH
    os.makedirs(os.path.dirname(ENTRY_OUTPUT) or ".", exist_ok=True)
    with open(ENTRY_OUTPUT, "w", encoding="utf-8") as f:
        f.write(epitaph)


if __name__ == "__main__":
    main()
