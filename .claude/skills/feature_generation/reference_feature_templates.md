# Feature Generation — Templates and Examples

## Feature Record Format

```
Feature: [Short, user-facing name]
Description: [One sentence — what the user can do with this feature]
JTBD: [Which job this fulfills]
Category: Core | Engagement | Operational | Growth
Competitor coverage: All / Most / Few / None
```

---

## Feature Categories Defined

**Core**
Features that deliver the central value proposition. Without these, the product does not exist. These are always MVP candidates.

**Engagement**
Features that improve retention, trust, and repeat use. Often important for post-MVP but can be MVP if central to value.

**Operational**
Admin, settings, configuration, account management. Usually lower priority for MVP.

**Growth**
Referral, sharing, virality, discovery mechanisms. Usually post-MVP for V1.

---

## Naming Conventions

Use user-facing language:
- "Customer check-in" not "visit logging endpoint"
- "Reward rule builder" not "discount configuration module"
- "Loyalty dashboard" not "analytics component"
- "Push notification campaign" not "notification service"

---

## Example Feature List — Coffee Shop Loyalty App

```
Feature: QR Code Check-In
Description: Customer scans a QR code at the counter to log their visit instantly.
JTBD: Track visits quickly at counter
Category: Core
Competitor coverage: Most

Feature: Digital Stamp Card
Description: Customer earns a virtual stamp for each qualifying purchase, visible in their mobile wallet.
JTBD: Track visits quickly at counter
Category: Core
Competitor coverage: All

Feature: Reward Rule Builder
Description: Owner sets rules once (e.g., "10 stamps = 1 free drink") and rewards apply automatically.
JTBD: Run automatically without management
Category: Core
Competitor coverage: Most

Feature: Push Notification Campaign
Description: Owner sends a custom push notification to all customers or a filtered segment.
JTBD: Send targeted promotions
Category: Engagement
Competitor coverage: Most

Feature: Customer Segments
Description: Filter customers by visit frequency, last visit date, or reward status.
JTBD: Send targeted promotions
Category: Engagement
Competitor coverage: Few

Feature: Win-Back Automation
Description: Automatically send a "we miss you" offer to customers who haven't visited in N days.
JTBD: Re-engage lapsed customers
Category: Engagement
Competitor coverage: Few

Feature: Loyalty Analytics Dashboard
Description: Owner sees total visits, active customers, reward redemption rate, and top loyal customers.
JTBD: See loyalty analytics
Category: Operational
Competitor coverage: Most

Feature: Apple/Google Wallet Integration
Description: Customers can add their stamp card to their mobile wallet for easy access.
JTBD: Track visits quickly at counter
Category: Engagement
Competitor coverage: Few

Feature: Owner Onboarding Wizard
Description: Step-by-step setup guide that gets a new owner from signup to first stamp card in under 5 minutes.
JTBD: Run automatically without management
Category: Core
Competitor coverage: None (gap found in research)

Feature: Multi-Location Support
Description: Owner manages loyalty across 2–3 locations from a single account.
JTBD: Run automatically without management
Category: Operational
Competitor coverage: Most (but complex UX noted as weak)
```
