---
name: ci-pipeline-test-advisor
description: "Review a CI pipeline and recommend test stages, gates, parallelization, and failure diagnostics. Use when CI configuration or test feedback is slow or unreliable."
---

# CI Pipeline Test Advisor

## When to Use
Use to review CI workflows, improve test feedback time/reliability, or place checks into pull request, scheduled, and release stages. Do not assume a provider, required gate, runtime budget, or deploy policy.

## Required Inputs
Inspect workflow files, provider and syntax version, triggers, runner types, test commands/durations, dependency/cache setup, artifact retention, permissions/secrets, flake history, branch protection, deployment boundaries, and constraints. Request permission before starting workflows, editing secrets, widening permissions, or deploying.

## Procedure
1. Trace workflow graph and identify which tests run, on what event/branch, with what dependencies and outputs. Preserve current security boundaries and least privilege.
2. Map tests by feedback value and dependencies: lint/unit early; integration/system later when infrastructure is ready; expensive or broad suites scheduled/release-only if risk policy permits. Avoid a rigid universal order.
3. Identify measured bottlenecks from job timings, queue time, cache hit data, and flaky reruns. Recommend targeted caching/sharding/parallelism only when workload supports it; parallelism may increase cost or contention.
4. Define failure policy for each class: required/blocking, advisory, scheduled, or quarantined with owner/expiry/issue and continued observability. Never hide or silently retry away a real failure.
5. Improve diagnostics: preserve test reports, logs, traces, and build metadata with appropriate retention and redaction. Check concurrency cancellation doesn't terminate required release work.
6. Validate provider-specific syntax and permissions using the repository's current official docs; propose minimal diff. Run local lint/validation if available, and report commands/results; do not claim workflow execution unless actually triggered.

## Output Contract
Return stage table `Stage | Trigger | Tests | Dependencies | Gate status | Artifact | Owner`; recommendations table `Priority | Evidence | Change | Expected effect | Risk/trade-off | Validation`; plus smallest workflow diff if requested, validation, and deferred items. Example: `PR | pull_request | unit + contract | build | required per policy | junit report | team owner`—policy must be supplied, not assumed.

## Quality Gate
Every suggested gate maps to release intent; proposed time gains are derived from measured timings or marked unestimated; flaky handling is temporary, visible, and owned; permissions/secrets do not widen casually; modified syntax matches actual CI provider; commands and execution status are exact.

## Evidence and Uncertainty
Cite workflow paths/lines, actual run summaries, timing data, branch policy, and authoritative provider docs. Apply four evidence checks—clear scope, traceable claims, complete contract, relevant verification—25 points each. Below 75/100, ask, qualify, or abstain; do not guess confidence percentages. Critical authorization, privacy, safety, or acceptance failures cannot be averaged away.
