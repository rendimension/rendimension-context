---
name: campaign-optimization-rules
description: Rules engine for campaign optimization including when to kill, scale, refresh, or restructure ads, budget reallocation logic, A/B test conclusion criteria, and optimization calendar.
---

# Campaign Optimization Rules

## Kill Rules
- Meta: CTR <0.5% after 1K impressions, CPL >2x target ($160+), zero leads after $100
- LinkedIn: CTR <0.2% after 5K impressions, CPL >2x target ($500+), zero leads after $200

## Scale Rules
- CPL below target 7+ days → increase budget 20% max
- Wait 3-4 days between increases
- Alternative: duplicate winning ad set with new audience

## Refresh Rules
- Frequency >3 and rising → new creative
- CTR declining 2 weeks → refresh
- Keep winning HOOK, change VISUAL (or vice versa)

## Budget Reallocation (Weekly)
- Bottom 25% by CPL → reduce 30% or pause
- Top 25% → increase 20%
- Maintain 30% for testing

## A/B Test Criteria
- Min 1K impressions/variant (Meta), 5K (LinkedIn)
- Min 7 days
- Winner needs 20%+ better CPL

## Calendar
Day 1-3: HANDS OFF | Day 4-7: Monitor | Day 7: Kill losers | Day 14: Optimize | Day 21: Scale winners | Day 28: Full review
