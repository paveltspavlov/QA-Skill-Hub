---
id: error-monitoring-setup
name: "Error Monitoring Setup"
folder: skills
section: dev
summary: "Adds production error handling and monitoring — React error boundaries, backend error middleware, Sentry integration, structured logging, and alert rules."
tags:
  - "error-handling"
  - "monitoring"
  - "sentry"
  - "logging"
  - "observability"
  - "frontend"
  - "backend"
---

# Error Monitoring Setup

## Role

You are a senior engineer. You set up error monitoring (Sentry / Rollbar / Datadog) with correct breadcrumbs, context, and alerting.

## When to trigger this skill

Setting up observability for a new project, after a production incident, or adding Sentry/Datadog.

Also trigger when the user says things like:

- "help me with development"
- "generate a error monitoring setup"
- "adds production error handling and monitoring"

## What it does

The agent instruments your app:
- **Frontend**: error boundaries per route, unhandled rejection catcher, Sentry browser SDK
- **Backend**: error middleware with structured error classes, request ID propagation, Sentry server SDK
- **Logging**: structured JSON (pino) with correlation IDs
- **Alerts**: error spike → Slack, new error type → on-call
- **Source maps**: upload config for readable production traces

## How it works (agent process)

```
# Claude Code:
> Set up error monitoring with Sentry for Next.js + Express

# The agent will:
# 1. Install Sentry SDKs
# 2. Generate error boundaries and middleware
# 3. Configure source map uploads
# 4. Add request ID propagation
# 5. Generate alert rule suggestions
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You set up error monitoring (Sentry / Rollbar / Datadog) with correct breadcrumbs, context, and alerting.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Adds production error handling and monitoring — React error boundaries, backend error middleware, Sentry integration, structured logging, and alert rules. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (development concerns).
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
2. Main deliverable for "Error Monitoring Setup" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

SDK wiring, breadcrumbs, PII scrubbing, release tracking, alert rules.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Error monitoring:
- Provider: Sentry
- Frontend: error boundary per route
- Backend: custom error classes extending BaseAppError
- Logging: pino JSON, log level from env
- Alerts: new error → Slack, >10 same in 5min → PagerDuty
- Never log passwords, tokens, PII
```
