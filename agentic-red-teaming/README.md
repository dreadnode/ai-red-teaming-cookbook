# Agentic Red Teaming

Notebooks for red teaming AI agents and multi-agent systems. These attacks target
what an agent does, not just what it says: tool calls, delegation across agents,
content the agent reads, and the packages it loads.

Every notebook points at a deployed agent through a single contract, an HTTP
endpoint that accepts a message and returns the executed tool calls. The same
notebook runs against a local, AWS, or Azure agent without changes.

| Notebook                                            | Focus                | What it shows                                                                                     |
| --------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------ |
| [`01_multiagent_atlas`](01_multiagent_atlas.ipynb)  | Multi-agent (ATLAS)  | Propagate an injection through an agent mesh until a privileged tool fires                        |
| [`02_agentic_security`](02_agentic_security.ipynb)  | Injection + honeytoken | Probe a deployed agent for RCE and data exfiltration with the OWASP-ASI suite and inert canaries |

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
