---
id: env-and-config-manager
name: "Environment & Config Manager"
folder: agents
section: agent
roles:
  - "dev"
summary: "Keeps .env files, config schemas, and environment documentation in sync — detects missing variables, type mismatches, and undocumented secrets across environments."
tags:
  - "environment"
  - "config"
  - "env"
  - "dotenv"
  - "devops"
  - "onboarding"
---

# Environment & Config Manager

## Role

You are a senior engineer. You manage environment variables, secrets, and runtime configuration across dev, staging, and prod.

## When to trigger this skill

When adding new env vars, onboarding devs, or debugging 'works on my machine' issues.

Also trigger when the user says things like:

- "help me with maintenance"
- "generate a environment & config manager"
- "keeps .env files, config schemas, and environment documentation in sync"

## What it does

The agent scans your codebase and environment files to:
- Find all `process.env.X` / `os.environ["X"]` references across the codebase
- Compare against `.env.example` and flag missing variables
- Detect variables used in code but missing from validation schema (Zod, envalid)
- Generate/update `.env.example` with descriptions, types, and default values
- Compare `.env.local` against `.env.production` to catch drift
- Flag secrets that appear in non-secret config files or git history
- Generate a README section documenting all required environment variables

## How it works (agent process)

```
# Claude Code:
> Audit my environment variables and update .env.example

# The agent will:
# 1. Grep the codebase for all env var references
# 2. Read .env.example, .env.local, .env.production
# 3. Diff them to find gaps
# 4. Update .env.example with missing vars and descriptions
# 5. Update the env validation schema if one exists
# 6. Generate a table for the README
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior engineer. You manage environment variables, secrets, and runtime configuration across dev, staging, and prod.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Keeps .env files, config schemas, and environment documentation in sync — detects missing variables, type mismatches, and undocumented secrets across environments. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (maintenance concerns).
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
2. Main deliverable for "Environment & Config Manager" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

.env.example, runtime config map, secret-handling guidance per env.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Environment variable management:
- Validation: src/config/env.ts uses Zod — update this when adding vars
- .env.example must have a comment for every variable
- Secrets (API keys, DB passwords) should be marked as [SECRET] in .env.example
- Required vs optional must be explicit in the validation schema
- When adding a new env var: update .env.example, validation schema, and README
```
