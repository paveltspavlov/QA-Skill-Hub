---
name: warehouse-cost-analyzer
description: "Analyze warehouse cost drivers from actual query, storage, and compute evidence. Use for cost reviews or optimization proposals."
---

# Warehouse Cost Analyzer

## Procedure
1. Identify platform, billing period, workload, cost units, owners, and available query/billing exports.
2. Rank drivers using measured bytes scanned, runtime, idle capacity, repeated work, storage growth, and refresh frequency.
3. Separate confirmed waste from hypotheses. Estimate changes only with a platform rate and workload baseline.
4. Recommend bounded experiments; define success metrics and guard against lower cost at unacceptable reliability or freshness.
5. Protect query text and user identifiers when sharing reports.

## Output
A ranked cost-driver report with evidence, measurement plan, trade-offs, and next experiment.

## References
- [Spark SQL performance tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
