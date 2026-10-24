---
name: security-testing
description: "Plan safe, authorized application-security tests tailored to the system, threat model, and business risk. Use for security test design and scoped reviews."
---

# Security Testing

## Safety and authorization
Confirm written scope, environment, accounts, permitted techniques, data handling, and stop conditions before testing a live system. Do not exploit, exfiltrate, disrupt, persist, or test outside scope. Use staging or synthetic data where possible. If scope is unclear, ask before action.

## Procedure
1. Understand assets, trust boundaries, data sensitivity, user roles, architecture, and intended/disallowed use cases.
2. Select relevant test areas from the system’s risks: authentication, authorization, input/output handling, session, configuration, error handling, sensitive data, dependencies, and client-side behavior.
3. Tailor the OWASP WSTG techniques to the application. Treat them as a starting set, not an exhaustive checklist.
4. For each test, record objective, preconditions, safe steps, expected control, evidence, and cleanup/stop condition.
5. Validate findings and severity against actual impact and evidence. Separate confirmed vulnerabilities from hypotheses and tool alerts.
6. Report remediation and retest criteria without reproducing secrets or exposing sensitive data.

## Output
A scoped test plan or findings report with authorization assumptions, prioritized risks, evidence, remediation, and limitations.

## References
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
