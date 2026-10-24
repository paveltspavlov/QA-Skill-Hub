---
name: ai-test-strategy
description: "Design evidence-based test strategies for AI and ML systems. Use when validating models, data, fairness, safety, drift, or AI risk."
---

# AI Test Strategy

## When to Use
Use for AI-enabled products, ML pipelines, LLM applications, model release reviews, and post-deployment monitoring plans. Do not issue a legal compliance determination or assume model type, intended use, protected groups, or acceptable error rates.

## Required Inputs
Request the use case and intended users; model and pipeline boundaries; decisions affected and harm scenarios; available requirements, benchmark data, labels, baselines, and model/version details; deployment and fallback behavior; geographic/sector context; and owners. Mark unavailable inputs as unknown. Ask before setting any acceptance threshold that changes release decisions.

## Procedure
1. Map data ingestion, preprocessing, model, retrieval/tools, serving interface, users, downstream actions, and human review. Identify sources of truth and versioned artifacts.
2. Convert intended behavior and harms into measurable questions. Separate deterministic functional checks from statistical quality, safety, and human-judgment review.
3. Build a lifecycle matrix across data (quality, representativeness, leakage), model (task performance, calibration where relevant, robustness), fairness (stakeholder-defined subgroups and metrics), LLM-specific risks (grounding, refusal, prompt injection, privacy), integration (schema, timeout, fallback), and operations (drift, logging, rollback).
4. For each row specify dataset/slice, method, metric or rubric, owner, evidence source, release/monitoring decision, and unresolved dependency. Establish thresholds with the product/domain owner; no universal score is assumed.
5. Assess regulatory applicability only from verified jurisdiction, purpose, and authoritative current sources. Label this an issue for counsel/compliance where classification is uncertain.
6. Define versioned evaluation sets, change triggers, human escalation, monitoring limits, and safe rollback/review steps. Avoid exposing sensitive prompts or examples.

## Output Contract
Deliver `AI Test Strategy: <system>` with: (1) scope and system map; (2) risk register table `Risk ID | Component | Harm/Failure | Affected group | Evidence | Priority | Control`; (3) test matrix `Layer | Scenario | Dataset/Slice | Method | Metric/Rubric | Acceptance owner | Gate/Action`; (4) lifecycle/monitoring plan; (5) questions, assumptions, and exclusions. Example row: `LLM-03 | Retrieval | Unsupported policy claim | Customer | Cite answer to approved source | High | Grounded-answer rubric | Product/legal owner | Block if unsupported claim is confirmed`—the owner sets the rubric and gate; this row does not assert a test result.

## Quality Gate
Verify each material risk maps to a test or explicit accepted gap; dataset provenance and subgroup definitions are disclosed; statistical comparisons state sample and method; criteria are authorized and operational; tests distinguish model quality from interface behavior; rollback/human escalation are viable. Never infer fairness or safety from aggregate accuracy alone.

## Evidence and Uncertainty
Cite supplied requirements, dataset/model versions, executed evaluation artifacts, and current official documentation for consequential technical/regulatory claims. Label observations, hypotheses, and unknowns separately. Apply evidence readiness as four evidenced checks: clear scope, traceable claims, complete contract, and relevant verification (25 points each); below 75/100, ask, qualify, or abstain. Do not guess confidence percentages. A critical safety, authorization, privacy, or acceptance failure blocks readiness regardless of score.
