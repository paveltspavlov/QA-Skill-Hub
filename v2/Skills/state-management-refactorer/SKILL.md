---
name: state-management-refactorer
description: "Restructure tangled UI state without changing behavior. Use when state ownership, duplicated values, or prop flow makes a component difficult to maintain."
---

# State Management Refactorer

## Procedure
1. Trace state owners, update paths, derived values, side effects, and consumers.
2. Separate local interaction state from shared domain state and derived data.
3. Remove duplicate sources of truth; keep synchronization with external systems explicit.
4. For React projects, follow the installed version and avoid Effects for ordinary state derivation.
5. Add behavior tests before or during refactoring; preserve loading/error states and user-visible flows.

## Output
A small refactor plan or change with state-flow rationale and regression evidence.

## References
- [React Hooks](https://react.dev/reference/react/hooks)
