---
id: dev-prompts-7-1-write-a-correct-first-query-from-a-natural-language-question
name: "7.1 - Write a Correct-First Query from a Natural-Language Question"
folder: prompts
section: dev-prompts
summary: "Data Engineering & SQL"
tags:
  - "dev-prompts"
  - "data engineering & sql"
---

# Prompt 7.1 - Write a Correct-First Query from a Natural-Language Question

> Category: **Data Engineering & SQL**

When to use  When a stakeholder asks a question in plain English and you need a correct query before you worry about speed.

Expected output  A single SQL query + column meaning + the assumptions baked in + a short check you can run to trust the result.

Prompt

```
**Role:** You are a data-aware engineer who writes SQL that passes a peer review before it passes a profiler.

**Context:** Dialect: [SNOWFLAKE / BIGQUERY / POSTGRES / OTHER]. Schema - tables, PKs, and the grain of each - is:

[PASTE TABLE DEFINITIONS OR DESCRIPTIONS]

**Instruction:** Answer the question below.

1. Restate the question in terms of the schema (which tables, which grain).

2. List the assumptions you're making (time zone, de-duplication rule, late-arriving data handling).

3. Write the query.

4. Write a one-line sanity check - a row count or aggregate the reader can eyeball.

**Input:**

Question:

[PASTE]

**Constraints:**

- Prefer CTEs over nested subqueries for readability.

- No `SELECT *` in the final projection.

- Explicit joins - never comma-joins.

**Output Format:**

- Restated question

- Assumptions

- Query

- Sanity check
```
