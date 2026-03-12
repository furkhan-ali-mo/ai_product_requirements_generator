# Skills Strategy

This document explains why each skill exists, how they're designed, and how they compose into the full PRD workflow.

---

## Design Principles

### Progressive Disclosure

Each skill has a `SKILL.md` under 400 words. This is the entry point Claude reads when a skill is invoked. Detailed instructions, frameworks, templates, and examples live in `reference_*.md` files inside the same folder.

Why this matters: Claude's effective instruction window is finite. Loading a 2,000-word skill file for every step would crowd out context that Claude needs for the actual work. SKILL.md gives Claude what it needs to start; reference files give it depth when needed.

### Single Responsibility

Each skill has one job. `product_discovery` only clarifies the idea. `competitor_research` only researches competitors. This separation means:
- Skills are easier to test and improve independently
- Operators can invoke a single skill without running the full workflow
- Skills compose cleanly without unexpected interactions

### Grounded in Product Practice

Each skill reflects real product management methodology:
- Discovery questions drawn from design thinking and JTBD interviewing practices
- Competitor research structured around positioning and gap analysis, not just feature lists
- Prioritization using Value/Effort and RICE — frameworks used by actual PMs
- PRD template aligned with industry standards (not invented structure)

---

## Skill-by-Skill Rationale

### `product_discovery`

**Why it exists:** Operators arrive with half-formed ideas. Skipping discovery means building on assumptions. This skill forces structured clarification before any research or feature work begins.

**Key design choice:** Asks 4–6 targeted questions, not a fixed questionnaire. Different ideas have different gaps. A B2B SaaS idea needs different probing than a consumer mobile app.

### `competitor_research`

**Why it exists:** Most founders underestimate competition or miss adjacent alternatives. This skill creates a structured view of the market before feature decisions are made.

**Key design choice:** Uses Browser/Search MCP for live data. Accepts a fallback to training knowledge with explicit flagging when MCP is unavailable.

### `feature_generation`

**Why it exists:** Without structure, feature lists become wish lists disconnected from user needs. Grounding features in JTBDs ensures everything earns its place.

**Key design choice:** Generates JTBDs first, then derives features from them. This ordering is deliberate — JTBDs are the stable layer; features are one possible implementation of a job.

### `prioritization`

**Why it exists:** A list of 15 features cannot all be V1. This skill applies consistent scoring criteria so that the MVP/post-MVP cut has rationale the operator can stand behind.

**Key design choice:** Uses Value/Effort matrix as the primary tool (fast, intuitive) and RICE scoring for borderline cases (more rigorous). Keeps the operator in the decision loop for final calls.

### `prd_generation`

**Why it exists:** Synthesizes all prior context into a single, structured document. This is the primary output artifact.

**Key design choice:** The 12-section template is fixed and non-negotiable. This enforces completeness and ensures every PRD is comparable and actionable.

### `prd_quality_review`

**Why it exists:** Claude can generate a PRD that looks complete but has vague metrics, generic personas, or an over-scoped MVP. This skill runs a systematic check before saving.

**Key design choice:** Section-level rubrics with specific failure modes and fix instructions. "The persona section is weak" is not useful feedback. "Persona 1 has no frustration and no quote" is actionable.

### `subagent_creation`

**Why it exists:** Some product domains benefit from a persistent specialist. Rather than pre-bundling subagents that may not fit every operator's needs, this skill enables operators to create exactly the agents they need.

**Key design choice:** Interactive spec collection before any file is written. A subagent built from a bad spec is a liability, not an asset.

### `prd_operator_workflow`

**Why it exists:** The top-level orchestrator that makes the whole system feel like one coherent product experience rather than a collection of skills.

**Key design choice:** Explicit step transitions with context handoff formats. Each step's output is packaged into a named summary before the next step begins. This prevents context loss across a long session.

---

## How Skills Compose

```
prd_operator_workflow
    │
    ├── product_discovery ──────── Discovery Summary
    ├── competitor_research ─────── Competitor Summary
    ├── feature_generation ─────── JTBD list + Feature Candidates
    ├── prioritization ─────────── MVP Feature Set
    ├── prd_generation ─────────── Draft PRD (12 sections)
    └── prd_quality_review ─────── Approved PRD
```

Skills are called in sequence. Each skill consumes the output of the previous one. The context package format (defined in `prd_operator_workflow/reference_orchestration.md`) ensures clean handoffs.

Skills can also be invoked standalone by the operator at any time. For example:
- "Use the competitor_research skill to analyze the project management tools market"
- "Use the prioritization skill on this feature list I have"
