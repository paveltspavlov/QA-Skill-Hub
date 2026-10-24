---
name: test-design
description: "Design traceable functional and non-functional test cases from requirements, interfaces, or risks. Use before implementation, during review, or when coverage is unclear."
---

# Test Design

## Procedure
1. Establish the test basis, scope, assumptions, environment, and requirement/source IDs.
2. Identify test conditions, observable outcomes, data constraints, state, interfaces, and important risks.
3. Select techniques that fit the problem: equivalence partitioning, boundary value analysis, decision tables, state-transition testing, use-case testing, or experience-based exploration. Do not apply every technique mechanically.
4. Include positive, negative, boundary, error, and interaction cases where relevant. Define preconditions, steps, data, expected results, priority/rationale, and traceability.
5. Identify untestable criteria and missing expected behavior; ask clarifying questions rather than inventing an oracle.
6. Review for duplicate cases, ambiguous expected results, and gaps against the stated scope.

## Output
A prioritized, traceable test-case table plus assumptions, questions, and uncovered risks.

## References
- [ISTQB Certified Tester Foundation Level v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
