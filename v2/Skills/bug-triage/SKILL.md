---
name: bug-triage
description: "Turn defect reports into reproducible, evidence-based issues with clear impact and urgency. Use for incident reports, user complaints, and test failures."
---

# Bug Triage

## Procedure
1. Preserve the original report and identify environment, build/version, account/role, data, and frequency if supplied.
2. Separate observed result from expected result. Write minimal reproducible steps and capture logs, screenshots, request IDs, or test evidence when available.
3. Identify affected users, workflows, data integrity, security, availability, and a plausible workaround.
4. Assess severity (impact) separately from priority (urgency/order of work). Use the team's definitions; if absent, mark the rating provisional and explain the evidence.
5. Check for duplicates or related defects only when repository/tracker access is available. Do not claim a duplicate without checking.
6. Keep root-cause hypotheses separate from confirmed causes.

## Output
A concise title, environment, preconditions, reproduction steps, actual/expected results, evidence, severity, priority, workaround, and open questions.

## References
- [ISTQB CTFL v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
