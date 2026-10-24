---
name: bug-triage
description: "Turn defect reports into reproducible, evidence-based issues with clear impact and urgency. Use for incident reports, user complaints, and test failures."
---

# Bug Triage

## When to Use
Use when converting a user complaint, incident, test failure, or defect report into a trackable issue; when prioritizing bugs; or when assessing whether a reported problem is reproducible. Keep operational incident response distinct from issue classification.

## Required Inputs
Preserve the original report. Gather product/build, environment/browser/device, account/role (avoid personal identifiers), preconditions, test data, steps, actual and expected behavior with source, frequency, timestamps/timezone, logs/screenshots/request IDs, affected workflow/users, and workaround. Ask only questions likely to change reproduction or impact assessment.

## Procedure
1. Quote or link original wording and separate observed facts, user expectation, and inference. Do not fill missing expected behavior from intuition; seek requirements or ask the reporter.
2. Create the smallest safe reproduction with exact setup and steps. Preserve nondeterminism evidence; record whether independently reproduced, not reproduced, or not attempted.
3. Assess impact: affected users/roles, workflow criticality, scope, data integrity/confidentiality, availability, and workaround. Separate severity (impact) from priority (urgency/order).
4. Use team severity/priority definitions. If unavailable, give provisional labels with explicit rationale and request the team's scale; never invent a numeric score. Flag security/privacy/production-impacting reports for the designated response path.
5. Search duplicates or linked defects only with authorized tracker access; cite the record checked. Keep root-cause hypotheses separate from confirmed cause.
6. Write regression coverage and unresolved questions. Avoid attaching secrets, credentials, or unnecessary personal data.

## Output Contract
Return `Title`, `Status (New/Reproduced/Not Reproduced/Needs Information)`, `Environment`, `Preconditions`, numbered `Reproduction Steps`, `Actual`, `Expected + source`, `Evidence`, `Impact`, `Severity`, `Priority`, `Workaround`, `Related issues checked`, `Root-cause hypothesis (unconfirmed)`, `Regression test`, and `Open questions`. Sample: `Expected: save confirmation per AC-7; actual: spinner remains (screen capture at timestamp); reproduced twice in staging; priority provisional pending team scale.`

## Quality Gate
Steps are executable by another person; expectation is traceable or explicitly unknown; impact and urgency aren't conflated; evidence and reproduction status are accurate; proposed severity follows team policy; duplicate claims cite a real lookup; sensitive data is removed.

## Evidence and Uncertainty
Use original report, source requirements, reproduction logs, and authorized tracker results. Separate verified facts, hypotheses, and unknowns. Apply four readiness checks—scope clear, claims traceable, contract complete, verification done or explicitly unavailable—25 points each. Below 75/100, ask, qualify, or abstain; never give guessed confidence percentages. Critical safety, privacy, authorization, or acceptance failures block readiness regardless of score.
