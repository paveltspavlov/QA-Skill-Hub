---
name: feature-flag-integrator
description: "Wrap a feature in a controlled rollout flag with safe defaults and a removal plan. Use for gradual release, experiments, and emergency disablement."
---

# Feature Flag Integrator

## Procedure
1. Identify the feature boundary, owner, rollout audience, default behavior, and behavior when the flag service is unavailable.
2. Reuse the project's flag provider and naming conventions; define a typed flag and explicit default.
3. Keep evaluations near the feature boundary and avoid inconsistent checks within one user operation.
4. Add tests for on/off/default/provider failure and cohort rules; avoid sensitive targeting data.
5. Record a cleanup trigger/date and remove stale branches after rollout.

## Output
A flag configuration or rollout plan with defaults, tests, owner, and cleanup criteria.
