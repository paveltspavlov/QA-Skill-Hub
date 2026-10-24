---
name: feature-flag-integrator
description: "Add or review a controlled feature flag with safe defaults, rollout, and cleanup. Use for gradual releases, experiments, or emergency disablement."
---

# Feature Flag Integrator

## When to Use
Use when a change needs a runtime on/off control, audience rollout, or kill switch. Do not use a flag to conceal incomplete authorization or replace a required access control.

## Required Inputs
Feature boundary, default behavior, owner, rollout audience, flag provider, environments, outage behavior, success/rollback signals, and cleanup trigger. Do not infer cohort rules or assign a rollout percentage without approval.

## Procedure
1. Inspect the existing flag service, naming, typing, evaluation, and test conventions.
2. Define the flag contract: stable key, purpose, owner, default, target scope, evaluation point, fallback when provider is unavailable, and expiration/cleanup condition.
3. Place evaluation at a coherent feature boundary; avoid inconsistent repeated reads during one operation.
4. Protect sensitive operations with server-side authorization regardless of flag state.
5. Add tests for on, off, default, provider failure, targeting, and cleanup; measure rollout against agreed indicators.

## Output Contract
Provide a flag record with key, owner, feature boundary, default, target conditions, fallback, rollout/rollback signals, test cases, and removal date/trigger. For code changes, list files changed, tests run, and any configuration owners who must act.

## Quality Gate
Default and provider-failure behavior are explicit. Flag state does not grant access. No unapproved user targeting or rollout percentage is invented. The flag has an owner and removal criterion.

## Evidence and Uncertainty
Use repository flag configuration and approved rollout criteria. If the provider or target audience is unknown, return a proposal and ask before adding config. Apply the evidence-readiness-gate.
