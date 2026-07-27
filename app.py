import os
import zipfile
import tempfile
import streamlit as st
from collections import Counter

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI


DEFAULT_SYSTEM_PROMPT = """
Eres CBIA (Construction Bid Intelligence Assistant).

Tu misión es ayudar a estimadores y contratistas a analizar Bid Packages de construcción.

REGLAS:
- Usa únicamente la información encontrada en el Bid Package.
- Nunca inventes información.
- Siempre cita documento, categoría y página.
- Si la información no existe, dilo claramente.
- Si hay conflicto entre documentos, indícalo.
- Los Addenda prevalecen sobre documentos anteriores.

Formato:
Respuesta
Evidencia
Documento
Categoría
Página
Notas adicionales
"""


def setup_environment():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY no encontrada.")
    return api_key


def extract_bid_package(zip_path):
    folder = tempfile.mkdtemp()
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(folder)
    return folder


def classify_document(filename):
    name = filename.lower()

    if "bond" in name:
        return "Bond Forms"
    elif "addendum" in name:
        return "Addendum"
    elif "plan" in name or "specification" in name:
        return "Plans and Specifications"
    elif "condition" in name:
        return "General Conditions"
    elif "agreement" in name or "contract" in name:
        return "Contract Documents"
    elif "itb" in name or "invitation" in name:
        return "Bid Instructions"
    return "Other Documents"


def build_inventory(folder):
    inventory = []

    for root, _, files in os.walk(folder):
        for file in files:
            inventory.append({
                "filename": file,
                "category": classify_document(file)
            })

    return inventory


def load_documents(folder):
    documents = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".pdf"):
                path = os.path.join(root, file)
                documents.extend(PyPDFLoader(path).load())

    return documents


def add_metadata(documents, inventory):
    category_map = {
        x["filename"]: x["category"]
        for x in inventory
    }

    for doc in documents:
        filename = os.path.basename(doc.metadata["source"])
        doc.metadata["category"] = category_map.get(
            filename, "Unknown"
        )
        doc.metadata["page_number"] = doc.metadata.get("page", 0) + 1

    return documents


def create_vectorstore(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.from_documents(chunks, embeddings)


def build_llm():
    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=setup_environment(),
        model="cohere/north-mini-code:free",
        temperature=0.1
    )


def retrieve_context(vectorstore, question, k=5):
    docs = vectorstore.similarity_search(question, k=k)

    context = ""

    for doc in docs:
        context += f"""
DOCUMENT: {os.path.basename(doc.metadata['source'])}
CATEGORY: {doc.metadata['category']}
PAGE: {doc.metadata['page_number']}

{doc.page_content}

-----------------------------
"""

    return context


def ask_cbia(question, vectorstore, llm):
    context = retrieve_context(vectorstore, question)

    prompt = f"""
{DEFAULT_SYSTEM_PROMPT}

Evidence from Bid Package:

{context}

Question:
{question}

Answer using only the evidence provided.
"""

    return llm.invoke(prompt).content


def main():

    st.set_page_config(
        page_title="CBIA - Construction Bid Intelligence Assistant",
        layout="wide"
    )

    st.title("🏗️ CBIA - Construction Bid Intelligence Assistant")
    st.write(
        "Upload a Bid Package (.zip) and ask questions about the documents."
    )

    uploaded = st.file_uploader(
        "Upload Bid Package",
        type="zip"
    )

    if uploaded:

        if "vectorstore" not in st.session_state:

            with st.spinner("Processing Bid Package..."):

                temp_zip = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".zip"
                )

                temp_zip.write(uploaded.read())
                temp_zip.close()

                folder = extract_bid_package(
                    temp_zip.name
                )

                inventory = build_inventory(folder)

                docs = load_documents(folder)
                docs = add_metadata(
                    docs,
                    inventory
                )

                st.session_state.vectorstore = create_vectorstore(
                    docs
                )

                st.session_state.llm = build_llm()

                st.success(
                    f"Package loaded: {len(docs)} pages indexed"
                )

        question = st.text_input(
            "Ask CBIA about the Bid Package:"
        )

        if question:

            with st.spinner("Analyzing..."):

                answer = ask_cbia(
                    question,
                    st.session_state.vectorstore,
                    st.session_state.llm
                )

            st.markdown(answer)


if __name__ == "__main__":
    main()
