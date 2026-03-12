# Subagent File Template

## File Location

All subagent files are saved to:
```
.claude/agents/[subagent_name].md
```

Naming rules:
- Lowercase only
- Words separated by underscores
- Descriptive and specific: `market_analyst` not `agent1`

---

## Subagent File Format

```markdown
---
name: [subagent_name]
description: [One sentence — when Claude should use this subagent. Be specific about triggers.]
model: claude-sonnet-4-6
tools:
  - [ToolName]
  - [ToolName]
---

# [Subagent Display Name]

## Purpose

[2–3 sentences describing what this subagent does and why it exists as a specialist.]

## Scope

This subagent handles:
- [Task 1]
- [Task 2]

This subagent does NOT handle:
- [Out of scope task 1]
- [Out of scope task 2]

## Behavior

[Describe how the subagent should approach its tasks. Include:
- What inputs it expects
- How it processes them
- What format it outputs in]

## Output Format

[Describe the exact output structure expected. Examples:
- A markdown report with sections [X, Y, Z]
- A JSON object with keys [a, b, c]
- A bulleted list of findings]

## Guardrails

- [Specific constraint 1]
- [Specific constraint 2]
```

---

## Frontmatter Fields Explained

| Field | Description | Example |
|---|---|---|
| `name` | Filename slug (lowercase_underscores) | `market_analyst` |
| `description` | When to use this agent — Claude uses this to decide when to invoke it | `Use when researching competitor products and market positioning` |
| `model` | Claude model ID | `claude-sonnet-4-6` |
| `tools` | List of tools this agent can access | `WebSearch`, `Read`, `Write` |

---

## Available Tools Reference

Common tools you can grant to subagents:

| Tool | Purpose |
|---|---|
| `Read` | Read files from the filesystem |
| `Write` | Write files to the filesystem |
| `WebSearch` | Search the web (requires Search MCP) |
| `WebFetch` | Fetch content from a URL |
| `Bash` | Execute shell commands |
| `Grep` | Search file contents |
| `Glob` | Find files by pattern |

Grant only the tools the subagent genuinely needs. Prefer `Read`-only access unless writing is required.
