---
name: code-review
description: "Review a change for correctness, security, maintainability, and test gaps using the stated requirements and project conventions. Use before accepting or merging a change."
---

# Code Review

## Procedure
1. Read the change and relevant surrounding code; identify the base version and intended behavior.
2. Check correctness, edge/error handling, authorization/data boundaries, unsafe input handling, resource use, compatibility, and test coverage.
3. Report only actionable findings. For each, include severity, file/line or precise evidence, impact, and a minimal suggested fix.
4. Distinguish confirmed vulnerabilities/bugs from questions and non-blocking suggestions. Do not report style preferences as defects.
5. Do not edit or auto-fix unless the user explicitly requests changes. Re-review the updated diff after fixes.

## Output
Findings first, ordered by severity; then tested areas, gaps, assumptions, and non-blocking suggestions. If there are no findings, state the scope reviewed and what was not reviewed.

## Safety
Do not execute untrusted code or perform live destructive security tests during review. Request authorization for actions with external side effects.

## References
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
- [GitHub custom-agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
