# Website & Blog — Rendimension.com | Operaciones

Documento operativo para el website principal y el blog de Rendimension.
**REGLA:** No tocar el diseño del website principal (Elementor). Solo trabajar sobre el blog.

## Acceso al WordPress

- **Hosting:** Hostgator México → cPanel → WordPress
- **URL WP Admin:** https://www.rendimension.com/wp-admin/
- **WordPress user:** hugoa5166e13285
- **REGLA:** No tocar la interfaz del website (diseño complejo Elementor). Solo trabajar con el blog.

## Stack Técnico del Sitio

- **CMS:** WordPress + UICore Theme + Elementor Pro
- **SEO:** Rank Math Pro
- **Cache:** WP Rocket
- **Forms:** Fluent Forms
- **Plugins clave:** WPCode, Element Pack Pro, Complianz, Babylovegrowth, FileBird
- **Posts:** /blog/%postname%/ — 166 artículos activos
- **Pages:** URL raíz propia (/slug/) — 88 páginas (87 publicadas)

## Estructura del Blog

- **URL del blog:** https://rendimension.com/blog/
- **Categoría principal posts n8n:** "Renderings" — ID: 1465
- **Estructura objetivo:** rendimension.com/blog/SLUG

## Workflow n8n — WordPress Blog Rendimension

- **Workflow ID:** fQ2k6PIiMG958wywRjAqR
- **URL:** https://n8n.srv1286578.hstgr.cloud/workflow/fQ2k6PIiMG958wywRjAqR
- **Google Sheet topics:** https://docs.google.com/spreadsheets/d/18FsoXne3uslpcr8FmGbBDJmSbXkVldytKhtbyjOmCzQ/edit
- **Pipeline:** Google Sheets → Brand Config → Perplexity (research) → Claude AI (contenido bloques) → Gemini (imagen) → WP Media API → WP Posts API → Google Sheets (update status)

## Reglas Permanentes

- Los 301 deben estar activos indefinidamente (mínimo 1 año)
- Nunca borrar un post viejo sin tener la redirección activa
- **No editar ni tocar el diseño del website principal bajo ninguna circunstancia**

## Case Studies — Arquitectura de URLs

- **Índice:** rendimension.com/case-studies/
- **Individual:** rendimension.com/case-studies/[cliente]/
- **Parent Page ID:** 5611
- **Template:** elementor_canvas.php
- **Estilo:** PREMIUM (diseño oscuro, visual, igual que Homepage y About Us)

## Case Studies Live

| Caso | URL | Rank Math Score |
|---|---|---|
| Alo Yoga | /case-studies/alo-yoga/ | 85+ |
| House of Speed | /case-studies/3d-renders-investor-pitch/ | 88/100 |
| Historic Firehouse | /case-studies/historic-firehouse-restaurant-rendering/ | 87/100 |

## Pendientes SEO

| Tarea | Detalle | Bloqueado por |
|---|---|---|
| Google Indexing API | Crear Service Account en Google Cloud, subir JSON a Rank Math | Hugo |
| Redirect /services/interior-rendering | Definir URL destino | Hugo |
| Redirect /blog/meet-us | → /rendimension-team/ | Claude |
| Redirect /blog/team | → /rendimension-team/ | Claude |
