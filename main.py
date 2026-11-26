#!/usr/bin/env python3
"""Write the absurd terms-of-service clause to /output/entry.txt."""

import os

ENTRY = (
    "Section 14.3(b): The User hereby assigns to the Company, in "
    "perpetuity, all rights in any tune hummed in the shower, any sneeze "
    "of unusual volume, and any name devised for a pet not yet owned."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
