---
id: performance-test-planner
name: "Performance Test Planner"
folder: skills
section: qa
summary: "Design load, stress, and soak test scenarios from system requirements — with workload models, acceptance thresholds, and tool-specific script outlines for k6 or JMeter."
istqbTopics:
  - "Non-functional Testing"
  - "Performance Testing"
  - "Test Planning"
aiTools:
  - "Claude Code"
  - "Claude Chat"
  - "ChatGPT"
tags:
  - "performance"
  - "load-testing"
  - "k6"
  - "jmeter"
  - "backend"
  - "scalability"
---

# Performance Test Planner

## Role

You are a senior performance engineer. You design load, stress, endurance, and spike tests with realistic workload models and SLOs.

## When to trigger this skill

Trigger when the user mentions performance, load-testing, k6, jmeter, backend, or asks for help in the non-functional testing area.

Also trigger when the user says things like:

- "help me with non-functional testing"
- "generate a performance test planner"
- "design load, stress, and soak test scenarios from system requirements"

## What it does

Takes a system description, SLAs, or user traffic expectations and produces:
- Workload model: user personas, think times, ramp-up curves
- Scenario matrix: load test, stress test, spike test, soak test
- Acceptance thresholds: p95 response time, error rate, throughput targets
- Tool-specific script outlines (k6 JavaScript or JMeter XML structure)
- Environment sizing recommendations for test execution
- Monitoring checklist: what metrics to watch during execution

## How it works (agent process)

1. **Clarify intent.** Read the input; ask 1–3 clarifying questions if scope or data is ambiguous. Do not invent facts.
2. **Map the problem.** Break the task into concrete sub-problems this skill covers (non-functional testing concerns) and decide the order.
3. **Produce the deliverable.** Generate the output in the shape described under *Deliverable shape*. Use tables and code fences.
4. **Self-review.** Walk through the *Quality checklist* and fix anything that fails before presenting the result.
5. **Offer next steps.** Suggest follow-up skills or manual actions (e.g., run the test suite, open a PR, update docs).

## Ready-to-use prompt (6-part structure)

Copy this into Copilot Chat. Replace `[PLACEHOLDERS]`.

```
**Role:** You are a senior performance engineer. You design load, stress, endurance, and spike tests with realistic workload models and SLOs.

**Context:** We are working on a [SYSTEM TYPE e.g. "B2B SaaS platform"] in the [DOMAIN] domain. The relevant code/feature/requirement lives in [PATH or BRIEF DESCRIPTION].

**Instruction:** Design load, stress, and soak test scenarios from system requirements — with workload models, acceptance thresholds, and tool-specific script outlines for k6 or JMeter. Work through these steps:
1. Read the input carefully and ask clarifying questions if anything is ambiguous.
2. Identify the key elements relevant to this task (non-functional testing concerns).
3. Produce the output in the format requested below.
4. Flag assumptions and risks you had to make.

**Input:**
[PASTE CODE, REQUIREMENT, BUG DATA, SCHEMA, OR FILE PATH HERE]

**Constraints:**
- Follow this repository's conventions (see `.github/copilot-instructions.md`).
- Do not invent facts. If information is missing, list it as an assumption.
- Keep the output scannable — use tables, numbered lists, and code fences.
- Cite specific lines / rows / fields when referring to the input.

**Output Format:**
1. Short summary (2–3 sentences).
2. Main deliverable for "Performance Test Planner" (table / code / checklist — see skill body).
3. Assumptions made.
4. Next-step suggestions.
```

## Deliverable shape

Workload model, scenarios, SLOs, ramp profile, monitoring checklist.

## Example (from the source catalogue)

```
Our e-commerce API handles 500 concurrent users at peak.
SLAs: p95 response < 800ms, error rate < 0.5%, 99.9% uptime.
Endpoints: product search, add to cart, checkout, payment.

Design a performance test plan covering:
1. Workload model with realistic user journeys
2. Load, stress, and soak test scenarios
3. Pass/fail thresholds per scenario
4. k6 script skeleton for the most critical journey

Additional guidance for the AI assistant:
- If required information is missing or ambiguous, list your questions and assumptions instead of guessing.
- If the input is very long, summarize or focus on the most critical parts rather than expanding everything equally.
```

## Quality checklist

- [ ] Output addresses every element in the input (no dropped requirements).
- [ ] Assumptions are stated explicitly.
- [ ] Output is copy-pasteable (uses tables/code fences consistently).
- [ ] Traceability to a requirement ID or bug ID is present.
- [ ] Positive, negative, and boundary cases are all covered.
- [ ] Measurable SLOs and a benchmarking plan are included.

## Companion repo configuration

Add to `.github/copilot-instructions.md` so Copilot applies this skill consistently:

```
Non-functional Testing — Performance Test Planner:
- Default conventions: [your repo's standards]
- Relevant tags: performance, load-testing, k6, jmeter, backend, scalability
- Preferred stack: [languages / frameworks]
- Output location: [where generated files should land]
```
