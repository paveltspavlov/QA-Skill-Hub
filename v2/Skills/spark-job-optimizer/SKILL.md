---
name: spark-job-optimizer
description: "Diagnose and tune Spark SQL or DataFrame workloads using actual plans and runtime evidence. Use when job time, shuffle, skew, or memory use is a measured problem."
---

# Spark Job Optimizer

## Procedure
1. Inspect Spark version, workload, input sizes, cluster/resource settings, query plan, stage metrics, and representative run data.
2. Locate the bottleneck with evidence: skew, shuffle, partition sizing, join strategy, serialization, unnecessary scans, memory pressure, or stale statistics.
3. Change one factor at a time. Consider partitioning, statistics, join strategy, adaptive execution, and caching only when reuse justifies memory cost.
4. Validate correctness and compare repeated runs under equivalent data and cluster conditions. Do not copy config values blindly.
5. Report the measured effect, resource trade-offs, and remaining bottleneck.

## Output
A prioritized tuning plan or patch with plan/metric evidence and regression checks.

## References
- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
