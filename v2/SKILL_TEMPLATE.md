# Create a reusable skill for v2

Copy this template to `v2/Skills/<skill-name>/SKILL.md`, where `<skill-name>` is lowercase letters/numbers separated by single hyphens. The frontmatter `name` must exactly match the directory name.

```markdown
---
name: <skill-name>
description: <What the skill does and when an agent should select it.>
---

# <Skill title>

## Use when
<State the task trigger and scope.>

## Procedure
1. Inspect the supplied context and project conventions.
2. Ask only for information that blocks a correct or safe result.
3. Perform the task steps in a bounded, evidence-based way.
4. Verify the result; state checks that did not run.

## Output
<Exact expected deliverable and fields.>

## Quality and safety checks
<Traceability, non-goals, permissions, and uncertainty handling.>

## References
- [Official source](https://example.org/)
```

Keep the skill task-specific and platform-neutral. Put repeated task procedure here rather than in a role profile. Agents select skills; skill files contain the actual procedure. Do not add `allowed-tools` unless the target agent host supports it and the permissions have been reviewed.

This catalogue follows the Agent Skills convention: one directory per skill, a `SKILL.md` file, a lowercase hyphenated `name`, and a `description` that says what the skill does and when to use it. Run `python v2/generate_manifest.py` after adding a skill, then `python -m unittest tests.test_v2_catalog -v` to validate the catalogue.

References:
- [Agent Skills specification](https://agentskills.io/specification)
- [GitHub: Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
