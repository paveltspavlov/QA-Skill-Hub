---
name: react-component-generator
description: "Create or update a React component using the project's React version, design system, and accessibility conventions. Use for React UI components and interactions."
---

# React Component Generator

## Procedure
1. Inspect nearby components, React version, styling system, state conventions, and tests.
2. Clarify inputs, states, interactions, empty/loading/error behavior, and responsive requirements.
3. Use local state for local UI state and shared state only where the project requires it. Use Effects to synchronize with external systems, not for ordinary derived data flow.
4. Preserve semantic HTML, accessible names, keyboard behavior, and design tokens.
5. Add focused tests for observable behavior; run the project's checks. Do not add dependencies without approval.

## Output
A component and tests in existing project style, with behavior and accessibility notes.

## References
- [React Hooks](https://react.dev/reference/react/hooks)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
