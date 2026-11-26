#!/usr/bin/env python3
"""make.fun entry: Roast the Smart Fridge (smart-fridge-b).

The entry is one line roasting a smart fridge. The gag casts the
fridge as a passive-aggressive flatmate: it sends a "we need to
talk" text over a 2am snack run, then judges the leftovers as if
it contributed to the rent. The program checks the line against
the competition gate (RULES.txt: /output/entry.txt must be UTF-8
text of 1 to 160 characters, not only whitespace, a single line)
and writes it to /output/entry.txt.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 160


def build_entry():
    """Return the roast line, my own wording throughout."""
    # The turn is a relationship cliche in an appliance's mouth.
    # "We need to talk" is how a partner starts a row, and "like
    # it pays the rent" is the punch: a fridge very obviously does
    # not pay rent, so its judgement is pure cheek.
    return (
        "My smart fridge texts me 'we need to talk' every time I open "
        "it at 2am, then judges the leftovers like it pays the rent."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
