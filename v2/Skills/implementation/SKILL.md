---
name: implementation
description: "Implement a bounded software change that follows the project’s existing architecture and verification practices. Use for feature work, refactoring, and code changes requested by the user."
---

# Software Implementation

## Procedure
1. Read the relevant project context, source files, tests, and existing conventions before changing code. Use `project-context` when context is missing or stale.
2. Confirm acceptance criteria. Ask about requirements that materially affect behavior; do not invent product decisions.
3. Write the smallest test that demonstrates the requested behavior and confirm it fails for the expected reason when the repository has a test framework.
4. Make the minimum cohesive change. Reuse existing dependencies and patterns; do not introduce a framework or broad redesign without authorization.
5. Run the narrowest relevant tests, then applicable broader checks (lint, typecheck, build). Report exact commands and results; do not claim unrun checks.
6. Review the diff for scope, security, regressions, and accidental files. Do not commit, push, deploy, or publish unless requested.

## Output
A focused change with tests where feasible, verification evidence, remaining risks, and files touched.

## References
- [GitHub custom-agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
- [GitHub Copilot custom instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions)
