# Agentic Red Teaming

Notebooks for red teaming AI agents and multi-agent systems. These attacks target
what an agent does, not just what it says: tool calls, delegation across agents,
content the agent reads, and the packages it loads.

These notebooks either **provision a self-contained target environment** (`01`, `04`,
and the five-in-one ASI suite `06`) or **point at your own deployed agent** through a
single HTTP contract that accepts a message and returns the executed tool calls (`02`,
`03`, `05`). `07` runs a self-contained agent locally with your own provider key. The
deployed-agent notebooks run against a local, AWS, or Azure agent without changes.

| Notebook | Focus | What it shows |
| --- | --- | --- |
| [`01_multiagent_atlas`](01_multiagent_atlas.ipynb) | Multi-agent (ATLAS) | Propagate an injection through an agent mesh until a privileged tool fires (confused deputy) |
| [`02_agentic_security`](02_agentic_security.ipynb) | RCE + data exfiltration | Probe a deployed agent for command execution and exfil across its egress tools, honeytoken-proven |
| [`03_indirect_injection_web`](03_indirect_injection_web.ipynb) | Indirect prompt injection | Point a deployed agent at a page with hidden instructions and prove whether it acts on fetched content |
| [`04_ci_secret_exfiltration`](04_ci_secret_exfiltration.ipynb) | CI/CD secret exfiltration | Prove a CI assistant leaks its deploy secret to an external webhook (GitLost) |
| [`05_multistep_tool_attacks`](05_multistep_tool_attacks.ipynb) | Multi-step tool attacks | Algorithmic search for replay-stable read-then-exfiltrate causal paths |
| [`06_asi_mesh_probes`](06_asi_mesh_probes.ipynb) | OWASP-ASI mesh probes | Five deliberately vulnerable meshes (indirect-injection, memory, MCP, reasoning, supply-chain), one scored attack each |
| [`07_agentic_probes_2026`](07_agentic_probes_2026.ipynb) | Agentic probes (2026) | Evidence-gated tool-misuse RCE, MCP line-jump, RAG poisoning, and AgentVigil MCTS against a real tool-using agent |

## How ATLAS works

ATLAS (notebook `01`, and the engine behind the agentic suite) treats a multi-agent
system as a topology to search, not a single prompt to jailbreak:

1. **Probe** - send a message and watch which agent answers and which tools fire.
2. **Reason** - infer where the mesh trusts its input and which downstream agent holds
   the privileged tool the entry agent refused (the *why* behind each next move).
3. **Route and iterate** - re-aim the next probe at that weak link (another agent,
   surface, or phrasing) and repeat, keeping whatever moved closer to the objective.
4. **Score on action** - a run counts only when a privileged tool actually fires (e.g.
   `transfer_funds`, `admin_create_user`), never on words. ASR is the fraction of
   objectives reached; queries-per-objective is how efficiently it got there.

## Coverage

These notebooks map to the OWASP Top 10 for Agentic Applications (2026), each probing
one or more categories with the mapped attack strategies, transform families, and
matching detection scorers. See the
[Agentic Red Teaming Overview](https://docs.dreadnode.io/ai-red-teaming/how-to/agentic-red-teaming)
for the full category mapping.

## Prerequisites

Run [`../00_prerequisites.ipynb`](../00_prerequisites.ipynb) first to install the
CLI and sign in. Notebooks use your default `main` workspace. For the deployed-agent
notebooks (`02`, `03`, `05`), provide your agent endpoint and key through environment
variables (`AGENT_URL` / `AGENT_KEY`). Do not hard-code secrets in a notebook.
