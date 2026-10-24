---
name: dbt-model-generator
description: "Create dbt models and tests from verified business definitions. Use for staging, intermediate, or mart models in an existing dbt project."
---

# dbt Model Generator

## When to Use
Use when implementing or revising a dbt model and its documentation/tests. Do not invent business logic, grain, or materialization choices.

## Required Inputs
Inspect dbt version, project conventions, existing sources/refs/macros, model layer, source definition, business rule, output grain, consumers, materialization constraints, and test command. Ask when grain or metric semantics are unclear.

## Procedure
1. Trace the business definition to its approved source and state the model grain before writing SQL.
2. Follow adjacent project patterns for naming, `source`/`ref`, materialization, incremental keys, tests, and documentation; do not import generic naming rules over local conventions.
3. Implement the narrowest SQL transformation. Handle nulls, duplicates, late-arriving updates, timezones, and deletion behavior according to supplied rules.
4. Add schema YAML descriptions, key/relationship/accepted-value tests, and model contracts only when they match the project and stable interface.
5. Run parse/compile and relevant tests; compare row grain and sample results against the business definition. Report what was not executed.

## Output Contract
Deliver: model purpose and grain; source-to-target mapping; SQL or patch; YAML descriptions and tests; materialization/incremental strategy with rationale; assumptions/questions; and verification commands/results. For an analysis-only request, give this as an implementation-ready specification instead of claiming files changed.

## Quality Gate
Every output column has a documented source or expression. Tests map to a business rule or key. The model compiles and tests pass if those commands were run. No hard-coded environment relation or undocumented semantic assumption is introduced.

## Evidence and Uncertainty
Use the project's existing SQL, docs, and dbt metadata as primary evidence. Label unsupported business rules as open questions. Context7 may help retrieve version-specific dbt documentation if configured; verify behavior against dbt's official docs and the installed version. Apply the evidence-readiness-gate.

## References
- [dbt data tests](https://docs.getdbt.com/docs/build/data-tests)
- [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts)
