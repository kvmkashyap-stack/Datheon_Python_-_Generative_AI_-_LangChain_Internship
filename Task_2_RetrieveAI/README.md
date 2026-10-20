# RetrieveAI — RAG-Based Document Question Answering

## 1. Project Overview

RetrieveAI is a Python-based Generative AI application that answers questions about uploaded PDF and text documents using Retrieval-Augmented Generation (RAG), LangChain, Google Gemini, and ChromaDB.

Finding specific information in lengthy documents can be time-consuming. RetrieveAI addresses this problem by allowing users to upload documents and ask questions in natural language. The application retrieves relevant passages from the uploaded document and uses a large language model to generate answers grounded in the retrieved context.

The application combines document ingestion, recursive text chunking, vector embeddings, semantic retrieval, prompt engineering, and source citations to provide a document question-answering experience through a Streamlit web interface.

## 2. Problem Statement

Extracting relevant information from lengthy documents manually can be repetitive and inefficient. General-purpose language models may also generate unsupported answers when they lack access to the information required to answer a question.

The objective of RetrieveAI is to develop a document question-answering application that accepts PDF and text files, processes their content, retrieves relevant information for a user query, and generates context-grounded answers with source references.

The application should prioritize information contained in the uploaded document and avoid presenting unsupported information as fact.

## 3. Key Features

- **Document ingestion:** Loads content from PDF and TXT files.
- **Recursive text chunking:** Splits lengthy documents into smaller, overlapping text chunks for retrieval.
- **Vector embeddings:** Converts text chunks into vector representations for semantic search.
- **Vector database:** Uses ChromaDB to store and retrieve document embeddings.
- **Semantic retrieval:** Retrieves relevant passages based on the user's question.
- **LLM-based answer generation:** Uses Google Gemini through LangChain to generate answers from retrieved context.
- **Context-grounded responses:** Instructs the language model to answer using the retrieved document content.
- **Source citations:** Displays source references for answers, including the document name when available.
- **Unsupported-answer handling:** Abstains when the retrieved context does not adequately support an answer.
- **Streamlit interface:** Allows users to upload documents and ask questions without manually entering file paths.
- **Document isolation:** Uses separate vector-store locations for uploaded documents to reduce accidental mixing of unrelated document content.
- **Automated testing:** Uses pytest to test document loading, chunking, vector-store behavior, and RAG functionality.

## 4. Supported Inputs and Outputs

### Input

- PDF documents
- Plain-text (`.txt`) documents
- Natural-language questions about the uploaded document

### Output

- A generated answer based on retrieved document passages
- Source references associated with the retrieved context
- An abstention response when sufficient supporting information is unavailable

The quality of the response depends on the document content, retrieval results, embedding quality, and language-model behavior.

## 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini | Large Language Model used for answer generation |
| LangChain | Document processing, text splitting, embeddings, retrieval, and LLM integration |
| ChromaDB | Vector database for storing and searching document embeddings |
| Streamlit | Web interface for document uploads and question answering |
| PDF and text loaders | Loading supported document formats |
| RecursiveCharacterTextSplitter | Splitting documents into smaller, overlapping chunks |
| Vector embeddings | Representing text for semantic similarity search |
| Pydantic / Python validation | Supporting structured validation where applicable |
| pytest | Automated testing |
| python-dotenv | Loading API credentials from environment variables |

## 6. How It Works

RetrieveAI follows a Retrieval-Augmented Generation workflow.

1. **Document upload:** The user uploads a PDF or TXT file through the Streamlit interface.
2. **Document loading:** The application extracts readable text and associated metadata from the uploaded document.
3. **Text chunking:** The extracted content is divided into smaller, overlapping chunks using a recursive character text splitter.
4. **Embedding generation:** The application converts the chunks into vector embeddings.
5. **Vector storage:** The embeddings and associated document metadata are stored in ChromaDB.
6. **User query:** The user submits a natural-language question about the uploaded document.
7. **Semantic retrieval:** The application searches the vector database for passages relevant to the question.
8. **Prompt construction:** The retrieved passages are provided to the language model as supporting context alongside instructions to avoid unsupported claims.
9. **Answer generation:** Google Gemini generates an answer using the supplied context.
10. **Source references:** The application displays the answer along with available source information, such as the document filename.
11. **Unsupported questions:** When the retrieved context does not support a reliable answer, the application is instructed to abstain rather than invent information.

This approach combines the retrieval capabilities of a vector database with the language-generation capabilities of an LLM.

## 7. Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation combines information retrieval with language-model generation.

A conventional LLM generates responses from its learned parameters and the context supplied in a prompt. A RAG application first retrieves relevant information from an external knowledge source and then provides that information to the LLM to help answer the user's question.

RetrieveAI implements this workflow through three main stages:

### 1. Retrieval

The user's question is used to search for relevant document chunks in ChromaDB.

### 2. Augmentation

The retrieved passages are added to the prompt as contextual evidence for the language model.

### 3. Generation

The language model generates a response based on the question and retrieved context.

**Important:** RAG can improve grounding, but it does not guarantee factual correctness. Retrieval may miss relevant passages, and an LLM may still misinterpret the available evidence. Source citations and unsupported-answer handling help make the results easier to inspect.

## 8. Document Processing and Data Handling

RetrieveAI processes documents through a series of ingestion and retrieval steps.

- PDF and TXT loaders extract readable document content.
- Text splitting breaks long content into smaller chunks suitable for retrieval.
- Chunk overlap helps preserve context across adjacent chunks.
- Embeddings represent chunks in a form suitable for semantic similarity search.
- ChromaDB stores vectors and document metadata.
- Retrieved passages provide context for answer generation.
- Source metadata helps identify where supporting information originated.

The application maintains separate vector-store locations for uploaded documents to reduce the risk of retrieving content from an unrelated upload.

The application can only retrieve information present in the content it successfully extracts and indexes. Scanned PDFs may require OCR if their pages do not contain extractable text.

## 9. Project Structure

```text
Task_2_RetrieveAI/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── ingestion/
│   ├── __init__.py
│   ├── loader.py
│   └── chunker.py
├── prompts/
│   └── rag_prompt.py
├── retrieval/
│   ├── __init__.py
│   ├── vector_store.py
│   └── rag_chain.py
└── tests/
    ├── __init__.py
    ├── test_chunker.py
    ├── test_loader.py
    ├── test_vector_store.py
    └── test_rag_chain.py
```

### File Descriptions

- `app.py` — Runs the Streamlit web interface for document uploads and question answering.
- `main.py` — Provides the command-line entry point for the RAG workflow.
- `requirements.txt` — Lists the Python dependencies required to run the application.
- `ingestion/loader.py` — Loads supported PDF and text documents.
- `ingestion/chunker.py` — Splits document content into smaller chunks.
- `prompts/rag_prompt.py` — Defines instructions for grounded answers, source citations, and unsupported questions.
- `retrieval/vector_store.py` — Creates and manages the ChromaDB vector store and document embeddings.
- `retrieval/rag_chain.py` — Connects retrieval with LLM-based answer generation.
- `tests/test_chunker.py` — Tests text-chunking behavior.
- `tests/test_loader.py` — Tests supported document-loading behavior.
- `tests/test_vector_store.py` — Tests vector-store functionality.
- `tests/test_rag_chain.py` — Intended for RAG-chain tests.

Generated vector databases, uploaded-document data, virtual environments, and API credentials should remain outside version control.

## 10. Installation and Setup

### Prerequisites

- Python 3.12 or a compatible Python version
- A Google Gemini API key
- Internet access for API calls and any required model downloads
- Git, if cloning the repository

### 1. Clone the Repository

```bash
git clone https://github.com/kvmkashyap-stack/Datheon_Python_-_Generative_AI_-_LangChain_Internship.git
cd Datheon_Python_-_Generative_AI_-_LangChain_Internship/Task_2_RetrieveAI
```

### 2. Create and Activate a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file inside the `Task_2_RetrieveAI` directory using `.env.example` as a reference.

Add your Gemini API key using the environment-variable name expected by the application. For example, if the application reads `GEMINI_API_KEY`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Check the application's configuration and environment-variable references if your installed version uses a different variable name.

Replace the placeholder with your actual API key. Never commit the `.env` file or expose API credentials in source code.

### 5. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL in the terminal. Open that URL in your browser, upload a PDF or TXT document, and ask questions about its contents.

### 6. Run the Command-Line Application

The command-line entry point is also available:

```bash
python main.py
```

Follow the prompts provided by the application. Depending on the implementation, the CLI workflow may require a document path.

## 11. Running Tests

RetrieveAI uses pytest for automated testing of its core components.

Run the tests from the `Task_2_RetrieveAI` directory:

```bash
python -m pytest tests -v
```

The test suite covers the following areas:

- Text chunking behavior
- Supported document-loading behavior
- Vector-store operations
- RAG-chain behavior, where corresponding tests are implemented

Test results should be reported based on the actual pytest output. A test file that exists but contains no test functions does not contribute any executed tests.

Tests that exercise live Google Gemini calls may require a valid API key and network access. Unit tests should avoid unnecessary external API calls wherever possible.

## 12. Limitations

- Answer quality depends on document extraction, chunk size, chunk overlap, embedding quality, retrieval relevance, and model behavior.
- The application currently supports PDF and TXT documents rather than every document format.
- Scanned PDFs may require OCR before their content can be indexed.
- Relevant information may be missed when the retrieval process does not return the appropriate chunks.
- LLM-generated responses are not guaranteed to be factually correct, even when source passages are provided.
- Source references identify supporting document context but do not independently prove every generated claim.
- A valid Gemini API key, network connectivity, and an available model endpoint are required for live generation.
- Large documents may increase ingestion time, embedding costs, and storage requirements.
- The current application is designed as a local document question-answering tool rather than a production multi-user service.

## 13. Future Improvements

- Support additional formats, including DOCX and HTML.
- Add OCR for scanned PDF documents.
- Improve retrieval with hybrid search, metadata filtering, and reranking.
- Add configurable chunk sizes and overlap settings.
- Add page-level citations and more precise source highlighting.
- Expand automated tests for retrieval quality, unsupported questions, and citation validation.
- Add persistent document management and controls for removing indexed documents.
- Support multiple documents in a single knowledge base with explicit source filtering.
- Add conversation history for follow-up questions.
- Add evaluation datasets and metrics to measure retrieval relevance and answer faithfulness.
- Improve error handling, logging, and API-failure recovery.
- Deploy the application with authentication, resource limits, and production-grade monitoring.

## 14. Author

**K. V. Maheedhara Kashyap**

GitHub: [kvmkashyap-stack](https://github.com/kvmkashyap-stack)

---

*Developed as part of the Datheon Python, Generative AI, and LangChain internship tasks.*
