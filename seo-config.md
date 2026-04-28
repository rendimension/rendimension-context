# SEO Rendimension — Control de Configuración Completa

Fecha: 4 de Abril 2026 | Estado: Completado

## RANK MATH PRO — Configuración Completa

### 1. Image SEO
- ALT tag: ON → formato %filename%
- TITLE tag: ON → formato %title% %count(title)%
- Caption: OFF
- Description: OFF

### 2. Social Meta
- Facebook Page URL: https://www.facebook.com/rendimension
- Twitter/X handle: rendimension
- Facebook App ID: limpiado (estaba con valor incorrecto)

### 3. Local SEO
- Business Name: Rendimension
- Address: 4300 Biscayne Boulevard, Miami, FL 33137, US
- Phone: +1-305-290-3717
- Email: 3d@rendimension.com
- Hours: Lunes–Domingo 09:00–17:00
- Country Code: US (ISO 3166-1)

### 4. Schema Template (Structured Data)
- Tipo: Service
- Service Type: "3D Architectural Rendering and Visualization"
- Headline: %seo_title%
- Description: %seo_description%
- Display Conditions: Entire Site
- Post ID: 5595
- Status: Publicado 4 Abr 2026

### 5. llms.txt (GEO — AI Engine Optimization)
- URL activa: https://rendimension.com/llms.txt
- Post types incluidos: Posts, Pages, Portfolio, Template Items
- Taxonomías: Categories
- Límite: 50 entradas

### 6. 404 Monitor + Redirections
- /blog/insights → /blog/ (301 Permanente)
- PENDIENTE: /services/interior-rendering → URL por definir
- PENDIENTE: /blog/meet-us → /rendimension-team/
- PENDIENTE: /blog/team → /rendimension-team/
- PENDIENTE: /blog/our-team → /rendimension-team/

### 7. Instant Indexing
- PENDIENTE: Requiere Google Cloud Service Account JSON de Hugo

## WP ROCKET — Configuración Completa

### File Optimization
- Minify CSS: ON
- Minify JS: ON
- Combine CSS/JS: OFF (Elementor)
- Defer JS: ON
- Delay JS: ON
- Self-host Google Fonts: ON

### Media
- LazyLoad Images: ON
- LazyLoad iframes: ON
- LazyLoad CSS BG Images: ON
- Add Image Dimensions: ON
- Auto Preload Fonts: ON

### Preload
- Preload Cache: ON
- Preload Links: ON
- Omitido intencionalmente: Remove Unused CSS — rompe Elementor

## Core Web Vitals (estado al inicio — referencia)
- LCP: 1.1s
- TBT: 4ms
- CLS: 0.000
- TTFB: 494ms

## Blog — Inventario de URLs
- Total publicados: 166 artículos
- URL base: https://rendimension.com/blog/

## Rank Math — Reglas Importantes

**Power words en WordPress en español:**
- WordPress en español = Rank Math usa lista de power words en ESPAÑOL exclusivamente
- "Proven", "Ultimate", "Trusted", "Amazing" = NO reconocidos en WP español
- Solución: Usar "Valor" (está en la lista española Y es válido en inglés)
- Siempre usar power words en español para Rank Math en este sitio

**TOC no detecta headings en Classic blocks:**
- El bloque rank-math/toc-block SOLO detecta headings como bloques tipados hermanos
- Siempre convertir Classic blocks antes de añadir TOC

**Descripción en píxeles vs caracteres:**
- Rank Math valida en PÍXELES (920px) además de caracteres (160)
- Mantener descripción bajo 150 chars si contiene caracteres especiales ($, números)
