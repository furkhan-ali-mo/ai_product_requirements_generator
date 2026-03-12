# Skill: prd_operator_workflow

## When to Use

Use this skill when the operator says something like:
- "Generate a PRD for this idea: ..."
- "Use the prd_operator_workflow skill"
- "Help me build a PRD from scratch"

This is the top-level orchestration skill. It composes all other skills into one end-to-end workflow.

## What It Solves

Operators arrive with a rough idea. This skill drives the full journey from vague concept to a complete, saved PRD artifact — in a single structured Claude Code session.

## Workflow

Execute these steps in strict order. Do not skip or reorder.

**Step 1 — Product Discovery**
Load and follow `.claude/skills/product_discovery/SKILL.md`.
Ask the operator 4–6 targeted clarifying questions. Synthesize answers into a Discovery Summary.

**Step 2 — Competitor Research**
Load and follow `.claude/skills/competitor_research/SKILL.md`.
Use Browser/Search MCP to identify 3–5 direct competitors. Extract positioning signals and gaps.

**Step 3 — Feature Generation**
Load and follow `.claude/skills/feature_generation/SKILL.md`.
Generate 10–20 candidate features grounded in user jobs-to-be-done from Step 1.

**Step 4 — Prioritization**
Load and follow `.claude/skills/prioritization/SKILL.md`.
Score and rank features. Select the MVP feature set (5–8 features max).

**Step 5 — PRD Generation**
Load and follow `.claude/skills/prd_generation/SKILL.md`.
Write the full 12-section PRD using all prior context. Use the PRD template in reference files.

**Step 6 — Quality Review**
Load and follow `.claude/skills/prd_quality_review/SKILL.md`.
Validate PRD completeness and quality. Fix any gaps before proceeding.

**Step 7 — Save Artifact**
Save the final PRD to `outputs/generated_prds/prd_YYYYMMDD_HHMMSS.md`.
Confirm the save path to the operator.

## Expected Outputs

- A saved PRD markdown file in `outputs/generated_prds/`
- A summary message to the operator confirming the file path and key decisions made

## Key Guardrails

- Only accept software/app MVP ideas. Redirect physical product or service ideas.
- Do not save the PRD until it has passed quality review.
- Do not skip the discovery step even if the operator seems confident about their idea.
- If any step produces insufficient output, surface the gap and ask before proceeding.

## Reference Files

- `reference_orchestration.md` — detailed orchestration notes, handoff formats between steps, and context packaging
- See individual skill folders for each step's detailed instructions
