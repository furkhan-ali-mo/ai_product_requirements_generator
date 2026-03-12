# Competitor Research — Search Strategy

## Query Construction

Construct searches from the Discovery Summary. Use 3–5 different query types.

### Query Templates

| Intent | Query Pattern | Example |
|---|---|---|
| Direct competitors | "[core use case] app" | "loyalty program app for small businesses" |
| User-based search | "[target user] software tools" | "coffee shop owner management tools" |
| Problem-based | "how to [solve the problem]" | "how to run digital loyalty program without developer" |
| Product Hunt | "site:producthunt.com [use case]" | "site:producthunt.com loyalty app" |
| Review aggregators | "best [category] software 2024" | "best loyalty program software small business" |
| App Store analogue | "[use case] iOS app" | "loyalty stamp card iOS app" |

---

## MCP Usage

When Browser/Search MCP is available:
1. Run 3–5 queries using the search tool
2. For the top 3 results per query, fetch the page content
3. Extract: product name, value prop, features, pricing, user reviews

When MCP is unavailable:
- Fall back to Claude's training knowledge
- Clearly label outputs: `[Note: based on training data, may be outdated]`

---

## What to Look For

On competitor websites and listings, capture:
- **Tagline** — what they claim to do
- **Target user** — who they say they serve
- **Top features** — what they lead with
- **Pricing** — free tier, paid plans, pricing model
- **Reviews/complaints** — from G2, Capterra, App Store, Product Hunt comments

---

## Competitor Tiers

Organize findings into tiers:

**Tier 1 — Direct Competitors**
Same target user, same core problem. These are the most important to analyze.

**Tier 2 — Adjacent Competitors**
Similar problem, different user segment or platform. Watch these for feature trends.

**Tier 3 — Indirect Alternatives**
What users do today without dedicated software (spreadsheets, paper, etc.). Important for understanding switching behavior.

---

## Red Flags to Note

- A competitor that's well-funded and moving into your exact space
- A market where multiple startups have failed — note why
- A dominant incumbent where users are very locked in (switching costs)
