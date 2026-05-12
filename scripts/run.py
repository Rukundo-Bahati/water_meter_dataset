#!/usr/bin/env python3
"""
run.py

Helper to run project scripts using the project's virtualenv Python when available.

Usage:
    # runs scripts/03_train.py using the venv python if present
    python3 scripts/run.py 03_train --epochs 1

Or pass a path to a script directly:
    python3 scripts/run.py scripts/05_retrain.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def find_venv_python(root: Path) -> Path | None:
    # Windows
    win = root / "venv" / "Scripts" / "python.exe"
    win_alt = root / "venv" / "Scripts" / "python"
    # POSIX
    posix = root / "venv" / "bin" / "python"

    for p in (win, win_alt, posix):
        if p.exists():
            return p

    return None


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python3 scripts/run.py <script> [args...]")
        return 2

    script_arg = argv[1]
    extra_args = argv[2:]

    root = Path(__file__).resolve().parent.parent

    # Accept either '03_train' -> scripts/03_train.py or full path
    if Path(script_arg).suffix == "":
        script_path = root / "scripts" / f"{script_arg}.py"
    else:
        script_path = Path(script_arg)

    if not script_path.exists():
        print(f"Script not found: {script_path}")
        return 3

    venv_python = find_venv_python(root)

    if venv_python:
        # Re-exec into the venv python with the target script and args
        os.execv(str(venv_python), [str(venv_python), str(script_path), *extra_args])
    else:
        print("No virtualenv python found; running with current interpreter.")
        os.execv(sys.executable, [sys.executable, str(script_path), *extra_args])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
