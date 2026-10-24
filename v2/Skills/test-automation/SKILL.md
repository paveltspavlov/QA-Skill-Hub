---
name: test-automation
description: "Design, implement, or improve automated tests using the repository’s existing framework. Use for unit, integration, UI, and end-to-end automation."
---

# Test Automation

## Procedure
1. Inspect existing test files, framework, fixtures, conventions, dependencies, and exact run commands before choosing a pattern.
2. Select a test level that gives useful feedback without unnecessary environment complexity. Keep each test focused and independent.
3. Prefer meaningful assertions on user-visible behavior or stable interfaces. For browser tests, use accessible role/name/label locators or explicit test contracts; avoid selectors coupled to incidental DOM structure.
4. Use deterministic data, explicit setup/cleanup, and the framework’s wait/assertion mechanisms. Avoid arbitrary sleeps, shared mutable state, hidden dependencies, and flaky network assumptions.
5. Cover representative success, failure, and boundary behavior. Do not generate tests that assert undocumented or invented behavior.
6. Run the narrow test first, then relevant suites. Report actual results and unrun checks.

## Output
Tests in the project's existing style, plus rationale, execution command, actual results, and known gaps.

## References
- [Playwright best practices](https://playwright.dev/docs/best-practices)
- [Playwright locators](https://playwright.dev/docs/locators)
