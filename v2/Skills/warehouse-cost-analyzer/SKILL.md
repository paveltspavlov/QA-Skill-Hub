---
name: warehouse-cost-analyzer
description: "Analyze warehouse cost drivers from actual query, storage, and compute evidence. Use for cost reviews or optimization proposals."
---

# Warehouse Cost Analyzer

## When to Use
Use for warehouse/platform cost reviews, billing spikes, query/storage/compute optimization, and experiments to reduce spend while preserving correctness, freshness, and reliability. Do not recommend deletion or changes based on generic thresholds.

## Required Inputs
Identify platform and edition/version, billing period and timezone, currency/unit, billing exports, query history, workload/owner mapping, storage/compute metrics, schedules/refreshes, business freshness and latency requirements, environment split, and read-only permissions. Provide current platform pricing/rate source before dollar estimates. Redact query literals and user identifiers.

## Procedure
1. Define the cost scope and reconcile source billing totals. Separate compute, storage, transfer, and service-specific charges; note credits, reservations, and shared allocations where visible.
2. Rank drivers using observed bytes scanned, execution count/runtime, warehouse/cluster idle time, queueing, storage growth, materialization/refresh frequency, and failed/retried work. Distinguish measurement from attribution inference.
3. For each candidate, calculate baseline from supplied data and stated pricing formula; include period, units, allocation method, uncertainty, and any cost transferred to another workload. If rates or denominator are absent, provide a measurement experiment, not a savings figure.
4. Propose reversible, bounded experiments: query pruning/projection, schedule/concurrency changes, right-sizing, caching/materialization alternatives, retention review. Do not drop data or alter production automatically; require owner approval and recovery plan.
5. Pair spend with correctness, freshness, latency, availability, and concurrency measures. Set experiment acceptance criteria with owners; compare representative periods and workloads.

## Output Contract
Return `Scope and sources`; ranked table `Rank | Driver | Evidence query/period | Cost units | Baseline | Candidate change | Estimated effect/formula | Quality trade-off | Owner/next step`; `Experiment and rollback`; `Uncertainty`. Example: `1 | repeated full scan | query history, dates stated | bytes scanned × applicable rate | measured scan volume | test partition filter | estimate only after repeat rate/rate source | verify identical results + latency | data owner`. Never assert savings without both baseline and rate evidence.

## Quality Gate
Billing reconciliation is explained; rankings distinguish observed metrics from attribution; units and periods align; price source is current and platform-specific; quality guardrails and rollback are defined; privacy-safe evidence is used; no unmeasured savings claim or destructive recommendation.

## Evidence and Uncertainty
Ground totals in billing exports/query telemetry and price assumptions in official platform documentation or supplied invoice rates. Apply readiness across scope, traceable claims, complete contract, and relevant verification (25 points each). Below 75/100, ask, qualify, or abstain; never invent confidence percentages. Critical safety, privacy, authorization, or acceptance failures cannot be averaged away.
