# Subagent Design — Dynamic Creation Model

## Philosophy

Subagents in this workspace are not pre-built tools. They are specialist agents created on demand by the operator, guided by Claude using the `subagent_creation` skill.

This design choice reflects a real principle: a subagent built for your specific product domain is more useful than a generic one. A market analyst subagent for the healthcare SaaS space should behave differently than one for consumer mobile apps.

---

## How Subagent Creation Works

1. **Operator requests a subagent**
   ```
   Use the subagent_creation skill to create a market analyst subagent for the
   B2B fintech space.
   ```

2. **Claude collects the spec**
   Claude asks for:
   - Subagent name
   - Purpose (one sentence)
   - Task scope (what it handles / what it doesn't)
   - Model to use
   - Tools allowed
   - Skills to preload
   - Expected output format
   - Read-only or write permissions

3. **Claude writes the subagent file**
   The file is created at `.claude/agents/[name].md` using the standard subagent format.

4. **Subagent persists across sessions**
   Once created, Claude will invoke the subagent automatically when its `description` matches a task.

---

## Subagent File Format

```markdown
---
name: [subagent_name]
description: [When Claude should use this subagent — specific trigger description]
model: claude-sonnet-4-6
tools:
  - WebSearch
  - Read
---

# [Display Name]

## Purpose
[2–3 sentences]

## Scope
Handles: [list]
Does NOT handle: [list]

## Behavior
[Input → Processing → Output description]

## Output Format
[Exact structure of what the subagent returns]

## Guardrails
[Specific constraints]
```

---

## Example: Creating a Market Analyst Subagent

**Operator prompt:**
```
Use the subagent_creation skill to create a market analyst subagent.
```

**Claude's questions:**
```
1. What should this subagent be named? (e.g., market_analyst)
2. What market or domain should it specialize in? (e.g., B2B fintech, consumer mobile)
3. What specific tasks should it handle?
4. Should it have web search access?
5. What format should its reports be in?
```

**Operator answers:**
```
1. fintech_market_analyst
2. B2B fintech — payment infrastructure and billing tools for SMBs
3. Competitor research, market gap analysis, pricing research
4. Yes, web search
5. Markdown report with competitor table and gap section
```

**Resulting file: `.claude/agents/fintech_market_analyst.md`**

```markdown
---
name: fintech_market_analyst
description: Use when researching competitors, market positioning, or pricing in the B2B fintech space — specifically payment infrastructure and billing tools for SMBs.
model: claude-sonnet-4-6
tools:
  - WebSearch
  - WebFetch
  - Read
---

# Fintech Market Analyst

## Purpose

Specializes in competitive research and market analysis for B2B fintech products targeting SMB payment infrastructure and billing. Returns structured competitor landscapes with gap analysis.

## Scope

Handles:
- Competitor identification in B2B fintech / billing / payment tools
- Pricing model research and benchmarking
- Feature gap identification vs. market leaders
- Market signal extraction from news, reviews, and product launches

Does NOT handle:
- Feature generation or prioritization
- PRD writing
- User persona creation

## Behavior

1. Accepts: product category, target user, optional geographic scope
2. Searches for direct competitors using fintech-specific query patterns
3. Extracts pricing, features, positioning from competitor pages
4. Returns structured Competitor Summary

## Output Format

Markdown report with:
- Competitors table (name, target segment, pricing, top features, weakness)
- Common features across market
- Identified gaps
- Differentiation opportunity paragraph

## Guardrails

- Only cite products that exist and can be verified
- Flag data older than 12 months
- Do not invent pricing data
- Focus on SMB-relevant competitors, not enterprise-only tools
```

---

## When to Create Subagents

Consider creating a subagent when:
- You will run multiple PRD sessions in the same market vertical
- You want consistent competitor research methodology across sessions
- You need a persona builder with deep knowledge of a specific user type
- You want a user story writer that references your company's specific personas

Avoid creating subagents for one-off tasks — use skills directly instead.

---

## Subagent vs. Skill: When to Use Each

| Use a Skill when... | Use a Subagent when... |
|---|---|
| Following a standard workflow step | Specializing for a specific domain |
| Running the full PRD pipeline | Persistent research across many sessions |
| The task is one-time | The task will recur frequently |
| You need step-by-step orchestration | You need a focused specialist |
