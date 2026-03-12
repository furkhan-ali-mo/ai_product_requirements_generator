You are an expert Claude Code developer and AI systems engineer.

Your task is to build a complete Claude Code-native workspace called:

claude_code_prd_generator

This repository is NOT a web app and does NOT include a UI.

Instead, this repository is designed to be used by a product operator inside Claude Code.

==================================================
CORE OPERATOR WORKFLOW
==================================================

The operator workflow is:

1. Clone/download this repo
2. Open a terminal in the repo
3. Launch Claude Code
4. Give Claude a product idea
5. Ask Claude to use the top-level orchestration skill
6. Claude uses the repository’s CLAUDE.md, skills, hooks, MCP integrations, and optionally creates subagents
7. Claude generates a complete Product Requirements Document (PRD)

This project must demonstrate deep usage of:

- CLAUDE.md
- Skills
- Hooks
- MCP servers
- Dynamic subagent creation via a skill

This project is primarily:
1. a Claude Code customization showcase
2. an AI PM tool

Do not build a web interface.
Do not build a Streamlit app.
Focus on building a clean, well-structured Claude Code workspace.

==================================================
PROJECT PURPOSE
==================================================

This workspace converts a rough startup software/app idea into a structured Product Requirements Document.

Target user:
- a product operator, founder, or builder working directly inside Claude Code

The system should help with:
- idea clarification
- user discovery
- competitor research
- persona creation
- feature generation
- MVP scoping
- feature prioritization
- PRD writing

The final output should be a structured PRD document saved as an artifact.

==================================================
PRODUCT SCOPE
==================================================

In scope:
- software/app MVP ideas only
- product discovery through Claude conversation
- competitor and market scanning
- feature ideation
- prioritization
- final PRD generation
- saving generated PRDs

Out of scope for V1:
- UI
- file upload
- collaborative editing
- iterative post-generation rewrite loop
- design mockups
- analytics dashboards

Important:
The workflow should generate the PRD in one pass after clarification.
No iterative editing loop is needed in V1.

==================================================
PRD STRUCTURE
==================================================

All generated PRDs must contain these sections:

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

==================================================
REPOSITORY STRUCTURE
==================================================

Create a Claude Code workspace with this structure:

claude_code_prd_generator/
├── README.md
├── CLAUDE.md
├── .env.example
├── requirements.txt
├── .claude/
│   ├── skills/
│   │   ├── product_discovery/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   ├── competitor_research/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   ├── feature_generation/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   ├── prioritization/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   ├── prd_generation/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   ├── prd_quality_review/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   ├── subagent_creation/
│   │   │   ├── SKILL.md
│   │   │   └── reference.md
│   │   └── prd_operator_workflow/
│   │       ├── SKILL.md
│   │       └── reference.md
│   ├── agents/
│   ├── hooks/
│   │   ├── validate_prd.py
│   │   └── save_artifact.py
│   └── settings.json
├── outputs/
│   └── generated_prds/
└── docs/
    ├── architecture.md
    ├── operator_workflow.md
    ├── skills_strategy.md
    ├── subagent_design.md
    └── portfolio_case_study_outline.md

==================================================
IMPORTANT SKILL DESIGN RULE
==================================================

Each skill folder must contain:
- SKILL.md

Each skill folder may also contain:
- reference.md
- frameworks.md
- examples.md
- templates.md

Critical rule:
Every SKILL.md must be concise and under roughly 400 to 500 words maximum.

SKILL.md should only contain:
- when the skill should be used
- what problem it solves
- the high-level workflow
- expected outputs
- key guardrails

All detailed instructions, templates, checklists, examples, frameworks, and long guidance must go into supporting reference files inside the same skill folder.

This rule is extremely important.
Do not put all detail into SKILL.md.
Use progressive disclosure properly.

==================================================
SKILLS TO IMPLEMENT
==================================================

Create these skills:

1. product_discovery
2. competitor_research
3. feature_generation
4. prioritization
5. prd_generation
6. prd_quality_review
7. subagent_creation
8. prd_operator_workflow

These must be realistic and thoughtfully designed, not placeholders.

==================================================
TOP LEVEL ORCHESTRATION SKILL
==================================================

Create a top-level skill:

prd_operator_workflow

This is the main skill the operator will invoke.

The operator should be able to say something like:
“Use the prd_operator_workflow skill to generate a PRD for this idea.”

This skill must instruct Claude to orchestrate the workflow using the other skills.

Expected workflow inside this skill:

1. Use product_discovery
2. Use competitor_research
3. Generate personas and problem framing
4. Use feature_generation
5. Use prioritization
6. Use prd_generation
7. Use prd_quality_review
8. Save final PRD artifact

This top-level skill must clearly explain how the other skills are composed into one operator workflow.

==================================================
SPECIAL SKILL: subagent_creation
==================================================

Create a skill:

subagent_creation

Purpose:
This skill teaches Claude how to help the operator create subagents interactively from the terminal.

Important:
The repository should NOT ship with predefined ready-made subagent files.

Instead:
- include templates and examples in reference files
- let Claude create permanent subagent files inside `.claude/agents/` only when the operator asks for them

When this skill is used, Claude should ask the operator for:

- subagent name
- purpose
- description
- model to use
- tools allowed
- whether it should preload certain skills
- task boundaries
- expected output format
- whether it should be read-only or have write permissions

After collecting answers, Claude should create the subagent file under:
`.claude/agents/`

The skill should help Claude do this well and consistently.

==================================================
SUBAGENT DESIGN RULES
==================================================

Do not pre-create actual subagent files in the repository.

Instead:
- keep `.claude/agents/` present as an empty directory or with a small README/placeholder note if needed
- include templates/examples in docs or skill reference files
- actual subagents are created later by Claude in response to operator requests using the subagent_creation skill

The subagents, once created, should be permanent files in `.claude/agents/`.

==================================================
HOOKS
==================================================

Create hooks under:

.claude/hooks/

Hook 1:
validate_prd.py

Purpose:
Validate final PRD structure.

Checks:
- all required PRD headings exist
- success metrics section exists
- MVP scope exists
- risks and assumptions section exists

Hook 2:
save_artifact.py

Purpose:
Save generated PRD artifacts.

Behavior:
- save PRD markdown to outputs/generated_prds/
- use timestamped filenames

Important:
In V1, hooks only need to validate final PRD output and save artifacts.
Do not validate subagent creation in V1.

==================================================
HOOK CONFIGURATION
==================================================

Configure hooks through:

.claude/settings.json

Ensure hooks are set up to support:
- final PRD validation
- artifact saving

Use hooks for deterministic checks and persistence behavior, not broad strategic reasoning.

==================================================
MCP USAGE
==================================================

Design the workspace assuming integration with these MCPs:

1. Browser/Search MCP
2. Filesystem MCP

Use cases:

Browser/Search MCP:
- competitor research
- lightweight market scanning

Filesystem MCP:
- saving PRD artifacts
- accessing templates and local artifacts

Make MCP usage explicit in:
- README
- docs
- skill reference files where relevant
- overall architecture

Even if MCP cannot be fully exercised during repository generation, structure the workspace as if MCP is a core part of the operating model.

==================================================
CLAUDE.MD REQUIREMENTS
==================================================

Create a root CLAUDE.md file.

It must define:
- project purpose
- target user
- output structure
- workflow order
- writing standards
- completion criteria

The CLAUDE.md must instruct Claude that:

- this workspace focuses on software/app MVP ideas only
- outputs must be clear and practical for non-technical founders
- every PRD must include all required sections
- recommendations must stay MVP-oriented
- the workflow order is:
  discovery → research → feature design → prioritization → PRD generation → validation → save artifact

Keep CLAUDE.md concise, clear, and high-signal.

==================================================
README REQUIREMENTS
==================================================

Create a strong portfolio-ready README with sections like:

- Project overview
- Why this workspace exists
- Target users
- Core problem
- Solution
- Claude Code features demonstrated
- Skills overview
- Top-level operator workflow
- Hooks architecture
- MCP integrations
- Dynamic subagent creation model
- Example operator workflow
- Example final PRD structure
- Repository structure
- How to use this workspace
- Future improvements

The README must clearly explain that:
- this is a Claude Code-native workspace
- the operator works directly in Claude Code terminal
- subagents are created dynamically by Claude when needed
- the repository intentionally showcases Claude Code customization patterns

==================================================
DOCS REQUIREMENTS
==================================================

Create the following docs:

1. architecture.md
Explain overall Claude Code-native workspace architecture.

2. operator_workflow.md
Explain how the operator uses the workspace in terminal.

3. skills_strategy.md
Explain why each skill exists and how the skills compose together.

4. subagent_design.md
Explain how subagents are created dynamically using the subagent_creation skill, including templates and examples.

5. portfolio_case_study_outline.md
Explain how to present this project in a portfolio.

==================================================
IMPLEMENTATION QUALITY
==================================================

Do not produce generic placeholder text.

Design realistic, useful skills.

Ensure every SKILL.md stays under 400 to 500 words.

Put detailed instructions into reference files.

Make the repository clean, modular, and understandable.

This must feel like a serious Claude Code workspace, not a toy example.

==================================================
EXPECTED OPERATOR EXPERIENCE
==================================================

The expected operator experience should look like this:

1. Operator opens repo in terminal
2. Runs Claude Code
3. Says:
   “Use the prd_operator_workflow skill to generate a PRD for this idea: ...”
4. Claude runs discovery
5. Claude uses relevant skills
6. Claude may, if needed, use the subagent_creation skill to help create specialized subagents
7. Claude validates the final PRD
8. Claude saves the artifact

==================================================
FINAL QUALITY BAR
==================================================

Before considering the task complete, verify that:

- all five Claude Code setups are clearly represented
- every skill has a concise SKILL.md plus supporting reference file(s)
- no SKILL.md exceeds about 400 to 500 words
- no UI or app code exists
- the repo is clearly Claude Code-native
- the top-level orchestration skill is central and well-designed
- subagents are not pre-bundled, but templates/examples for creating them are included
- hooks only validate final PRD output in V1
- the project reads as both a Claude Code showcase and an AI PM tool

Now build the full repository.