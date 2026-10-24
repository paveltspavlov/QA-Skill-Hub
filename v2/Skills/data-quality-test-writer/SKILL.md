---
name: data-quality-test-writer
description: "Create reusable data-quality assertions for tables and pipelines. Use when validating freshness, uniqueness, completeness, relationships, distributions, or business rules."
---

# Data Quality Test Writer

## Procedure
1. Identify the data asset, owner, business meaning, grain, expected volume/freshness, and downstream use.
2. Translate each rule into a query/assertion that returns failing records or an interpretable metric.
3. Cover nulls, uniqueness, accepted values, relationships, freshness, volume, and business-specific anomalies as justified by risk.
4. Use project-native test conventions. Ensure failures show debugging context without exposing sensitive data.
5. Run against representative test data; document thresholds and distinguish anomalies from hard constraints.

## Output
A data-quality test suite or matrix with rule, scope, threshold, failure evidence, and owner.

## References
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests)
