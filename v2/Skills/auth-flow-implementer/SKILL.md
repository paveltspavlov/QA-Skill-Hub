---
name: auth-flow-implementer
description: "Implement or review authentication using the existing identity provider and explicit security requirements. Use for sign-in, session, token, or account-recovery changes."
---

# Auth Flow Implementer

## Procedure
1. Identify the identity provider, client/server boundaries, user roles, session model, and requirements.
2. Reuse the established provider SDK and secure session/token patterns; do not write custom cryptography or invent protocol behavior.
3. Cover success, invalid credentials, expired/revoked session, authorization failure, recovery, rate limits, and safe errors as relevant.
4. Keep secrets out of source, logs, URLs, and client-visible storage unless the approved design requires otherwise.
5. Add authorization-boundary tests; ask before touching production identity configuration.

## Output
A scoped flow design or implementation with security assumptions and verification cases.

## References
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest)
