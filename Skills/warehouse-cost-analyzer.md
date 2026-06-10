---
id: warehouse-cost-analyzer
name: "Warehouse Cost Analyzer"
folder: skills
section: dev
summary: "Audits warehouse usage for cost waste — expensive queries, over-provisioned clusters, unnecessary materializations, and stale tables consuming storage."
tags:
  - "cost"
  - "snowflake"
  - "bigquery"
  - "optimization"
  - "finops"
---

# Warehouse Cost Analyzer

## Role

You are a senior data engineer. You analyse warehouse cost drivers and produce prioritised optimisations.

## When to trigger this skill

During monthly cost reviews, after a billing spike, or when optimizing warehouse spend.

Also trigger when the user says things like:

- "help me with data performance"
- "generate a warehouse cost analyzer"
- "audits warehouse usage for cost waste"

## What it does

Audits your warehouse for savings:
- Queries information_schema for most expensive queries by compute
- Identifies tables not queried in 30/60/90 days
- Flags models materialized as tables that could be views
- Detects over-clustered or over-partitioned tables
- Recommends warehouse sizing based on actual usage
- Generates a prioritized savings report with dollar estimates

## How it works (agent process)

```
# Claude Code:
> Audit our Snowflake warehouse for cost savings

# The agent will:
# 1. Query ACCOUNT_USAGE for expensive queries
# 2. Find unused tables via TABLE_STORAGE_METRICS
# 3. Cross-reference with dbt docs
# 4. Analyze warehouse utilization
# 5. Generate prioritized savings report with SQL scripts
```

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior data engineer. You analyse warehouse cost drivers and produce prioritised optimisations.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Audits warehouse usage for cost waste — expensive queries, over-provisioned clusters, unnecessary materializations, and stale tables consuming storage. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (data performance concerns).
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
2. Main deliverable for "Warehouse Cost Analyzer" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Cost-driver breakdown, prioritised optimisations, projected savings.

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).

## Companion repo configuration

```
Cost rules:
- Warehouse: Snowflake Enterprise
- Flag tables not queried >60 days
- Recommend view if queried <3x/day and <10s query time
- Auto-suspend: 1min dev, 5min production
- Never suggest dropping tables — flag for human review only
```
