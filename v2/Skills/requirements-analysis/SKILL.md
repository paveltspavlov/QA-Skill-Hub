---
name: requirements-analysis
description: "Extract testable outcomes, rules, constraints, ambiguities, and traceability from requirements. Use for user stories, specifications, change requests, and acceptance criteria."
---

# Requirements Analysis

## Procedure
1. Identify the source and preserve its terminology, IDs, and version. Separate explicit requirements from inferred context.
2. Extract actors, goals, preconditions, business rules, inputs, outputs, constraints, error behavior, and acceptance criteria.
3. Rewrite each criterion so it is observable and testable without changing intent. Map every criterion to its source location.
4. Find ambiguity, contradiction, missing boundary/error cases, dependencies, and non-functional requirements. Ask only questions whose answers change implementation or test outcomes.
5. Produce a traceability table: source ID/location → requirement/criterion → open question or risk → suggested verification.
6. Mark assumptions and unresolved decisions; never invent behavior to fill a gap.

## Output
A concise requirement summary, testable criteria, traceability, material ambiguities, and prioritized clarifying questions.

## Quality checks
- Each criterion has observable evidence or is explicitly marked untestable.
- Preserve source IDs and distinguish missing information from defects.
- Do not claim full coverage unless every supplied requirement is mapped.

## References
- [ISTQB CTFL v4.0](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/)
