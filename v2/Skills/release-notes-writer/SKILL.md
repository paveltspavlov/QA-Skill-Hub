---
name: release-notes-writer
description: "Use when producing release notes from a verified tag or change range."
---

## When to Use
Use for a release announcement, changelog entry, or user-facing summary after the relevant commits/merged PRs are known. Do not invent release contents, dates, versions, or upgrade instructions.

## Required Inputs
Require exact previous/current tag or commit range, product/audience, release version/date only if set, changelog format, merged PR/issues source, known migration/security notes, and whether unreleased/hidden work is excluded.

## Procedure
1. Resolve the precise change range and verify merged commits/PRs; exclude unrelated, reverted, draft, and unreleased work according to policy.
2. Group changes by user impact (Added, Changed, Fixed, Security, Deprecated/Removed, Migration) only where applicable; translate implementation detail for audience without changing claims.
3. Mark breaking changes and required actions from evidence, including migration order or data/config changes. Keep internal fixes separate if release format demands.
4. Link issue/PR identifiers only when verifiable; do not expose sensitive details.
5. Cross-check note list against range and repository changelog; confirm version/date and run any release-note lint/check.

## Output Contract
Return fields: **Version/date** (verified or TBD); **Compared range**; **Highlights**; **Added/Changed/Fixed**; **Breaking/deprecation**; **Security** (only verified and disclosed safely); **Upgrade actions**; **Credits/links** if supported. Worked example: `1.4.0 — Added CSV export; Fixed timezone display; Upgrade: run migration X` only when each item is confirmed in the release range and migration docs.

## Quality Gate
Every bullet maps to a merged change in the exact range; omit or qualify ambiguous commits. Do not promise availability, compatibility, security remediation, or data migration without evidence. Do not convert commit subjects into end-user claims without checking behavior. State omissions (e.g., range unavailable) and use “TBD” for unset version/date.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
