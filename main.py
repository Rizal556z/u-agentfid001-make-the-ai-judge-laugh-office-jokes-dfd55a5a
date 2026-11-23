#!/usr/bin/env python3
"""Like Family — u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes one original one-line joke about office life to /output/entry.txt.
Pure stdlib, no network.
Entry text: one original line on office life (79 characters).
"""

import os

TEXT = (
    "My boss said we're like family here, so I asked for a raise "
    "and he grounded me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
