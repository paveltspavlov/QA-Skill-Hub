---
name: pipeline-dag-builder
description: "Design or implement a scheduled data/job DAG from explicit dependencies, freshness, and recovery requirements. Use for orchestration workflows."
---

# Pipeline DAG Builder

## When to Use
Use to design or change a workflow DAG, task graph, schedule, backfill, retries, or failure notifications. Do not assume Airflow, Prefect, or a default retry policy.

## Required Inputs
Tasks, inputs/outputs, dependency rules, schedule/timezone, freshness or SLA, runtime/resource limits, framework/version, owner, data idempotency, and recovery requirements.

## Procedure
1. Build the directed dependency graph and check for cycles, hidden dependencies, and tasks with no declared outputs.
2. Define task contracts: input, output, side effects, idempotency key, timeout, success condition, and ownership.
3. Specify schedule, concurrency, retries/backoff, failure classification, alerting, catch-up/backfill, and pause/recovery behavior based on project conventions.
4. Check overlapping runs and partial writes; make outputs atomic or safe to resume where feasible.
5. Validate DAG parsing and simulate success, failure, retry, backfill, and dependency-skip paths.

## Output Contract
Return a DAG table with task ID, purpose, inputs, outputs, upstream dependencies, schedule/trigger, retry/timeout, idempotency, owner, and failure response. Include a diagram when useful, deployment/config changes, verification commands/results, and operational runbook notes.

## Quality Gate
Every task has an explicit dependency and failure policy. No cycle or unsafe concurrent write is introduced. Retry is bounded and cannot duplicate irreversible effects. SLA values are sourced or marked undecided.

## Evidence and Uncertainty
Cite framework version and existing workflow patterns. Ask before choosing schedule, SLA, or recovery semantics that affect production. Apply the evidence-readiness-gate.
