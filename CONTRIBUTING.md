# Contributing

Thanks for helping improve the Dreadnode AI Red Teaming Cookbook.

## Conventions

- Concise markdown before every code cell; explain the *why*, not the obvious.
- Each attack notebook: a "what is / why it matters (CIA)" intro, a prerequisites
  banner, a link to the matching Learning Guide page, a "Read the findings" link to
  the platform, a "Homework" section, and a TUI / CLI footer.
- ASCII only - no em dashes or smart quotes.
- **Keep the execution outputs** so readers can see the results and charts
  without running anything. Just make sure a notebook runs cleanly end to end
  before committing its outputs.

## Before opening a PR

CI runs two checks on every PR - **gitleaks** secret scanning and notebook
validation. Run the validation locally first:

```bash
python scripts/check_notebooks.py
```

It validates every notebook's nbformat schema and the Python syntax of each code
cell (allowing top-level `await`), exiting non-zero on the first problem.
