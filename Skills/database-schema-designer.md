---
id: database-schema-designer
name: "Database Schema Designer"
folder: skills
section: dev
summary: "Design normalized database schemas from business requirements — with table definitions, relationships, indexes, constraints, and migration scripts."
aiTools:
  - "Claude Code"
  - "Claude Chat"
  - "ChatGPT"
tags:
  - "database"
  - "sql"
  - "prisma"
  - "schema"
  - "migrations"
  - "backend"
  - "data-modeling"
---

# Database Schema Designer

## Role

You are a senior database engineer. You design normalised relational schemas, indexes, and constraints that serve the application's query patterns.

## When to trigger this skill

Trigger when the user mentions database, sql, prisma, schema, migrations, or asks for help in the backend development area.

Also trigger when the user says things like:

- "help me with backend development"
- "generate a database schema designer"
- "design normalized database schemas from business requirements"

## What it does

Takes a feature description or domain model and produces:
- Table/collection definitions with appropriate data types
- Relationships (1:1, 1:N, M:N with junction tables)
- Index recommendations for common query patterns
- Constraints (unique, check, foreign key, not null)
- Soft delete vs hard delete strategy
- Audit columns (createdAt, updatedAt, createdBy)
- Migration script in your ORM format (Prisma, Alembic, Knex, raw SQL)
- Seed data script for development

## How it works (agent process)

1. **Clarify intent.** Read the input; ask 1–3 clarifying questions if scope or data is ambiguous. Do not invent facts.
2. **Map the problem.** Break the task into concrete sub-problems this skill covers (backend development concerns) and decide the order.
3. **Produce the deliverable.** Generate the output in the shape described under *Deliverable shape*. Use tables and code fences.
4. **Self-review.** Walk through the *Quality checklist* and fix anything that fails before presenting the result.
5. **Offer next steps.** Suggest follow-up skills or manual actions (e.g., run the test suite, open a PR, update docs).

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior database engineer. You design normalised relational schemas, indexes, and constraints that serve the application's query patterns.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Design normalized database schemas from business requirements — with table definitions, relationships, indexes, constraints, and migration scripts. Work through these steps:
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
2. Main deliverable for "Database Schema Designer" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

ERD notes, DDL, indexes, constraints, migration ordering.

## Example (from the source catalogue)

```
Domain: Online course platform
Entities: Users, Courses, Lessons, Enrollments, Progress, Reviews

Business rules:
- A user can be both instructor and student
- Courses have ordered lessons grouped into modules
- Progress tracks per-lesson completion with timestamps
- Reviews are 1-5 stars with optional text, one per user per course

Generate: Prisma schema, explain index choices,
include seed script with 3 courses and 10 users.

Additional guidance for the AI assistant:
- If required information is missing or ambiguous, list your questions and assumptions instead of guessing.
- If the input is very long, summarize or focus on the most critical parts rather than expanding everything equally.
```

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

Add to `.github/copilot-instructions.md` so Copilot applies this skill consistently:

```
Backend Development — Database Schema Designer:
- Default conventions: [your repo's standards]
- Relevant tags: database, sql, prisma, schema, migrations, backend, data-modeling
- Preferred stack: [languages / frameworks]
- Output location: [where generated files should land]
```
