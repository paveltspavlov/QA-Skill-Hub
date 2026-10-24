---
name: pipeline-dag-builder
description: "Design a data or job pipeline DAG from explicit dependencies, freshness, and recovery requirements. Use when tasks must be scheduled and orchestrated."
---

# Pipeline DAG Builder

## Procedure
1. Extract tasks, inputs/outputs, dependency edges, schedule, data freshness, runtime, and ownership.
2. Inspect the orchestration framework already in use. Do not assume Airflow, Prefect, or another scheduler without evidence.
3. Make retries bounded and safe; define idempotency, backfill/catch-up, timeouts, sensors, and failure notifications.
4. Avoid hidden dependencies and cyclic graphs. State data contracts and prevent concurrent runs from corrupting shared outputs.
5. Add validation for graph structure and a failure/retry path; document deployment and rollback.

## Output
A DAG/flow plan or code in the existing framework, with dependency and recovery notes.
