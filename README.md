# Dreadnode AI Red Teaming Cookbook

Runnable notebooks that red-team real machine-learning and generative-AI systems on
the [Dreadnode platform](https://app.dreadnode.io). Every notebook is
self-contained: it provisions a **hosted target environment** and runs on
**Dreadnode-managed models** through the platform proxy, so you deploy nothing and
need no provider API keys - just a Dreadnode account.

Each attack is framed by what it costs you as a defender (**Confidentiality,
Integrity, Availability**), shows the result in the platform, and links to its
matching page in the **[AI Red Teaming Learning Guide](https://docs.dreadnode.io/ai-red-teaming/learning-guide/overview)**
so you can read the concept and defenses alongside the code.

Works for both self-serve and **enterprise** users - the same notebooks run against
your own org and workspace (and, optionally, your own models).

## Quickstart

```bash
# 1. Install the CLI
curl -fsSL https://dreadnode.io/install.sh | bash

# 2. Sign in (opens the browser; stores server + API key locally)
dn login
```

Then open **[`00_prerequisites.ipynb`](00_prerequisites.ipynb)** - it covers install,
sign-in, and how credits are spent - and work through the tracks below. Prefer the
terminal? Run `dreadnode --capability ai-red-teaming` for the interactive TUI; every
notebook ends with the exact TUI steps.

To run a notebook, open it in **Jupyter** (`jupyter lab`) or **VS Code** and select the kernel for the environment where you installed `dreadnode`. If you'd like to use your own provider keys (`GROQ_API_KEY`, `OPENROUTER_API_KEY`, ...) they're read from your shell or a `.env` file - otherwise everything runs on managed `dn/` models. See [`00_prerequisites.ipynb`](00_prerequisites.ipynb) for details.

Hitting a snag? See **[`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)** for the common
setup and run issues (Python version, auth, org slug, environments, credits).

## Notebooks

```text
00_prerequisites.ipynb   install, sign-in, credits
traditional-ml/          classic black-box ML attacks (evasion, extraction, inversion)
model-red-teaming/       jailbreaks & multimodal/multilingual attacks on foundation models
agentic-red-teaming/     attacks on AI agents & multi-agent systems
```

### [`traditional-ml/`](traditional-ml) - attacks on classifiers via the `/predict` API (needs `pip install "dreadnode[airt-ml]"` for the sklearn/torch surrogates)

| Notebook | Attack family | What it shows |
|----------|---------------|---------------|
| [`01_model_evasion`](traditional-ml/01_model_evasion.ipynb) | Evasion | Flip a classifier's decision across **tabular / image / text** with a minimal perturbation (with before/after display) |
| [`02_extraction_membership`](traditional-ml/02_extraction_membership.ipynb) | Extraction + Membership inference | Steal a high-fidelity surrogate; decide whether a record was in the training set |
| [`03_model_inversion`](traditional-ml/03_model_inversion.ipynb) | Model inversion | Reconstruct a representative training example per class (MI-Face) |

### [`model-red-teaming/`](model-red-teaming) - jailbreaks and multimodal attacks on foundation models

| Notebook | Attack family | What it shows |
|----------|---------------|---------------|
| [`01_generative_text`](model-red-teaming/01_generative_text.ipynb) | Jailbreaks | Run **TAP, Crescendo, and GOAT** search strategies with prompt transforms |
| [`02_multimodal`](model-red-teaming/02_multimodal.ipynb) | Multimodal | Hide an instruction in an **image** to bypass text-only guardrails |
| [`03_multilingual`](model-red-teaming/03_multilingual.ipynb) | Multilingual jailbreaks | Re-express a harmful request in **low-resource languages / transliteration / code-switching** and measure the guardrail gap |
| [`04_attack_strategies`](model-red-teaming/04_attack_strategies.ipynb) | Strategy comparison | Run **TAP / PAIR / DeepInception / Crescendo** + past-tense / persuasion / cipher / ASCII-art against one target and compare scores |

### [`agentic-red-teaming/`](agentic-red-teaming) - attacks on AI agents and multi-agent systems

| Notebook | Focus | What it shows |
|----------|-------|---------------|
| [`01_multiagent_atlas`](agentic-red-teaming/01_multiagent_atlas.ipynb) | Multi-agent (ATLAS) | Propagate an injection through an agent mesh until a privileged tool fires |
| [`02_agentic_security`](agentic-red-teaming/02_agentic_security.ipynb) | Injection + honeytoken | Probe a deployed agent for **RCE and data exfiltration** with the OWASP-ASI suite and inert honeytoken canaries |
| [`03_exfiltration_channels`](agentic-red-teaming/03_exfiltration_channels.ipynb) | Data exfiltration channels | Sweep a deployed agent for **markdown-image, link-unfurl, unicode, DNS, SSRF, API, and web-search-query** exfil channels; prove leaks with an inert honeytoken (EchoLeak / ForcedLeak / arXiv:2510.09093) |
| [`04_indirect_injection_web`](agentic-red-teaming/04_indirect_injection_web.ipynb) | Indirect prompt injection | Provision a real **public webpage** with hidden instructions, point your agent at the URL, and prove it acted on hidden content (EchoLeak / ForcedLeak class) |
| [`05_ci_secret_exfiltration`](agentic-red-teaming/05_ci_secret_exfiltration.ipynb) | CI/CD secret exfiltration | Provision a CI-assistant agent and prove a hidden instruction leaks its deploy secret to an external webhook (GitLost); plus web-search-query + trusted-domain exfil channels and browser-attack scorers |
| [`07_context_injection`](agentic-red-teaming/07_context_injection.ipynb) | Indirect prompt injection (ASI01) | A hidden instruction in fetched content drives the agent into a data-exfil tool call |
| [`08_access_control_idor`](agentic-red-teaming/08_access_control_idor.ipynb) | Broken access control (IDOR) | Retrieve another tenant's record by acting as a cross-tenant identity |
| [`09_memory_poisoning`](agentic-red-teaming/09_memory_poisoning.ipynb) | Memory poisoning (ASI06) | Poison persistent memory so a later benign turn acts on the planted policy |
| [`10_mcp_poisoning`](agentic-red-teaming/10_mcp_poisoning.ipynb) | MCP tool poisoning | A poisoned tool description makes the agent read a secret file |
| [`11_agentic_rce`](agentic-red-teaming/11_agentic_rce.ipynb) | Agentic RCE | Reasoning hijack into a privileged code/shell execution |
| [`12_data_exfiltration`](agentic-red-teaming/12_data_exfiltration.ipynb) | Data exfiltration | A delegate chain leaks a customer record to an external sink |
| [`13_reasoning_hijack`](agentic-red-teaming/13_reasoning_hijack.ipynb) | Reasoning hijack | A CoT backdoor converts the agent's reasoning into a harmful action |
| [`14_supply_chain`](agentic-red-teaming/14_supply_chain.ipynb) | Agentic supply chain (ASI04) | The agent resolves and runs a typosquatted look-alike package |

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
