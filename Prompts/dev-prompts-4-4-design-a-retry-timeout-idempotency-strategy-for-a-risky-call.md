---
id: dev-prompts-4-4-design-a-retry-timeout-idempotency-strategy-for-a-risky-call
name: "4.4 - Design a Retry / Timeout / Idempotency Strategy for a Risky Call"
folder: prompts
section: dev-prompts
summary: "API & Architecture Design"
tags:
  - "dev-prompts"
  - "api & architecture design"
---

# Prompt 4.4 - Design a Retry / Timeout / Idempotency Strategy for a Risky Call

> Category: **API & Architecture Design**

When to use  When integrating with an external API and need an explicit resilience plan rather than a vibe.

Expected output  A resilience spec: timeouts, retry policy, idempotency keys, circuit-breaker behaviour, and what failure looks like to the user.

Prompt

```
**Role:** You are an integration engineer who has been burned enough times to design resilience before the first call goes out.

**Context:** The external system is [SYSTEM]. Its published SLA is [SLA]. The call is [READ / WRITE] and happens on [HOT / COLD PATH]. The user-facing impact of a failure is [DESCRIBE].

**Instruction:** Design the resilience strategy for this integration.

1. Pick a timeout (connect and total) based on the SLA plus a safety factor - name the numbers.

2. Decide whether retries are safe (is the call idempotent? can we make it idempotent with a key?).

3. If retries are safe, define the backoff (base, factor, max attempts, jitter).

4. Define a circuit-breaker threshold so we stop hammering a dead dependency.

5. Define user-facing behaviour on exhaustion (fail, degrade, queue).

**Input:**

Call description:

[METHOD, ENDPOINT, PAYLOAD SHAPE]

Idempotency mechanism available (if any):

[DESCRIBE OR "NONE"]

**Constraints:**

- Do not retry writes that aren't idempotent - ever.

- Timeouts must be finite. No "default to infinity".

- Name actual numbers, not "configurable".

**Output Format:**

- Timeouts: connect / total

- Idempotency plan

- Retry policy: attempts / base / factor / jitter / max delay

- Circuit breaker: window / threshold / cooldown

- Failure UX
```
