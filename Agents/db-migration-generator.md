---
id: db-migration-generator
name: "DB Migration Generator"
folder: agents
section: agent
roles:
  - "dev"
summary: "Generates safe, reversible database migration scripts from a schema change description — with up/down logic, data backfill steps, and zero-downtime deployment notes."
tags:
  - "database"
  - "migrations"
  - "prisma"
  - "sql"
  - "backend"
  - "schema"
---

# DB Migration Generator

## Role

You are a senior backend engineer. You generate safe forward/backward database migrations with data-backfill plans where needed.

## When to trigger this skill

When adding/modifying database tables, columns, indexes, or constraints.

Also trigger when the user says things like:

- "help me with code generation"
- "generate a db migration generator"
- "generates safe, reversible database migration scripts from a schema change description"

## What it does

The agent takes a schema change request and produces:
- Migration file in your ORM format (Prisma, Knex, Alembic, raw SQL)
- Reversible down migration that safely rolls back
- Data backfill script if the migration requires populating a new column
- Zero-downtime deployment sequence (e.g., add column nullable → backfill → add constraint → deploy code)
- Index impact analysis: will this migration lock the table? For how long?
- Validation query to verify the migration succeeded in production

## How it works (agent process)

```
# Claude Code:
> Add a `role` enum column to the users table with default 'member'

# The agent will:
# 1. Read the current schema (prisma/schema.prisma or migration history)
# 2. Generate the migration file
# 3. Generate the down migration
# 4. If table has >100K rows, warn about lock time and suggest
#    a phased approach
# 5. Run `prisma migrate dev` (or equivalent) to apply locally
# 6. Verify with a test query
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior backend engineer. You generate safe forward/backward database migrations with data-backfill plans where needed.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generates safe, reversible database migration scripts from a schema change description — with up/down logic, data backfill steps, and zero-downtime deployment notes. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (code generation concerns).
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
2. Main deliverable for "DB Migration Generator" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Up / Down scripts, backfill plan, ordering, verification SQL.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `CLAUDE.md`:
```
Database migration rules:
- ORM: Prisma with PostgreSQL
- Every migration must be reversible — include down logic
- New non-nullable columns must be added in 2 steps:
  1. Add as nullable with default
  2. Backfill, then add NOT NULL constraint
- Never drop columns in the same deploy as the code change that removes usage
- Add an index for any column used in WHERE or JOIN clauses
- Migration names: YYYYMMDD_description (e.g., 20260407_add_user_role)
```
