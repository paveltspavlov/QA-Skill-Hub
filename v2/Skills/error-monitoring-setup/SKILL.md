---
name: error-monitoring-setup
description: "Improve error handling and monitoring without leaking sensitive data. Use when production failures lack actionable diagnostics or consistent recovery."
---

# Error Monitoring Setup

## When to Use
Use to design or improve application error handling, telemetry, alerting, and recovery for services, APIs, background jobs, or user interfaces. Do not assume the monitoring vendor, baseline, alert threshold, or incident process.

## Required Inputs
Inspect system architecture and error paths, runtime/framework/provider and versions, existing logs/metrics/traces, incident examples, service objectives and traffic baseline, ownership/on-call routing, privacy/data classification, retention, and alert response expectations. Obtain authorization before production config changes or emitting test events.

## Procedure
1. Map error origin → handling layer → client/queue/system outcome. Classify expected user errors, dependency failures, internal faults, and cancellation separately; define safe recovery semantics from product contract.
2. Select structured fields useful for grouping/correlation: event name, service/version/environment, operation, error class, correlation/request ID, dependency, outcome, and timestamp. Add context only when justified; redact credentials, tokens, personal data, request bodies, and sensitive SQL.
3. Choose logs, metrics, traces, or events according to diagnostic question. Preserve causal chain without duplicating stack traces at every layer. Ensure user-facing messages reveal no internal secrets.
4. Define alerts tied to actionable symptoms, baseline/volume, owner, severity, deduplication, and runbook. Derive thresholds from supplied SLO/history and response capacity; otherwise mark as proposed for owner review, not configured truth.
5. Document retry, timeout, fallback, dead-letter/replay, and escalation behavior where relevant. Retries require transient classification and safe idempotency.
6. Validate with controlled injected failures: event produced, correlation intact, redaction verified, user response/fallback correct, alert routed, and recovery observed. Avoid testing destructive production paths.

## Output Contract
Return `Monitoring design` and table `Failure class | User/system behavior | Event/metric | Required fields | Redactions | Alert condition/source | Owner/runbook | Validation`. Include config/code only when provider/version known; list actual redaction/alert tests and unconfigured assumptions. Example: `dependency timeout | bounded fallback per contract | dependency_failure counter + correlated error event | service, operation, request ID, class | omit auth header/body | alert after agreed error budget condition | service owner | inject timeout in staging`.

## Quality Gate
Every signal answers an operational question; no sensitive fields are logged; alert conditions have a source and responder; messages preserve useful context without leaking internals; recovery behavior is contract-consistent; test claims match actual runs. Use current official provider docs for provider-specific syntax.

## Evidence and Uncertainty
Base changes on code, incident traces, data policy, SLOs, and measured baselines. Distinguish a proposed alert from deployed configuration. Apply four evidence checks—scope clarity, claim traceability, output completeness, relevant verification—25 points each; below 75/100, ask, qualify, or abstain. Never guess confidence percentages. Critical privacy, authorization, safety, or acceptance failures cannot be averaged away.
