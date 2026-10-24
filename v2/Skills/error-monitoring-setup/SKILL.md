---
name: error-monitoring-setup
description: "Improve error handling and monitoring without leaking sensitive data. Use when production failures lack actionable diagnostics or consistent recovery."
---

# Error Monitoring Setup

## Procedure
1. Inspect existing logging, error boundaries/middleware, monitoring provider, alert routing, and data classification.
2. Define error categories, user-safe messages, retry/recovery behavior, and the context needed to diagnose failures.
3. Add structured, correlated events while redacting credentials, tokens, personal data, and sensitive request bodies.
4. Set alerts against actionable symptoms and documented thresholds; avoid noisy alerts or guessed baselines.
5. Test error paths, fallback behavior, and redaction; document ownership and incident response links.

## Output
A monitoring change or plan with event fields, redaction, alert criteria, and validation evidence.
