---
name: ad-type-decision-engine
description: Automated decision logic for choosing ad types based on campaign objective, audience, budget, available assets, and funnel stage, with decision tree format and budget thresholds.
---

# Ad Type Decision Engine

## Decision Tree
```
Platform = Meta?
├── Budget < $30/day → Single Image only
├── Budget $30-$100/day
│   ├── Have video? → Video + Single Image
│   └── No video? → Carousel + Single Image
└── Budget > $100/day → Full mix: Video + Carousel + Image + Reel

Platform = LinkedIn?
├── Budget < $50/day → Single Image only
├── Budget $50-$150/day
│   ├── Have video? → Video + Single Image
│   └── No video? → Document + Single Image
└── Budget > $150/day → Full mix: Video + Document + Image
```

## Minimum Viable Campaigns

### Meta $30/day: 1 campaign, 2 ad sets, 3 ads each (Single Image)
### Meta $75/day: 1 campaign, 3 ad sets, 4 ads each (Image + Carousel)
### LinkedIn $50/day: 1 campaign, 2 ad sets, 3 ads each (Single Image)
### LinkedIn $100/day: 1 campaign, 3 ad sets, 4 ads each (Image + Document)

## Asset Requirements
| Format | Production Time | Tool |
|---|---|---|
| Single Image | 1-2 hours | Canva |
| Carousel | 3-5 hours | Canva |
| Reel | 4-8 hours | Canva/External |
| Document PDF | 3-5 hours | Canva/21ST |
| Video | 4-8 hours | External |
