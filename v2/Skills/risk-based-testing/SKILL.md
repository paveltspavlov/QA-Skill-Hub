---
name: risk-based-testing
description: "Prioritize testing by product risk, change impact, likelihood, exposure, and available time. Use for regression planning, release decisions, and constrained test windows."
---

# Risk-Based Testing

## Procedure
1. Define the decision, scope, release/change, and available testing time.
2. Identify quality risks from user impact, data/security exposure, change size, complexity, dependencies, usage frequency, and failure history.
3. Rate likelihood and impact using an agreed scale. If no scale exists, use qualitative labels and state their meaning; do not invent precise probabilities.
4. Map each material risk to a test, evidence source, owner, and residual risk.
5. Prioritize tests by expected risk reduction, dependencies, and execution cost. Explain what is deferred and why.
6. Reassess priorities when new evidence, failures, or scope changes appear.

## Output
A risk register and ordered test plan with rationale, coverage gaps, time trade-offs, and release caveats.

## References
- [ISTQB CTFL v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
