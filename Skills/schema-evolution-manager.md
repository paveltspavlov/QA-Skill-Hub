---
id: schema-evolution-manager
name: "Schema Evolution Manager"
folder: skills
section: dev
summary: "Manages schema changes across warehouses safely — generates ALTER scripts, backward-compatible Avro/Protobuf updates, and downstream impact analysis."
tags:
  - "schema"
  - "data-warehouse"
  - "avro"
  - "protobuf"
  - "migrations"
  - "backward-compatibility"
---

# Schema Evolution Manager

## Role

You are a senior data engineer. You evolve warehouse schemas safely — additive changes, deprecation windows, consumer communication.

## When to trigger this skill

When modifying warehouse tables, event schemas, or shared data contracts between teams.

Also trigger when the user says things like:

- "help me with data modeling"
- "generate a schema evolution manager"
- "manages schema changes across warehouses safely"

## What it does

The agent handles schema changes across the data stack:
- Generates ALTER TABLE scripts for warehouse changes (BigQuery, Snowflake, Redshift)
- Checks backward compatibility for event schemas (Avro, Protobuf, JSON Schema)
- Maps downstream impact: which dashboards, models, and consumers break
- Produces a migration runbook with rollback steps
- Updates dbt schema.yml and tests to match

## How it works (agent process)

```
# Claude Code:
> Add a loyalty_tier column to dim_customers and update downstream models

# The agent will:
# 1. Read current table definition
# 2. Generate ALTER TABLE
# 3. Grep dbt models referencing the table
# 4. Update schema.yml and add tests
# 5. List affected downstream consumers
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior data engineer. You evolve warehouse schemas safely — additive changes, deprecation windows, consumer communication.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Manages schema changes across warehouses safely — generates ALTER scripts, backward-compatible Avro/Protobuf updates, and downstream impact analysis. Work through these steps:
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
2. Main deliverable for "Schema Evolution Manager" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Additive change + deprecation window + consumer comms + rollback.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

```
Schema rules:
- Warehouse: Snowflake
- Never drop or rename columns — add new, deprecate old
- New columns must be nullable or have a default
- Update dbt schema.yml for every schema change
- Generate a stakeholder changelog entry for every change
```
