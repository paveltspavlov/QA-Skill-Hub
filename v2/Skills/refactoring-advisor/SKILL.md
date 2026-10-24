---
name: refactoring-advisor
description: "Plan behavior-preserving refactoring for complex or duplicated code. Use when maintainability is the goal and functional change is not requested."
---

# Refactoring Advisor

## Procedure
1. Identify the target, current behavior, callers, dependencies, and tests.
2. Describe the design smell using concrete evidence; avoid aesthetic-only claims.
3. Propose small refactor steps that preserve observable behavior and keep the system testable after each step.
4. Identify characterization or regression tests needed before changing structure.
5. Separate safe refactoring from feature work, broad rewrites, or dependency migrations; ask before expanding scope.

## Output
A prioritized plan with code locations, behavior-preservation checks, and risks; make edits only when requested.
