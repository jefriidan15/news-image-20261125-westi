#!/usr/bin/env python3
"""Entry for make.fun news-image-20261125.

Copies the front-page image shipped in this repository to the
output location the grader reads: /output/entry.png (or the
directory named by MAKEFUN_OUTPUT_DIR when it is set).

Standard library only, no network, deterministic: the bytes
written are exactly the bytes of entry.png in this repository.
"""

import os
import shutil
from pathlib import Path

# The image is part of the repository, so the copy is a pure file
# operation: same input bytes in, same output bytes out, every run.


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
