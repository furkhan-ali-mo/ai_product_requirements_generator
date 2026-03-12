# Skill: feature_generation

## When to Use

Use this skill after `competitor_research` has produced a Competitor Summary. Use it to generate a candidate feature list grounded in real user needs.

## What It Solves

Feature lists without structure become wish lists. This skill generates features tied directly to user jobs-to-be-done, informed by competitor gaps and discovery insights. Every feature earns its place.

## Workflow

**Phase 1 — Extract User Jobs**
From the Discovery Summary, extract 3–5 core Jobs To Be Done (JTBDs):
- Format: "When [situation], I want to [motivation], so I can [outcome]."
- These are the anchor points for every feature.

See `reference_jtbd.md` for the full JTBD framework and examples.

**Phase 2 — Generate Feature Candidates**
For each JTBD, generate 2–4 features that directly fulfill that job.
Also generate features that address competitor gaps identified in research.

Target: 12–20 total candidate features.

For each feature, capture:
- Feature name (short, clear)
- Description (one sentence — what it does for the user)
- JTBD it fulfills
- Whether competitors offer it (yes/no/partially)

**Phase 3 — Categorize Features**
Group features into categories:
- Core (must-have to deliver the core value proposition)
- Engagement (improve retention, trust, and repeat use)
- Operational (admin, settings, configuration)
- Growth (sharing, referral, discovery)

**Phase 4 — Validate Coverage**
Check that each of the 3–5 JTBDs has at least 2 features addressing it. If not, generate more.

## Expected Outputs

- JTBD list (3–5 jobs)
- Feature Candidate List (12–20 features, with JTBD mapping and category)
- Ready for handoff to `prioritization`

## Key Guardrails

- Every feature must tie to at least one JTBD. No features "just because."
- Do not include infrastructure or technical tasks as user features.
- Do not include features scoped for v3 when you're defining v1 candidates.
- Keep feature names user-facing. "User profile" not "user entity database model."

## Reference Files

- `reference_jtbd.md` — Jobs To Be Done framework, question prompts, examples
- `reference_feature_templates.md` — feature naming conventions, category definitions, full example output
