---
name: database-schema-designer
description: "Use when translating domain requirements into a relational or document data model."
---

## When to Use
Use for new entities, relationships, constraints, query-oriented indexing, or schema review before migration.

## Required Inputs
Require domain entities and invariants, ownership and tenant boundaries, lifecycle/deletion rules, expected queries and sort/filter patterns, data volume/growth estimates if available, consistency/uniqueness rules, database/ORM/version, and compatibility/migration constraints. Ask about ambiguous cardinality or retention.

## Procedure
1. Extract entities, attributes, optionality, identity, lifecycle, privacy class, and invariants; trace each to supplied requirements.
2. Model relationships and cardinality; resolve many-to-many junctions, ownership, uniqueness scope, nullability, referential actions, and audit needs. Avoid adding conventional timestamps or soft deletes unless required.
3. Map named query patterns to candidate indexes; discuss selectivity/write cost and inspect actual database docs/plans before consequential choices.
4. Produce schema in requested dialect/ORM plus constraints and illustrative seed only if requested. Review destructive data implications and separate model proposal from executable migration.
5. Validate ORM/schema syntax, generate migration diff in a disposable/local context if available, and test constraints/representative queries.

## Output Contract
Return: **Requirements-to-model map**; **Entities and fields** (type, nullable, default only when justified, key/constraint); **Relationships/cardinality**; **Indexes with query rationale**; **Deletion/retention and tenant strategy**; **Schema code**; **Open questions and verification**.

## Quality Gate
Every model element traces to a requirement or a clearly marked design proposal. Constraints enforce important invariants at the correct scope; data type names match the chosen database. Indexes cite workload evidence or are labeled hypotheses. Do not invent scale, seed facts, cascade policy, or compliance retention. Validate against the actual engine/ORM version and flag performance choices needing plans or representative data.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
