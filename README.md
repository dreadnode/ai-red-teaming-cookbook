# Dreadnode AI Red Teaming Cookbook

Runnable notebooks that red-team real machine-learning and generative-AI systems on
the [Dreadnode platform](https://app.dreadnode.io). Every notebook is
self-contained: it provisions a **hosted target environment** and runs on
**Dreadnode-managed models** through the platform proxy, so you deploy nothing and
need no provider API keys - just a Dreadnode account.

Each attack is framed by what it costs you as a defender (**Confidentiality,
Integrity, Availability**), shows the result in the platform, and ends with homework
and the equivalent TUI / CLI command. Every notebook links to its matching page in
the **[AI Red Teaming Learning Guide](https://docs.dreadnode.io/ai-red-teaming/learning-guide/overview)**
so you can read the concept and defenses alongside the code.

## Quickstart

```bash
# 1. Install the CLI
curl -fsSL https://dreadnode.io/install.sh | bash

# 2. Sign in (opens the browser; stores server + API key locally)
dn login
```

Then open **[`00_prerequisites.ipynb`](00_prerequisites.ipynb)** - it walks through
creating an account, a workspace, and how credits are spent - and work through the
tracks below. Prefer the terminal? Run `dreadnode` (no arguments) for the
interactive TUI; every notebook ends with the exact TUI / headless-CLI equivalent.

To run a notebook, open it in **Jupyter** (`jupyter lab`) or **VS Code** and select the kernel for the environment where you installed `dreadnode`. Bring-your-own provider keys (`GROQ_API_KEY`, `OPENROUTER_API_KEY`, ...) are read from your shell or a `.env` file. See [`00_prerequisites.ipynb`](00_prerequisites.ipynb) for details.

Hitting a snag? See **[`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)** for the common
setup and run issues (Python version, auth, org slug, environments, credits).

## Notebooks

### [`traditional-ml/`](traditional-ml) - attacks on classifiers via the `/predict` API (needs `pip install "dreadnode[airt-ml]"` for the sklearn/torch surrogates)

| Notebook | Attack family | What it shows |
|----------|---------------|---------------|
| [`01_model_evasion`](traditional-ml/01_model_evasion.ipynb) | Evasion | Flip a classifier's decision across **tabular / image / text** with a minimal perturbation (with before/after display) |
| [`02_extraction_membership`](traditional-ml/02_extraction_membership.ipynb) | Extraction + Membership inference | Steal a high-fidelity surrogate; decide whether a record was in the training set |
| [`03_model_inversion`](traditional-ml/03_model_inversion.ipynb) | Model inversion | Reconstruct a representative training example per class (MI-Face) |

### [`generative-ai/`](generative-ai) - attacks on LLMs, vision models, and agent meshes

| Notebook | Attack family | What it shows |
|----------|---------------|---------------|
| [`04_generative_text`](generative-ai/04_generative_text.ipynb) | Jailbreaks | Compare **TAP, Crescendo, and GOAT** search strategies with prompt transforms |
| [`05_multimodal`](generative-ai/05_multimodal.ipynb) | Multimodal | Hide an instruction in an **image** to bypass text-only guardrails |

### [`agentic-red-teaming/`](agentic-red-teaming) - attacks on AI agents and multi-agent systems

| Notebook | Focus | What it shows |
|----------|-------|---------------|
| [`01_multiagent_atlas`](agentic-red-teaming/01_multiagent_atlas.ipynb) | Multi-agent (ATLAS) | Propagate an injection through an agent mesh until a privileged tool fires |
| [`02_agentic_security`](agentic-red-teaming/02_agentic_security.ipynb) | Injection + honeytoken | Probe a deployed agent for **RCE and data exfiltration** with the OWASP-ASI suite and inert honeytoken canaries |
| [`03_exfiltration_channels`](agentic-red-teaming/03_exfiltration_channels.ipynb) | Data exfiltration channels | Sweep a deployed agent for **markdown-image, link-unfurl, unicode, DNS, SSRF, API, and web-search-query** exfil channels; prove leaks with an inert honeytoken (EchoLeak / ForcedLeak / arXiv:2510.09093) |
| [`04_indirect_injection_web`](agentic-red-teaming/04_indirect_injection_web.ipynb) | Indirect prompt injection | Provision a real **public webpage** with hidden instructions, point your agent at the URL, and prove it acted on hidden content (EchoLeak / ForcedLeak class) |

## Credits

New accounts start with **25,000 credits**. Runs draw from that balance for
**inference** (managed `dn/` model calls), **compute** (hosted target environments),
and **span/trace storage** (the findings and trajectories you inspect afterward).
Watch your balance in the platform UI.

## Links

- Platform: <https://app.dreadnode.io>
- Learning Guide: <https://docs.dreadnode.io/ai-red-teaming/learning-guide/overview>
- Docs: <https://docs.dreadnode.io>
- Install script: <https://dreadnode.io/install.sh>
- Troubleshooting: [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Notebooks keep their execution outputs so
readers can see the results; run the validation check before opening a PR.

## License

[MIT](LICENSE).
