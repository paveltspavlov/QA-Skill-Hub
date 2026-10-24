---
name: spark-job-optimizer
description: "Diagnose and tune measured Spark SQL/DataFrame bottlenecks using plans and runtime evidence. Use for slow, skewed, shuffle-heavy, or memory-bound jobs."
---

# Spark Job Optimizer

## When to Use
Use when there is a reproducible performance problem and representative data/metrics. Do not tune by copying a configuration value from another cluster.

## Required Inputs
Spark/runtime version, code/query, input sizes and formats, cluster/executor configuration, query plan, stage/task metrics, baseline runtime, correctness checks, and target SLO/cost constraints.

## Procedure
1. Capture a representative baseline and inspect physical plan, statistics, stages, skew, shuffle, spills, executor memory, and scan volume.
2. Identify the dominant measured bottleneck; separate evidence from likely causes.
3. Propose one bounded change at a time: pruning/partitioning, join strategy, statistics, adaptive execution, skew handling, file sizing, or cache only when repeated reuse justifies memory cost.
4. Validate semantic equivalence, then benchmark repeated runs on equivalent input and configuration; record variance and resource cost.
5. Document rollback and the next bottleneck. Do not promise speedup without measurement.

## Output Contract
Return baseline table (metric/value/source), plan evidence, bottleneck hypothesis, proposed change, expected mechanism, correctness tests, benchmark setup, before/after results or “not measured,” resource/cost trade-offs, and rollback. If code changes are made, list paths and exact commands/results.

## Quality Gate
A recommendation maps to a measured bottleneck. Comparisons use equivalent data and conditions. Correctness is checked independently from runtime. No unmeasured speedup or universal config is claimed.

## Evidence and Uncertainty
Use Spark plans, event logs, metrics, and the installed version's official docs. Context7 may retrieve version-specific docs if available; verify consequential configuration behavior against Spark docs. If there is no baseline, return a diagnostic plan, not a claim of optimization.

## References
- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
