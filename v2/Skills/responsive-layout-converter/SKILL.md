---
name: responsive-layout-converter
description: "Use when adapting an existing interface to a wider range of viewports."
---

## When to Use
Use for a desktop-only page/component, overflow issue, or responsive UI audit. Preserve content, task order, branding and interaction unless a redesign is requested.

## Required Inputs
Require target component/page, supported viewport range/devices, design tokens and CSS framework, content priorities, navigation behavior, browser support, accessibility requirements, and visual references. Inspect current layout and avoid assuming fixed breakpoint names/values.

## Procedure
1. Inspect markup, layout rules, assets, design tokens, interaction states and existing responsive conventions.
2. Test or reason from actual content at narrow and wide sizes; identify clipping, overflow, unreadable density, reordered actions, hidden controls and horizontal scrolling.
3. Choose fluid constraints and content-driven breakpoints, adapt grids/nav/tables/forms, and preserve logical DOM and keyboard order. Avoid hiding critical actions solely for space.
4. Check zoom/reflow, text scaling, focus, touch/target requirements against the project’s applicable accessibility standard; verify thresholds in official docs rather than copying universal numbers.
5. Validate representative viewport sizes and interactions in browser/device tooling if available; run visual/a11y tests and report unsupported combinations.

## Output Contract
Return: **Page/component and viewport scope**; **Breakage map**; **Breakpoint/layout decisions**; **Code changes**; **Accessibility/content-order checks**; **Viewport and test evidence**; **Unverified cases**. Include exact viewport dimensions only when tested.

## Quality Gate
Content remains available and usable without overlap, unintended clipping, or loss of task-critical function. Breakpoints fit observed content rather than presumed devices. DOM order and focus order remain logical; target-size and reflow claims cite the actual standard/version if stated. Distinguish browser-observed results from code review; do not claim full device coverage from a small sample.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
