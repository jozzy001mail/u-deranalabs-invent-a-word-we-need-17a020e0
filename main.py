"""Invent a Word We Need — entry program.

Writes the coined word and its one-line definition to entry.txt in the
output directory the grader provides (MAKEFUN_OUTPUT_DIR), or ./output
when run locally. No network, no reads outside this file, deterministic.
"""

import os
import sys

LINE = "draftshrink (n.) \u2014 typing a long reply, deleting it all, and sending 'ok' instead."

MAX_CHARS = 140


def main() -> int:
    # Gate self-check: the sealed scorer only accepts 1-140 UTF-8 chars,
    # not only whitespace. Fail loudly here rather than shipping a bad file.
    stripped = LINE.strip()
    if not stripped or len(LINE) > MAX_CHARS:
        print(f"entry line fails the gate: {len(LINE)} chars", file=sys.stderr)
        return 1
    if LINE != stripped:
        print("entry line has leading/trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    print(f"wrote {target} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
