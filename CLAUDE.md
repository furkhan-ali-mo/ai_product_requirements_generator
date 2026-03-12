# CLAUDE.md — PRD Generator Workspace

## Project Purpose

This workspace converts a rough software or app idea into a structured Product Requirements Document (PRD). You are operating inside a Claude Code-native AI PM workspace designed to guide founders, product operators, and builders through structured product discovery and documentation.

## Target User

Product operators, founders, and builders working directly inside Claude Code. Assume the user is non-technical or semi-technical. Write outputs that are clear, practical, and jargon-free.

## Scope Constraint

This workspace handles **software and app MVP ideas only**. Do not generate PRDs for physical products, services, or non-software ideas. If the operator gives a non-software idea, clarify and redirect.

## Workflow Order

Always follow this sequence:

1. **discovery** — clarify the idea, problem, and users via `product_discovery`
2. **research** — scan competitors and market signals via `competitor_research`
3. **feature design** — generate and frame features via `feature_generation`
4. **prioritization** — rank features by value and effort via `prioritization`
5. **PRD generation** — write the full structured PRD via `prd_generation`
6. **validation** — check structure and completeness via `prd_quality_review`
7. **save artifact** — persist final PRD to `outputs/generated_prds/`

Never skip steps. Never reorder steps.

## Required PRD Sections

Every generated PRD must contain all of these sections in order:

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

A PRD missing any section is incomplete and must not be saved.

## Writing Standards

- Write for non-technical founders. Avoid implementation jargon.
- Be specific. Avoid vague language like "intuitive" or "seamless."
- Every persona must have a name, role, goal, and frustration.
- Every user story must follow: "As a [persona], I want to [action] so that [outcome]."
- Success metrics must be measurable. Include specific KPIs.
- MVP scope must be ruthlessly minimal — only what validates the core hypothesis.

## Skills Available

| Skill | Purpose |
|---|---|
| `product_discovery` | Clarify idea, users, problem |
| `competitor_research` | Scan market and competitors |
| `feature_generation` | Generate and frame features |
| `prioritization` | Rank features by value/effort |
| `prd_generation` | Write the full PRD document |
| `prd_quality_review` | Validate structure and completeness |
| `subagent_creation` | Create specialized Claude subagents |
| `prd_operator_workflow` | Top-level orchestration skill |

## Completion Criteria

The workflow is complete when:

- All 12 PRD sections are written
- The PRD has passed quality review
- The artifact is saved to `outputs/generated_prds/` with a timestamped filename

## MCP Integrations

- **Browser/Search MCP** — used during competitor research for market scanning

## Hooks

- `validate_prd.py` — runs after PRD generation to check required sections
- `save_artifact.py` — saves final PRD to `outputs/generated_prds/`
