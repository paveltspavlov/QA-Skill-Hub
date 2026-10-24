---
name: ci-pipeline-test-advisor
description: "Review a CI pipeline and recommend test stages, gates, parallelization, and failure diagnostics. Use when CI configuration or test feedback is slow or unreliable."
---

# CI Pipeline Test Advisor

## Procedure
1. Inspect workflow files, triggers, runner environments, dependencies, caches, secrets, and current test commands.
2. Map test types to the earliest reliable stage; distinguish fast required checks from slower scheduled or release checks.
3. Identify concurrency, caching, sharding, flaky-test handling, artifacts, and failure-reporting opportunities without widening permissions casually.
4. Verify provider-specific workflow syntax and permissions against the repository's actual CI platform.
5. Recommend the smallest change; do not trigger workflows, deploy, or edit secrets without authorization.

## Output
A stage table, prioritized recommendations, workflow change when requested, and validation commands.

## References
- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [Playwright best practices](https://playwright.dev/docs/best-practices)
