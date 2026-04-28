## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)

---

# RENDIMENSION — REGLAS PERMANENTES DEL PROYECTO

> Verificado y aprobado por Hugo Ramirez el 26 de abril de 2026.
> Estas reglas NO se pueden cambiar sin aprobación explícita de Hugo.

---

## STACK DEL SITIO

- **CMS:** WordPress en Hostgator México
- **Theme:** UICore (NO es un tema estándar — tiene sus propias variables CSS)
- **Builder:** Elementor Pro (TODAS las páginas premium se construyen aquí)
- **SEO:** Rank Math
- **Cache:** WP Rocket
- **URL WP Admin:** https://www.rendimension.com/wp-admin/
- **REGLA CRÍTICA:** NUNCA usar Gutenberg para páginas premium. Solo Elementor.
- **REGLA CRÍTICA:** NUNCA tocar el diseño del website principal bajo ninguna circunstancia.

---

## DESIGN SYSTEM — VALORES REALES (extraídos del CSS vivo, verificados 26 abr 2026)

### Tipografía
| Elemento | Font | Size | Weight | Line-Height | Letter-Spacing |
|---|---|---|---|---|---|
| **ÚNICA FUENTE** | **Inter** | — | — | — | El sitio usa Inter, NO Roboto |
| Body / párrafo | Inter | 16px | 400 (normal) | 1.875 | 0em |
| H1 | Inter | 72px (desktop) | 600 | 1.2 | -0.027em |
| H2 | Inter | 48px (desktop) | 700 | 1.175 | -0.027em |
| H3 | Inter | 24px | 600 | 1.2 | -0.027em |
| H4 | Inter | 21px | 600 | 1.42 | -0.027em |
| H5 | Inter | 16px | 600 | 1.187 | -0.015em |
| H6 | Inter | 14px | 600 | 1.2 | -0.027em — UPPERCASE |

### Colores
| Variable UICore | Valor | Uso |
|---|---|---|
| `--uicore-secondary-color` | **#FF5F03** | Naranja brand — botones, accents, íconos, bordes decorativos |
| `--uicore-headline-color` | **#070707** | Headings sobre fondos claros |
| `--uicore-body-color` | **#6E7A84** | Texto body global |
| `--uicore-dark-color` | **#242728** | Dark surfaces |
| `--uicore-accent-color` | **#D1345B** | H5, labels de categoría |
| `--uicore-white-color` | **#FFFFFF** | Texto sobre fondos oscuros |
| `--uicore-light-color` | **#959C9C** | Texto secundario |
| Fondo dark páginas premium | **#000000 / #0a0a0a** | Background de secciones oscuras |
| Fondo light | **#f8f8f8** | Secciones claras alternadas |

### COLORES PROHIBIDOS
- ❌ Cualquier naranja distinto a `#FF5F03`
- ❌ Marrones cálidos como `#1a1208`, `#2d1f10`, `#1a1a1a` con tinte cálido
- ❌ Roboto, Poppins, Montserrat u otras fuentes — solo Inter

### Layout
- **Container max-width:** 1170px
- **Padding secciones:** 80px top/bottom (desktop)
- **Padding container:** 40px left/right

---

## TIPOS DE PÁGINA

| Tipo | Ejemplos | Estilo |
|---|---|---|
| **Premium** | Homepage, About, Services, Case Studies | Dark, visual, Elementor full-design, imágenes grandes |
| **City Pages** | Coral Gables, Houston, Miami | Texto rico, SEO, más liviano |
| **Blog** | /blog/[slug]/ | Post estándar WordPress |

---

## TEMPLATE CONGELADO — CASE STUDIES

**Aprobado por Hugo Ramirez el 26 de abril de 2026.**
**CONGELADO. No se puede rediseñar. No se puede reinterpretar. No se puede mezclar con otros templates.**

### Estructura de URLs
- Índice: `rendimension.com/case-studies/`
- Individual: `rendimension.com/case-studies/[cliente]/`

### Secciones OBLIGATORIAS en este orden exacto

1. **NAV GLOBAL** — El menú del sitio (Who we are / What we do / Our work / FAQ / Contact / Get a Quote). Nunca crear uno propio.

2. **HERO** — Fondo negro `#000`, imagen del render a la derecha (55% ancho, overlay gradient izquierda), tag de categoría con borde naranja, H1 grande blanco, stats en línea (separados por · ), dos botones (primario naranja sólido + secundario borde blanco).

3. **STATS BAR** — Fondo `#0a0a0a`, 4 columnas separadas por líneas verticales sutiles, número grande en naranja `#FF5F03`, label en uppercase pequeño, subtítulo gris.

4. **EL PROBLEMA** — Fondo `#000`, 2 columnas: izquierda (label naranja + H2 blanco + párrafo + lista de bullets con punto naranja), derecha (blockquote con borde izquierdo naranja + caja de scope).

5. **LO QUE HIZO RENDIMENSION** — Fondo `#f8f8f8`, label naranja + H2 dark + párrafo, grid 2 columnas de cards blancas (número de paso, título, descripción, imagen placeholder).

6. **GALERÍA DE RENDERS** — Fondo `#0a0a0a`, grid asimétrico (render grande 2/3 + 2 renders pequeños 1/3), segunda fila 3 columnas iguales.

7. **RESULTADOS** — Fondo `#000`, label + H2 blanco, 3 cards con ícono naranja, número grande, título, descripción.

8. **QUOTE** — Fondo sólido `#FF5F03`, blockquote grande centrado en blanco, cite en uppercase.

9. **CTA** — Fondo `#000`, label naranja + H2 blanco grande + párrafo gris + 2 botones centrados.

10. **FOOTER GLOBAL** — El footer del sitio (UICore). Nunca crear uno propio. Siempre usar el template de footer global de UICore/Elementor.

### Reglas de implementación en Elementor

- Cada sección es una **Elementor Section** con fondo aplicado a nivel de sección
- El menú y footer son **Elementor Theme Builder templates** — no se construyen dentro de la página
- Los títulos usan el **widget Heading de Elementor** con tipografía tomada del Global Kit
- El texto usa el **widget Text Editor de Elementor**
- Los botones usan el **widget Button de Elementor** con estilo personalizado
- Los stats usan el **widget Counter o Heading** de Elementor
- Las imágenes usan el **widget Image de Elementor** con overlay en CSS
- **Page Title del tema UICore debe ocultarse** con CSS en Elementor page-level: `.uicore-page-title { display: none !important; }`

### Lo que SOLO cambia entre casos de estudio
- Nombre del cliente
- Texto del tag de categoría (ej: "Case Study: Retail" / "Case Study: Residential")
- H1 — título del caso
- Stats específicos del proyecto
- Contenido del problema, solución y resultados
- Imágenes de renders
- Quote específica del proyecto
- URL slug

### Lo que NUNCA cambia
- Estructura de secciones
- Orden de secciones
- Colores
- Tipografía
- Espaciados
- Menú y footer

### SEO / GEO / AI CITABILITY — REGLA OBLIGATORIA (aplica a todos los case studies)

**El layout NO cambia. Solo se optimiza el contenido dentro del template.**

Cada case study basado en este template DEBE cumplir las siguientes reglas de contenido:

#### H1
- Basado en resultado de negocio real (no genérico, no estético)
- Claro, específico, long-tail
- ❌ "3D Renders for Alo Yoga" → ✅ "How Alo Yoga Secured Retail Approval with Photorealistic Store Renderings in Miami"

#### Headings (H2, H3)
- Enfocados en decisiones reales del cliente, no decorativos
- Deben responder preguntas que un cliente potencial buscaría
- ❌ "The Challenge" → ✅ "Why Alo Yoga Needed Renderings Before Breaking Ground"

#### Narrativa del contenido
- Estructura obligatoria: **problema → decisión → resultado**
- Evitar lenguaje centrado en "renders" o estética — hablar de negocio, decisiones, resultados
- El cliente es el protagonista; Rendimension es el habilitador

#### GEO (Geographic Entity Optimization)
- Integrar ubicación de forma natural en el texto (no forzada)
- Mencionar ciudad, mercado, contexto de expansión donde aplique
- Ejemplos: "Miami retail corridor", "South Florida luxury market", "Coral Gables zoning approval"

#### AI Citability
- Frases cortas, directas y citables — que una IA pueda extraer y citar literalmente
- Evitar relleno, adjetivos vacíos, frases largas sin sustancia
- Cada sección debe tener al menos 1-2 frases citables (40-60 palabras máximo por frase citable)

#### FAQ (obligatoria en cada case study)
- Mínimo 4 preguntas, máximo 8
- Preguntas reales que un cliente buscaría en Google o le preguntaría a una IA
- Schema FAQPage implementado en Rank Math
- ❌ "What is a case study?" → ✅ "How long does a commercial rendering project take for a retail space?"

---

## CASOS DE ESTUDIO ACTIVOS

| Cliente | URL | Estado |
|---|---|---|
| Alo Yoga | /case-studies/alo-yoga-store-rendering/ | Roto — pendiente reconstruir con template |
| Southwest Ranches | /case-studies/southwest-ranches-luxury-home-rendering/ | Roto — pendiente reconstruir con template |
| Historic Firehouse | /case-studies/historic-firehouse-restaurant-rendering/ | Pendiente verificar |
| House of Speed | /case-studies/3d-renders-investor-pitch/ | Pendiente verificar |

---

## PROCESO OBLIGATORIO — 3 FASES PARA CUALQUIER PÁGINA NUEVA

### Fase 1 — DISEÑO
- Para case studies: usar el template congelado arriba. Sin excepciones.
- Para otros tipos: definir layout antes de escribir contenido y aprobar con Hugo.

### Fase 2 — CONTENIDO
- H1 ultra-descriptivo y long-tail
- Bloque de respuesta directa (40-60 palabras citables para GEO)
- H2/H3 como preguntas reales del usuario
- Tablas comparativas donde aplique
- Entidades: Rendimension, ciudad, tipo de proyecto, cliente
- FAQ obligatoria (4-8 preguntas con schema FAQPage)
- Longitud: 1,500-2,500 palabras (pilar)

### Fase 3 — SEO
- Keyword en H1, meta title y primer párrafo
- Schema markup: CaseStudy / Article / LocalBusiness
- Internal links configurados
- Rank Math: keyword, meta description, schema
- Indexación solicitada en GSC

---

## REGLAS GLOBALES PERMANENTES

1. NO tocar el diseño del website principal (Elementor) bajo ninguna circunstancia
2. NO usar Gutenberg para páginas premium — solo Elementor
3. NO usar la API REST de WordPress para crear contenido de páginas — usar Elementor
4. El menú y footer SIEMPRE son los templates globales de UICore — nunca crear uno propio dentro de una página
5. Los 301 redirects deben estar activos indefinidamente (mínimo 1 año)
6. Nunca borrar un post viejo sin tener la redirección activa
7. Cache de WP Rocket debe limpiarse después de cualquier cambio (Clear and Preload)

---

## COMANDO DE INICIO — SESIONES FUTURAS DE CASE STUDIES

Para iniciar cualquier sesión de case study sin repetir contexto, usar exactamente este comando:

```
Read CLAUDE.md and use case-study-master-template-v2.html. Do not redesign. Proyecto: [nombre]. Empieza en STEP 1.
```

**STEP 1** = Recopilar contenido real del proyecto (H1, stats, problema, solución, resultados, quote, imágenes, FAQ)
**STEP 2** = Rellenar tokens del template con contenido real cumpliendo reglas SEO/GEO/AI
**STEP 3** = Implementar en Elementor (HTML widget con CSS scoped)
**STEP 4** = Limpiar caché WP Rocket + solicitar indexación en GSC

El archivo template está en:
`outputs/case-study-master-template-v2.html`
(ruta completa disponible en el historial de sesión si se necesita)
