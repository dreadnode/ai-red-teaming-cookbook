# Agentic Red Teaming

Notebooks for red teaming AI agents and multi-agent systems. These attacks target
what an agent does, not just what it says: tool calls, delegation across agents,
content the agent reads, and the packages it loads.

These notebooks either **provision a self-contained target environment** (the
OWASP-ASI mesh probes `07`/`09`/`10`/`13`/`14`, plus `01`/`05`) or **point at your
own deployed agent** through a single contract - an HTTP endpoint that accepts a
message and returns the executed tool calls (`02`, `04`). The deployed-agent
notebooks run against a local, AWS, or Azure agent without changes.

| Notebook | Focus | What it shows |
| --- | --- | --- |
| [`01_multiagent_atlas`](01_multiagent_atlas.ipynb) | Multi-agent (ATLAS) | Propagate an injection through an agent mesh until a privileged tool fires (confused deputy) |
| [`02_agentic_security`](02_agentic_security.ipynb) | RCE + data exfiltration | Probe a deployed agent for command execution and exfil across its egress tools, honeytoken-proven |
| [`04_indirect_injection_web`](04_indirect_injection_web.ipynb) | Indirect prompt injection | Point a deployed agent at a page with hidden instructions and prove whether it acts on fetched content |
| [`05_ci_secret_exfiltration`](05_ci_secret_exfiltration.ipynb) | CI/CD secret exfiltration | Prove a CI assistant leaks its deploy secret to an external webhook (GitLost) |
| [`07_context_injection`](07_context_injection.ipynb) | Indirect injection (ASI01) | A hidden instruction in fetched content drives a data-exfil tool call |
| [`09_memory_poisoning`](09_memory_poisoning.ipynb) | Memory poisoning (ASI06) | Poison persistent memory so a later benign turn acts on it |
| [`10_mcp_poisoning`](10_mcp_poisoning.ipynb) | MCP tool poisoning | A poisoned tool description makes the agent read a secret file |
| [`13_reasoning_hijack`](13_reasoning_hijack.ipynb) | Reasoning hijack | A CoT backdoor converts reasoning into a harmful action |
| [`14_supply_chain`](14_supply_chain.ipynb) | Supply chain (ASI04) | The agent resolves and runs a typosquatted look-alike package |

## Coverage

These notebooks map to the OWASP Top 10 for Agentic Applications (2026), each probing
one or more categories with the mapped attack strategies, transform families, and
matching detection scorers. See the
[Agentic Red Teaming Overview](https://docs.dreadnode.io/ai-red-teaming/how-to/agentic-red-teaming)
for the full category mapping.

## Prerequisites

Run [`../00_prerequisites.ipynb`](../00_prerequisites.ipynb) first to install the
CLI and sign in. Notebooks use your default `main` workspace. For the deployed-agent
notebooks (`02`, `04`), provide your agent endpoint and key through environment
variables (`AGENT_URL` / `AGENT_KEY`). Do not hard-code secrets in a notebook.
