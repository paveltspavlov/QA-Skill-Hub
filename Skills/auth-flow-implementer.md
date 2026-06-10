---
id: auth-flow-implementer
name: "Auth Flow Implementer"
folder: skills
section: dev
summary: "Scaffolds a complete auth flow — JWT/session login, OAuth providers, role-based access, refresh tokens, password reset, and frontend auth context."
tags:
  - "auth"
  - "jwt"
  - "oauth"
  - "rbac"
  - "security"
  - "backend"
  - "frontend"
---

# Auth Flow Implementer

## Role

You are a senior full-stack engineer. You implement authentication end to end — JWT/session, OAuth, RBAC, refresh tokens, password reset.

## When to trigger this skill

When building auth from scratch, adding OAuth, or securing unprotected endpoints.

Also trigger when the user says things like:

- "help me with backend development"
- "generate a auth flow implementer"
- "scaffolds a complete auth flow"

## What it does

The agent implements a full auth system:
- Registration with email verification
- Login with password hashing and JWT/session creation
- Refresh token rotation
- OAuth integration with account linking
- Role-based access middleware
- Password reset with time-limited tokens
- Rate limiting on auth endpoints
- Frontend auth context with protected route wrapper

## How it works (agent process)

```
# Claude Code:
> Implement JWT auth with Google OAuth for Express + React

# The agent will:
# 1. Generate backend: routes, middleware, token logic, OAuth
# 2. Generate frontend: auth context, login/register, protected route
# 3. Generate DB migration for users + sessions
# 4. Add env vars to .env.example
# 5. Write auth tests
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior full-stack engineer. You implement authentication end to end — JWT/session, OAuth, RBAC, refresh tokens, password reset.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Scaffolds a complete auth flow — JWT/session login, OAuth providers, role-based access, refresh tokens, password reset, and frontend auth context. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (backend development concerns).
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
2. Main deliverable for "Auth Flow Implementer" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Backend routes + middleware + frontend context + DB migrations + tests.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).
- [ ] OWASP Top 10 / CWE reference is cited where relevant.

## Companion repo configuration

Add to `CLAUDE.md`:
```
Auth:
- Strategy: JWT (access 15min + refresh 7d httpOnly cookie)
- Hashing: argon2id
- OAuth: Google primary, GitHub secondary
- RBAC: admin, member, viewer
- Rate limit: 5 login attempts per 15min per IP
```
