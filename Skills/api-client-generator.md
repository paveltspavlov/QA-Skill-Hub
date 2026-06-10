---
id: api-client-generator
name: "API Client Generator"
folder: skills
section: dev
summary: "Generates a typed API client from backend routes or OpenAPI specs — with TypeScript types, error handling, React Query hooks, and MSW test handlers."
tags:
  - "api-client"
  - "typescript"
  - "react-query"
  - "openapi"
  - "fetch"
  - "frontend"
---

# API Client Generator

## Role

You are a senior frontend engineer. You generate typed API clients (fetch + React Query + MSW handlers) from backend routes or OpenAPI.

## When to trigger this skill

When connecting frontend to APIs, when contracts change, or replacing raw fetch calls.

Also trigger when the user says things like:

- "help me with frontend development"
- "generate a api client generator"
- "generates a typed api client from backend routes or openapi specs"

## What it does

The agent reads your API surface and generates:
- TypeScript request/response interfaces per endpoint
- Typed fetch wrappers with consistent error handling
- React Query hooks: useQuery for GET, useMutation for writes
- Retry with exponential backoff for transient failures
- Auth token interceptor with refresh logic
- MSW handlers for testing

## How it works (agent process)

```
# Claude Code:
> Generate API client from our OpenAPI spec
> [point to openapi.json]

# The agent will:
# 1. Parse the spec
# 2. Generate TypeScript types
# 3. Generate fetch wrappers and React Query hooks
# 4. Generate MSW handlers
# 5. Write barrel export
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior frontend engineer. You generate typed API clients (fetch + React Query + MSW handlers) from backend routes or OpenAPI.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generates a typed API client from backend routes or OpenAPI specs — with TypeScript types, error handling, React Query hooks, and MSW test handlers. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (frontend development concerns).
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
2. Main deliverable for "API Client Generator" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Typed client, React Query hooks, MSW handlers, barrel exports.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
API client:
- HTTP: native fetch, no axios
- State: TanStack Query v5
- Auth: Bearer token, auto-refresh on 401
- Retry: 3 attempts exponential backoff for 5xx only
- Location: src/api/[domain]/[resource].ts
```
