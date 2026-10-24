---
name: accessibility-review
description: "Review web and app interfaces against applicable accessibility criteria and propose testable fixes. Use for UI changes, accessibility audits, and release checks."
---

# Accessibility Review

## When to Use
Use for UI components, page flows, design changes, accessibility bug reports, and release audits. Confirm the required standard/version and conformance level from the user or policy; never assume a legal target. Review web interfaces against WCAG only when applicable and supported by observed evidence.

## Required Inputs
Request URLs or code/build, target platforms and browsers, affected flows, expected user groups, target standard/version/level, policy and scope, available assistive technology, and permission for live inspection. For a visual-only artifact, state that DOM and runtime behavior could not be verified.

## Procedure
1. Define pages, states, interactions, and user flows. Inspect semantic roles/names/values, headings/landmarks, labels, instructions, validation/error feedback, keyboard access, focus order/visibility, dialogs, dynamic updates, contrast, zoom/reflow, motion, and target size as relevant.
2. Test with keyboard alone and, where possible, representative screen-reader/browser combinations. Record exact element, state, key sequence or AT output, and expected basis.
3. Use automated checks as a discovery aid for machine-detectable issues. A clean scan does not establish accessibility or WCAG conformance; human review remains necessary.
4. Map a finding to a WCAG 2.2 criterion and level only when the actual failure and criterion match. If uncertain, label “potential barrier—criterion unconfirmed.” Avoid legal conclusions.
5. Recommend the smallest semantic or interaction fix and a reproducible retest, including positive and error-state checks. Track fixed, not retested, and out-of-scope separately.

## Output Contract
Return summary plus table `ID | Status (Confirmed/Potential/Not Tested) | Page/state/element | User impact | Evidence/reproduction | WCAG criterion + level (or unconfirmed) | Fix | Retest`. Add `Coverage` with flows, browser/AT combinations, methods, and exclusions; list automation tool and actual version/output only if run. Sample row: `A11Y-1 | Confirmed | dialog after Save | keyboard user cannot reach Close | Tab sequence stops before dialog controls | 2.1.1 A, if verified against criterion | include reachable controls and manage focus | repeat keyboard sequence`.

## Quality Gate
Every confirmed finding has reproducible evidence and a defensible criterion mapping; user-impact and severity rationale are explicit; no automated-only conformance claim; tested and untested scope are distinct; fixes include retest steps. Use W3C's current WCAG text/Quick Reference for consequential criterion interpretation.

## Evidence and Uncertainty
Record build/page, browser/AT, steps, screenshots/DOM or tool output, and source criterion. Apply evidence readiness with four supported checks—clear scope, traceable claims, complete output, relevant verification—25 points each. Below 75/100, ask, qualify, or abstain; do not guess confidence percentages. Critical safety, authorization, privacy, or acceptance failures block readiness regardless of score.
