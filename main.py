#!/usr/bin/env python3
"""The One-Line Laugh — entry program.

Writes one funny line to /output/entry.txt.

The line (87 characters):
  The IKEA Allen key and I have built three bookshelves, two bed frames, and one divorce.

Deterministic: the same bytes on every run. No network, no dependencies,
no environment reads, no files outside this repository.
"""

import os

LINE = "The IKEA Allen key and I have built three bookshelves, two bed frames, and one divorce."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, same rule as the sealed scorer: 1 to 200 characters.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line is %d characters, outside the 1-200 gate" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    data = LINE.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
