# Model Red Teaming

Notebooks for red teaming foundation models directly - what a model **says** when
pushed: jailbreaks that defeat safety training, and multimodal payloads that smuggle
an instruction past text-only guardrails. The target is the model itself (via the
platform proxy), not an agent's tools or memory.

For attacks on what an **agent does** (tool calls, delegation, memory, fetched
content), see [`../agentic-red-teaming/`](../agentic-red-teaming). For classic
black-box ML models (evasion, extraction, inversion), see
[`../traditional-ml/`](../traditional-ml).

| Notebook | Attack family | What it shows |
| --- | --- | --- |
| [`04_generative_text`](04_generative_text.ipynb) | Jailbreaks | Compare TAP, Crescendo, and GOAT search strategies with prompt transforms |
| [`05_multimodal`](05_multimodal.ipynb) | Multimodal | Hide an instruction in an image to bypass text-only guardrails |

## Prerequisites

Run [`../00_prerequisites.ipynb`](../00_prerequisites.ipynb) first to install the
CLI, sign in, and create a workspace.
