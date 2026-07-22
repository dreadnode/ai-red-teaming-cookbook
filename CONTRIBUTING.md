# Contributing

Thanks for helping improve the Dreadnode AI Red Teaming Cookbook.

## The notebooks are generated

Do **not** hand-edit the `.ipynb` files - they are produced by
[`tools/build_notebooks.py`](tools/build_notebooks.py). Edit the generator and
regenerate:

```bash
python tools/build_notebooks.py
```

Committed notebooks have **no execution outputs** (they are generated clean). Please
keep it that way so diffs stay readable.

## Conventions

- Concise markdown before every code cell; explain the *why*, not the obvious.
- Each attack notebook: a "what is / why it matters (CIA)" intro, a prerequisites
  banner, a "Read the findings" link to the platform, a "Homework" section, and a
  TUI / CLI footer.
- ASCII only - no em dashes or smart quotes.

## Before opening a PR

```bash
python - <<'PY'
import nbformat, ast, glob
for f in glob.glob("**/*.ipynb", recursive=True):
    nb = nbformat.read(f, as_version=4); nbformat.validate(nb)
    for c in nb.cells:
        if c.cell_type == "code":
            src = c.source
            try:
                ast.parse(src)
            except SyntaxError:
                ast.parse("async def _w():\n" + "\n".join("    " + l for l in src.splitlines()))
    print("ok", f)
PY
```

CI runs this same check on every PR.
