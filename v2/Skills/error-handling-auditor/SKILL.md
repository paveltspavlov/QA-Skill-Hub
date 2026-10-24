---
name: error-handling-auditor
description: "Audit code paths for unhandled, swallowed, or unsafe failures. Use when reviewing error propagation, retries, recovery, and negative tests."
---

# Error Handling Auditor

## When to Use
Use for code review or test design focused on exception paths, rejected promises, error translation, retry behavior, user-safe responses, and recovery. Do not prescribe blanket retries or treat every catch block as a defect.

## Required Inputs
Ask for the relevant code and call path, language/framework/runtime version, error contract, dependency behavior, retry/idempotency guarantees, user-facing requirements, logging/redaction policy, and desired audit scope. Include tests and surrounding callers when available; absent upstream context limits conclusions.

## Procedure
1. Trace failures from source through each handler to observable response/state. Mark where errors are propagated, translated, retried, logged, suppressed, or converted to fallback.
2. Inspect unhandled exceptions/rejections, empty or log-only catches, overly broad catches, lost causes/context, unsafe detail exposure, inconsistent API shapes, missing cancellation/timeouts, and frontend boundaries where relevant.
3. For each external operation, verify whether retry is safe: transient condition, bounded attempts/backoff defined by policy, idempotency or deduplication, timeout, and cancellation. Do not invent values or recommend retry for non-idempotent work without safeguards.
4. Derive negative tests from code and stated contracts: dependency unavailable, malformed response, timeout, permission denial, cancellation, partial success, and exhausted recovery as applicable.
5. Rank findings by demonstrated impact and reach, not code style. Recommend a minimal fix and a regression assertion; identify operational metrics or alerts only when useful.

## Output Contract
Use findings table `ID | Location | Triggering failure | Current behavior (evidence) | Impact | Severity | Recommended change | Regression test`. Severity values: `Critical`, `High`, `Medium`, `Low`, `Unverified`; explain rubric and mark uncertain items Unverified. Include reviewed paths, excluded paths, and tests actually run. Sample: `EH-1 | handler.ts:42 | repository rejects | catch returns success-shaped empty list (line evidence) | caller cannot distinguish outage | High | preserve failure contract and add safe fallback if specified | assert error response on repository rejection`.

## Quality Gate
Verify every claim against the control flow or reproducible behavior, distinguish intentional fallback from swallowing, ensure error messages do not expose secrets/PII, test both failure and recovery behavior, and avoid duplicate findings for one root defect. Do not edit code unless asked.

## Evidence and Uncertainty
Use source locations, contract text, tests, logs, and observed output; do not claim a runtime fault from static suspicion alone. Apply evidence readiness as four checks—scope clear, claims traceable, deliverable complete, verification performed or transparently unavailable—25 points each. Below 75/100, ask, qualify, or abstain; never guess a confidence percentage. A critical authorization, privacy, safety, or acceptance failure blocks readiness regardless of score.
