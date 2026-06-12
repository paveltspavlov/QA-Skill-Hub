---
id: pipeline-dag-builder
name: "Pipeline DAG Builder"
folder: skills
section: dev
summary: "Generates Airflow DAGs, Prefect flows, or dbt project scaffolds from a plain-English pipeline description — with dependency chains, retries, and alerting."
tags:
  - "airflow"
  - "prefect"
  - "dbt"
  - "dag"
  - "etl"
  - "orchestration"
  - "data-engineering"
---

# Pipeline DAG Builder

## Role

You are a senior data engineer. You design Airflow / Dagster / Prefect DAGs with correct task dependencies, retries, and SLAs.

## When to trigger this skill

When creating a new data pipeline, ETL job, or scheduled transformation workflow.

Also trigger when the user says things like:

- "help me with orchestration"
- "generate a pipeline dag builder"
- "generates airflow dags, prefect flows, or dbt project scaffolds from a plain-english pipeline description"

## What it does

Takes a pipeline description and generates:
- DAG file with task dependencies, schedule, and timeout config
- Retry logic with exponential backoff per task type
- SLA/alerting configuration for late or failed runs
- Idempotent task design (safe to re-run without duplicates)
- Connection/variable references (no hardcoded credentials)
- Sensor tasks for upstream data dependencies

## How it works (agent process)

```
# Claude Code:
> Create an Airflow DAG: extract orders from Postgres daily,
> transform in Spark, load to BigQuery, trigger dbt, Slack on failure

# The agent will:
# 1. Read existing DAGs for conventions
# 2. Generate DAG matching your project patterns
# 3. Create helper functions
# 4. Add connection references to README
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior data engineer. You design Airflow / Dagster / Prefect DAGs with correct task dependencies, retries, and SLAs.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Generates Airflow DAGs, Prefect flows, or dbt project scaffolds from a plain-English pipeline description — with dependency chains, retries, and alerting. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (orchestration concerns).
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
2. Main deliverable for "Pipeline DAG Builder" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Task graph, retries, SLAs, backfill strategy, alerting.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

```
Pipeline rules:
- Orchestrator: Airflow 2.x with TaskFlow API
- Default retries: 3 with 5-minute delay
- All tasks must be idempotent — use date partitions
- Connections: Airflow Variables, never hardcode
- Include a data quality check after every load step
```
