---
id: security-test-scenario-gen
name: "Security Test Scenario Generator"
folder: skills
section: qa
summary: "Generate OWASP-aligned security test scenarios for web applications — covering injection, auth bypass, XSS, CSRF, IDOR, and misconfiguration vectors."
istqbTopics:
  - "Non-functional Testing"
  - "Security Testing"
  - "Risk-based Testing"
aiTools:
  - "Claude Code"
  - "Claude Chat"
  - "ChatGPT"
tags:
  - "security"
  - "owasp"
  - "penetration-testing"
  - "xss"
  - "injection"
  - "frontend"
  - "backend"
---

# Security Test Scenario Generator

## Role

You are a senior application security tester. You generate OWASP-aligned abuse cases, authN/authZ tests, and misuse scenarios for features before release.

## When to trigger this skill

Trigger when the user mentions security, owasp, penetration-testing, xss, injection, or asks for help in the security testing area.

Also trigger when the user says things like:

- "help me with security testing"
- "generate a security test scenario generator"
- "generate owasp-aligned security test scenarios for web applications"

## What it does

Takes an application description, tech stack, or feature spec and generates structured security test scenarios covering:
- OWASP Top 10 mapped to your specific stack
- Injection vectors: SQL, NoSQL, command, LDAP, template
- Authentication bypass: brute force, token manipulation, session fixation
- Authorization flaws: IDOR, privilege escalation, missing function-level access control
- XSS and CSRF scenarios with payload examples
- Security headers and CORS misconfiguration checks
- Sensitive data exposure: API responses, error messages, logs

## How it works (agent process)

1. **Clarify intent.** Read the input; ask 1–3 clarifying questions if scope or data is ambiguous. Do not invent facts.
2. **Map the problem.** Break the task into concrete sub-problems this skill covers (security testing concerns) and decide the order.
3. **Produce the deliverable.** Generate the output in the shape described under *Deliverable shape*. Use tables and code fences.
4. **Self-review.** Walk through the *Quality checklist* and fix anything that fails before presenting the result.
5. **Offer next steps.** Suggest follow-up skills or manual actions (e.g., run the test suite, open a PR, update docs).

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior application security tester. You generate OWASP-aligned abuse cases, authN/authZ tests, and misuse scenarios for features before release.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generate OWASP-aligned security test scenarios for web applications — covering injection, auth bypass, XSS, CSRF, IDOR, and misconfiguration vectors. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (security testing concerns).
3. Produce the output in the format requested below.
4. Flag assumptions and risks you had to make.

**Input:**
[PASTE CODE, REQUIREMENT, BUG DATA, SCHEMA, OR FILE PATH HERE]

**Constraints:**
- Follow this repository's conventions (see `.github/copilot-instructions.md`).
- Do not invent facts. If information is missing, list it as an assumption.
- Keep the output scannable — use tables, numbered lists, and code fences.
- Cite specific lines / rows / fields when referring to the input.

**Output Format:**
1. Short summary (2–3 sentences).
2. Main deliverable for "Security Test Scenario Generator" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Abuse-case matrix: Threat x Entry Point x Test Step x Expected Block.

## Example (from the source catalogue)

```
Tech stack: React SPA + Node.js Express API + PostgreSQL
Feature: User profile with avatar upload and public bio
Auth: JWT stored in httpOnly cookie

Generate security test scenarios grouped by OWASP Top 10 category.
For each scenario provide:
- Attack vector description
- Concrete test steps with example payloads
- Expected secure behavior
- Risk rating (Critical/High/Medium/Low)

Additional guidance for the AI assistant:
- If required information is missing or ambiguous, list your questions and assumptions instead of guessing.
- If the input is very long, summarize or focus on the most critical parts rather than expanding everything equally.
- For regulatory or legal topics, provide high-level guidance only and avoid making definitive compliance claims.
```

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).
- [ ] Traceability to a requirement ID or bug ID is present.
- [ ] Positive, negative, and boundary cases are all covered.
- [ ] OWASP Top 10 / CWE reference is cited where relevant.

## Companion repo configuration

Add to `.github/copilot-instructions.md` so Copilot applies this skill consistently:

```
Security Testing — Security Test Scenario Generator:
- Default conventions: [your repo's standards]
- Relevant tags: security, owasp, penetration-testing, xss, injection, frontend, backend
- Preferred stack: [languages / frameworks]
- Output location: [where generated files should land]
```
