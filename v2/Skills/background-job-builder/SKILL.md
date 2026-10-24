---
name: background-job-builder
description: "Use when adding durable asynchronous jobs, queues, workers, or scheduled tasks."
---

## When to Use
Use when work must execute outside a request or be retried, scheduled, or processed in parallel. Choose existing infrastructure rather than assuming BullMQ, Celery, Redis, or a scheduler.

## Required Inputs
Require job purpose and trigger, payload/source of truth, ordering and delivery expectations, idempotency key, retryable/permanent errors, concurrency limits/throughput evidence, timeout/cancellation behavior, data retention, queue/worker framework and version, observability, and deploy/shutdown model.

## Procedure
1. Inspect existing queue, producer, worker, schema, deployment and test patterns; confirm framework capabilities in official versioned docs.
2. Define payload schema and lifecycle (enqueue, start, progress reporting if consumers need it, success/failure, retry, dead-letter/manual replay, cancellation). Decide idempotency and duplicate-delivery handling; assume at-least-once only when verified for this system.
3. Implement producer and worker with bounded resource use, explicit retry classification/backoff from requirements, safe logging, graceful shutdown, and transaction/outbox coordination if the business action demands atomic enqueue.
4. Expose worker health/metrics only through established observability conventions.
5. Test malformed payloads, duplicate jobs, transient/permanent failures, retry exhaustion, shutdown, and replay; run worker tests and applicable checks.

## Output Contract
Return: **Job contract** (name, trigger, payload, idempotency, outcomes); **Queue/worker flow**; **Retry and failure policy**; **Files/config/deploy changes**; **Operational signals/replay procedure**; **Verification**. Short example: “send invoice email” stores invoice ID, reloads authoritative invoice at execution, uses a stable delivery key, retries only transient provider failures, and records terminal failure—if that matches the system contract.

## Quality Gate
A duplicate or retry cannot silently repeat unsafe effects; permanent errors do not loop indefinitely. Concurrency, retry counts, delays, and retention are requirements/evidence-driven—not copied arbitrary defaults. Shutdown and poison-message behavior are explicit. Do not claim delivery guarantees, exactly-once semantics, or latency without verified implementation evidence.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
