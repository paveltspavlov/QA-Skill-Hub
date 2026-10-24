---
name: debugging
description: "Reproduce and diagnose software failures from code, logs, or behavior, then verify a minimal fix. Use for errors, failing tests, regressions, and unexpected output."
---

# Debugging

## Procedure
1. Capture the exact observed behavior, expected behavior, environment, and reproduction steps. Separate facts from hypotheses.
2. Reproduce the failure with the narrowest reliable command or test. Do not change code before identifying a testable failure when a test harness exists.
3. Trace the failing path through relevant code, inputs, configuration, and recent changes. Test one hypothesis at a time and prefer evidence that can falsify it.
4. Identify the root cause only when evidence supports it. Otherwise report ranked hypotheses and the next diagnostic step.
5. Add or update a regression test, apply the smallest fix, and rerun the failing case plus relevant regression checks.
6. Report remaining uncertainty and any checks that could not run.

## Output
Reproduction, evidence, confirmed cause or ranked hypotheses, fix, verification, and residual risk.

## References
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
- [ISTQB CTFL v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
