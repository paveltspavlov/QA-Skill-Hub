# QA Skill Hub

A static catalogue for reusable QA and software-development agents, Agent Skills, and prompt templates. The root page is **v2.0**; the version switch next to the banner opens the preserved **v1.0** catalogue.

## What changed in v2.0

- Exactly four cross-platform role agents: **Developer**, **Documentation Analyst**, **QA Engineer**, and **Automation QA Engineer**.
- V2 has **62 reusable skills**: the 50-skill core/specialist catalogue, 11 restored specialist workflows from the v1 agent set, and a shared evidence-readiness gate. Each role links relevant skills; users can add and link their own.
- Project work begins by inspecting and maintaining concise context under the project’s established `.copilot/` or `.vscode/` convention.
- A separate **M365 Agents** page shows Microsoft 365 Copilot versions of the same four roles, each with name, description, self-contained instruction prompt, and five starter-prompt templates. M365 instructions do not depend on shared Skills.
- GitHub Copilot exports are adapters: role profiles export as `.agent.md`; skills remain standard `SKILL.md` files. The role instructions and skill procedures remain tool-neutral.
- Every role applies an evidence-readiness gate: 75% means checklist evidence coverage, not probability of correctness. Below threshold, unscorable, or critical failures require clarification, a qualified partial answer, or abstention; unsupported facts and fabricated verification are prohibited.

## Repository layout

```text
.
├── index.html                 # v2.0 app (default)
├── v1.html                    # v1.0 app snapshot
├── Agents/ Skills/ Prompts/   # preserved v1 content
├── manifest.json              # preserved v1 manifest
├── generate_content.py        # legacy v1 content helper
├── v2/
│   ├── Agents/                # four neutral role profiles
│   ├── Skills/<name>/SKILL.md # reusable Agent Skills
│   ├── manifest.json          # v2 catalogue manifest
│   ├── m365-agents.json       # four M365 configurations
│   ├── generate_manifest.py   # updates v2 manifest after content changes
│   ├── SKILL_TEMPLATE.md      # create a custom skill
│   └── RESEARCH-SOURCES.md    # official references used for v2
└── tests/test_v2_catalog.py   # schema and catalogue checks
```

The app is plain HTML, CSS, JavaScript, JSON, and Markdown; there is no build step or runtime dependency installation.

## Run locally

From the repository root:

```bash
python -m http.server 8000
```

Open <http://localhost:8000/>. The app fetches Markdown and JSON over HTTP, so do not open the HTML files through `file://`.

## Use the catalogue

- Use the large **V1.0 / V2.0** switch in the banner to compare versions.
- In v2, filter the catalogue by **Agents**, **Skills**, or **Prompts**. Agent cards list their linked skills; select a skill link to open its procedure.
- The **Copilot Agent** export is a GitHub Copilot custom-agent profile (`.github/agents/<id>.agent.md`). The **Agent Skill** export is a standard `SKILL.md` (`.github/skills/<name>/SKILL.md`). These are convenience exports; the underlying role and skill content is platform-neutral.
- Select **M365 Agents** for the four Microsoft 365 Copilot configurations. The page shows field character counts and lets you copy each field or starter prompt.
- Review and test any generated agent instructions before using them in a project.

## Add or update a v2 skill

1. Create `v2/Skills/<skill-name>/SKILL.md`, using `v2/SKILL_TEMPLATE.md`.
2. Keep `name` equal to the directory name; use lowercase letters, numbers, and single hyphens. Keep the `description` concise and state what the skill does and when it should be selected.
3. Include `When to Use`, `Required Inputs`, `Procedure`, `Output Contract`, `Quality Gate`, and `Evidence and Uncertainty` sections. Specify exact deliverable fields and checkable acceptance criteria; include a worked example for ambiguous or high-risk outputs. Apply the evidence-readiness-gate; never invent facts, sources, expected results, or verification.
4. Add the skill ID to the `skills` list of each relevant v2 role profile in `v2/Agents/`. Reusing the same skill from multiple roles is encouraged.
5. Rebuild the catalogue manifest and run validation:

```bash
python v2/generate_manifest.py
python -m unittest tests.test_v2_catalog -v
```

The v1 `generate_content.py` and root `manifest.json` remain for the legacy catalogue; they do not rewrite v2 content.

## Edit M365 agent profiles

Edit `v2/m365-agents.json`. Each profile must stay within Microsoft 365 Agent Builder limits: name 30 characters, description 1,000, instruction prompt 8,000. Keep exactly five starter prompts per profile. The current M365 schema allows up to 12 conversation starters; these v2 profiles are intentionally self-contained and do not use shared Skills.

## Version preservation

V1 content remains in the original `Agents/`, `Skills/`, `Prompts/`, and `manifest.json`. `v1.html` preserves the prior app, with only a version switch added. V2 content is separate under `v2/`, so editing a v2 role or skill does not alter v1.

## Research and design references

See [v2/RESEARCH-SOURCES.md](v2/RESEARCH-SOURCES.md) for the official GitHub, Agent Skills, Microsoft, ISTQB, Playwright, W3C, and OWASP sources used in the v2 update.
