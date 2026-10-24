---
name: performance-test-planner
description: "Plan realistic load, stress, spike, and endurance tests. Use when setting performance workloads, acceptance criteria, or execution monitoring."
---

# Performance Test Planner

## When to Use
Use to plan performance validation for APIs, services, data systems, and user journeys; create workload models or k6/JMeter outlines; or investigate capacity and latency risks. This skill plans and interprets tests; it does not assert that a system meets an SLO without measured execution evidence.

## Required Inputs
Collect system boundaries and critical journeys; traffic profile and user mix; throughput/concurrency assumptions and their source; payload/data characteristics; SLOs or business acceptance criteria; dependencies and rate limits; representative environment and data; test window, safety limits, observability, and tool preference. Ask for missing values that determine pass/fail; use marked TBDs rather than invented numbers.

## Procedure
1. Define objective, in-scope endpoints, excluded dependencies, baseline, and safety/stop conditions. Confirm authorized environment and whether production testing is explicitly permitted.
2. Translate supplied traffic evidence into arrival rate or concurrent-user profile, journey proportions, think time, payload mix, and ramp/steady-state/cool-down. Show formulas and assumptions; distinguish peak, average, and forecast traffic.
3. Select the needed profiles: baseline/load for expected demand; stress to characterize limits; spike for abrupt change; endurance for degradation over time. Set duration and load only from requirements or agreed test capacity.
4. Define pass/fail criteria from approved SLOs: latency percentiles, throughput, error/timeout rate, resource saturation, and correctness. State measurement window, aggregation, and exclusions; do not manufacture thresholds.
5. Map a test script to journeys with setup, warm-up, checks, data isolation, cleanup, and correlation IDs. Avoid a load generator becoming the bottleneck.
6. Pair service metrics with client-side results, dependency telemetry, logs, and infrastructure metrics. Specify stop triggers and post-run reconciliation.

## Output Contract
Return `Performance Test Plan: <system>` with: `Scope and SLOs`; workload table `Journey | Share/source | Arrival or users | Payload/data | Think time | Evidence`; scenario table `Scenario | Profile | Duration | Pass criteria | Stop condition`; environment/monitoring; tool/script outline; risks, assumptions, and run status. Example row: `Search | 60% from access logs (period stated) | ramp to agreed peak | sampled catalog | measured distribution | Evidence: access-log query`. Do not imply the example's values apply universally.

## Quality Gate
Check workload proportions are coherent and sourced, scenario matches objective, generator capacity and test-data cleanup are addressed, thresholds have an owner/source, instrumentation can measure each criterion, safety limits are explicit, and any script uses the chosen tool's current official syntax. No success claim without captured results.

## Evidence and Uncertainty
Tie claims to requirements, traffic exports, environment inventory, official tool documentation, and raw run reports. State missing baselines and confounders. Score evidence readiness only from four observed checks—scope clarity, claim traceability, contract completeness, and relevant verification—25 points each. Below 75/100, ask, qualify, or abstain; do not invent confidence percentages. Critical safety, authorization, privacy, or acceptance failures block readiness regardless of score.
