---
id: background-job-builder
name: "Background Job Builder"
folder: skills
section: dev
summary: "Sets up background job processing — queue, workers, retry policies, dead letter handling, and monitoring for async tasks like emails, exports, and webhooks."
tags:
  - "queues"
  - "bullmq"
  - "celery"
  - "background-jobs"
  - "backend"
  - "async"
---

# Background Job Builder

## Role

You are a senior backend engineer. You implement background jobs (BullMQ / Sidekiq / Celery / etc.) with retry, dead-letter queues, and observability.

## When to trigger this skill

When offloading slow ops: email, PDF generation, data exports, webhook delivery, image processing.

Also trigger when the user says things like:

- "help me with backend development"
- "generate a background job builder"
- "sets up background job processing"

## What it does

The agent sets up a job system:
- Queue infrastructure (BullMQ or Celery)
- Typed job definitions with payload validation
- Worker with concurrency control and graceful shutdown
- Retry: exponential backoff, dead letter queue
- Job progress reporting
- Admin health endpoint

## How it works (agent process)

```
# Claude Code:
> Set up background jobs for email sending and PDF reports

# The agent will:
# 1. Set up BullMQ with Redis
# 2. Generate typed job definitions
# 3. Generate worker with retry/error handling
# 4. Add enqueue helper for route handlers
# 5. Update docker-compose
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior backend engineer. You implement background jobs (BullMQ / Sidekiq / Celery / etc.) with retry, dead-letter queues, and observability.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Sets up background job processing — queue, workers, retry policies, dead letter handling, and monitoring for async tasks like emails, exports, and webhooks. Work through these steps:
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
2. Main deliverable for "Background Job Builder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Queue definition, worker, retry/DLQ, metrics, smoke tests.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Background jobs:
- Queue: BullMQ + Redis
- Retry: 3 attempts, exponential (1m, 5m, 15m)
- Dead letter: move after max retries, alert Slack
- Concurrency: 5 per queue
```
