import hashlib
import os
import tempfile
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from ingestion.loader import load_document
from ingestion.chunker import split_documents
from retrieval.vector_store import create_vector_store
from retrieval.rag_chain import answer_question


load_dotenv()

st.set_page_config(
    page_title="RetrieveAI",
    page_icon="??",
    layout="centered",
)

st.title("?? RetrieveAI")
st.caption("Upload a document and ask questions about its contents.")

if not os.getenv("GEMINI_API_KEY"):
    st.error("GEMINI_API_KEY is missing. Add it to your .env file.")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "txt"],
    help="Select a PDF or TXT file from your computer.",
)

if uploaded_file is None:
    st.info("Upload a PDF or TXT document to get started.")
    st.stop()

file_bytes = uploaded_file.getvalue()
file_hash = hashlib.sha256(file_bytes).hexdigest()
upload_key = f"{uploaded_file.name}:{file_hash}"

if st.session_state.get("upload_key") != upload_key:
    st.session_state.upload_key = upload_key
    st.session_state.messages = []
    st.session_state.db_directory = str(
        Path("uploaded_db") / file_hash
    )
    st.session_state.indexed = False

if not st.session_state.get("indexed", False):
    suffix = Path(uploaded_file.name).suffix.lower()

    try:
        with st.spinner("Reading and indexing your document..."):
            temporary_path = None

            try:
                with tempfile.NamedTemporaryFile(
                    mode="wb",
                    suffix=suffix,
                    delete=False,
                ) as temporary_file:
                    temporary_file.write(file_bytes)
                    temporary_path = temporary_file.name

                documents = load_document(temporary_path)

                for document in documents:
                    document.metadata["source"] = uploaded_file.name

                chunks = split_documents(documents)

                if not chunks:
                    st.error("No readable text was found in this document.")
                    st.stop()

                create_vector_store(
                    chunks,
                    persist_directory=st.session_state.db_directory,
                    source_path=uploaded_file.name,
                )

            finally:
                if temporary_path and os.path.exists(temporary_path):
                    os.remove(temporary_path)

        st.session_state.indexed = True
        st.success(
            f"Indexed **{uploaded_file.name}** "
            f"into {len(chunks)} text chunks."
        )

    except Exception as exc:
        st.error(f"Could not process this document: {exc}")
        st.stop()

st.divider()
st.subheader("Ask your document")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            st.markdown("**Sources**")
            for source in message["sources"]:
                st.markdown(f"- {source}")

question = st.chat_input("Ask a question about your document...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching your document..."):
            try:
                result = answer_question(
                    question,
                    persist_directory=st.session_state.db_directory,
                )

                st.markdown(result["answer"])

                if result["sources"]:
                    st.markdown("**Sources**")
                    for source in result["sources"]:
                        st.markdown(f"- {source}")

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": result["answer"],
                        "sources": result["sources"],
                    }
                )

            except Exception as exc:
                st.error(f"Could not answer your question: {exc}")
