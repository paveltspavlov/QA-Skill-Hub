---
name: accessibility-review
description: "Review web and app interfaces against applicable accessibility criteria and propose testable fixes. Use for UI changes, accessibility audits, and release checks."
---

# Accessibility Review

## Procedure
1. Identify the interface, user flows, technologies, target conformance level, and any applicable policy. Do not assume a legal target.
2. Inspect semantic structure, names/roles/values, keyboard operation, focus order/visibility, labels, errors, contrast, zoom/reflow, target size, motion, and assistive-technology behavior as relevant.
3. Map findings to WCAG 2.2 success criteria only when the evidence supports the mapping. Include level, affected users, exact location, impact, and a reproducible check.
4. Use automated tools for repeatable checks, but supplement them with keyboard and human review; an automated scan alone cannot establish conformance.
5. Suggest a minimal fix and a regression check. Distinguish verified issues, potential barriers, and items not tested.

## Output
Prioritized findings with criterion references, evidence, remediation, retest steps, and untested scope.

## References
- [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
