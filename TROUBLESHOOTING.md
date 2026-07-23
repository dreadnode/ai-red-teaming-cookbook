# Troubleshooting

Common issues when running the cookbook notebooks, and how to fix them. If you
hit something not covered here, open an issue.

## Installation

### `pip install dreadnode` fails to find a compatible version, or `ModuleNotFoundError: No module named 'dreadnode'`

The SDK requires **Python 3.11 - 3.13**. Several systems (for example Ubuntu
22.04) ship Python 3.10, on which the install resolves nothing and the import
then fails.

Use a 3.11+ interpreter. The quickest way is [uv](https://docs.astral.sh/uv/):

```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
uv pip install "dreadnode>=2.0.37" jupyter
```

Verify:

```bash
python -c "import dreadnode, sys; print(dreadnode.__version__, sys.version.split()[0])"
```

## Authentication

### Calls fail with an auth error before anything runs

Sign in first so the SDK has a server and token:

```bash
dn login        # opens the browser (device flow)
```

Alternatively, set `DREADNODE_API_KEY` (and `DREADNODE_SERVER` if you self-host)
in your environment before calling `dn.configure()`.

## Configuration

### `403: You do not have permission to perform this action on this organization`

`ORG` is pointing at a workspace you are not a member of. Set it to **your own**
organization slug - the one in your platform URL
(`https://app.dreadnode.io/<your-org-slug>/...`):

```python
ORG = "your-org-slug"   # from your platform URL, not "dreadnode"
WORKSPACE = "main"
```

## Environments

### Provisioning takes a little while

`provision()` spins up a hosted target and polls until the service answers.
This normally takes about 10 - 60s per environment (state moves `building` ->
`ready`), and the helper prints the URL once it is live. If an environment never
becomes ready within the timeout, re-run the cell.

### A `dn/<model>` id is not available

Managed model availability varies by platform and deployment. If a `dn/<id>`
referenced in a notebook returns a not-found or routing error, swap it for a
model your platform exposes (check the models list in the platform UI or ask
your admin) and update `TARGET_MODEL` / the attacker / the judge accordingly.

## Credits

### A run stops partway, or a call is rejected unexpectedly

Runs draw down credits for inference (managed `dn/` calls), compute (hosted
target environments), and span/trace storage. Check your balance in the platform
UI and top up if it is depleted.
