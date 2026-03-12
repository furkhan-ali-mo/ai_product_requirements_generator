# Skill: prd_quality_review

## When to Use

Use this skill immediately after `prd_generation` produces a draft PRD. Run it before saving any artifact.

## What It Solves

PRDs fail in different ways — missing sections, vague metrics, shallow personas, or bloated MVP scopes. This skill runs a systematic quality check and surfaces gaps with specific fix instructions rather than generic feedback.

## Workflow

**Phase 1 — Structure Check**
Verify all 12 required sections are present and in the correct order.

Required sections (in order):
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

Any missing section = FAIL. Do not proceed until all sections exist.

**Phase 2 — Content Quality Check**
For each section, apply the quality rubric in `reference_quality_rubric.md`.

Check for the most common failure modes:
- Vague problem statements
- Generic personas without names/frustrations
- JTBD statements that are feature requests
- User stories not in "As a / I want / So that" format
- Success metrics without numbers or timeframes
- MVP scope that includes more than 8 features
- Risks without mitigation strategies

**Phase 3 — Fix or Approve**
For each failing section:
- State what's wrong (specific, not generic)
- Rewrite the section or request a specific fix
- Re-check after the fix

When all checks pass: APPROVE and hand off to save artifact step.

## Expected Outputs

- Quality Review Report (pass/fail per section + specific notes)
- Approved PRD (all sections passing)
- Ready for artifact save

## Key Guardrails

- Do not approve a PRD with any missing required section.
- Do not approve vague success metrics without measurable targets.
- Do not approve personas without at least one named persona with goal + frustration.
- If the MVP scope has more than 8 features, flag it and ask the operator to cut.
- Be direct in feedback — "Section 11 has no measurable targets" is better than "Section 11 could be improved."

## Reference Files

- `reference_quality_rubric.md` — full quality checklist per section, failure modes, fix instructions
