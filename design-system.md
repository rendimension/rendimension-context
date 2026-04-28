# Rendimension Proposal — Design System

## FORMAT

- Page size: Letter (8.5 × 11 in)
- Orientation: Portrait
- One slide = one page, no exceptions
- Overflow rule: if content does not fit, reduce text — never allow overflow or overlap

---

## LAYOUT

### Page Frame
```
Margin top:    0.65 in
Margin bottom: 0 (footer handles it)
Margin left:   0.75 in
Margin right:  0.75 in
Max content width: 7 in
```

### Slide Structure
```
[HEADER]   — brand mark + slide label        ~0.5 in
[CONTENT]  — main body, flex column          fills remaining
[FOOTER]   — brand + client + page number    ~0.4 in
```

### Overflow Enforcement
- Screen: slides render at 850px × 1100px with `overflow:hidden`
- Print: `height:11in; overflow:hidden` — hard stop
- Content that disappears = content that exceeds capacity = must be cut, not rearranged

---

## TYPOGRAPHY

### Fonts
- Headings: Georgia (serif)
- Body, labels, UI: Inter (sans-serif)

### Scale

| Role | Size (screen) | Size (print) | Font | Weight |
|---|---|---|---|---|
| Cover title | 72px | 60pt | Georgia | 400 |
| Section heading | 36px | 30pt | Georgia | 400 |
| Section heading small | 30px | 26pt | Georgia | 400 |
| Package name (3-pkg) | 20px | 16pt | Georgia | 400 |
| Package name (4-pkg) | 16px | 13pt | Georgia | 400 |
| Step title | 20px | 17pt | Inter | 400 |
| Body text | 14px | 10pt | Inter | 400 |
| Table body (3-pkg) | 13px | 9.5pt | Inter | 400 |
| Table body (4-pkg) | 11px | 8.5pt | Inter | 400 |
| Label / eyebrow | 11px | 9pt | Inter | 700 |
| Caption / note | 11px | 8pt | Inter | 400 |
| Footer | 10px | 8pt | Inter | 500 |

---

## COLORS

```
--navy:       #1A2744   Primary headings, borders
--gold:       #C9A84C   Accents, checkmarks, underlines, pills
--gold-tint:  #F6EED6   Light gold fills
--gold-wash:  #FBF6E6   Featured column background
--ink:        #2C3040   High-contrast body text
--body:       #4A5068   Standard body text
--muted:      #8A8F9E   Labels, captions
--rule:       #E3E3E6   Dividers
--rule-soft:  #EFEFF2   Table row dividers
--paper:      #FFFFFF   Page background
```

---

## SLIDE TEMPLATES

### TEMPLATE 1 — Cover
```
Layout: Single column, left-aligned
- Brandmark + gold rule
- Cover title (Georgia, large) — project type
- Subtitle (Georgia italic, gold) — "Prepared for [Client]"
- Horizontal rule
- 2-col meta grid: [Client info] | [Project info]
- Date
Cap: title max 5 words
```

### TEMPLATE 2 — Real Challenge
```
Layout: 2-column grid (1fr 1fr), 48px gap
Left: eyebrow + heading + underline + 2 challenge paragraphs + pull quote + close
Right: eyebrow + heading + underline + intro line + 4 bullet points
Cap: 2 paragraphs per column max, 4 bullets max
```

### TEMPLATE 3 — Our Approach
```
Layout: Header + 3-column step grid
- Intro line (1 sentence)
- 3 steps: gold border top + number + title + description
Cap: 50 words per step max
```

### TEMPLATE 4 — Options Table (3-package)
```
Columns: Question (44%) | Pkg1 (18.67%) | Pkg2 (18.67%) | Pkg3 (18.67%)
Header: package name + price
Rows: question + 3 check values
Summary: answered count + readiness label
Rules:
  - Max 14 data rows total
  - Row height: fixed — no wrapping in check cells
  - Featured column (middle): gold-wash background
  - Font: 13px body
  - Check values: yes | no | text:LABEL (max 2 words)
```

### TEMPLATE 4B — Options Table (4-package)
```
Columns: Question (34%) | Pkg1 (16.5%) | Pkg2 (16.5%) | Pkg3 (16.5%) | Pkg4 (16.5%)
Header: package name + price (all 4 visible)
Rules:
  - Max 12 data rows total (fewer than 3-pkg due to extra column)
  - Row height: fixed, tighter than 3-pkg
  - Featured column (Option 3): gold-wash background
  - Font: 11px body, 10px labels
  - Question text: max 7 words per row (shorter than 3-pkg)
  - Check values: yes | no only (no text labels — no space)
  - Package name: shorter labels (max 2 words)
  - Price: visible on all 4 columns — no "custom" or "TBD"
```

### TEMPLATE 5 — What's Included
```
Layout: 3×2 grid (6 cards max)
Each card: number (gold) + pill + title + description + optional subs
Rules:
  - Max 6 deliverables
  - Title: 3 words max
  - Description: 30–40 words max
  - Subs: 4 items max
  - Font: title 16px, body 12px, subs 11px
```

### TEMPLATE 6 — Next Steps
```
Layout: Single column
- Body lines (4 max, 20 words each)
- Italic close (1 sentence)
- CTA box: question (left, Georgia italic) + signoff (right, gold divider)
```

---

## PRINT RULES

```css
@media print {
  section.slide {
    width: 8.5in;
    height: 11in;
    overflow: hidden;
    page-break-after: always;
  }
  .pad { padding: 0.65in 0.75in 0.45in 0.75in; }
}
```
