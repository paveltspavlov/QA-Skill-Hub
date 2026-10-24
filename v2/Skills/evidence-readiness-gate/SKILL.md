---
name: evidence-readiness-gate
description: "Check evidence, completeness, and verification before finalizing consequential work. Use for factual, technical, QA, and repository deliverables."
---

# Evidence Readiness Gate

Use this cross-cutting procedure before presenting a factual, technical, QA, or repository deliverable as ready. This gate measures evidence readiness, not the probability that an answer is correct.

## When to Use
Use before finalizing consequential analyses, recommendations, test plans, documentation, code changes, reviews, or any answer that may be relied on. Skip numeric scoring for casual or purely creative requests with no material factual claims; still do not invent facts.

## Required Inputs

Identify the user’s requested outcome, the applicable task-specific output contract, the available evidence, and any consequential risks. Evidence may be the user’s supplied requirements, repository files, test output, approved documentation, or retrieved primary sources. Use Context7 only when it is actually available and relevant to a named library; resolve the correct library and version, then verify consequential behavior against the official documentation or repository. Context7 is a retrieval aid, not proof that a claim is current or correct.

## Procedure

1. Restate the acceptance target internally as observable checks. Preserve identifiers, values, and source wording exactly; distinguish a stated requirement from an inference.
2. List the material claims or expected results and link each to its evidence. For software work, use paths, symbols, requirements, test output, command results, or current official documentation. Do not fabricate tool runs, source references, expected behavior, test outcomes, or data.
3. Check for missing, conflicting, stale, or ambiguous evidence. Ask a concise question when the missing information could change the answer, implementation, expected result, or safety. If the gap is non-blocking, state the assumption explicitly and keep the result conditional.
4. Confirm that the task-specific output contract is satisfied field by field. Separate observations, inferences, recommendations, and unknowns.
5. Run the smallest relevant validation available. Report exactly what ran and its result; mark unavailable or unrun checks as unverified.
6. Score evidence readiness using the four equally weighted checks below. A check passes only when supported by observable evidence; do not award partial credit to make the threshold.

## Evidence-Readiness Score

Scope and acceptance target are clear: 25 points.
Material claims and expected results are traceable to supplied or retrieved evidence: 25 points.
The task-specific deliverable contains all required fields and separates facts from inferences: 25 points.
Relevant verification was performed, or the unverified portions and reasons are explicit: 25 points.

Calculate the score as points passed divided by applicable points, multiplied by 100. Mark a check not applicable only when the task genuinely has no such requirement, explain why, and exclude it from the denominator. Never invent evidence to pass a check. A score of 75 or higher means the deliverable may be presented with any remaining gaps plainly disclosed. Below 75, or when the score cannot be supported, ask for the missing information, deliver only a clearly labeled provisional portion, or abstain.

A critical safety, authorization, privacy, source-integrity, or acceptance-criterion failure blocks a ready result regardless of the score. An evidence-readiness score is not calibrated confidence, a probability of correctness, or a guarantee of quality. Do not print a percentage by default. If the user asks for it, label it “evidence readiness,” show the numerator, denominator, and failed or excluded checks, and never call it a confidence probability.

## Output Contract

For consequential work, include the task-specific deliverable followed by a concise evidence note with supporting inputs or sources, unresolved questions or assumptions, checks actually performed, and any unverified scope. For QA findings, include reproducible evidence and affected requirement or location. For code changes, identify changed files and actual tests or checks. For research, cite factual claims and distinguish source statements from recommendations.

## Quality Gate

Before delivery, verify that every requested output field is present, every material fact is supported or marked unknown, no missing requirement has been silently invented, risks and contrary evidence are disclosed, and the reported checks match actual tool results. If any critical gate fails, do not label the work ready.

## Evidence and Uncertainty

Use the user request, project artifacts, verified tool results, and current authoritative sources as evidence. Record the exact evidence that supports a pass; absence of a failed test or missing source is not evidence that a claim is true. Separate direct observation, inference, and recommendation. If the applicable denominator or a pass/fail decision cannot be justified, mark the score unscorable and ask, qualify, or abstain. Do not present the score as calibrated confidence or probability.

## Example

A test plan has clear acceptance criteria and a complete scenario table, but no test execution occurred. The scope, traceability, and output checks pass; verification is explicitly unrun. Report a provisional plan with the unrun check disclosed and calculate readiness only from applicable, evidenced checks. Do not state that the feature passed testing or invent a percentage likelihood that the plan is correct.
