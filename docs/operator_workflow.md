# Operator Workflow Guide

This document explains how to use the claude_code_prd_generator workspace as an operator inside Claude Code.

---

## Setup (First Time)

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd claude_code_prd_generator
   ```

2. **Configure MCP servers**
   ```bash
   cp .env.example .env
   # Edit .env with your MCP API keys
   ```

3. **Launch Claude Code**
   ```bash
   claude
   ```
   Claude will automatically load `CLAUDE.md` on startup.

---

## Standard Workflow

### Step 1: Trigger the orchestration skill

Say:
```
Use the prd_operator_workflow skill to generate a PRD for this idea: [your idea]
```

Example:
```
Use the prd_operator_workflow skill to generate a PRD for this idea:
A B2B SaaS tool that helps solo consultants track client project hours,
auto-generate invoices, and send payment reminders without switching between
different tools.
```

### Step 2: Answer discovery questions

Claude will ask 4–6 targeted questions to clarify your idea. Answer them concisely. If you're unsure, say so — Claude will flag the assumption.

Example exchange:
```
Claude: Who is your primary user? Describe their role and context.

You: Freelance consultants and independent contractors, typically working alone,
     billing 3–8 clients at a time. They're not accountants — they just want
     to get paid without the admin overhead.
```

### Step 3: Review research findings

Claude will share a Competitor Summary after running market research. You can:
- Accept it and move on
- Ask Claude to dig deeper into a specific competitor
- Point out a competitor Claude missed

### Step 4: Review feature generation

Claude will present the Feature Candidate List with JTBD mappings. You can:
- Accept the list
- Ask Claude to add a specific feature you care about
- Ask why a feature was or wasn't included

### Step 5: Review MVP scope

Claude will present the prioritized MVP feature set. This is the most important review point. You can:
- Accept the MVP scope
- Add a feature (Claude will explain the trade-off)
- Cut a feature to simplify further

### Step 6: Wait for PRD generation

Claude writes the full 12-section PRD. No interaction needed during this step.

### Step 7: PRD is validated and saved

Hooks run automatically:
- `validate_prd.py` checks all 12 sections
- `save_artifact.py` saves to `outputs/generated_prds/`

Claude will confirm the save path:
```
PRD saved: outputs/generated_prds/prd_consultant_tracker_20260312_143022.md
```

---

## Optional: Create Subagents

If you want a specialized agent for ongoing work (e.g., a dedicated market analyst), say:

```
Use the subagent_creation skill to create a market analyst subagent.
```

Claude will ask for the spec and write the subagent file to `.claude/agents/`. The subagent persists across sessions.

---

## Retrieving Your PRD

Your PRD is saved to:
```
outputs/generated_prds/prd_[product_slug]_[timestamp].md
```

Open it with any markdown viewer, paste it into Notion, or share it directly with your team.

---

## Tips for Best Results

**Be specific in your initial idea.** The more context you give, the fewer clarifying questions Claude needs to ask.

**Trust the MVP scope.** Claude applies strict prioritization rules. If you're pushing back on cuts, ask Claude to explain the JTBD test — it's usually right.

**Use subagents for repeat work.** If you're running multiple PRDs in the same market, create a market analyst subagent once and reuse it across sessions.

**Review the Risks section carefully.** The assumptions listed there are the ones most likely to break your hypothesis. Address them before building.

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Hook fails with "missing sections" | Ask Claude to add the missing section before saving |
| Competitor research returns no results | MCP may be unconfigured. Check `.env`. Claude will fall back to training knowledge. |
| PRD saved to wrong location | Check `PROJECT_ROOT` in `.claude/settings.json` |
| Claude doesn't follow the workflow | Check that `CLAUDE.md` is present in the repo root |
