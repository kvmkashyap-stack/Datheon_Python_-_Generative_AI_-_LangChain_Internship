# Task 2: RetrieveAI — RAG Document Question Answering

RetrieveAI is a document question-answering application built using Retrieval-Augmented Generation (RAG). Users can upload PDF or TXT files through a Streamlit interface and ask questions about their contents.

## Features

- Upload PDF and TXT documents directly through the web interface.
- Extract and recursively chunk document text.
- Generate embeddings using Google Gemini.
- Store and retrieve document chunks using ChromaDB.
- Generate context-grounded answers using Gemini.
- Display source citations, including PDF page numbers when available.
- Reject unsupported questions when the retrieved context is insufficient.
- Keep indexed uploads in document-specific database directories.

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- ChromaDB
- PyPDF

## Setup

1. Create and activate a Python virtual environment.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example` and add your Gemini API key.

4. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal, upload a PDF or TXT file, and ask questions.

## Run Tests

```bash
python -m pytest tests -v
```

## Project Structure

- `app.py` — Streamlit upload and chat interface.
- `main.py` — Command-line interface.
- `ingestion/loader.py` — PDF and TXT loading.
- `ingestion/chunker.py` — Recursive text chunking.
- `retrieval/vector_store.py` — Embeddings and ChromaDB operations.
- `retrieval/rag_chain.py` — Retrieval, answer generation, and citation handling.
- `prompts/rag_prompt.py` — Instructions for grounded answers.
- `tests/` — Automated tests.

## Limitations

- Requires a valid Google Gemini API key and internet access for embedding and answer generation.
- Scanned PDFs without extractable text may require OCR.
- TXT files do not provide PDF-style page citations.
- Answers depend on the relevance and quality of retrieved document chunks.
