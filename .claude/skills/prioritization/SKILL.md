# Skill: prioritization

## When to Use

Use this skill after `feature_generation` has produced a Feature Candidate List. Use it to rank features and define the MVP scope.

## What It Solves

A list of 15 features cannot all be built in V1. This skill applies structured scoring to objectively rank features, select the MVP set, and defer the rest — with clear rationale the operator can defend.

## Workflow

**Phase 1 — Score Each Feature**
Apply the Value/Effort Matrix to each feature candidate.

For each feature, assign:
- **Value** (H/M/L): How much does this directly deliver the core value proposition or drive user adoption?
- **Effort** (H/M/L): How complex is this to build for an MVP? (not a production-grade estimate — think prototype)

See `reference_scoring.md` for scoring rubrics and tie-breaking rules.

**Phase 2 — Apply RICE (for borderline cases)**
For features that cluster near the MVP/post-MVP line, apply RICE scoring:
- Reach × Impact × Confidence / Effort
- Use relative scores (1–10), not absolute numbers

**Phase 3 — Select MVP Feature Set**
Apply these rules to define the MVP:
- All "Core" category features with H or M value → MVP
- All H Value + L Effort features → MVP regardless of category
- Max MVP size: 5–8 features (ruthlessly minimal)
- Anything deferred goes to "Post-MVP" backlog

**Phase 4 — Sanity Check**
Before finalizing:
- Does the MVP set deliver the core value proposition end-to-end?
- Can a user complete their primary JTBD with only these features?
- Is there anything in MVP that could be cut without breaking the core experience?

## Expected Outputs

- Feature Scoring Table (all candidates with Value/Effort scores)
- MVP Feature Set (5–8 features with justification)
- Post-MVP Backlog (deferred features)
- Ready for handoff to `prd_generation`

## Key Guardrails

- Do not let the operator add features to MVP without explicit trade-off discussion.
- Do not score features based on how fun or interesting they are to build.
- MVP must be testable with real users — not a prototype, not a concept.
- If the operator pushes back on cuts, use the JTBD test: "Which job does this feature fulfill that isn't already covered?"

## Reference Files

- `reference_scoring.md` — Value/Effort rubrics, RICE formula, tie-breaking rules
- `reference_mvp_principles.md` — MVP definition principles, common MVP mistakes, cut/keep decision framework
