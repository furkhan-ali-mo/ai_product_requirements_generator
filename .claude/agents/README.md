# .claude/agents/

This directory is intentionally empty.

Subagents are not pre-bundled in this repository. They are created dynamically by Claude during a session, guided by the `subagent_creation` skill.

## How to Create a Subagent

During a Claude Code session, say:

```
Use the subagent_creation skill to create a [subagent type] subagent.
```

Claude will ask you for the subagent spec and write the definition file here.

## Templates and Examples

See `.claude/skills/subagent_creation/` for:
- `reference_subagent_template.md` — file format and frontmatter reference
- `reference_subagent_examples.md` — ready-to-adapt examples (market analyst, persona builder, user story writer)

## What Gets Created

Each subagent is a markdown file with YAML frontmatter:

```
.claude/agents/
└── market_analyst.md
└── persona_builder.md
└── user_story_writer.md
```

Once created, subagents persist across sessions and Claude will use them automatically when their `description` matches the task at hand.
