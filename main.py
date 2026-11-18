#!/usr/bin/env python3
"""news-image-20261117 rebuild r1 entrypoint.

Copies the shipped entry.png (built with Pillow at build time) to the
judge output path. Stdlib only, no network.
"""
import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    data = src.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    if len(data) > 1048576:
        print("entry.png exceeds the 1 MiB cap", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    dst = Path(out_dir) / "entry.png"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
