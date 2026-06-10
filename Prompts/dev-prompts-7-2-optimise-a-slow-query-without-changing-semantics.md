---
id: dev-prompts-7-2-optimise-a-slow-query-without-changing-semantics
name: "7.2 - Optimise a Slow Query Without Changing Semantics"
folder: prompts
section: dev-prompts
summary: "Data Engineering & SQL"
tags:
  - "dev-prompts"
  - "data engineering & sql"
---

# Prompt 7.2 - Optimise a Slow Query Without Changing Semantics

> Category: **Data Engineering & SQL**

When to use  When a query is correct but slow, and the plan has at least one ugly shape (full scan, N+1 subquery, missed index).

Expected output  A rewritten query with the same result set + a rationale + any schema/index change that would be needed.

Prompt

```
**Role:** You are an engineer who reads execution plans before rewriting queries.

**Context:** Dialect: [DIALECT]. Table sizes: [APPROX ROWS PER TABLE]. Known indexes: [LIST].

**Instruction:** Optimise the query below.

1. Describe the suspected performance issue in one line (full scan / hashed join on wrong key / filter after the join / N+1 subquery / other).

2. Rewrite the query so the result set is identical.

3. Suggest the smallest schema change (if any) that would help - index or materialised view.

4. Predict the effect on a 10x larger table.

**Input:**

Query:

[PASTE]

Explain output (if available):

[PASTE]

Key statistics:

[ROW COUNTS / CARDINALITY]

**Constraints:**

- The result set must be identical - prove it by describing what a comparison test would check.

- Don't "fix" by adding LIMIT unless the caller already accepted partial results.

- Flag if the real fix is upstream (schema change, pre-aggregate).

**Output Format:**

- Problem (one line)

- Rewritten query

- Schema change suggestion (optional)

- Predicted behaviour at 10x scale
```
