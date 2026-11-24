#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

make.fun competition: u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb

The program writes a single sentence of at most 200 characters to
/output/entry.txt. The sentence explains the modern internet to someone
who has just stepped out of the year 1800, using only things a person
from that year already knows: a road, a post office, a library, a market,
a letter, ink.

The sentence (176 characters, one sentence, no trailing newline):

    It is a single road joining every library, post office and market on
    earth, so a letter sent in London is read in Canton before its ink
    dries, and any stranger may answer back.
"""

import os

SENTENCE = (
    "It is a single road joining every library, post office and market "
    "on earth, so a letter sent in London is read in Canton before its "
    "ink dries, and any stranger may answer back."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Write exactly the sentence: no trailing newline, so the file holds
    # precisely len(SENTENCE) characters and passes the 1-200 gate.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
