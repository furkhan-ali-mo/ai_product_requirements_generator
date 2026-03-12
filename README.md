# claude_code_prd_generator

A Claude Code-native workspace that transforms a rough startup idea into a structured Product Requirements Document — entirely inside your terminal.

---

## Why This Exists

Writing a real PRD takes hours of research, synthesis, and structured thinking. Most founders skip it. This workspace automates the full product discovery and documentation process using Claude Code's native customization features: skills, hooks, MCP integrations, and dynamically created subagents.

This is not a web app. There is no UI. The operator works directly inside Claude Code, and Claude handles the rest.

---

## Target Users

- Founders with a rough product idea
- Product managers scoping an MVP
- Technical builders who want structured requirements before building
- Builders exploring Claude Code as an AI PM workspace

---

## Core Problem

Turning a vague idea into a structured, actionable PRD requires:
- Clarifying the problem and user
- Researching the competitive landscape
- Generating and prioritizing features
- Writing clear user stories and success metrics

This takes hours when done manually. This workspace does it in one orchestrated Claude Code session.

---

## Solution

A Claude Code workspace with:
- A top-level orchestration skill (`prd_operator_workflow`)
- Specialized sub-skills for each phase of product discovery
- Hooks that validate and persist the final output
- MCP integrations for live market research
- Dynamic subagent creation when deeper specialization is needed

---

## Claude Code Features Demonstrated

| Feature | How It's Used |
|---|---|
| **CLAUDE.md** | Defines workflow order, writing standards, scope constraints, and completion criteria |
| **Skills** | 8 modular skills covering discovery, research, feature design, prioritization, PRD writing, and review |
| **Hooks** | `validate_prd.py` checks required sections; `save_artifact.py` persists the artifact |
| **MCP Servers** | Browser/Search MCP for competitor research and market scanning |
| **Dynamic Subagents** | `subagent_creation` skill guides Claude to create persistent `.claude/agents/` files on demand |

---

## Skills Overview

| Skill | Purpose |
|---|---|
| `prd_operator_workflow` | **Top-level orchestration** — runs the full PRD pipeline |
| `product_discovery` | Clarifies idea, problem space, and target users |
| `competitor_research` | Scans market, finds competitors, extracts signals |
| `feature_generation` | Generates features grounded in user jobs-to-be-done |
| `prioritization` | Ranks features using value/effort and RICE frameworks |
| `prd_generation` | Writes the complete structured PRD |
| `prd_quality_review` | Validates PRD completeness and quality |
| `subagent_creation` | Interactively creates persistent Claude subagents |

---

## Top-Level Operator Workflow

The operator triggers the entire pipeline with a single instruction:

```
Use the prd_operator_workflow skill to generate a PRD for this idea: [your idea]
```

Claude then orchestrates the full workflow:

```
1. product_discovery    → clarify idea, users, problem
2. competitor_research  → scan market and competitors (Browser MCP)
3. feature_generation   → generate feature set from user needs
4. prioritization       → rank features by value and effort
5. prd_generation       → write the full structured PRD
6. prd_quality_review   → validate all 12 required sections
7. save artifact        → persist to outputs/generated_prds/
```

---

## Hooks Architecture

Hooks run deterministic checks after PRD generation:

**`validate_prd.py`**
- Checks all 12 required PRD sections are present
- Fails with a clear error if any section is missing
- Runs as a PostToolUse hook after PRD write

**`save_artifact.py`**
- Saves the final PRD markdown to `outputs/generated_prds/`
- Uses timestamped filenames: `prd_YYYYMMDD_HHMMSS.md`
- Runs automatically after successful validation

Hooks are configured in `.claude/settings.json`.

---

## MCP Integrations

**Browser/Search MCP**
Used during competitor research to:
- Search for competing products
- Extract positioning and feature signals
- Identify market gaps

MCP servers must be configured before use. See `.env.example` for required variables and `docs/architecture.md` for setup details.

---

## Dynamic Subagent Creation

Subagents are not pre-bundled in this repository. Instead, the `subagent_creation` skill guides Claude to create persistent subagent definition files inside `.claude/agents/` at the operator's request.

Example: an operator might ask Claude to create a `market_analyst` subagent that specializes in competitor research with access to the Browser MCP. Claude collects the spec interactively and writes the agent file.

See `docs/subagent_design.md` for templates and examples.

---

## Example Operator Session

```
Operator: Use the prd_operator_workflow skill to generate a PRD for this idea:
          A mobile app that helps independent coffee shop owners manage their
          loyalty programs without needing a developer.

Claude:   [Runs product_discovery — asks 4–6 clarifying questions]
          [Runs competitor_research — scans Stamp Me, Yotpo, Square Loyalty]
          [Runs feature_generation — generates 15 features mapped to JTBDs]
          [Runs prioritization — scores features, selects MVP set]
          [Runs prd_generation — writes full 12-section PRD]
          [Runs prd_quality_review — validates completeness]
          [Saves artifact — outputs/generated_prds/prd_20260312_143022.md]
```

---

## Example PRD Structure

Every generated PRD contains:

```
1.  Product Overview
2.  Problem Statement
3.  Target Users
4.  User Personas
5.  Jobs To Be Done
6.  Proposed Solution
7.  Feature List
8.  MVP Scope
9.  Feature Prioritization
10. User Stories
11. Success Metrics
12. Risks and Assumptions
```

---

## Repository Structure

```
claude_code_prd_generator/
├── README.md
├── CLAUDE.md                        # Workspace rules and workflow
├── .env.example                     # MCP environment variables
├── requirements.txt
├── .claude/
│   ├── skills/
│   │   ├── prd_operator_workflow/   # Top-level orchestration skill
│   │   ├── product_discovery/
│   │   ├── competitor_research/
│   │   ├── feature_generation/
│   │   ├── prioritization/
│   │   ├── prd_generation/
│   │   ├── prd_quality_review/
│   │   └── subagent_creation/
│   ├── agents/                      # Created dynamically by Claude
│   ├── hooks/
│   │   ├── validate_prd.py
│   │   └── save_artifact.py
│   └── settings.json
├── outputs/
│   └── generated_prds/              # PRD artifacts saved here
└── docs/
    ├── architecture.md
    ├── operator_workflow.md
    ├── skills_strategy.md
    ├── subagent_design.md
    └── portfolio_case_study_outline.md
```

---

## How to Use This Workspace

1. Clone this repository
2. Copy `.env.example` to `.env` and configure MCP credentials
3. Open the repo in a terminal
4. Run `claude` to launch Claude Code
5. Say: `Use the prd_operator_workflow skill to generate a PRD for this idea: [your idea]`
6. Answer Claude's clarifying questions
7. Retrieve your PRD from `outputs/generated_prds/`

---

## Future Improvements

- Iterative PRD editing loop (post-V1)
- Slack/Notion export hooks
- Pre-built market analyst and persona builder subagents
- Multi-idea comparison mode
- Stakeholder review mode with comment annotations
