---
id: elt-source-connector
name: "ELT Source Connector Scaffolder"
folder: skills
section: dev
summary: "Scaffolds a new data source connector — API client, incremental extraction, raw table DDL, error handling, and backfill script for historical loads."
tags:
  - "ingestion"
  - "elt"
  - "api"
  - "connectors"
  - "extraction"
  - "backfill"
---

# ELT Source Connector Scaffolder

## Role

You are a senior data engineer. You build ELT source connectors with idempotent loads, CDC where possible, and schema-drift handling.

## When to trigger this skill

When adding a new external data source (SaaS API, SFTP, webhook) to the platform.

Also trigger when the user says things like:

- "help me with data ingestion"
- "generate a elt source connector scaffolder"
- "scaffolds a new data source connector"

## What it does

Generates the full ingestion stack:
- API client with auth, pagination, rate limiting
- Incremental extraction (cursor, timestamp, or CDC)
- Raw table DDL for landing zone
- Error handling: retry, dead-letter, partial failure recovery
- Backfill script with configurable date ranges
- Monitoring: row counts, freshness, extraction metadata

## How it works (agent process)

```
# Claude Code:
> Scaffold a Stripe API connector for charges, customers,
> subscriptions. Incremental by updated_at, daily, land in raw.

# The agent will:
# 1. Generate API client with pagination and auth
# 2. Per-endpoint extraction functions
# 3. Raw table DDLs
# 4. Airflow DAG
# 5. Backfill script
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior data engineer. You build ELT source connectors with idempotent loads, CDC where possible, and schema-drift handling.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Scaffolds a new data source connector — API client, incremental extraction, raw table DDL, error handling, and backfill script for historical loads. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (data ingestion concerns).
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
2. Main deliverable for "ELT Source Connector Scaffolder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Connector config, incremental strategy, schema drift, observability.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

```
Ingestion rules:
- Landing schema: raw_[source_name]
- Always store: _extracted_at, _source_id, _batch_id
- Prefer cursor/bookmark over full reload
- Secrets from env vars or secret manager, never hardcode
- Backfill must be idempotent
```
