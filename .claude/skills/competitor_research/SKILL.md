# Skill: competitor_research

## When to Use

Use this skill after `product_discovery` has produced a Discovery Summary. Use it any time the operator asks for a market scan, competitive landscape analysis, or wants to understand what already exists.

## What It Solves

Operators often have blind spots about what's already been built. This skill systematically identifies competitors, extracts their positioning and feature signals, and surfaces the gaps your product can fill.

## Workflow

**Phase 1 — Search (Browser/Search MCP)**
Using the Discovery Summary as input, search for direct and indirect competitors.

Search queries to construct (see `reference_search_strategy.md`):
- Direct: "[problem] app", "[target user] software", "[use case] tool"
- Adjacent: tools that solve the same JTBD differently
- Category: app store searches, Product Hunt, G2 listings

Identify 3–5 competitors. For each, capture:
- Product name and URL
- Target user
- Core value proposition
- Top 3–5 features
- Pricing model
- Notable weaknesses or complaints (from reviews, if accessible)

**Phase 2 — Synthesis**
Build a Competitor Summary (see format in `reference_analysis.md`):
- Competitors table
- Common features (what everyone does)
- Gaps (what none or few do well)
- Differentiation opportunity

**Phase 3 — Signal Extraction**
Identify 2–3 market signals relevant to the operator's product:
- Is the market growing or shrinking?
- Are there user complaints that suggest unmet needs?
- Are incumbents moving upmarket, leaving a gap?

## Expected Outputs

- Competitor Summary with table and gap analysis
- Ready for handoff to `feature_generation`

## Key Guardrails

- Do not invent competitors. Only cite what you can find or reasonably know.
- If Browser/Search MCP is unavailable, use Claude's training knowledge but flag it clearly as potentially outdated.
- Do not turn this into a deep investment analysis — stay focused on product signals.
- Limit to 3–5 direct competitors. Do not sprawl into 10+ tangential tools.

## Reference Files

- `reference_search_strategy.md` — how to construct effective search queries for this domain
- `reference_analysis.md` — Competitor Summary format, gap analysis framework, signal extraction examples
