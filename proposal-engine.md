# Rendimension Proposal Engine

## HOW TO GENERATE A PROPOSAL

Follow these steps in order. Do not skip any.

---

## STEP 1 — INTAKE

Collect from Hugo before generating anything:

```
Client name (full):
Client first name:
Client company:
Project type: medical / residential / investor / retail / historic
Building / project name:
Location (city, state):
Month + Year:
Number of packages: 3 or 4
Package names + prices (all confirmed by Hugo):
Target sale (which package Hugo wants client to choose):
Anchor package (which package makes others feel reasonable):
Minimum acceptable package:
Any specific pain point or context:
```

Do not generate content until all fields are confirmed.

---

## STEP 2 — SELECT FRAMEWORK

Match project type to framework in CLAUDE.md.

Load:
- Problem framing for that type
- Table categories and decision questions for that type
- Deliverable set for that type

---

## STEP 3 — CONFIRM PACKAGE STRATEGY

### For 3 packages:
| Package | Role | Featured |
|---|---|---|
| Option 1 | Entry — limited | No |
| Option 2 | Recommended — practical | YES |
| Option 3 | Premium — complete | No |

### For 4 packages:
| Package | Role | Featured |
|---|---|---|
| Option 1 | Minimum viable | No |
| Option 2 | Solid — practical | No |
| Option 3 | Sweet spot — best balance | YES |
| Option 4 | Anchor — premium, expensive | No |

Pricing check (4-package):
- Option 1 and 2 must not be too close together
- Option 2 and 3 should be close enough that Option 3 feels reachable
- Option 4 must be high enough to anchor perception upward
- All prices visible — no "custom" pricing ever

---

## STEP 4 — BUILD TABLE QUESTIONS

Table rows must be client decision questions, not deliverable counts.

Good format: "Can I [action] with this package?"
- Can I understand the full scope of this project?
- Can I picture the space before it's built?
- Can I share this with a buyer, investor, or tenant?
- Can I use this to launch the project publicly?
- Can I present this in a formal meeting?

Bad format (never use):
- "3 exterior renders"
- "Includes floor plan"
- "Everything in Package 2 plus..."

### Row capacity by package count:
| Structure | Max rows | Max categories |
|---|---|---|
| 3-package | 14 | 4 |
| 4-package | 12 | 4 |

For 4-package: keep question text to 7 words max per row.
For 4-package: use yes/no only — no text labels in check cells.

---

## STEP 5 — GENERATE CONTENT (SLIDE BY SLIDE)

### Slide 1 — Cover
- Title: project type (2–5 words)
- Subtitle: "Prepared for [Client Name]"
- Meta: client name, company, building, location, date

### Slide 2 — Real Challenge
- 2 challenge paragraphs (40–60 words each)
- Pull quote (15–25 words, citable)
- Challenge close (4–6 words, bold)
- Objective intro (1 sentence)
- 4 objective bullets

### Slide 3 — Our Approach
- Intro line (15–20 words)
- 3 steps: title + description (max 50 words each)

### Slide 4 — Options Table
- Heading (8–12 words)
- Intro line (1–2 sentences)
- Decision questions table (see Step 4)
- Summary row: answered count + readiness label per package

### Slide 5 — What's Included
- Max 6 deliverables
- Each: title (3 words max) + description (30–40 words) + subs (4 max)
- Pill labels: "All packages" | "Option X+" | "Option X only"

### Slide 6 — Next Steps
- 4 lines (20 words max each)
- Italic close (12–18 words)
- CTA question (5–8 words)
- Signoff: Hugo's name + email + phone

---

## STEP 6 — CAPACITY CHECK

Before writing HTML, verify each slide fits within limits.

| Slide | Hard limit |
|---|---|
| 2 — Challenge | 2 paragraphs, 4 bullets |
| 3 — Approach | 3 steps, 50 words each |
| 4 — Table (3-pkg) | 14 rows, 4 categories |
| 4 — Table (4-pkg) | 12 rows, 4 categories, 7 words per question |
| 5 — Deliverables | 6 cards, 40 words each |
| 6 — Closing | 4 lines, 20 words each |

If any section exceeds its limit → cut content. Do not adjust the layout.

---

## STEP 7 — GENERATE HTML

1. Copy `proposal-template.html` → `[client-slug]-proposal.html`
2. Edit only the CONFIG object
3. Do not touch anything outside CONFIG
4. For 4-package: use 4 entries in `packages[]` with `featured:true` on Option 3

```bash
cp "C:/Users/rendi/Desktop/proposal-template.html" \
   "C:/Users/rendi/Desktop/[client-slug]-proposal.html"
```

---

## STEP 8 — VALIDATE BEFORE DELIVERING

```
[ ] Pre-build questions answered (3 vs 4, target, anchor, minimum)
[ ] All 6 slides present
[ ] No [PLACEHOLDER] text remaining
[ ] No em-dashes (—) anywhere
[ ] Correct featured package (middle for 3-pkg, Option 3 for 4-pkg)
[ ] All prices confirmed by Hugo — none invented
[ ] No content overflows in browser preview
[ ] File named: [client-slug]-proposal.html
```

---

## NAMING CONVENTION

```
File:  [client-slug]-proposal.html
Slug:  lowercase, hyphens, no spaces
Ex:    sarah-johnson-retail-leasing-proposal.html
       marcus-wei-investor-pitch-proposal.html
```

---

## DELIVERY

- Primary: HTML → browser → Print → Save as PDF (Letter, no margins)
- Secondary: Canva 16:9 deck (on request only)
- Always share path with Hugo for review before sending to client
