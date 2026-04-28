# Rendimension Express Estimator

**Live URL:** https://quotes.rendimension.com
**Owner:** Hugo — Rendimension
**Stack:** Single HTML file (vanilla HTML/CSS/JS, no frameworks)

## What is this?

A premium online quoting tool for architectural visualization services.
Clients can build their own estimate in ~2 minutes and either pay a deposit,
request an email quote, or book a consultation call.

## Brand Slogan

**It's not seeing it. It's knowing it's right.**

## Project Structure

```
rendimension-cotizador/
  CLAUDE.md                ← Master instructions for Claude Code
  README.md                ← This file
  src/
    index.html             ← The cotizador (single file, deploy this)
  docs/
    BLUEPRINT.md           ← Full flow design with screen-by-screen specs
    PRICING-MASTER.txt     ← All service prices and rules
    BRAND-NOTES.txt        ← Brand config, colors, API key placeholders
    FLOW-WIREFRAME.txt     ← Original wireframe
    MARKETING-AUDIT.md     ← CRO audit (strategy reference only)
  agents/
    AGENT-SYSTEM.md        ← 4-agent copy pipeline (must-read before editing text)
  deploy/
    DEPLOY-GUIDE.md        ← How to upload to cPanel / HostGator
```

## Quick Start for Claude Code

1. Read `CLAUDE.md` first — it has everything
2. The deliverable is `src/index.html`
3. Before changing ANY user-facing text, read `agents/AGENT-SYSTEM.md`
4. For pricing logic, read `docs/PRICING-MASTER.txt`
5. To deploy, follow `deploy/DEPLOY-GUIDE.md`

## Two Client Paths

**Homeowner path:** Guided, warm, simple language. System recommends a package.
**Professional path:** Fast, direct, full configurator with all services.

Both paths converge at the contact form and estimate screen.

## Key Integrations (Not Yet Configured)

- **Stripe:** For deposit payments (tiered by estimate total)
- **EmailJS:** For sending estimates to client email + notifying Hugo
- **Calendly:** For booking consultation calls
- **Google Analytics:** For tracking (Phase 3)
