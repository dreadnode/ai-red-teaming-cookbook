# Agentic Red Teaming

Notebooks for red teaming AI agents and multi-agent systems. These attacks target
what an agent does, not just what it says: tool calls, delegation across agents,
content the agent reads, and the packages it loads.

These notebooks either **provision a self-contained target environment** (the
`07`-`14` OWASP-ASI mesh probes, plus `04`/`05`) or **point at your own deployed
agent** through a single contract - an HTTP endpoint that accepts a message and
returns the executed tool calls (`02`, `03`). The deployed-agent notebooks run
against a local, AWS, or Azure agent without changes.

| Notebook | Focus | What it shows |
| --- | --- | --- |
| [`01_multiagent_atlas`](01_multiagent_atlas.ipynb) | Multi-agent (ATLAS) | Propagate an injection through an agent mesh until a privileged tool fires |
| [`02_agentic_security`](02_agentic_security.ipynb) | Injection + honeytoken | Probe a deployed agent for RCE and data exfiltration with the OWASP-ASI suite and inert canaries |
| [`03_exfiltration_channels`](03_exfiltration_channels.ipynb) | Data exfiltration channels | Sweep a deployed agent for markdown/link/unicode/DNS/SSRF/API/web-search exfil channels, honeytoken-proven |
| [`04_indirect_injection_web`](04_indirect_injection_web.ipynb) | Indirect prompt injection | Provision a real public webpage with hidden instructions and prove the agent acted on hidden content |
| [`05_ci_secret_exfiltration`](05_ci_secret_exfiltration.ipynb) | CI/CD secret exfiltration | Prove a CI assistant leaks its deploy secret to an external webhook (GitLost) |
| [`07_context_injection`](07_context_injection.ipynb) | Indirect injection (ASI01) | A hidden instruction in fetched content drives a data-exfil tool call |
| [`08_access_control_idor`](08_access_control_idor.ipynb) | Access control (IDOR) | Retrieve another tenant's record via a cross-tenant identity |
| [`09_memory_poisoning`](09_memory_poisoning.ipynb) | Memory poisoning (ASI06) | Poison persistent memory so a later benign turn acts on it |
| [`10_mcp_poisoning`](10_mcp_poisoning.ipynb) | MCP tool poisoning | A poisoned tool description makes the agent read a secret file |
| [`11_agentic_rce`](11_agentic_rce.ipynb) | Agentic RCE | Reasoning hijack into a privileged code/shell execution |
| [`12_data_exfiltration`](12_data_exfiltration.ipynb) | Data exfiltration | A delegate chain leaks a customer record to an external sink |
| [`13_reasoning_hijack`](13_reasoning_hijack.ipynb) | Reasoning hijack | A CoT backdoor converts reasoning into a harmful action |
| [`14_supply_chain`](14_supply_chain.ipynb) | Supply chain (ASI04) | The agent resolves and runs a typosquatted look-alike package |

## Coverage

These notebooks map to the OWASP Top 10 for Agentic Applications (2026). The agentic
suite in `02_agentic_security` drives every category, selecting the mapped attack
strategies, applying the transform families, and scoring with the matching detection
scorers. See the
[Agentic Red Teaming Overview](https://docs.dreadnode.io/ai-red-teaming/how-to/agentic-red-teaming)
for the full category mapping.

## Prerequisites

Run [`../00_prerequisites.ipynb`](../00_prerequisites.ipynb) first to install the
CLI, sign in, and create a workspace. Provide your agent endpoint and key through
environment variables. Do not hard-code secrets in a notebook.
