---
name: dbt-model-generator
description: "Create or update dbt models from documented business definitions and project conventions. Use for staging, intermediate, or mart models and their tests."
---

# dbt Model Generator

## Procedure
1. Inspect dbt version, model layers, materializations, naming conventions, sources, and existing macros.
2. Translate the business definition into grain, dimensions, measures, filters, joins, and null/late-arriving behavior. Ask where semantics are unclear.
3. Build SQL using project conventions and explicit `ref`/`source` dependencies; avoid environment-specific relation names.
4. Add model/column descriptions, data tests, and a contract only where the model is a stable interface and the project supports it.
5. Run parsing/compilation and relevant tests; compare output grain and representative results to the definition.

## Output
Model SQL/YAML, lineage dependencies, tests, and business-rule questions.

## References
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests)
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
