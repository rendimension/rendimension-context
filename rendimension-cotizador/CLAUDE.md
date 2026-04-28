# CLAUDE.md — Rendimension Express Estimator

## Project Overview

This is the Rendimension Express Estimator — a premium online quoting system
deployed at **quotes.rendimension.com**. It is a single HTML file with all
CSS and JavaScript inline, hosted on cPanel (HostGator Mexico).

**Owner:** Hugo — Rendimension
**Business:** Architectural visualization — 3D renderings, VR/AR experiences,
architectural drafting, and website development for real estate and
construction clients in the US market.

## Brand Positioning

**Slogan:** It's not seeing it. It's knowing it's right.

Rendimension does NOT sell renders. It sells **certainty before construction
decisions**. Clients use visualization to make expensive design, renovation,
presentation, and investment decisions with more confidence.

## Architecture

- **Platform:** Single HTML file (no frameworks, no build step)
- **Hosting:** quotes.rendimension.com via cPanel File Manager
- **Deploy:** Upload `src/index.html` as `index.html` to `/home2/rendimen/quotes.rendimension.com/`
- **Payments:** Stripe Checkout (redirect mode) — keys not yet configured
- **Email:** EmailJS — keys not yet configured
- **Booking:** Calendly — link not yet configured

## Key Files

```
src/index.html          ← The cotizador. THE deliverable. Everything is here.
docs/BLUEPRINT.md       ← Full flow design, screen-by-screen specs, copy
docs/PRICING-MASTER.txt ← All service prices and pricing rules
docs/BRAND-NOTES.txt    ← Brand config, colors, API keys (placeholders)
docs/FLOW-WIREFRAME.txt ← Original wireframe with all screens
docs/MARKETING-AUDIT.md ← CRO audit (use for strategy, NOT for copy voice)
agents/AGENT-SYSTEM.md  ← 4-agent pipeline for all copy decisions
deploy/DEPLOY-GUIDE.md  ← How to upload to cPanel
```

## The 4-Agent Copy Pipeline

Every piece of text in the cotizador MUST pass through this pipeline.
Read `agents/AGENT-SYSTEM.md` for full details.

**Order:**
1. **Decision Certainty Agent** — Translates product language → decision support language
2. **Anti-Cliche Brand Language Agent** — Kills generic phrases, enforces premium voice
3. **Language Simplification Agent** — Converts to 8th-grade readability
4. **UX Flow & Conversion Agent** — Places copy in the right screen, validates flow

**BANNED phrases** (never use in any copy):
- visualize your vision
- bring ideas to life
- stunning renderings / stunning visuals
- immersive experience(s)
- cutting edge
- elevate your project
- close deals faster
- beat the competition
- transform your vision into reality
- showcase your property
- photorealistic excellence

**Preferred voice:**
- Clear over clever
- Calm over urgent
- Specific over abstract
- Useful over impressive
- Premium through restraint, not through adjectives
- Sounds like a serious firm, not a SaaS landing page

## Dual-Path Flow

The cotizador has TWO paths based on who the client is:

### Path A: Homeowner / Personal Project
```
Hero → Who Are You? (select "personal") → What are you working on?
→ What do you want to feel sure about? → Recommended Package
→ (optional: Customize) → Contact → Estimate
```
- Guided, warm, simple language
- System RECOMMENDS a package based on answers
- Option to customize if they want

### Path B: Professional / Client Project
```
Hero → Who Are You? (select "professional") → Project Type
→ Full Configurator → Contact → Estimate
```
- Fast, direct, full control
- All services visible with checkboxes + sliders
- Running total always visible

### Skip Link
"I already know what I need → Skip to services" bypasses path selection
and goes directly to the full configurator.

## Pricing Rules

### Renderings (per image)
- Standard Rendering: $499
- Detailed Rendering: $750
- Showcase Rendering: $1,200
- Additional Angle: $299 (only visible when Standard or Detailed is selected)
- 3D Floor Plan: $850

### Walkthroughs & Tours (base + per sqft)
- VR Walkthrough (Meta Quest): $3,500 + $2.90/sqft (500-10,000 sqft)
- Browser Tour: $2,500 + $1.50/sqft (500-10,000 sqft)
- Video Walkthrough: $2,500 + $2.00/sqft (500-10,000 sqft)
- Interactive VR: $3,500 + $4.00/sqft (500-10,000 sqft)

### Drafting & Design
- Construction Drawings: $380/plan (1-20)
- Architectural Design: $3.50/sqft (500-20,000 sqft)
  - Includes 1 Standard Rendering per 1,000 sqft (auto-calculated)

### Website (radio selection, one at a time)
- No website needed (default)
- Project Landing Page: $7,000
- Business Website: $9,500
- Full Brand Site: $14,500
- E-commerce / Portal: $18,000

## Conversion Tier Logic

The estimate screen shows different CTAs based on total:

| Total | Primary CTA | Deposit |
|-------|-------------|---------|
| Under $2,000 | "Start My Project" | Full payment or 50% |
| $2,000 – $10,000 | "Reserve My Project — $500" | $500 flat |
| Over $10,000 | "Schedule Strategy Session — $250" | $250 reservation |

- Deposits count toward project total
- Benefit framing: "priority scheduling" — NOT "SAVE X% TODAY"
- No fake urgency, no countdown timers, no discount-first language

## Homeowner Package Recommendations

Based on their "what do you want to feel sure about" answer:

| Selection | Recommended Package | Price Range |
|-----------|-------------------|-------------|
| "See how it will look" | 3 Standard Renderings | $1,497 |
| "Compare materials" | 2 Detailed Renderings + 1 Additional Angle | $1,799 |
| "Show family" | 2 Standard Renderings + Browser Tour (1,000 sqft) | $4,498 |
| "HOA/permit" | 3 Standard Renderings + 1 3D Floor Plan | $2,347 |
| "Quick price" | Skip directly to full configurator | — |

## Visual Design

- Dark navy gradient: #0A1628 → #0F2035
- Card background: #132A45
- CTA blue: #1565C0
- Accent bright: #2196F3
- Accent light: #4FC3F7
- Text: #FFFFFF / #B0BEC5
- Font: Inter (Google Fonts, weights 400/500/600/700)
- Border: rgba(33, 150, 243, 0.2)
- Mobile-first, works on all devices
- Cards with hover glow, selected state with blue border
- Progress bar on every screen except hero
- Bottom nav: Estimate | Portfolio | Contact

## What Needs to be Done Next

### Phase 1: Core Build (Current)
- [ ] Verify all screens render correctly
- [ ] Test dual-path flow (homeowner + professional)
- [ ] Test all pricing calculations
- [ ] Test responsive layout (mobile, tablet, desktop)
- [ ] Test auto-advance on card selections
- [ ] Test accordion functionality on services screen
- [ ] Test quote summary panel updates in real-time
- [ ] Test form validation on contact screen
- [ ] Test estimate screen population
- [ ] Test tiered CTA logic (under $2k / $2k-$10k / over $10k)
- [ ] Verify recommended packages for homeowner path

### Phase 2: Integrations
- [ ] Configure EmailJS (Service ID, Template ID, Public Key)
- [ ] Configure Stripe Checkout (Publishable Key, deposit logic)
- [ ] Configure Calendly link for consultation booking
- [ ] Set up Hugo notification email on every submission
- [ ] First-time email token logic (localStorage)

### Phase 3: Polish
- [ ] Add real testimonials (replace placeholder)
- [ ] Add real portfolio images
- [ ] Add Rendimension logo (SVG)
- [ ] SEO meta tags
- [ ] Open Graph tags for social sharing
- [ ] Google Analytics tracking
- [ ] Quote ID format: RD-YYMMDD-XXXX

### Phase 4: Post-Launch
- [ ] PDF quote generation
- [ ] CRM integration (HubSpot / Airtable / Google Sheets)
- [ ] n8n automation workflow
- [ ] A/B testing framework
- [ ] Follow-up email sequence

## Development Rules

1. **Single file.** Everything in one HTML file. No separate CSS/JS files.
2. **No frameworks.** Vanilla HTML/CSS/JS only. No React, no Vue, no Tailwind.
3. **Mobile-first.** Design for 375px first, then scale up.
4. **Test every change.** Open in browser and click through both paths.
5. **Run copy through the agent pipeline.** If changing any user-facing text,
   check it against the banned phrases list and voice guidelines.
6. **No fake urgency.** No countdown timers, no "SAVE X% TODAY", no promo language.
7. **Deposits, not discounts.** Frame as "counts toward your total" + "priority scheduling".
8. **8th-grade readability.** Short sentences. Simple words. One idea per sentence.

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)
