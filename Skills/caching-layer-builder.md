---
id: caching-layer-builder
name: "Caching Layer Builder"
folder: skills
section: dev
summary: "Adds Redis caching — cache-aside pattern, TTL tuning, invalidation on writes, request deduplication, and cache hit/miss metrics."
tags:
  - "caching"
  - "redis"
  - "performance"
  - "backend"
  - "invalidation"
  - "scalability"
---

# Caching Layer Builder

## Role

You are a senior backend engineer. You design cache-aside layers with Redis — TTL tuning, invalidation on writes, request deduplication, and hit/miss metrics.

## When to trigger this skill

When APIs are slow, DB is under read pressure, or adding Redis to the stack.

Also trigger when the user says things like:

- "help me with backend development"
- "generate a caching layer builder"
- "adds redis caching"

## What it does

The agent adds intelligent caching:
- Identifies cacheable endpoints (read-heavy, infrequently changing)
- Implements cache-aside with typed Redis wrapper
- Sets TTLs by data change frequency
- Cache invalidation on writes
- Request deduplication for concurrent identical requests
- Cache hit/miss metrics logging

## How it works (agent process)

```
# Claude Code:
> Add Redis caching to product catalog endpoints

# The agent will:
# 1. Read endpoint handlers
# 2. Identify cacheable responses and TTLs
# 3. Generate typed Redis wrapper
# 4. Add cache-aside to GETs, busting to writes
# 5. Update docker-compose with Redis
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior backend engineer. You design cache-aside layers with Redis — TTL tuning, invalidation on writes, request deduplication, and hit/miss metrics.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Adds Redis caching — cache-aside pattern, TTL tuning, invalidation on writes, request deduplication, and cache hit/miss metrics. Work through these steps:
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
2. Main deliverable for "Caching Layer Builder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Typed Redis wrapper, cache-aside per endpoint, invalidation on writes, metrics.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).
- [ ] Measurable SLOs and a benchmarking plan are included.

## Companion repo configuration

Add to `CLAUDE.md`:
```
Caching:
- Provider: Redis via ioredis
- Key format: [service]:[entity]:[id]
- Default TTL: 5min lists, 15min single entity
- Never cache: user-specific data, auth responses
- Log hit/miss ratio per endpoint
```
