---
id: dbt-model-generator
name: "dbt Model Generator"
folder: skills
section: dev
summary: "Creates dbt models from business requirements — staging, intermediate, and mart layers with materialization strategy, incremental logic, and full documentation."
tags:
  - "dbt"
  - "data-modeling"
  - "dimensional"
  - "star-schema"
  - "sql"
  - "analytics"
---

# dbt Model Generator

## Role

You are a senior analytics engineer. You build dbt models (staging / intermediate / mart) with tests, docs, and lineage.

## When to trigger this skill

When adding a new data source, building a mart, or refactoring transformation layers.

Also trigger when the user says things like:

- "help me with data modeling"
- "generate a dbt model generator"
- "creates dbt models from business requirements"

## What it does

Generates the full dbt model chain:
- **Staging**: column renaming, type casting, filtering from raw source
- **Intermediate**: joins, deduplication, business logic
- **Mart**: final dimensional model (fact or dimension) for analytics
- Materialization strategy per layer (view → ephemeral → incremental/table)
- Incremental logic with merge keys and late-arriving data handling
- schema.yml with descriptions, tests, and tags

## How it works (agent process)

```
# Claude Code:
> Create dbt models for Stripe subscriptions.
> Need: MRR, churn date, plan changes over time

# The agent will:
# 1. Read your dbt project structure and naming conventions
# 2. Generate stg, int, and fct models
# 3. Generate schema.yml with tests
# 4. Update sources.yml
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior analytics engineer. You build dbt models (staging / intermediate / mart) with tests, docs, and lineage.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Creates dbt models from business requirements — staging, intermediate, and mart layers with materialization strategy, incremental logic, and full documentation. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (data modeling concerns).
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
2. Main deliverable for "dbt Model Generator" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Staging / intermediate / mart SQL + schema.yml tests + docs + lineage.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

```
dbt conventions:
- Naming: stg_[source]__[table], int_[concept], fct_/dim_[noun]
- Staging: views, 1:1 with source, only rename + cast
- Marts: incremental for facts >1M rows
- Every model must have a primary key test and a description
```
