---
name: git-workflow-automator
description: "Design or update repository Git workflow files and conventions from team requirements. Use for branching, hooks, commit standards, and release flow."
---

# Git Workflow Automator

## Procedure
1. Inspect branch conventions, release process, repository settings, and CI workflows.
2. Clarify team size, protected branches, review requirements, release cadence, and automation permissions.
3. Propose the smallest workflow change; keep credentials out of files and grant least privilege to automation tokens.
4. Use dry-run or local validation where available. Never push, tag, or change remote settings without explicit authorization.
5. Document the workflow, failure path, recovery, and ownership.

## Output
A branching/release convention or workflow file, rationale, permissions, and validation steps.

## References
- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
