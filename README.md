# CBIA - Construction Bid Intelligence Assistant

Asistente basado en IA para analizar documentación de licitaciones de construcción, extraer requisitos clave y ayudar a equipos de estimación a preparar ofertas competitivas y cumplir con los requerimientos del proyecto.

# 🏗️ CBIA – Construction Bid Intelligence Agent

**CBIA (Construction Bid Intelligence Agent)** es un agente inteligente desarrollado para asistir en el análisis de paquetes de licitación (Bid Packages) del sector construcción mediante técnicas de **Retrieval-Augmented Generation (RAG)**.

El sistema permite transformar cientos de páginas de documentos técnicos en una base de conocimiento consultable mediante lenguaje natural, proporcionando respuestas fundamentadas exclusivamente en la documentación del proyecto.

---

## 🎯 Objetivo

Automatizar el análisis de licitaciones de construcción permitiendo que un usuario pueda realizar preguntas como:

* ¿Cuál es el presupuesto del proyecto?
* ¿Qué Addendum modificó este requisito?
* ¿Qué documentos debo entregar con la oferta?
* ¿Cuál es la fecha límite?
* ¿Qué exige el Performance Bond?

Cada respuesta se genera utilizando únicamente la evidencia encontrada dentro del Bid Package.

---

## ✨ Características

* Clasificación automática de documentos del Bid Package.
* Extracción de texto desde archivos PDF.
* Enriquecimiento de metadatos (documento, categoría y página).
* División inteligente del contenido en *chunks* para mejorar la recuperación de información.
* Búsqueda semántica mediante embeddings locales.
* Base vectorial utilizando FAISS.
* Recuperación de evidencia relevante (RAG).
* Respuestas estructuradas y trazables al documento original.

---

## 🛠️ Tecnologías utilizadas

* Python
* Google Colab
* LangChain
* FAISS
* Sentence Transformers (HuggingFace)
* Cohere (LLM)
* GitHub

---

## 📂 Flujo del proyecto

```
Bid Package (PDF)

        │

        ▼

Clasificación de documentos

        │

        ▼

Extracción de texto

        │

        ▼

Enriquecimiento de metadatos

        │

        ▼

Creación de Chunks

        │

        ▼

Embeddings Locales

        │

        ▼

FAISS Vector Store

        │

        ▼

Búsqueda Semántica

        │

        ▼

LLM + RAG

        │

        ▼

Respuesta basada en evidencia
```

---

## 🔒 Política de confianza (Trust Policy)

CBIA fue diseñado bajo un principio fundamental:

> **Toda respuesta debe poder rastrearse hasta el documento original.**

Por esta razón:

* Cada respuesta indica la fuente utilizada.
* Se identifica el documento, la categoría y la página correspondiente.
* Si la información no existe dentro del Bid Package, el agente lo comunica explícitamente en lugar de inventar una respuesta.

---

## ⚠️ Desafíos durante el desarrollo

Durante el desarrollo surgieron varios retos técnicos que permitieron fortalecer la arquitectura del proyecto:

* Cambios en los modelos de embeddings disponibles en Gemini.
* Restricciones de cuota (Rate Limits) de la API de Google AI Studio.
* Migración desde embeddings en la nube hacia embeddings locales mediante Sentence Transformers.
* Organización del notebook para mantener un flujo de trabajo claro y reproducible.
* Implementación de un sistema de recuperación semántica independiente del proveedor del modelo de lenguaje.

Estas decisiones hicieron que la arquitectura fuera más robusta, portable y fácil de reproducir.

---

## 📌 Estado del proyecto

✅ Clasificación automática de documentos

✅ Extracción de texto desde PDF

✅ Enriquecimiento de metadatos

✅ División en chunks

✅ Embeddings locales

✅ Base vectorial FAISS

✅ Recuperación semántica (RAG)

✅ Respuestas fundamentadas mediante LLM

---

## 👩‍💻 Autora

**Yisdenis Quiroz**

Ingeniera Civil | Data Specialist | AI Trainer

Proyecto desarrollado como parte del proceso de aprendizaje y aplicación práctica de Inteligencia Artificial Generativa, LangChain y arquitecturas RAG orientadas al sector construcción.

