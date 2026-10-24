---
name: caching-layer-builder
description: "Use when introducing or changing a cache for a measured access pattern."
---

## When to Use
Use for a specific latency/load problem, cache invalidation design, or removal of unsafe/stale caching. Do not add cache because a data type seems cacheable.

## Required Inputs
Require observed bottleneck or goal, data ownership and freshness tolerance, read/write patterns, privacy/tenant boundaries, consistency requirements, cache provider/client/version, key cardinality, failure policy, invalidation events, metrics, and representative workload/test data.

## Procedure
1. Inspect query paths, authorization scope, data mutation points, existing caches, metrics and provider docs. Establish the source of truth and acceptable staleness; if not provided, ask or keep recommendation provisional.
2. Select a cache pattern (e.g., cache-aside) based on write/read behavior; define key schema including tenant/user scope where needed, serialization/versioning, TTL/invalidation, stampede controls, and cache outage behavior.
3. Implement only measured paths; never cache authorization-sensitive responses without an explicit safe partition and policy. Invalidate/update on all relevant writes or document bounded staleness.
4. Add observable hit/miss, eviction/error, and latency signals without logging sensitive values.
5. Test stale-read boundaries, invalidation, key isolation, outage/fallback and concurrent misses; compare against baseline only using actual measurements.

## Output Contract
Return: **Problem/baseline evidence**; **Cache design** (pattern, keys, isolation, TTL/staleness, invalidation); **Changed paths**; **Failure and observability policy**; **Test/benchmark results**. If no baseline exists, state an instrumentation/experiment plan instead of claiming a performance gain.

## Quality Gate
Keys cannot collide across tenants or permissions; source-of-truth writes and invalidations are traced and tested. TTLs and eviction choices are justified by freshness and provider behavior, not arbitrary universal defaults. Cache failure cannot bypass auth or corrupt writes. Validate provider/version semantics in official docs and do not fabricate hit ratios or latency reductions.

## Evidence and Uncertainty
Assess evidence readiness, not probability of correctness. Check: (1) scope and acceptance are clear; (2) material claims trace to supplied requirements, inspected repository evidence, or official documentation for the actual version; (3) every required deliverable field is present and facts, inferences, assumptions, and unknowns are separated; (4) relevant verification ran, or the unverified scope and reason are explicit. Award 25 points only for each evidenced, applicable pass; justify and exclude genuinely inapplicable checks from the denominator. At 75% or higher, deliver with remaining gaps disclosed. Below 75%, ask for missing information, qualify a limited provisional result, or abstain. Critical authorization, security, privacy, data-integrity, or acceptance gaps block readiness regardless of score. Never invent a confidence percentage, source, command, test result, or behavior. Context7 is optional retrieval only; verify consequential claims in official version-matched documentation or the repository. Report only checks actually performed.
