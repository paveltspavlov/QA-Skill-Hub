---
name: database-migration-generator
description: "Use when generating an executable database schema or data migration."
---

## When to Use
Use to produce a migration for a named database/ORM and existing schema. Do not use for a conceptual model alone; use database-schema-designer first when requirements/cardinality are unresolved.

## Required Inputs
Require engine/version, ORM/migration framework/version, current schema and migration conventions, desired before/after state, existing row/volume characteristics if known, constraints, downtime/lock budget, deployment order, rollback/data retention policy, and test database command. Never assume a migration can reverse data loss.

## Procedure
1. Inspect current schema, migration history, connection/config conventions, deployment ordering and installed tool docs. Confirm target engine/version and existing data semantics.
2. Translate desired state into ordered operations; assess locks, table rewrites, backfill size, uniqueness violations, nullability, defaults, foreign keys and mixed-version application compatibility.
3. Prefer expand/backfill/contract for incompatible or large changes: introduce compatible nullable shape, deploy compatible code, backfill in bounded/restartable batches if required, validate, then enforce constraint/remove old shape in a later safe phase. Use this only if architecture supports phased rollout.
4. Generate migration in project format; include explicit transaction/lock behavior supported by engine. Define down migration only when data can be restored safely; otherwise state irreversible and propose recovery.
5. Run migration lint/dry-run and apply/rollback on disposable test DB using representative schema/data; verify postconditions, no unintended data changes, and app compatibility.

## Output Contract
Return: **Engine/tool/version**; **Before/after schema**; **Migration file(s)**; **Deployment order/compatibility**; **Data/locking risk**; **Rollback or irreversibility and recovery**; **Pre/postflight queries/checks**; **Actual test execution/results**. Worked example: adding a required `timezone` to existing users may need nullable add → application default/explicit backfill → null audit → constraint in a later migration; use only if verified business default and deployment model support it.

## Quality Gate
No destructive SQL or irreversible transformation without explicit requirement and confirmed backup/recovery path. Backfills are idempotent/restartable when possible and sized from evidence; generated SQL matches installed engine syntax. Tests run against the intended engine, not just string snapshots, where available. Never claim zero downtime or safe rollback without a demonstrated deployment/data analysis.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
