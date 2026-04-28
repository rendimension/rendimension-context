# CLAUDE.md — Directriz Obligatoria: Case Studies Rendimension

> **Versión:** 2026-04-26 | Basado en sesiones completas: Alo Yoga (#1), House of Speed (#2), Historic Firehouse (#3) + estrategia factory process 26 Abr 2026
> **Estado:** ACTIVO — aplica a todos los case studies futuros de Rendimension

---

## 0. FACTORY PROCESS — REGLAS ABSOLUTAS (NUNCA VIOLAR)

> Origen: 26 Abril 2026 — Hugo identificó loops infinitos, errores de layout/footer/menú/márgenes y tiempo perdido en correcciones. Estas reglas reemplazan cualquier improvisación.

### MENU Y FOOTER — RESUELTO PERMANENTEMENTE (26 Abr 2026)

El problema de menú/footer en case studies está resuelto via **snippet WPCode de CSS puro** (sin add_action) usando la body class `.parent-pageid-5611` que WordPress inyecta automáticamente en todas las child pages de /case-studies/. **Este fix aplica a todos los case studies futuros sin ninguna acción adicional.** No tocar, no rediseñar.

### PRINCIPIO CENTRAL: DUPLICAR, NO CONSTRUIR

**House of Speed (page ID 2185) es el template vivo.** Está en 88/100, layout correcto, footer OK, menú OK. Toda página nueva parte de duplicar esta página — nunca de HTML desde cero.

```
Flujo obligatorio por cada case study:
1. Duplicar HOS en Elementor (respira_create_page_duplicate o REST API)
2. Actualizar SOLO el HTML widget (texto + imágenes del cliente)
3. Actualizar post_content SEO via set-page-v2
4. Actualizar RM meta via snippet one-time
5. Agregar elseif al snippet 5911 (schema)
6. Verificar score 85+ → CERRADO
```

### REGLAS ANTI-LOOP (INVIOLABLES)

| # | Regla | Consecuencia si se viola |
|---|---|---|
| 1 | **Máximo 2 intentos por paso** | Si falla 2 veces: PARAR, reportar el error exacto a Hugo, proponer ruta alternativa. NUNCA seguir intentando variaciones del mismo enfoque. |
| 2 | **Preparar TODOS los HTMLs antes de deployar** | Los 5 HTMLs se validan en Python localmente. Si alguno falla la validación, se corrige. Solo después se toca WordPress. |
| 3 | **Validación Python obligatoria antes de cada deploy** | Checklist: cero em-dashes, cero non-ASCII, word count 2500+, keyword density 0.7-1.5%. Si alguno falla → corregir en local, no en producción. |
| 4 | **Criterio de DONE binario — sin excepciones** | Score 85+ ✅ + screenshot desktop OK ✅ + footer visible ✅ = CERRADO. Sin ajustes adicionales de estilo, márgenes, spacing después de este punto. |
| 5 | **Sin correcciones de layout post-deploy** | Errores de layout, márgenes, safe frames se corrigen en el template base (HOS duplicado) ANTES de deployar, no después. |
| 6 | **Sin loops de "un ajuste más"** | Una vez que los 5 criterios de DONE están en verde, la tarea termina. No existe "mientras arreglo esto rápido". |
| 7 | **No tocar CSS global** | Nunca modificar estilos que afecten más de una página durante una sesión de case studies. Eso va en sesión separada. |
| 8 | **Rate limit activo siempre** | Máx 1 request/10s a rendimension.com. Pausar n8n workflows ANTES de iniciar. |

### DEFINICION DE DONE (BINARIA)

Una página de case study está DONE cuando pasa estos 5 checks. Si alguno es NO → trabajar ese punto. Si todos son SI → CERRADO SIN EXCEPCION.

- [ ] Score Rank Math: **85+/100** verificado en WP Admin block editor
- [ ] Screenshot desktop: hero visible, footer correcto, sin elementos rotos
- [ ] Screenshot mobile (375px): texto legible, CTAs accesibles
- [ ] Schema validado: Article + FAQPage en snippet 5911
- [ ] URL publicada: status Published, parent 5611, slug correcto (sin `-2`)

### FASE DE PREPARACION (hacerla UNA VEZ antes de deployar las 5)

```
FASE 0 — Verificar template base HOS (2185)
  → Screenshot actual: desktop + mobile
  → Si hay algo mal: corregirlo en HOS ANTES de duplicar
  → HOS aprobado = template locked

FASE 1 — Preparar los 5 HTMLs (batch, local)
  → Script Python con variables por cliente
  → Validación automática de los 5
  → Todos pasan → deploy

FASE 2 — Deploy secuencial (1 página a la vez)
  → Duplicar HOS → actualizar widget → SEO → RM → schema
  → 3s mínimo entre requests

FASE 3 — Verificación final (una pasada, sin loop)
  → 5 screenshots
  → 5 scores en WP Admin
  → Done checklist por cada página
  → CERRADO
```

### CASOS PENDIENTES — 5 CASE STUDIES FRESH (26 Abr 2026)

| # | Cliente | Tipo | Datos en Notion | Datos en WP existente |
|---|---|---|---|---|
| 1 | Alo Yoga | Retail / Luxury | SI (pagina Notion completa) | SI (page 5813, score 69) |
| 2 | House of Speed | Commercial / Investor pitch | SI (pagina Notion completa) | SI (page 2185, score 88) — BASE TEMPLATE |
| 3 | Historic Firehouse | Hospitality / Preservation | SI (pagina Notion completa) | SI (page 2122, score 87) |
| 4 | Hollywood Hills | Residential / Luxury | NO (extraer de WP existente) | SI (pagina mala — extraer info) |
| 5 | Southwest Ranches | Residential / Luxury estate | NO (extraer de WP existente) | SI (pagina mala — extraer info) |

**Para Hollywood Hills y Southwest Ranches:** leer la pagina mala existente en WP → extraer cliente, datos, imagenes FileBird → usar como input para el HTML del widget. Luego borrar la pagina vieja.

---

## 1. ANTI LOOP PROTOCOL

Estas reglas se activan automáticamente. No requieren que Hugo las mencione.

- **No rediseñar templates aprobados.** Si existe un template final (`alo-yoga-preview.html`), adaptarlo. Nunca crear uno desde cero.
- **No crear versiones nuevas si ya existe una final.** Buscar primero en `Desktop/`, `AppData/Local/Temp/`, y memoria antes de generar cualquier archivo.
- **No usar scripts complejos si Elementor puede resolverse directo.** Si el HTML widget acepta el contenido via `$e.run()` + `setSetting()`, usar eso. No crear pipelines de Python/curl innecesarios para lo que Elementor ya puede hacer.
- **No releer archivos en loop.** Un archivo se lee UNA sola vez por sesión. Si ya está en contexto, no volver a leerlo.
- **Detenerse si pasan más de 10 minutos sin avance claro.** Si un mismo paso falla 2+ veces consecutivas: parar, reportar el bloqueo a Hugo con el error exacto, y proponer una ruta alternativa. No seguir intentando variaciones del mismo enfoque fallido.
- **No hacer tool calls sin plan aprobado.** Máximo 5-10 líneas de plan → esperar "ok" de Hugo → ejecutar.

---

## 2. WORDPRESS ELEMENTOR IMPLEMENTATION PROTOCOL

### Cómo inyectar el HTML widget (método validado)

1. Abrir editor Elementor: `?post=[ID]&action=elementor`
2. Cargar HTML en memoria del editor: `window.__html__ = \`[contenido]\``
3. Encontrar widget + inyectar + guardar en un solo script:

```javascript
async () => {
  var found = null;
  function walk(c) {
    if (!c || found) return;
    if (c.model && c.model.get && c.model.get('widgetType') === 'html') { found = c; return; }
    var kids = c.children;
    if (!kids) return;
    if (Array.isArray(kids)) kids.forEach(walk);
    else if (kids.models) kids.models.forEach(walk);
    else { for (var i = 0; i < kids.length; i++) walk(kids[i]); }
  }
  walk(elementor.documents.getCurrent().container);
  if (!found) return 'WIDGET NOT FOUND';
  found.model.setSetting('html', window.__html__);
  var result = await $e.run('document/save/default');
  return 'SAVED';
}
```

### Reglas de implementación

- **Template de página:** SIEMPRE `elementor_canvas`. Si no, el theme Lumi renderiza su propio header encima del diseño.
- **Comando de guardado:** `$e.run('document/save/default')` — es awaitable y confirma guardado real. NO usar `onClickButtonPublish()` solo (es async sin await confiable).
- **Nonce REST vs AJAX:** `elementorCommon.config.rest.nonce` para REST API. `elementorCommon.config.ajax.nonce` para AJAX. Son distintos e intercambiarlos da 403.
- **Chrome DevTools MCP:** Usar `evaluate_script` con parámetro `function` (no `script`). Firma: `async () => { ... }`.
- **Browser tier:** Chrome es "read" en computer-use — no puede hacer clicks ni typing. Usar DevTools MCP (`evaluate_script`) para toda interacción con el editor.
- **Si el HTML widget no existe:** Crear uno nuevo desde Elementor antes de intentar inyectar. No asumir que ya hay un widget vacío.

### Qué NO hacer en Elementor

- Nunca sobrescribir `post_content` via `set-page-v2` en páginas con Gutenberg blocks visibles (páginas "mixed"). Verificar tipo primero.
- Nunca tocar secciones existentes del diseño (hero, galerías, CTAs originales).
- Nunca usar `doc.save()` — no existe en Elementor moderno.
- Nunca dispersar la implementación en múltiples scripts cuando un solo script puede hacer todo.

---

## 3. CASE STUDY MASTER TEMPLATE RULES

- **Template aprobado:** `C:/Users/rendi/Desktop/case-study-master-template-v1.html` — es el ÚNICO punto de partida para todos los case studies futuros. No crear templates alternativos. No rediseñar.
- **Estructura INTOCABLE:** `Hero → Stats Bar → Executive Summary → Gallery → Story/Challenges → Before/After Table → FAQ Grid → CTA + Author Bio`. El orden y las secciones no se modifican.
- **Solo cambia:** textos, imágenes, datos del cliente, keyword, namespace CSS (`.cs-alo` → `.cs-[cliente]`).
- **El HTML del widget es widget-only:** Sin `<html>`, `<head>`, `<body>`. Solo el contenido interior.
- **Namespace CSS por cliente:** Cada case study tiene su propio prefijo `.cs-[cliente]` para evitar colisiones de estilos entre páginas.
- **Imágenes:** Confirmar URLs reales de FileBird/Media Library antes de generar el HTML. No usar placeholders en producción.
- **Verificación antes de inyectar:** Correr búsqueda de em-dashes (`—`) y non-ASCII en el HTML. Si hay alguno, limpiar antes de continuar.

---

## 4. SEO / GEO / AI CITABILITY RULES

### Rank Math (post_content)

- **post_content y `_elementor_data` son independientes** en páginas `elementor_canvas`. El diseño visual no se afecta al actualizar `post_content`.
- **Mínimo 2500 palabras**, keyword density ~1% (25-30 ocurrencias), mínimo 2 H2/H3 con keyword.
- **Score mínimo: 85/100.** Cerrar la tarea con score menor = tarea incompleta.
- **Guardar en cada ajuste** — Rank Math no persiste si se navega sin guardar.

### GEO / AI Citability (BLOQUEANTE antes de cerrar cada caso)

| Item | Requisito |
|---|---|
| URL publicada | `rendimension.com/case-studies/[slug]/`, status Published, parent 5611 |
| Article schema | En snippet 5911: headline, author, publisher, datePublished, dateModified |
| FAQPage schema | En snippet 5911: 5+ preguntas (mismas que en el HTML visible) |
| robots.txt | GPTBot, Google-Extended, PerplexityBot, anthropic-ai, ClaudeBot en Allow |
| Fechas visibles | `<time datetime="YYYY-MM-DD">` visible en HTML |
| sameAs | Organization.sameAs con rendimension.com + LinkedIn en schema |

### Anchor text

- PROHIBIDO: "learn more", "click here", "see our work"
- CORRECTO: "explore our luxury retail visualization services", "view the Alo Yoga case study"

### Frases propietarias (repetir 2-3x por caso)

- "Rendimension acts as an external decision layer for luxury retail expansion before construction begins."
- "Pre-Construction Decision System"
- "First visual set delivered in 48 to 72 hours."

---

## 5. VERSION CONTROL RULES

- **Un archivo final por caso.** Formato: `[cliente]-case-study-final.html`. Si ya existe un `-final`, no crear `-final-v2` ni `-final-updated`. Editar el existente.
- **Antes de crear cualquier archivo:** buscar en `Desktop/`, `AppData/Local/Temp/`, y memoria si ya existe.
- **Naming de payloads temporales:** `[cliente]_widget_only.html` (widget HTML) y `wp_payload.json` (payload para set-page-v2). Reutilizar, no acumular versiones.
- **WPCode snippets:** Usar snippets existentes (5819, 5910, 5911) con `elseif` para nuevas páginas. Nunca crear snippets separados por página.
- **Documentar en MEMORY.md** al cerrar cada caso: WP ID, slug, score, estado.

---

## 6. FINAL VALIDATION RULES

**Antes de declarar cualquier case study como "done", verificar TODOS estos puntos:**

### Visual (desktop + mobile)

- [ ] **Abrir la URL publicada en desktop** y tomar screenshot — confirmar hero visible, no hay header del tema encima
- [ ] **Verificar en mobile** (viewport 375px) — el hero no está cortado, el texto es legible, CTAs son accesibles
- [ ] Galería cargando imágenes reales (no placeholders negros/grises)
- [ ] Animaciones `.fade-up` funcionando al hacer scroll
- [ ] Nav fijo en top, CTAs naranjas visibles

### SEO / Rank Math

- [ ] Score verificado en WP Admin block editor: mínimo **85/100**
- [ ] Focus keyword correcto en Rank Math panel
- [ ] SEO title y meta description configurados y dentro de límites (60/160 chars)
- [ ] Slug correcto (sin `-2` al final — si aparece, hay un redirect duplicado en RM)

### GEO / AI Citability

- [ ] Los 6 items del checklist de Fase 2.2 (ver sección 4 arriba) completados
- [ ] Schema validado en Rich Results Test (sin errores críticos)
- [ ] GEO files subidos al hosting root

### Documentación

- [ ] Notion actualizado con estado final del caso
- [ ] `memory/case_study_master_template.md` actualizado con el nuevo caso
- [ ] Este `CLAUDE.md` actualizado si se descubrió algo nuevo en el proceso

**Si algún item está en rojo: el caso NO está done. No se cierra hasta que todos estén en verde.**

---

## ANTES DE EMPEZAR CUALQUIER CASE STUDY

1. Leer `~/.claude/memory/case_study_master_template.md` — estado de casos activos
2. Verificar si la página ya existe en WP: `curl -s "https://rendimension.com/wp-json/wp/v2/pages?slug=[slug]"`
3. Confirmar imágenes curadas en FileBird antes de generar HTML
4. El template visual OBLIGATORIO es: `C:/Users/rendi/Desktop/alo-yoga-preview.html`

---

## TEMPLATE BASE — SINGLE SOURCE OF TRUTH

**Archivo oficial:** `C:/Users/rendi/Desktop/case-study-master-template-v1.html`

Este archivo es el template visual aprobado. **No modificar. No rediseñar. Solo usar como base para reemplazar contenido e imágenes.** Estructura INTOCABLE:
`Hero → Stats Bar → Executive Summary + Blockquote → Gallery (por ubicación) → Story/Challenges → Before/After Table → FAQ Grid → CTA + Author Bio`

Solo cambia: texto, imágenes, datos del cliente, keyword. Nunca la estructura CSS/JS base.

---

## STACK TÉCNICO: CÓMO FUNCIONA LA PÁGINA

```
WordPress page (template: elementor_canvas)
  └── Elementor editor
        └── Section > Column > HTML Widget
              └── [TODO EL DISEÑO VISUAL DEL CASE STUDY]
                  (CSS .cs-[cliente], HTML completo, JS animaciones)

post_content (separado del diseño visual)
  └── [CONTENIDO SEO — 2500+ palabras, solo lo lee Rank Math]
      (no aparece visualmente, inyectado via set-page-v2)
```

**Regla crítica:** El diseño visual vive en el HTML Widget de Elementor. El SEO de Rank Math vive en `post_content`. Son independientes. Tocar uno NO afecta el otro (siempre que la página sea `elementor_canvas`).

---

## FLUJO COMPLETO — 7 PASOS

### PASO 1 — Crear la página en WordPress

```bash
# Crear con parent_id = 5611 (/case-studies/)
curl -s -u hugo:[APP_PASSWORD] -X POST \
  "https://rendimension.com/wp-json/wp/v2/pages" \
  -H "Content-Type: application/json" \
  -d '{"title":"[Título]","slug":"[slug]","status":"publish","parent":5611,"template":"elementor_canvas"}'
# Guardar el ID que devuelve
```

Si la página ya existe, cambiar template a `elementor_canvas` via REST:
```bash
curl -s -u hugo:[APP_PASSWORD] -X POST \
  "https://rendimension.com/wp-json/wp/v2/pages/[ID]" \
  -H "Content-Type: application/json" \
  -d '{"template":"elementor_canvas"}'
```

### PASO 2 — Generar el HTML del widget

Copiar `alo-yoga-preview.html`, adaptar para el nuevo cliente:
- Cambiar namespace CSS: `.cs-alo` → `.cs-[cliente]`
- Cambiar textos, estadísticas, nombre del cliente
- Cambiar imágenes (URLs de FileBird/Media Library)
- Cambiar keyword en H1, executive summary, FAQ
- Verificar: **cero em-dashes (—)**, cero non-ASCII

Guardar como: `C:/Users/rendi/AppData/Local/Temp/[cliente]_widget_only.html`

El archivo debe ser el HTML del widget SOLAMENTE — sin `<html>`, `<head>`, `<body>`. Solo el contenido que va dentro del widget.

### PASO 3 — Inyectar el HTML en Elementor

Abrir el editor Elementor: `https://rendimension.com/wp-admin/post.php?post=[PAGE_ID]&action=elementor`

Vía Chrome DevTools MCP (`evaluate_script`):

```javascript
// Cargar el HTML en memoria (si el archivo es grande, pegarlo directo como string)
// window.__html__ = [contenido del archivo como string]

// Encontrar el HTML widget y actualizar
async () => {
  var found = null;
  function walk(c) {
    if (!c || found) return;
    if (c.model && c.model.get && c.model.get('widgetType') === 'html') { found = c; return; }
    var kids = c.children;
    if (!kids) return;
    if (Array.isArray(kids)) kids.forEach(walk);
    else if (kids.models) kids.models.forEach(walk);
    else { for (var i = 0; i < kids.length; i++) walk(kids[i]); }
  }
  walk(elementor.documents.getCurrent().container);
  if (!found) return 'WIDGET NOT FOUND';
  found.model.setSetting('html', window.__html__);
  var result = await $e.run('document/save/default');
  return 'SAVED: ' + JSON.stringify(result).substring(0, 100);
}
```

**Nonce correcto para REST API:** `elementorCommon.config.rest.nonce`
**Comando de guardado correcto:** `$e.run('document/save/default')` — devuelve Promise awaitable

### PASO 4 — Inyectar SEO content en post_content (para Rank Math)

Generar 2500+ palabras de contenido SEO en Python:

```python
focus_keyword = "[exact keyword]"
page_id = [PAGE_ID]

content = """[14 secciones según seo-geo-elementor-protocol.md]"""

# Limpiar non-ASCII
content = content.replace('—', '--').replace('’', "'")
content = content.replace('“', '"').replace('”', '"')

# Verificar densidad
words = len(content.split())
kw_count = content.lower().count(focus_keyword.lower())
assert words >= 2500
assert 0.7 <= kw_count/words*100 <= 1.5

import base64, json
b64 = base64.b64encode(content.encode('utf-8')).decode('ascii')
payload = json.dumps({'page_id': page_id, 'html_b64': b64})
with open('C:/Users/rendi/AppData/Local/Temp/wp_payload.json', 'w') as f:
    f.write(payload)
```

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d @"C:/Users/rendi/AppData/Local/Temp/wp_payload.json" \
  "https://rendimension.com/wp-json/rend-helper/v1/set-page-v2"
# Respuesta esperada: {"success":true,"update_result":true}
```

### PASO 5 — Configurar Rank Math (title, meta, keyword, slug)

WPCode snippet con patrón one-time (agregar al snippet 5819 existente o crear nuevo):

```php
add_action('init', function() {
    if (get_option('wpcode_ran_rankmath_[SLUG_UNICO]')) return;
    $page_id = [PAGE_ID];
    wp_update_post(['ID' => $page_id, 'post_name' => '[nuevo-slug]']);
    update_post_meta($page_id, 'rank_math_title', '[SEO Title max 60 chars con keyword al inicio]');
    update_post_meta($page_id, 'rank_math_description', '[Meta description max 160 chars]');
    update_post_meta($page_id, 'rank_math_focus_keyword', '[focus keyword]');
    update_option('wpcode_ran_rankmath_[SLUG_UNICO]', true);
}, 1);
```

### PASO 6 — Schema JSON-LD (FAQPage + Article)

Agregar `elseif ($page_id == [NEW_ID])` al **snippet WPCode 5911** existente.
Nunca crear snippets separados — todo en 5911.

Schemas obligatorios: `Article` + `FAQPage` + `Service` (con `alternateName`)

### PASO 7 — Verificar Rank Math score

Abrir: `https://rendimension.com/wp-admin/post.php?post=[PAGE_ID]&action=edit`

Target mínimo: **85/100**. Ver protocolo de 10 pasos en:
`~/.claude/rules/rank-math-score-optimization-protocol.md`

---

## REGLAS ABSOLUTAS

| Regla | Detalle |
|---|---|
| Template de página | SIEMPRE `elementor_canvas` — nunca `default` |
| Em-dashes | PROHIBIDOS en todo el HTML, incluyendo `<title>` y `<meta>` |
| Non-ASCII | Limpiar ANTES de base64 o Elementor los rechaza silenciosamente |
| Guardado en Elementor | `$e.run('document/save/default')` — no `onClickButtonPublish()` solo |
| Nonce REST vs AJAX | `elementorCommon.config.rest.nonce` para REST API (distinto al AJAX nonce) |
| post_content vs _elementor_data | Son independientes en páginas canvas. set-page-v2 toca solo post_content |
| Rate limit Hostgator | Máx 1 req/10s. Pausar n8n workflows antes de sesiones WP largas |
| Rank Math score | Mínimo 85/100 antes de cerrar la tarea |
| Schema FAQPage | Via WPCode snippet 5911 (wp_footer hook) — nunca en post_content |

---

## ARCHIVOS TÉCNICOS GEO (crear para cada caso)

Guardar en: `C:/Users/rendi/Desktop/geo-files/[cliente]/`

- `llms.txt` — índice Markdown curado para AI bots
- `llms-full.txt` — contexto completo
- `robots-additions.txt` — Allow para GPTBot, Google-Extended, PerplexityBot, anthropic-ai, ClaudeBot
- `image-sitemap-[cliente].xml` — con `image:title` y `image:caption`

Subir al root de rendimension.com via endpoint:
```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"filename":"llms.txt","content":"[contenido]"}' \
  "https://rendimension.com/wp-json/rend-helper/v1/write-root-file"
```
(Requiere snippet 5910 activo — desactivar después)

---

## INVENTARIO DE CASOS PUBLICADOS

| Cliente | WP ID | Slug | Score | Estado |
|---|---|---|---|---|
| Alo Yoga | 5813 | alo-yoga-store-rendering | 69/100 (pendiente fix) | LIVE |
| House of Speed | 2185 | 3d-renders-investor-pitch | 88/100 + layout fixed | LIVE |
| Historic Firehouse | 2122 | historic-preservation-rendering-atlanta | 87/100 | LIVE -- Schema FAQPage+Article verificados. GEO files subidos. 301 redirect activo. |

**Pendiente Alo Yoga:** Rank Math score bajó de 91 a 69 tras insertar HTML widget en esta sesión. Requiere inyectar post_content SEO de 2500 palabras via set-page-v2.

---

## ENDPOINTS CUSTOM RENDIMENSION

| Endpoint | Uso |
|---|---|
| `POST /wp-json/rend-helper/v1/set-page-v2` | Inyectar post_content como base64 |
| `POST /wp-json/rend-helper/v1/upload-media-v2` | Subir imagen al Media Library |
| `POST /wp-json/rend-helper/v1/write-root-file` | Escribir archivos al root del hosting |

Todos tienen `permission_callback => '__return_true'` (sin auth requerida).

---

## SNIPPETS WPCODE ACTIVOS

| ID | Función |
|---|---|
| 5819 | Rank Math meta (title, description, keyword, slug) via wp_update_post |
| 5910 | write-root-file endpoint REST (activar/desactivar según necesidad) |
| 5911 | FAQPage + Article + Service schema JSON-LD via wp_footer |

---

## CHECKLIST RÁPIDO POR CASO

```
CLIENTE: _______________  |  WP ID: ___  |  Slug: _______________
Focus Keyword: _______________

[ ] Template verificado: elementor_canvas
[ ] HTML widget generado (sin em-dashes, sin non-ASCII)
[ ] HTML widget inyectado en Elementor + guardado con $e.run()
[ ] post_content SEO inyectado (2500+ palabras, ~1% keyword density)
[ ] Rank Math: title, meta, keyword, slug configurados
[ ] Schema: Article + FAQPage en snippet 5911
[ ] GEO files creados (llms.txt, llms-full.txt, robots-additions.txt, image-sitemap)
[ ] GEO files subidos al hosting root
[ ] GSC: indexación solicitada
[ ] Rank Math score: ___/100 (mínimo 85)
[ ] Documentado en Notion + memory/case_study_master_template.md
```

---

*Creado: 25 abril 2026 | Hugo Ramirez + Claude | Basado en 3 case studies completados y ~100 turnos de trabajo acumulado*
