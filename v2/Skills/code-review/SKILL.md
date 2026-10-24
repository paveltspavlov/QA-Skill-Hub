---
name: code-review
description: "Review a change for correctness, security, maintainability, and test gaps using the stated requirements and project conventions. Use before accepting or merging a change."
---

# Code Review

## When to Use
Use before accepting/merging a change, during requested review of a patch, or to audit a specific implementation against stated behavior. Review the intended diff against its base; do not silently expand into an unbounded codebase audit.

## Required Inputs
Obtain diff/commit range and base, changed files with surrounding context, applicable requirements/API contracts, project conventions, runtime and framework versions as available, and requested review focus. Ask for missing baseline or specification if it changes correctness conclusions. Do not execute untrusted code.

## Procedure
1. Read the full diff and relevant callers/callees/tests/config/migrations. Confirm actual changed lines before assigning locations.
2. Review separate passes: correctness/state/edge conditions; security/trust boundaries/auth/data exposure; failure handling/concurrency; performance/resource use; compatibility/migrations; tests and operational completeness.
3. Trace each suspected issue to an execution path and state the concrete user/system impact. Report only actionable defects or risks; don't elevate style preferences. Map security references to authoritative standards only when relevant and precise.
4. Use severities `Blocker`, `High`, `Medium`, `Low`, `Info` only with an explained rubric: release-blocking consequence through non-blocking observation. If evidence is insufficient, ask or label as a question rather than invent a vulnerability.
5. Provide minimal fix direction; do not edit or auto-fix unless asked. After a fix, review the new diff and verify the specific regression test if authorized.

## Output Contract
Findings first, ordered by severity, each with `ID | Severity | File:line | Evidence | Impact | Suggested fix | Regression check`. Then `Reviewed scope`, `Checks actually run`, `Unreviewed areas`, `Questions`, and `Non-blocking notes`. If no findings, say “No actionable findings in reviewed scope” and list scope/limits. Sample: `R-1 | High | auth.ts:88 | branch skips role check for export path | user without export role can reach handler per call flow | apply same policy guard | test denied role`—only report after tracing that branch.

## Quality Gate
Each finding points to a real changed line or necessary context and a supported impact; no speculative assertion is phrased as fact; tests and modified areas are considered; severity is consistent; no formatting nits masquerade as defects. Do not alter files or perform live/destructive testing without explicit request and authorization.

## Evidence and Uncertainty
Use diff, code paths, tests, requirements, and actual command output; cite file/line or symbols. Score readiness via clear scope, traceable material claims, complete output, and relevant verification (25 points each). Below 75/100, ask, qualify, or abstain; no guessed confidence percentages. Critical security, privacy, authorization, or acceptance failures block readiness regardless of score.
