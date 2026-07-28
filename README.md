# 🏗️ CBIA – Construction Bid Intelligence Agent

**CBIA (Construction Bid Intelligence Agent)** es un agente inteligente desarrollado para asistir en el análisis de paquetes de licitación (Bid Packages) del sector construcción mediante técnicas de **Retrieval-Augmented Generation (RAG)**.

El sistema transforma cientos de páginas de documentos técnicos en una base de conocimiento consultable mediante lenguaje natural, proporcionando respuestas fundamentadas exclusivamente en la documentación del proyecto.

---

# 🎯 Objetivo

Automatizar el análisis de licitaciones de construcción permitiendo que un usuario pueda realizar preguntas como:

- ¿Cuál es el presupuesto del proyecto?
- ¿Qué Addendum modificó este requisito?
- ¿Qué documentos deben entregarse con la oferta?
- ¿Cuál es la fecha límite?
- ¿Qué exige el Performance Bond?

Cada respuesta se genera utilizando únicamente la evidencia encontrada dentro del Bid Package.

---

# ✨ Características

- 📄 Clasificación automática de documentos del Bid Package.
- 📚 Extracción de texto desde archivos PDF.
- 🏷️ Enriquecimiento de metadatos (documento, categoría y página).
- ✂️ División inteligente del contenido en *chunks*.
- 🧠 Búsqueda semántica mediante embeddings locales.
- 🔎 Base vectorial utilizando FAISS.
- 🤖 Recuperación de evidencia mediante arquitectura RAG.
- ✅ Respuestas estructuradas y trazables al documento original.

---

# 🛠️ Tecnologías utilizadas

- Python
- Google Colab
- LangChain
- FAISS
- Sentence Transformers (Hugging Face)
- Cohere
- Streamlit
- OpenRouter (LLM)
- GitHub

---

# 📂 Arquitectura

```text
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

## 🖥️ Cómo usar CBIA

1. Abre la aplicación en tu navegador (`http://localhost:8501`).
2. Sube el Bid Package (PDF o CSV) que quieras analizar usando el panel de carga.
3. Espera a que el sistema procese el documento (clasificación, chunking y creación de embeddings).
4. Escribe tu pregunta en el cuadro de texto, por ejemplo: "¿Cuál es el presupuesto del proyecto?"
5. El agente responderá citando el documento, la categoría y la página donde encontró la evidencia.
6. Si la información no existe en el Bid Package, el agente lo indicará explícitamente en lugar de inventar una respuesta.

---

# 🚀 Cómo ejecutar

Sigue estos pasos para ejecutar CBIA localmente:

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repositorio>
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar la variable de entorno

CBIA utiliza [OpenRouter](https://openrouter.ai/) como proveedor del LLM. Necesitas una API key propia:

```bash
# Linux / macOS
export OPENROUTER_API_KEY="tu_api_key_aquí"

# Windows (PowerShell)
$env:OPENROUTER_API_KEY="tu_api_key_aquí"
```

También puedes crear un archivo `.env` en la raíz del proyecto:

```
OPENROUTER_API_KEY=tu_api_key_aquí
```

### 4. Ejecutar la aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador (por defecto en `http://localhost:8501`).

---

# 💬 Ejemplos de preguntas

- ¿Cuál es el presupuesto del proyecto?
- ¿Qué Addendum modificó este requisito?
- ¿Qué documentos deben entregarse con la oferta?
- ¿Cuál es la fecha límite?
- ¿Qué exige el Performance Bond?

---

# 📝 Ejemplo de respuesta generada

> **Pregunta:** _What are the required documents for bid submission?_
>
> **Respuesta del agente:** _Respuesta de CBIA
**Respuesta**
El licitador debe presentar los siguientes documentos / anexos obligatorios para completar la presentación de la oferta:
1. Anexo de experiencia de personas clave** nombre y licencia del individuo que tendrá supervisión personal del trabajo.
2. ** Documentación de equipos** (a) Equipos de propiedad disponible para el trabajo, (b) Equipos que se comprarán para el trabajo propuesto, (c) Equipos que se alquilarán para el trabajo prop
3. Certificado de estatus, competencia y / o registro estatal del licitador. **
Formulario de confirmación** (la declaración de que el licitador reconoce que la información será utilizada por la ciudad y que está garantizada como verdadera).
5. **Formulario de verificación de antecedentes penales** (el formulario de verificación de antecedentes penales es el requisito de verificación de antecedentes referenced en los documentos de
**Evidencia utilizada**
Evidencia (extracto) |
Documento |
Categoría |
Página |
1 "*Respuesta requerida Experience of Key Individuals attachment (optional upload) State the name and licensing of the individual who will have personal supervision of the Work." ITB26
|2| "* "*Respuesta requerida What equipment will you purchase for the proposed Work?" | IT826-6310-258
Respuesta requerida What equipment do you own that is available for the Work? (Attach additional sheets as necessary)" | ITB26-6310-258-Fuel_Bay_Overhead_Canopy_Replacement.pdf | Bid _-_Fuel_Bay_Overhead_Canopy_Replacement.pdf | Bid Instructions | 31 |
|4| "*Respuesta requerida What equipment will you rent for the proposed Work?" | ITB26-6310-258- Fuel_Bay_Overhead_Canopy_Replacement.pdf | Bid Instructions | 31 |
"*Respuesta requerida Please attach certificate of status, competency, and/or state registration." ITB26-6310-258 Fuel Bay Overhead Canopy Replacement.pdf | Bid Instructions | 31 | 6 " The BIDDER acknowledges and understands that the information contained in this response shall be relied upon by CITY" (confirmación de la oferta) | ITB26-6310-258 Fuel Bay Overhead C
|7| "The Criminal Background Screening form is the background screening requirement referenced in the bid documents." | ADDENDUM 3-Fuel_Bay_Overhead_Canopy_Replacement.pdf | Addendum | 1 |

**Nivel de confianza**
**Alto** para los cinco elementos enumerados en las Instrucciones de Licitación (están marcados explícitamente como "Respuesta requerida*").
**Moderado para el Formulario de Verificación de Antecedentes Penales, ya que se menciona como el requisito referenced, pero no se enumera como un anexo separado en las Instrucciones de Lic
**Notas adicionales**
Todos los elementos enumerados en las Instrucciones de Licitación (página 31) deben ser proporcionados como parte de la respuesta de la oferta; el lenguaje "*Respuesta requerida" indica que El Addendum 3 aclara que el Formulario de Verificación de Antecedentes Penales satisface cualquier requisito de verificación de antecedentes, por lo que también debe ser incluido en la presen
Si algún otro documento (por ejemplo, el formulario de solicitud de pago, el formulario de licitación) se requiere, se haría referencia a él en los propios Documentos de Licitación; no se menciona)_
>
> **Documentos fuente**
 _ITB26-6310-25B_-_Fuel_Bay_Overhead_Canopy_Replacement.pdf
ADDENDUM 3- Fuel_Bay_Overhead_Canopy_Replacement.pdf
**Páginas**
31 (ITB Instrucciones de licitación)
1 (Addendum 3)_

---

# 🔒 Trust Policy

CBIA fue diseñado bajo un principio fundamental:

> **Toda respuesta debe poder rastrearse hasta el documento original.**

Por esta razón:

- Cada respuesta identifica la fuente utilizada.
- Se indica el documento, la categoría y la página correspondiente.
- Si la información no existe dentro del Bid Package, el agente lo comunica explícitamente en lugar de generar información inventada.

---

# ⚠️ Desafíos del desarrollo

Durante el desarrollo surgieron varios retos técnicos que permitieron fortalecer la arquitectura del proyecto:

- Cambios en los modelos de embeddings disponibles en Google AI Studio.
- Restricciones de cuota (Rate Limits) de la API de Gemini.
- Migración hacia embeddings locales utilizando Sentence Transformers.
- Organización del notebook para mantener un flujo claro y reproducible.
- Implementación de un sistema de recuperación semántica independiente del proveedor del modelo de lenguaje.

Estas decisiones hicieron que la arquitectura fuera más robusta, portable y fácil de reproducir.

---

# 📌 Estado del proyecto

- ✅ Clasificación automática de documentos
- ✅ Extracción de texto desde PDF
- ✅ Enriquecimiento de metadatos
- ✅ División en chunks
- ✅ Embeddings locales
- ✅ Base vectorial FAISS
- ✅ Recuperación semántica (RAG)
- ✅ Respuestas fundamentadas mediante LLM

---

# Bid Package (Sample)
Contiene ejemplos de documentos de licitación de construcción utilizados para probar el sistema de recuperación de datos de CBIA.

---
# Link del deployment

https://construction-bid-intelligence-agent-xnoiopw3hjsehzkbx4j9x9.streamlit.app/

---
# Video demostrativo:

https://youtu.be/N4ZYckGr6sU

---

# 🙏 Agradecimientos

Este proyecto fue desarrollado en el marco del programa de becas de **Oracle Cloud**, cuyo apoyo hizo posible el aprendizaje y la aplicación práctica de Inteligencia Artificial Generativa. Agradezco a Oracle Cloud por brindar la oportunidad de formación que permitió construir CBIA.

---

# 👩‍💻 Autora

**Yisdenis Quiroz**

Ingeniero Civil | Data Specialist | AI Trainer

Proyecto desarrollado como parte del aprendizaje y aplicación práctica de Inteligencia Artificial Generativa, LangChain y arquitecturas RAG orientadas al sector construcción.

