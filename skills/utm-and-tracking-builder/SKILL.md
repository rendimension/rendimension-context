---
name: utm-and-tracking-builder
description: UTM parameter standards, tracking setup guides for Meta Pixel and LinkedIn Insight Tag, conversion tracking configuration, and attribution model recommendations.
---

# UTM and Tracking Builder

## UTM Format
`?utm_source={platform}&utm_medium=paid-social&utm_campaign={brand}_{objective}_{audience}&utm_content={hook}_{format}_{variant}&utm_term={targeting}`

## Examples
Rendimension: `?utm_source=meta&utm_medium=paid-social&utm_campaign=rendimension_leadgen_architects&utm_content=luxurykitchen_carousel_A`
Reflex: `?utm_source=linkedin&utm_medium=paid-social&utm_campaign=reflex_leadgen_dealerprincipals&utm_content=closingrate_singleimage_A`

## Meta Pixel: Install on rendimension.com, configure PageView + Lead + ViewContent events, set up Conversions API
## LinkedIn Insight Tag: Install on reflexsystem.com, configure URL-based conversions for /demo-booked and /thank-you

## Attribution: Meta 7-day click/1-day view, LinkedIn 30-day click. Also track in Google Analytics.
