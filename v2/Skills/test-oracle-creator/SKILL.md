---
name: test-oracle-creator
description: "Define evidence-based expected results and pass/fail criteria from requirements and business rules. Use when test cases lack a clear oracle."
---

# Test Oracle Creator

## Procedure
1. Read the requirement, business rule, data model, and examples; record source locations.
2. Translate each rule into observable expected outcomes, including state changes, side effects, messages, and tolerances.
3. Cover valid, invalid, boundary, missing, and conflicting inputs where the rule supports them.
4. Separate deterministic expected results from human-judgment criteria; define a rubric for the latter.
5. Flag contradictory or unspecified behavior as a question; do not invent the oracle.

## Output
A table of rule/source → input conditions → expected result → evidence method, plus unresolved questions.

## References
- [ISTQB CTFL v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
