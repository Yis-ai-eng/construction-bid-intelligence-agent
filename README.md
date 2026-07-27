# CBIA - Construction Bid Intelligence Assistant

Asistente basado en IA para analizar documentación de licitaciones de construcción, extraer requisitos clave y ayudar a equipos de estimación a preparar ofertas competitivas y cumplir con los requerimientos del proyecto.

## Descripción General

CBIA (Construction Bid Intelligence Assistant) es un asistente inteligente basado en IA diseñado para ayudar a profesionales de la construcción en el análisis de paquetes de licitación.

El sistema utiliza una arquitectura de **Retrieval-Augmented Generation (RAG)** que permite recuperar información relevante de documentos de licitación y generar respuestas fundamentadas únicamente en la evidencia encontrada dentro de dichos documentos.

El objetivo principal de CBIA es reducir el tiempo dedicado a la revisión manual de paquetes de licitación, facilitar la identificación de requisitos críticos y mejorar el control de cumplimiento durante el proceso de preparación de ofertas.

---

## Planteamiento del Problema

Los paquetes de licitación en la industria de la construcción suelen contener cientos de páginas de información, incluyendo invitaciones a licitar, especificaciones técnicas, documentos contractuales, formularios obligatorios, requisitos de seguros, bonds y documentos de cumplimiento.

La revisión manual de esta información puede ser un proceso lento y aumenta el riesgo de omitir requisitos importantes.

Algunos desafíos comunes incluyen:

- Identificar formularios obligatorios para la presentación de ofertas.
- Encontrar requisitos de seguros y garantías (bonds).
- Localizar fechas límite e instrucciones de entrega.
- Extraer obligaciones contractuales y administrativas.
- Reducir errores humanos durante la preparación de ofertas.

---

## Solución Propuesta

CBIA proporciona un flujo inteligente de análisis documental combinando procesamiento de documentos, búsqueda semántica mediante bases vectoriales y modelos de lenguaje (LLM).

El asistente permite realizar preguntas sobre el paquete de licitación y genera respuestas estructuradas incluyendo:

- Respuesta al requerimiento solicitado.
- Evidencia utilizada para generar la respuesta.
- Documento fuente y página correspondiente.
- Nivel de confianza de la información obtenida.

Mediante el uso de RAG, CBIA reduce el riesgo de respuestas generadas sin fundamento, ya que el modelo utiliza como referencia únicamente la información recuperada desde los documentos cargados.

---
## Arquitectura del Sistema

CBIA utiliza una arquitectura basada en **Retrieval-Augmented Generation (RAG)**, combinando procesamiento documental, búsqueda semántica y modelos de lenguaje.

El flujo general del sistema es:
