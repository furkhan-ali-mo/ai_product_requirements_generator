# Prioritization — Scoring Reference

## Value/Effort Matrix

### Value Scoring Rubric

**High (H)**
- Directly delivers the core value proposition
- Users cannot accomplish their primary JTBD without it
- Strong signal from discovery that users would switch for this
- Competitor gap: none or few competitors do this well

**Medium (M)**
- Improves the core experience but isn't strictly required
- Would increase retention or engagement meaningfully
- Nice-to-have in V1 that experienced users would notice

**Low (L)**
- Marginal improvement to the experience
- Primarily operational or administrative
- Could wait until post-MVP without affecting core adoption

---

### Effort Scoring Rubric

**Low (L)**
- Can be implemented in days, not weeks
- Mostly UI/UX, no complex backend logic
- No third-party integrations required
- Standard patterns the team has built before

**Medium (M)**
- Requires 1–2 weeks of focused work
- Some backend logic or data modeling required
- One integration (e.g., push notifications, Stripe)

**High (H)**
- Requires 3+ weeks or significant complexity
- Multiple integrations, real-time features, or complex algorithms
- Significant testing and edge cases

---

## MVP Priority Matrix

```
         LOW EFFORT   MED EFFORT   HIGH EFFORT
HIGH VAL    MVP ★       MVP          Post-MVP
MED VAL     MVP         Post-MVP     Post-MVP
LOW VAL     Post-MVP    Post-MVP     Post-MVP
```

★ = Priority 1 — build first

---

## RICE Scoring Formula

Use RICE for close calls (features on the MVP/Post-MVP border).

```
RICE Score = (Reach × Impact × Confidence) / Effort

Where:
  Reach      = estimated % of users who benefit per period (1–10)
  Impact     = how much it moves the needle per user (1–10)
  Confidence = how certain are the estimates (0.5 / 0.8 / 1.0)
  Effort     = relative build effort in person-weeks (1–10)
```

Higher RICE score = higher priority.

---

## Tie-Breaking Rules

When two features have the same score:
1. Prefer the feature that unlocks other features downstream
2. Prefer the feature that addresses the highest-volume JTBD
3. Prefer the feature that differentiates from all competitors (gap feature)
4. Ask the operator to make the final call

---

## Example Scoring Table

| Feature | Value | Effort | RICE | Priority |
|---|---|---|---|---|
| QR Code Check-In | H | L | 9.6 | MVP ★ |
| Digital Stamp Card | H | L | 8.8 | MVP ★ |
| Reward Rule Builder | H | M | 7.2 | MVP |
| Owner Onboarding Wizard | H | M | 6.8 | MVP |
| Push Notification Campaign | M | M | 5.4 | MVP |
| Customer Segments | M | M | 4.8 | Post-MVP |
| Win-Back Automation | M | H | 3.2 | Post-MVP |
| Loyalty Analytics Dashboard | M | M | 4.4 | Post-MVP |
| Apple/Google Wallet Integration | M | H | 2.8 | Post-MVP |
| Multi-Location Support | L | H | 1.6 | Post-MVP |
