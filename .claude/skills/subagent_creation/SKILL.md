# Skill: subagent_creation

## When to Use

Use this skill when:
- The operator asks to create a specialized Claude subagent
- The current workflow would benefit from a dedicated specialist (e.g., a market analyst, persona builder, or user story writer)
- The operator says something like: "Can you create a subagent for competitor research?"

This skill creates **permanent subagent files** in `.claude/agents/`. These persist across sessions.

## What It Solves

Claude Code supports custom subagents defined as markdown files in `.claude/agents/`. This skill helps the operator create well-structured, useful subagents interactively — rather than creating them ad hoc with poor descriptions.

## Workflow

**Phase 1 — Collect Subagent Spec**
Ask the operator these questions (can be asked together):

1. What should this subagent be named? (used as filename, e.g., `market_analyst`)
2. What is its purpose in one sentence?
3. What specific tasks should it handle? (scope boundaries)
4. What model should it use? (default: claude-sonnet-4-6)
5. What tools should it have access to? (e.g., WebSearch, Read, Write)
6. Should it preload any skills from `.claude/skills/`?
7. What is the expected output format? (markdown report, structured list, JSON, etc.)
8. Should it have read-only access, or can it write files?

**Phase 2 — Generate Subagent File**
Using the collected spec, write a subagent definition file to `.claude/agents/[name].md`.

Follow the subagent file format in `reference_subagent_template.md`.

**Phase 3 — Confirm with Operator**
After creating the file:
- Show the operator the created file path
- Summarize the subagent's purpose, tools, and task boundaries
- Explain how to invoke it: "Ask Claude: use the [name] subagent to [task]"

## Expected Outputs

- A permanent subagent file at `.claude/agents/[subagent_name].md`
- Confirmation message with invocation instructions

## Key Guardrails

- Never create a subagent without collecting the spec first.
- Do not grant write permissions to subagents unless the operator explicitly confirms.
- Subagent names must be lowercase with underscores (e.g., `market_analyst`, not `MarketAnalyst`).
- Do not pre-create subagents speculatively — only when the operator requests it.
- Keep subagent scope narrow. A focused subagent is more useful than a general one.

## Reference Files

- `reference_subagent_template.md` — subagent file format, frontmatter fields, system prompt structure
- `reference_subagent_examples.md` — example subagent definitions for common PRD workflow roles
