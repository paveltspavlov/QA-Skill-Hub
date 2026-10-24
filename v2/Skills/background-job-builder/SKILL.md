---
name: background-job-builder
description: "Design background jobs with safe retries, idempotency, observability, and recovery. Use for asynchronous work such as exports, notifications, or data processing."
---

# Background Job Builder

## Procedure
1. Define trigger, input, completion condition, time budget, data ownership, and user-visible status.
2. Inspect the queue/worker framework already used. Specify idempotency key, retryable versus permanent errors, bounded backoff, timeout, and dead-letter/replay behavior.
3. Make progress and failure observable without logging secrets or unnecessary personal data.
4. Plan duplicate delivery, worker restart, partial completion, cancellation, and deployment compatibility.
5. Add tests for retry, idempotency, failure recovery, and cleanup; avoid launching live jobs without authorization.

## Output
A job contract, worker implementation or plan, operational signals, and recovery tests.
