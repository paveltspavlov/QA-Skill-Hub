---
id: dev-prompts-7-3-write-a-dbt-pipeline-model-from-a-business-definition
name: "7.3 - Write a dbt / Pipeline Model from a Business Definition"
folder: prompts
section: dev-prompts
summary: "Data Engineering & SQL"
tags:
  - "dev-prompts"
  - "data engineering & sql"
---

# Prompt 7.3 - Write a dbt / Pipeline Model from a Business Definition

> Category: **Data Engineering & SQL**

When to use  You have a business definition ('active customer = X in the last 30 days') and need a model with tests and documentation.

Expected output  A model file + schema tests + a docs block + notes on grain and refresh cadence.

Prompt

```
**Role:** You are an analytics engineer who builds models that are self-describing and that fail loudly when the source data drifts.

**Context:** Pipeline tool: [DBT / SPARK SQL / AIRFLOW + SQL / OTHER]. Upstream sources: [LIST]. Refresh cadence: [HOURLY / DAILY / OTHER].

**Instruction:** Build a model for the definition below.

1. Restate the definition in SQL-compatible terms (what's the grain? what's the time window? what's a tie-breaker?).

2. Write the model SQL.

3. Add tests that would catch upstream breakage - not null on join keys, unique on grain, accepted values where it matters.

4. Write a short docs block describing each output column.

**Input:**

Business definition:

[PASTE]

Upstream tables:

[LIST + GRAIN]

**Constraints:**

- Grain is declared explicitly.

- Time windows use a single, named reference point - no `now()` sprinkled everywhere.

- No silent coalescing of nulls into zero unless the definition says so.

**Output Format:**

- Restatement of the definition

- Model SQL

- Tests (inline or separate file)

- Docs block

Contributing New Prompts

This library grows by accretion. When you find a prompt that produces good output twice in a row against different inputs, add it using the template below. Consistency is what makes the library easy to search and the outputs easy to trust.

Prompt template

### Prompt [CATEGORY].[N] - [Descriptive Name]

**When to use:** [1 line - the trigger situation]

**Expected output:** [1 line - the shape of what you'll get back]

**Role:** You are a [specific role with concrete experience].

**Context:** [Stack, layer, constraints the task sits inside.]

**Instruction:** [Numbered reasoning steps + deliverables.]

**Input:** [Code / spec / trace / data.]

**Constraints:**

- [What the output must NOT do]

- [Guardrails - e.g. 'flag unknowns, do not invent']

**Output Format:** [Exact structure - file tree, diff, ADR, etc.]

Quality checklist before you commit a new prompt

Ran the prompt twice against different inputs - the output stayed on-format.

Placeholders are obvious ([SQUARE_BRACKETS]) so a teammate spots them before running.

The Role is specific enough to exclude generic, mid-level answers.

Constraints include at least one 'do not' - this is usually where quality lives.

Output Format would tell a reviewer what 'done' looks like without asking.
```
