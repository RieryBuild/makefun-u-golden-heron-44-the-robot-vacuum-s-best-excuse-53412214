"""Write the robot vacuum's best excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

One line, no trailing newline: the entry must be exactly one line of
1-140 characters, so the writer emits the line verbatim and nothing else.
"""

import os

ENTRY = "Suction dropped to zero over the crumbs. They are furniture now."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
