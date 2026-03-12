# Skill: prd_generation

## When to Use

Use this skill after `prioritization` has produced an MVP Feature Set. All prior context (Discovery Summary, Competitor Summary, Feature List, Prioritization scores) must be available before starting.

## What It Solves

Converts structured product research into a complete, readable PRD document that a founder, developer, or stakeholder can act on.

## Workflow

**Phase 1 — Context Assembly**
Before writing, collect and confirm all inputs are present:
- Discovery Summary (from product_discovery)
- Competitor Summary (from competitor_research)
- JTBD list (from feature_generation)
- MVP Feature Set with scores (from prioritization)

If any input is missing, stop and request it.

**Phase 2 — Write the PRD**
Write all 12 sections in order. Use the PRD template in `reference_prd_template.md`.

Do not skip sections. Do not merge sections. Do not change section names.

Section order:
1. Product Overview
2. Problem Statement
3. Target Users
4. User Personas
5. Jobs To Be Done
6. Proposed Solution
7. Feature List
8. MVP Scope
9. Feature Prioritization
10. User Stories
11. Success Metrics
12. Risks and Assumptions

**Phase 3 — Quality Pass**
Before handing off to `prd_quality_review`, self-check:
- Are all 12 sections present?
- Does each persona have name, role, goal, and frustration?
- Are user stories in "As a / I want / So that" format?
- Are success metrics specific and measurable?
- Is MVP scope ruthlessly minimal?

## Expected Outputs

- A complete PRD in markdown format
- Filename: `prd_[product_slug]_draft.md`
- Ready for `prd_quality_review`

## Key Guardrails

- Write for non-technical founders. No implementation details unless essential.
- Do not invent facts. Every claim should trace back to discovery or research.
- Be specific. Avoid "intuitive UX," "seamless experience," "powerful features."
- Success metrics must be measurable KPIs, not aspirational language.

## Reference Files

- `reference_prd_template.md` — complete 12-section PRD template with writing instructions per section
- `reference_prd_examples.md` — annotated examples of strong section writing
