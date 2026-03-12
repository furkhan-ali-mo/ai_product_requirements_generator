# Architecture — claude_code_prd_generator

## Overview

This workspace is a Claude Code-native application. There is no backend server, no web frontend, and no deployment infrastructure. The entire system runs inside a Claude Code terminal session, orchestrated by Claude using the workspace's CLAUDE.md, skills, hooks, and MCP connections.

```
Operator Terminal
      │
      ▼
  Claude Code
      │
      ├── CLAUDE.md ──────────────── Workspace rules, workflow order, writing standards
      │
      ├── .claude/skills/ ─────────── Behavioral instructions loaded by Claude on demand
      │   ├── prd_operator_workflow/  ← Top-level orchestrator
      │   ├── product_discovery/
      │   ├── competitor_research/    ← Uses Browser/Search MCP
      │   ├── feature_generation/
      │   ├── prioritization/
      │   ├── prd_generation/
      │   ├── prd_quality_review/
      │   └── subagent_creation/
      │
      ├── .claude/agents/ ─────────── Subagent definitions (created dynamically)
      │
      ├── .claude/hooks/ ──────────── Deterministic post-write checks
      │   ├── validate_prd.py         ← Checks 12 required sections
      │   └── save_artifact.py        ← Persists PRD with timestamped filename
      │
      ├── .claude/settings.json ───── Hook configuration and permissions
      │
      └── outputs/generated_prds/ ─── Final PRD artifacts saved here
```

---

## Core Architectural Principles

### 1. Skills as Behavioral Modules

Skills are markdown instruction files that Claude loads and follows during a session. Each skill:
- Has a concise `SKILL.md` (under 400 words) as the entry point
- Uses supporting `reference_*.md` files for detailed instructions and templates
- Is invoked by name: "Use the `competitor_research` skill"
- Can be composed: the `prd_operator_workflow` skill orchestrates all others in sequence

This design keeps Claude's active instruction context lean while making detailed guidance accessible progressively.

### 2. Orchestration via Top-Level Skill

The `prd_operator_workflow` skill acts as the conductor. It:
- Defines the canonical 7-step workflow
- Calls each sub-skill in order
- Packages context between steps (Discovery Summary → Competitor Summary → Feature List → etc.)
- Decides when to invoke the `subagent_creation` skill for deeper specialization

### 3. Hooks for Deterministic Enforcement

Hooks run after Claude writes files to `outputs/generated_prds/`. They are:
- **Not part of Claude's reasoning** — hooks are Python scripts that run outside the model
- **Deterministic** — they check structure and format, not quality or strategy
- **Blocking** — if `validate_prd.py` exits with code 1, Claude sees the error and must fix it before proceeding

This separation ensures that structural completeness is guaranteed by code, not just by Claude's judgment.

### 4. MCP for Live Data

**Browser/Search MCP** extends Claude's reach beyond training knowledge:
- Used in `competitor_research` to find real competitors and market signals
- Returns structured search results and page content for Claude to analyze

All file operations (reading templates, saving artifacts) use Claude Code's native `Read` and `Write` tools — no separate Filesystem MCP needed.

### 5. Dynamic Subagents

Subagents are not pre-defined in the repository. The `subagent_creation` skill guides Claude to create persistent `.md` files in `.claude/agents/` when the operator needs specialization. This design:
- Avoids shipping unused subagents
- Keeps the repository minimal and purposeful
- Enables operators to build their own specialized agent team over time

---

## Data Flow

```
Operator idea (natural language)
        │
        ▼
product_discovery ──→ Discovery Summary
        │
        ▼
competitor_research ──→ Competitor Summary  [Browser MCP]
        │
        ▼
feature_generation ──→ JTBD list + Feature Candidates
        │
        ▼
prioritization ──→ MVP Feature Set + Scores
        │
        ▼
prd_generation ──→ Draft PRD (12 sections, markdown)
        │
        ▼
prd_quality_review ──→ Approved PRD
        │
        ▼
Write to outputs/ ──→ [Hook: validate_prd.py] ──→ [Hook: save_artifact.py]
        │
        ▼
Timestamped PRD artifact in outputs/generated_prds/
```

---

## File Persistence

| Path | What Gets Written | When |
|---|---|---|
| `outputs/generated_prds/prd_*.md` | Final approved PRD | After quality review passes |
| `.claude/agents/*.md` | Subagent definitions | When operator requests via subagent_creation skill |

All other data (Discovery Summary, Competitor Summary, etc.) lives in Claude's active context during the session. It is not persisted to disk unless the operator explicitly asks for it.
