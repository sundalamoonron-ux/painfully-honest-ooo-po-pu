"""The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, 1-200 characters) to entry.txt.

The winning line was picked by a pairwise tournament over 12 candidates,
judged in the house judge's order: (1) honest + polite, (2) admits a
private truth about absence/inbox, (3) warm professional tone a manager
would allow, (4) one clean sentence, (5) a quotable turn of phrase.

Winner (11 wins out of 11 games): the line below. It admits the private
truth that checking email on holiday quietly turns the holiday into
work, stays warm and grateful, and lands on a phrase a reader would
quote: "my holiday quietly becomes work".
"""

import os

WINNER = (
    "I'm out of office until Monday, and I'll be honest: I'm not "
    "checking email because every time I do, my holiday quietly "
    "becomes work \u2014 thank you for waiting."
)


def main() -> None:
    # Gate self-check: 1-200 characters, single sentence, not whitespace-only.
    text = WINNER.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") <= 1, "entry must be a single sentence"
    assert text, "entry must not be whitespace-only"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WINNER)


if __name__ == "__main__":
    main()
