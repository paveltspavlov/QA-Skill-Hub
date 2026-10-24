# Create a reusable skill for v2

Copy this template to `v2/Skills/<skill-name>/SKILL.md`, where `<skill-name>` is lowercase letters/numbers separated by single hyphens. The frontmatter `name` must exactly match the directory name.

```markdown
---
name: <skill-name>
description: <What the skill does and when an agent should select it.>
---

# <Skill title>

## When to Use
<State the exact trigger and counter-trigger.>

## Required Inputs
<List required and optional inputs. Mark which missing inputs block correctness and which allow a conditional draft.>

## Procedure
1. Inspect the supplied source, project context, and established conventions.
2. Separate explicit evidence from inference. Ask only for information that changes correctness, safety, scope, or expected output.
3. Follow the task-specific steps below, with observable completion checks.
4. Verify the result with the narrowest relevant check; state commands and results actually observed.

## Output Contract
<Specify the exact heading structure, table columns, required fields, status values, and what each field must contain. Include a compact example for ambiguous or high-risk outputs.>

## Quality Gate
<Add task-specific, checkable acceptance criteria. A missing critical criterion blocks a ready result.>

## Evidence and Uncertainty
<Identify acceptable evidence and provenance. Never invent facts, test results, sources, expected behavior, or metrics. Distinguish observation, inference, and recommendation; ask, qualify, or abstain when the evidence is insufficient. Apply the evidence-readiness-gate skill.>

## References
- [Official source](https://example.org/)
```

Keep the skill task-specific and platform-neutral. Put repeated task procedure here rather than in a role profile. Agents select skills; skill files contain the actual procedure. Do not add `allowed-tools` unless the target agent host supports it and the permissions have been reviewed.

This catalogue follows the Agent Skills convention: one directory per skill, a `SKILL.md` file, a lowercase hyphenated `name`, and a `description` that says what the skill does and when to use it. Run `python v2/generate_manifest.py` after adding a skill, then `python -m unittest tests.test_v2_catalog -v` to validate the catalogue.

References:
- [Agent Skills specification](https://agentskills.io/specification)
- [GitHub: Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
