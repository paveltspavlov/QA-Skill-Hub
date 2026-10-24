---
name: react-component-generator
description: "Use when creating a React component from a concrete UI contract."
---

## When to Use
Use for a new or changed React component with specified purpose, props and interaction. Follow installed React and project UI libraries; do not choose Tailwind, state libraries, or Storybook by default.

## Required Inputs
Require component purpose, consumers and props/data shape, visual states, interactions/events, responsive/accessibility needs, existing component/design-system conventions, React/build versions, test/story expectations, and file location. Identify controlled/uncontrolled behavior and loading/empty/error states where relevant.

## Procedure
1. Inspect nearby components, tokens, primitives, type and test conventions; verify installed framework/library APIs in official docs where version matters.
2. Define prop contract, ownership of state, event semantics, composition boundaries and visible states. Clarify ambiguous interaction or accessibility requirements.
3. Implement semantic markup using existing primitives; preserve keyboard/focus behavior, labels, status/error announcements and reduced-motion patterns where relevant. Keep derived state derived and avoid speculative abstractions; use compound composition only when the UI contract benefits from coordinated subcomponents.
4. Add tests for primary rendering, interaction, disabled/loading/empty/error and accessibility semantics; add a story only if the project uses stories.
5. Run focused tests, typecheck/lint, and viewport/screenshot validation if available; inspect generated DOM and diff.

## Output Contract
Return: **Component purpose/contract**; **Files changed**; **Props/events**; **States and accessibility behavior**; **Tests/story**; **Verification**. Include code in project style. Example for a data table should specify columns, row identity, sort behavior and empty/loading states before implementing; do not invent keyboard shortcuts.

## Quality Gate
Props are typed and reflect actual consumer data; all states have intentional behavior. Use accessible native semantics and verify the named standard/library details in official version docs. No duplicated design-system components, hard-coded design tokens, or arbitrary keyboard behavior. Tests cover interaction and distinguish automated checks from manual assistive-technology review.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
