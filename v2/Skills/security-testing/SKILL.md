---
name: security-testing
description: "Plan safe, authorized application-security tests tailored to the system, threat model, and business risk. Use for security test design and scoped reviews."
---

# Security Testing

## When to Use
Use to design or review application-security tests for web/mobile/API systems, authN/authZ flows, data handling, uploads, integrations, or release threats. No exploit, scan, fuzz, or live test is authorized by default. Do not provide a compliance attestation.

## Required Inputs
Before any active test, confirm written authorization, target/environment, in-scope assets/accounts, allowed techniques and rate limits, data handling, test window, stop conditions, and emergency contact. For planning, request architecture/trust boundaries, roles, assets, data classes, entry points, intended protections, threat model, tech stack/version, and applicable policy. Use staging/synthetic data where possible.

## Procedure
1. Map assets, actors, trust boundaries, entry points, sensitive data, and security controls from supplied architecture/contracts. Identify threats relevant to the specific feature, not every generic category.
2. Select safe scenarios from authentication, authorization/object ownership (IDOR), input handling/injection, output encoding/XSS, CSRF/session, upload, configuration/headers, dependency, error/logging, and data exposure as applicable. Use OWASP WSTG as a test reference, not proof of complete coverage.
3. For each case specify objective, preconditions, harmless input/steps, expected defensive behavior from contract/policy, evidence, cleanup, and stop condition. Use non-destructive proof and do not exfiltrate data, persist access, evade controls, or disrupt service.
4. Validate potential findings: reproduce within scope, distinguish tool alert from confirmed issue, assess realistic impact and affected privilege/data, redact secrets, and cite exact endpoint/code/evidence.
5. Recommend minimal remediation and a safe retest. Ask for explicit approval before active tests or external calls; stop if target identity or scope is ambiguous.

## Output Contract
Return `Authorization and scope`; test matrix `ID | Threat/control | Asset/entry point | Preconditions | Safe steps | Expected control/source | Evidence | Risk | Cleanup/stop`; findings `Finding | Status (Confirmed/Hypothesis/False positive) | Impact | Evidence | Remediation | Retest`. Sample: `SEC-4 | object-level auth | GET /records/{id} | two owned test accounts | request account B's synthetic record as A | deny or contract-defined non-disclosure | status/body + server audit event | provisional until response observed | delete fixtures`.

## Quality Gate
Authorization and boundaries are explicit; no unapproved exploit testing; test cases are non-destructive and policy-grounded; severity reflects demonstrated impact; findings redact sensitive data; remediation and retest are actionable. Verify references with the current OWASP WSTG and applicable authoritative docs; no blanket OWASP coverage claim.

## Evidence and Uncertainty
Use scope approval, threat model, contracts, code, sanitized request/response evidence, logs, and current authoritative docs. Separate observation from inference. Apply readiness across scope, claim traceability, complete contract, verification (25 points each); below 75/100, ask, qualify, or abstain. Never guess confidence percentages. Critical authorization, privacy, safety, or acceptance failures block readiness regardless of score.
