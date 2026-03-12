# Skill: product_discovery

## When to Use

Use this skill at the start of the PRD workflow, or any time the operator needs to clarify and structure their product idea before moving into research or feature work.

## What It Solves

Operators arrive with vague, incomplete, or assumption-heavy ideas. This skill extracts what's actually true about the problem, user, and context — before any research or feature work begins.

## Workflow

**Phase 1 — Initial Intake**
Ask the operator to describe their idea in 2–3 sentences if they haven't already.

**Phase 2 — Targeted Clarification (4–6 questions)**
Select questions from `reference_questions.md` based on what's unclear. Do not ask all questions — pick the 4–6 most critical gaps.

Categories to probe:
- Who exactly is the user?
- What specific pain are they experiencing?
- What do they do today instead?
- What makes this worth building now?
- What's the deployment context (mobile, web, B2B, B2C)?
- Are there known constraints (budget, timeline, technical)?

**Phase 3 — Synthesis**
After collecting answers, synthesize into a Discovery Summary:
- Product idea (one sentence)
- Core problem (one sentence)
- Target user (one sentence)
- Key insight or unique angle
- Known constraints

**Phase 4 — Validation Check**
Before handing off to the next skill, confirm:
- Is this a software/app idea? (If not, stop and redirect.)
- Is the problem specific enough to generate user stories?
- Is the target user specific enough to build personas around?

## Expected Outputs

- A completed Discovery Summary (structured, 5–8 lines)
- Ready for handoff to `competitor_research`

## Key Guardrails

- Do not generate features or solutions during discovery — stay focused on the problem.
- Do not accept "everyone" as a target user. Push for a specific primary persona.
- Do not proceed if the problem is too vague. Ask one more targeted question.
- Scope: software/app MVPs only.

## Reference Files

- `reference_questions.md` — full bank of discovery questions by category
- `reference_synthesis.md` — how to write a Discovery Summary, with examples
