# Image Pipeline — Reglas, Configuración y Protocolos (Fase 2.5)

**Creado:** 7 abril 2026 | **n8n Workflow:** RlKwFzFPYIZskIFt | Protocolo permanente para todos los proyectos de Rendimension

## Propósito

Este documento registra TODAS las reglas, decisiones y configuraciones del pipeline automático de imágenes de Rendimension. Aplica a todos los proyectos actuales y futuros como protocolo permanente.

## Tipos de Archivo por Proyecto

| Formato | Qué es | Acción del Pipeline |
|---|---|---|
| PDF | Planos, indicaciones o instrucciones de trabajo. NUNCA renders finales. | IGNORAR |
| PNG / JPG / JPEG | Renders finales O referencias de clientes. | PROCESAR |
| DXF, DWG, SKP, AI, PSD | Archivos de trabajo técnico. | IGNORAR |
| ZIP | Paquetes de entrega. El pipeline no descomprime. | IGNORAR |
| DOC, DOCX, XLS | Administrativos. | IGNORAR |

**Regla fija de Hugo:** Los PDFs son siempre planos o instrucciones. Hugo NUNCA envía renders finales en PDF.

## Keywords que Identifican Renders Finales (alta prioridad)

- "Final" en el asunto o cuerpo del correo
- "Final Hi Res" o "Hi Res" = versión de alta resolución lista para uso profesional
- "Final Files" = entrega completa del proyecto
- Archivos mayores de 2MB con extensión PNG/JPG generalmente son renders

## Keywords que Identifican Correos de Revisión (baja prioridad)

- "Updates", "Edits", "Changes", "Markup", "Comments" = instrucciones de revisión, no renders finales
- "Proposal", "Estimate", "Invoice" = administrativos
- Archivos menores de 500KB suelen ser referencias o planos, no renders

## Configuración Técnica del Pipeline

### Nodo: Resize Image
- Ancho: 2400px
- Alto: 0 (proporcional automático)
- Modo: resize by width
- Razón: renders originales son típicamente 4K+. 2400px es reducción limpia.

### Nodo: Upload to WordPress
- Endpoint: https://rendimension.com/wp-json/wp/v2/media
- Credencial: TICrJJ1LAadP9pqu (Wordpress account)
- Binary field: data (output del nodo Resize Image)
- Después de subir: pipeline llama a FileBird API para asignar la imagen a la carpeta correcta

### Nodo: Generate Alt Tag
Detecta tipo de proyecto: retail / hospitality / residential / commercial / architectural
Detecta tipo de vista: interior, exterior, lobby, storefront, fitting room, etc.
Detecta locación desde lista de ubicaciones conocidas (Boston, Stanford, Bloor, Cabazon, Miami, etc.)

## Estrategia de Alt Tags y SEO/GEO

**Formato del alt tag:**
[Cliente] [tipo de vista], [ciudad], [keyword de servicio] by Rendimension

**Ejemplo Alo Yoga Stanford:**
- Alt: Alo Yoga interior view, Stanford, CA, retail interior rendering by Rendimension
- Title: Alo Yoga Stanford, CA interior view | Retail store design | Rendimension
- Caption: Alo Yoga retail store design rendering, Stanford, CA. Photorealistic architectural visualization by Rendimension — Hugo Ramirez, Architect. Miami, FL.

**Entidades cubiertas:**
- Rendimension (empresa) en alt, title, caption, description
- Hugo Ramirez, Architect (persona) en caption y description

**Keywords de servicio incluidos automáticamente:**
retail store design, retail interior rendering, store visualization, commercial interior rendering, store design, 3D architectural rendering

## Organización en WordPress: FileBird

Estructura de carpetas:
```
Rendimension Renders/
  Alo Yoga/
    Stanford/
    Boston/
    Toronto Bloor/
    Cabazon/
  [Siguiente cliente]/
    [Locación]/
```

## Contactos Alo Yoga

| Nombre | Email | Rol |
|---|---|---|
| Jackie Balmanoukian | Jackie.Balmanoukian@aloyoga.com | Contacto principal, Store Design & Architecture |
| Sarah Holden | Sarah.Holden@aloyoga.com | Store Design & Architecture |
| Laura Donovan | Laura.Donovan@aloyoga.com | Store Design & Architecture |
| Lunch Brent | Lunch.Brent@aloyoga.com | Senior Store Designer |

Dominios: @aloyoga.com, @bellacanvas.com

## Estrategia de Query Gmail por Proyecto

```
# Query base (todos los adjuntos imagen de un cliente)
from:[contacto@cliente.com] has:attachment (filename:jpg OR filename:png)

# Query prioritaria (renders finales)
subject:"Final" from:[cliente] has:attachment

# Query alta calidad
subject:("Final Hi Res" OR "Final Files") has:attachment
```

Query recomendada para Alo Yoga:
```
(from:aloyoga.com OR from:bellacanvas.com OR subject:"Alo") has:attachment (filename:jpg OR filename:png OR filename:jpeg)
```

Para activar el pipeline via webhook:
```
POST https://n8n.srv1286578.hstgr.cloud/webhook/image-pipeline
{
  "gmail_query": "from:aloyoga.com has:attachment (filename:jpg OR filename:png)",
  "client_name": "Alo Yoga"
}
```
