---
name: responsive-layout-converter
description: "Adapt an existing interface for responsive layouts while preserving content, function, and accessibility. Use when a desktop-only page or component must support smaller viewports."
---

# Responsive Layout Converter

## Procedure
1. Inspect layout rules, design tokens, component structure, and supported viewport range.
2. Identify content that overflows, becomes unreadable, or changes task order at narrower sizes.
3. Propose fluid sizing and breakpoints based on content needs rather than device names alone.
4. Preserve keyboard access, visible focus, semantic order, readable text, and sufficiently large interaction targets.
5. Test representative viewports, zoom/reflow, and interactions; report untested combinations.

## Output
Responsive changes or a breakpoint plan with visual and accessibility regression checks.

## References
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
