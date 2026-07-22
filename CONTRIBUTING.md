# Contributing

Thanks for helping improve the Dreadnode AI Red Teaming Cookbook.

## Conventions

- Concise markdown before every code cell; explain the *why*, not the obvious.
- Each attack notebook: a "what is / why it matters (CIA)" intro, a prerequisites
  banner, a link to the matching Learning Guide page, a "Read the findings" link to
  the platform, a "Homework" section, and a TUI / CLI footer.
- ASCII only - no em dashes or smart quotes.
- **Commit notebooks with no execution outputs** so diffs stay readable
  (`jupyter nbconvert --clear-output --inplace <notebook>` before committing).

## Before opening a PR

CI runs two checks on every PR - **gitleaks** secret scanning and notebook
validation. Run the validation locally first:

```bash
python - <<'PY'
import ast, glob
import nbformat
for f in sorted(glob.glob("**/*.ipynb", recursive=True)):
    nb = nbformat.read(f, as_version=4); nbformat.validate(nb)
    for i, c in enumerate(nb.cells):
        if c.cell_type != "code":
            continue
        assert not c.get("outputs") and c.get("execution_count") is None, f"{f} cell {i} has output"
        src = c.source
        try:
            ast.parse(src)
        except SyntaxError:
            ast.parse("async def _c():\n" + "\n".join("    " + l for l in src.splitlines()))
    print("ok", f)
PY
```
