# Portfolio Case Study Outline

Use this document to structure how you present `claude_code_prd_generator` in a portfolio, interview, or technical writeup.

---

## Recommended Framing

Position this project as:
> "A Claude Code-native workspace that demonstrates deep, practical use of every major Claude Code customization feature — built around a real AI PM use case."

This framing works for:
- Developer portfolio showcases
- AI engineering job applications
- Technical blog posts
- Claude Code ecosystem contributions

---

## Case Study Structure

### 1. Problem Worth Solving (1–2 paragraphs)

Describe the real problem:
- Founders and PMs spend hours turning rough ideas into structured PRDs
- Most AI tools give you a generic template; none guide you through the full discovery → research → prioritization → documentation pipeline
- Claude Code is powerful but its customization features (skills, hooks, MCP, subagents) are underutilized and poorly documented with real-world examples

### 2. Why Claude Code (not a web app)

Explain the deliberate choice:
- The terminal is where builders already work
- Claude Code's context loading, skill composition, and hook system are purpose-built for this kind of workflow
- No deployment, no server, no UI — the workspace IS the product
- This is a demonstration of Claude Code as a platform, not just a chat interface

### 3. Architecture Decisions Worth Highlighting

**Skill design with progressive disclosure**
- SKILL.md under 400 words, all detail in reference files
- Why: Claude's instruction context is finite; lean entry points + rich reference files solve this

**Hooks as deterministic enforcers**
- validate_prd.py ensures no PRD is saved without all 12 sections
- This is the "code guarantees structure; Claude provides intelligence" separation
- Show the hook code — it's clean Python using only stdlib

**Dynamic subagent creation**
- No pre-built agents shipped in the repo
- The subagent_creation skill guides Claude to write permanent `.md` files in `.claude/agents/`
- Show an example of a created subagent file

**MCP as live data layer**
- Competitor research uses Browser/Search MCP for real market data
- This is the key difference between a static prompt and a live research workflow

### 4. Walk Through a Session

Show the full operator experience:
1. Clone repo, run `claude`
2. One trigger prompt: "Use prd_operator_workflow for this idea..."
3. Discovery questions → Research → Feature list → Prioritization → PRD
4. Hook runs, validates, saves artifact
5. Open `outputs/generated_prds/` — PRD is there

If possible, include a screenshot or recording of the terminal session.

### 5. What This Demonstrates (Technical Breadth)

Frame each feature explicitly:

| Feature | Depth of Usage |
|---|---|
| CLAUDE.md | Full workspace instructions including workflow order, writing standards, scope constraints, completion criteria |
| Skills | 8 skills with concise SKILL.md + supporting reference files; modular, composable, standalone-invocable |
| Hooks | PostToolUse hooks with Python validation and artifact persistence; deterministic exit codes |
| MCP | Browser/Search MCP for live competitor research; graceful fallback to training knowledge |
| Subagents | Dynamic creation via skill; interactive spec collection; persistent `.claude/agents/` files |

### 6. What You'd Build Next

Show product thinking, not just technical execution:
- Iterative PRD editing loop
- Slack/Notion export hooks
- Pre-built vertical-specific subagent library
- Multi-idea comparison mode
- Team mode with stakeholder review annotations

### 7. Key Lessons / Insights

Include 2–3 genuine insights from building this:

Examples:
- "Skills work best when you apply progressive disclosure. Trying to put everything in one file kills both readability and Claude's ability to follow it."
- "Hooks are underrated. The ability to enforce deterministic guarantees on Claude's output with code — not just instructions — changes the reliability of AI workflows."
- "Dynamic subagent creation is more useful than pre-built subagents. Operators need specialists tailored to their domain, not generic templates."

---

## Suggested Formats

**For GitHub Portfolio:**
- Strong README (already written) covers most of this
- Add a demo GIF or screenshot to the README
- Pin the repo

**For Blog Post:**
- Use the architecture diagram from `docs/architecture.md`
- Include the full discovery → PRD session as a narrative walkthrough
- Focus on "what this taught me about building Claude Code workspaces"

**For Interview:**
- Lead with the operator experience (the "one trigger" story)
- Go deep on one technical choice (skill design or hooks — pick the one you know best)
- End with: "The broader lesson is that Claude Code is a platform, not a chatbot wrapper."

**For Technical Talk:**
- 5 slides: Problem → Architecture diagram → Live demo → Design decisions → Lessons
- Live demo is essential — the terminal experience is the product
