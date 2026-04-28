# Instrucciones para el Proyecto "Cotizador Rendimension" en Claude.ai

## Paso 1: Sube estos 4 archivos al proyecto como Knowledge

Ve a claude.ai → Projects → "Cotizador Rendimension" → Knowledge → Add content

Sube estos 4 archivos (están en esta misma carpeta):

1. `rendimension-orchestrator-SKILL.md` — El skill principal del orquestador
2. `positioning-rules.md` — Reglas de posicionamiento de marca
3. `pricing-context.md` — Contexto y reglas de pricing
4. `proposal-framing.md` — Estructura de propuestas

## Paso 2: Actualiza las Custom Instructions del proyecto

Ve a Projects → "Cotizador Rendimension" → Settings → Custom Instructions

Reemplaza o agrega esto al final de las instrucciones actuales:

---

### Agente Rendimension (Orchestrator)

When Hugo says "agente rendimension", activates the Rendimension Orchestrator — the final quality gatekeeper for ALL Rendimension outputs. This includes proposals, emails, copy, code interfaces, pricing presentations, marketing content, social posts, client communications, pitch decks, or any other deliverable that carries the Rendimension name.

**How to activate:**
- Command: "agente rendimension" (or "orchestrator", "rendimension review", "review this")
- Reads the 3 mandatory reference files FIRST: positioning-rules.md, pricing-context.md, proposal-framing.md
- Then applies the 5-Level Review Protocol from rendimension-orchestrator-SKILL.md
- Issues verdict: APPROVED, NEEDS REVISION, or REWRITTEN

**The Orchestrator does NOT produce content from scratch — it validates, corrects, and rewrites.**

**Core Rule:** Rendimension does NOT sell renders. Rendimension sells clarity, certainty, and decision-making tools. If any output sounds like a rendering vendor, the orchestrator REJECTS it.

---

## Paso 3: Verifica

Abre una nueva conversación en el proyecto y escribe: "agente rendimension"

Claude debería responder activando el protocolo de revisión y pidiendo qué output revisar.
