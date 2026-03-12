# Orchestration Reference — prd_operator_workflow

## Inter-Step Handoff Format

After each step, package the outputs into a structured context block before moving to the next step. This ensures downstream skills have everything they need.

### After Step 1 (Discovery)
```
DISCOVERY SUMMARY
- Product idea: [one sentence]
- Core problem: [one sentence]
- Target user: [one sentence]
- Key insight: [one sentence]
- Constraint: [any technical/budget/time constraint mentioned]
```

### After Step 2 (Competitor Research)
```
COMPETITOR SUMMARY
- Competitors identified: [list 3–5 names]
- Common features across competitors: [list]
- Gaps/weaknesses found: [list]
- Differentiation opportunity: [one sentence]
```

### After Step 3 (Feature Generation)
```
FEATURE CANDIDATE LIST
- [Feature name]: [one-line description] | JTBD: [job it addresses]
- ... (10–20 features)
```

### After Step 4 (Prioritization)
```
MVP FEATURE SET (scored)
- [Feature]: Value [H/M/L] | Effort [H/M/L] | Priority [1–N]
MVP includes: [list features in MVP]
Post-MVP: [list deferred features]
```

## Subagent Decision Point

Before Step 2, evaluate whether a subagent would accelerate the research:

- If the idea is in a complex/niche market → consider creating a `market_analyst` subagent via `subagent_creation`
- If the idea requires deep persona work → consider creating a `persona_builder` subagent
- Otherwise, proceed without subagents

To create a subagent: load `.claude/skills/subagent_creation/SKILL.md` and follow the interactive process before resuming the main workflow.

## Progress Signaling

At each step transition, briefly signal to the operator:

```
✓ Step 1 complete — Discovery Summary captured
→ Starting Step 2: Competitor Research...
```

This keeps the operator informed without requiring interaction.

## Error Handling

| Situation | Action |
|---|---|
| Operator idea is non-software | Stop, explain scope constraint, ask to reframe |
| Competitor search returns no results | Note limitation, proceed with known market analogues |
| Feature list has fewer than 8 features | Ask operator to expand before prioritizing |
| PRD fails quality review | Fix specific gaps, do not re-run entire workflow |

## Final Confirmation Message

After saving the artifact, deliver this to the operator:

```
PRD generation complete.

Saved to: outputs/generated_prds/prd_[timestamp].md

Summary:
- Product: [name]
- MVP Features: [count] features selected
- Competitors analyzed: [count]
- Sections: 12/12 complete

Next steps: review the PRD, share with stakeholders, or ask Claude to create
a specialized subagent for deeper research using the subagent_creation skill.
```
