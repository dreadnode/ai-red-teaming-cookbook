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
| [`01_generative_text`](01_generative_text.ipynb) | Jailbreaks | Compare TAP, Crescendo, and GOAT search strategies with prompt transforms |
| [`02_multimodal`](02_multimodal.ipynb) | Multimodal | Hide an instruction in an image to bypass text-only guardrails |
| [`03_multilingual`](03_multilingual.ipynb) | Multilingual jailbreaks | Re-express a harmful request in low-resource languages / transliteration / code-switching and measure the guardrail gap |
| [`04_attack_strategies`](04_attack_strategies.ipynb) | Strategy comparison | Run TAP / PAIR / DeepInception / Crescendo and past-tense / persuasion / cipher / ASCII-art against one target and compare scores |

## Prerequisites

Run [`../00_prerequisites.ipynb`](../00_prerequisites.ipynb) first to install the
CLI, sign in, and create a workspace.
