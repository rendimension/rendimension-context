---
name: platform-format-selector
description: Decision engine for selecting optimal ad formats per platform, with decision matrix mapping objective, audience, and funnel stage to recommended format, specs, and variant requirements.
---

# Platform Format Selector

## Meta Decision Matrix (Rendimension)

| Objective | Funnel | Format | Specs | Variants |
|---|---|---|---|---|
| Awareness | Top | Reel | 1080x1920, 15-30s | 3 |
| Awareness | Top | Single Image | 1080x1350 | 3 |
| Engagement | Top | Carousel | 1080x1080, 5-7 cards | 2 |
| Lead Gen | Middle | Single Image + Form | 1080x1080 | 3 |
| Lead Gen | Middle | Video | 1080x1080, 30-60s | 2 |
| Conversions | Bottom | Testimonial | 1080x1350 | 2 |
| Retargeting | Bottom | Before/After Carousel | 1080x1080, 4 cards | 2 |

## LinkedIn Decision Matrix (Reflex)

| Objective | Funnel | Format | Specs | Variants |
|---|---|---|---|---|
| Awareness | Top | Single Image | 1200x628 | 3 |
| Thought Leadership | Top | Document Carousel | 1080x1080 PDF, 5-7 pages | 2 |
| Lead Gen | Middle | Video Demo | 1920x1080, 30-90s | 2 |
| Lead Gen | Middle | Single Image + Lead Form | 1200x628 | 3 |
| Conversions | Bottom | Case Study Graphic | 1200x628 | 2 |
| Retargeting | Bottom | Single Image + Direct CTA | 1080x1080 | 2 |

## Selection Process
1. Determine platform (Rendimension→Meta, Reflex→LinkedIn)
2. Determine campaign objective
3. Determine funnel stage (top/middle/bottom)
4. Look up matrix → get format
5. Verify asset availability
6. Determine variant count (min 3 copy × 2 visual)

## Platform Specs

### Meta
| Format | Dimensions | Max Duration/Size |
|---|---|---|
| Feed Image | 1080x1350 (4:5) | 30MB |
| Stories/Reels | 1080x1920 (9:16) | 90s / 4GB |
| Carousel | 1080x1080/card | 10 cards, 30MB each |
| Video | 1080x1350 | 240s / 4GB |

### LinkedIn
| Format | Dimensions | Max Duration/Size |
|---|---|---|
| Single Image | 1200x628 or 1080x1080 | 5MB |
| Document | 1080x1080/page | 10 pages, 100MB |
| Video | 1920x1080 or 1080x1080 | 30 min, 200MB |
