# GEO/SEO Workflow — Directriz Permanente para Páginas Web

Aplica a: Toda página nueva de Rendimension, Reflex, Prestige 360, hugoramirez.co con contenido SEO/GEO
Creado: 2026-04-08 | Basado en: Revisión con 4 AIs (Gemini, Perplexity, Grok, ChatGPT) + caso Alo Yoga

## CUÁNDO USAR ESTE WORKFLOW

Siempre que se cree o actualice una página web con intención de ser citada por AI engines (Google AI Overviews, Perplexity, ChatGPT Search, Claude, Bing Copilot).

## FASES (en orden estricto)

### FASE 1 — DISEÑO
Ver page-creation-process.md en reglas globales.

### FASE 2 — CONTENIDO CON OPTIMIZACIÓN GEO

Estructura obligatoria de secciones:
1. H1 ultra-descriptivo + keyword + resultado
2. Executive Summary — bullets AI-extractables + claim propietario en blockquote + definición de categoría explícita
3. The Real Problem (H2) + subsecciones H3
4. Project Context (H2) con lista de retos técnicos resueltos
5. The Decision Gap (H2) — aquí se crea la categoría nueva
6. Who This Is For / Who It Is Not (H2) — filtro de comprador (CRÍTICO para conversión y citación)
7. The Approach (H2) con pasos numerados H3
8. Before vs After (H2) — tabla HTML comparativa
9. Measurable Outcomes (H2) con H3 por resultado
10. Why Others Fail (H2)
11. How It Works (H2) — operativo con lista numerada + internal links
12. FAQ (H2) — mínimo 5 preguntas con schema FAQPage
13. Key Takeaway (H2) con blockquote citable
14. CTA + Author Bio (E-E-A-T)

Reglas de contenido:
- Frase propietaria repetida 2-3 veces en el documento
- Definición de categoría en blockquote: "[Categoría]: A process that allows [cliente] to [resultado]"
- Anchor text keyword-rich NUNCA genérico ("Explore our luxury retail visualization services" NO "Learn more")
- 4 intenciones cubiertas: informativa, comercial, comparativa, operativa
- Keywords variantes: photorealistic [X] renders, [X] fit-out visualization, [X] brand rollout, rollout support, stakeholder alignment

### FASE 2.5 — CONSULTA CON LOS 4 AMIGOS (OBLIGATORIA — 2 RONDAS)

Esta fase es obligatoria para toda página nueva con contenido SEO/GEO.

**Ronda 1 — Cada AI con su enfoque:**

| AI | Preguntar sobre |
|---|---|
| Gemini | E-E-A-T, Google AI Overviews, entidades, schema JSON-LD, robots.txt, sitemaps |
| Perplexity | Keywords reales usados en búsquedas, páginas citadas en el nicho, archivos técnicos (llms.txt) |
| Grok | Psicología del comprador, objeciones mentales, comportamiento en X/Reddit |
| ChatGPT | Síntesis de los 3 + estructura final + Category Design + posicionamiento |

Aplicar todos los cambios al contenido.

**Ronda 2 — Mostrar contenido actualizado a los 4:**
- Enviar el contenido completo actualizado a cada uno
- Preguntar: ¿qué iteración final harías antes de publicar?
- Aplicar cambios finales
- Claude ensambla el archivo definitivo con todos los inputs de las 2 rondas.

### FASE 3 — ARCHIVOS TÉCNICOS GEO
- llms.txt en raíz: curado, Markdown simple, no inflado. Incluye: nombre empresa, descripción 1 línea, servicios, páginas clave, frases citeables
- llms-full.txt: contexto completo para agentes AI
- robots.txt additions: Google-Extended, PerplexityBot, ChatGPT-User, anthropic-ai, ClaudeBot — todos con Allow: /
- Image sitemap: image:title + image:caption para cada render/imagen importante
- Meta robots en HTML: max-snippet:-1, max-image-preview:large, max-video-preview:-1

### FASE 4 — SCHEMA JSON-LD

Para case studies, usar:
- Article (con Person author + Organization publisher + about[] + mainEntity CreativeWork)
- FAQPage (mínimo 5-6 preguntas)
- Service (con areaServed, serviceType, audience, alternateName = nombre de categoría)

Propiedades críticas:
- sameAs en Organization: LinkedIn, Clutch, Houzz
- keywords en Article
- alternateName en Service = nombre de categoría (ej. "Pre-Construction Decision System")

### FASE 5 — PUBLICACIÓN Y DISTRIBUCIÓN
1. Subir a WordPress / Elementor Pro
2. Configurar Rank Math: keyword, meta description, schema
3. Solicitar indexación en Google Search Console
4. Subir llms.txt y llms-full.txt a raíz del hosting
5. Actualizar sitemap.xml
6. Distribuir: WordPress primero, esperar 1h, luego LinkedIn + Medium + X

## CHECKLIST PRE-PUBLICACIÓN
- [ ] H1 con keyword + resultado
- [ ] Executive Summary con claim propietario en blockquote
- [ ] Definición de categoría explícita
- [ ] Sección "Who This Is For / Who It Is Not"
- [ ] Tabla Before/After en HTML
- [ ] 4 intenciones: informativa, comercial, comparativa, operativa
- [ ] FAQ con mínimo 5 preguntas + schema FAQPage
- [ ] Internal links con anchor text keyword-rich (no genérico)
- [ ] Author bio con LinkedIn
- [ ] Schema: Article + FAQPage + Service
- [ ] Meta robots max-snippet:-1
- [ ] llms.txt actualizado en el sitio
- [ ] Image sitemap con titles + captions
- [ ] Google-Extended permitido en robots.txt
- [ ] 2 rondas de revisión con los 4 amigos completadas

## FRASES CITEABLES (Rendimension — usar como modelo)
- "Rendimension acts as an external decision layer for luxury retail expansion before construction begins."
- "Pre-Construction Decision System: A process that allows retail brands to validate spatial, branding, and operational decisions before construction begins."
- "The cost of making the wrong decision in retail is measured in millions. The cost of validating it visually is a fraction of that."
- "5 years. 20+ stores. 3 continents. Zero failed openings due to visual misalignment."
- "First visual set delivered in 48 to 72 hours."
