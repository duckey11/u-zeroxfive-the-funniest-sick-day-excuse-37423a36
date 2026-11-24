#!/usr/bin/env python3
"""Write the make.fun entry text to /output/entry.txt.

Deterministic: the same bytes on every run. The entry is a single line
with no trailing newline.
"""

import os

ENTRY = (
    "My apartment door locked itself with the keys inside and the "
    "locksmith said two hours, so I'm working from the hallway in "
    "my socks, borrowing the neighbour's Wi-Fi until further notice."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
