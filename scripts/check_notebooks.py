#!/usr/bin/env python3
"""Validate every notebook: nbformat schema + Python syntax of each code cell.

Mirrors the notebook-validation check CI runs on every PR. Run it before opening
a PR:

    python scripts/check_notebooks.py

Exits non-zero on the first invalid notebook.
"""

import ast
import glob
import sys

import nbformat


def check(path: str) -> None:
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        src = cell.source
        try:
            ast.parse(src)
        except SyntaxError:
            # Cells may use top-level await; wrap in an async def and retry.
            ast.parse("async def _c():\n" + "\n".join("    " + line for line in src.splitlines()))


def main() -> int:
    paths = sorted(glob.glob("**/*.ipynb", recursive=True))
    if not paths:
        print("no notebooks found")
        return 0
    for path in paths:
        check(path)
        print("ok", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
