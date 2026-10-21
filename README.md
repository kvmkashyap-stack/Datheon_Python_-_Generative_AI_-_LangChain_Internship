# Python + Generative AI & LangChain Internship

**Internship Organization:** Datheon  
**Role:** AI Engineer Intern — Python, Generative AI & LangChain  
**Batch:** 01 (NMIT)  
**Application ID:** DT-2026-L6RWR

## About This Repository

This repository contains the projects developed as part of the Python + Generative AI & LangChain Internship at Datheon. The goal is to build practical applications using Python, Large Language Models (LLMs), prompt engineering, structured output validation, Retrieval-Augmented Generation (RAG), vector databases, AI agents, and interactive applications.

Each task is maintained in a separate folder with its own source code, dependencies, tests where applicable, and detailed README documentation.

## Internship Tasks

### Task 1 — SmartExtract: Structured Resume Information Extraction

**Status:** Completed

SmartExtract is a Python application that uses a generative AI model and LangChain to extract structured information from resume text. It validates generated data using Pydantic and produces JSON output.

**Key concepts and technologies:**
- Python
- Google Gemini
- LangChain
- Prompt engineering
- Pydantic schema validation
- Structured JSON output
- Automated testing with pytest

**Project folder:** [`Task_1_SmartExtract/`](./Task_1_SmartExtract/)

**Documentation:** [`Task 1 README`](./Task_1_SmartExtract/README.md)

### Task 2 — RetrieveAI: RAG Document Question Answering

**Status:** Completed

RetrieveAI is a document question-answering application built using Retrieval-Augmented Generation (RAG). Users can upload PDF or TXT documents through a Streamlit interface and ask questions about their contents. The application retrieves relevant document chunks and generates context-grounded answers with source citations.

**Key concepts and technologies:**
- Python
- LangChain document loaders
- Recursive text splitting
- Google Gemini embeddings and generation
- ChromaDB vector storage
- Retrieval-Augmented Generation
- Source citations and PDF page references
- Streamlit
- Automated testing with pytest

**Project folder:** [`Task_2_RetrieveAI/`](./Task_2_RetrieveAI/)

**Documentation:** [`Task 2 README`](./Task_2_RetrieveAI/README.md)

### Task 3 — NexusAI: Multi-Tool Autonomous AI Agent

**Status:** Completed

NexusAI is a multi-tool AI agent built using LangChain and Google Gemini. It analyzes user queries, selects appropriate tools, and combines their results to generate useful responses. The project includes a command-line interface and a modern, ChatGPT-style Streamlit chat interface.

**Key concepts and technologies:**
- Python
- LangChain agents and tool calling
- Google Gemini
- DuckDuckGo web search
- AST-based mathematical calculator
- Local document reader
- PDF, TXT, Markdown, CSV, and JSON file handling
- Streamlit conversational interface
- File uploads
- Automated testing with pytest

**Available tools:**
- **Web Search:** Retrieves relevant information from the web using DuckDuckGo.
- **Calculator:** Evaluates supported mathematical expressions using a restricted AST-based implementation.
- **File Reader:** Reads supported local documents from the configured data directory.

**Project folder:** [`Task_3_NexusAI/`](./Task_3_NexusAI/)

**Documentation:** [`Task 3 README`](./Task_3_NexusAI/README.md)

**How to run:** Navigate to `Task_3_NexusAI/`, install its dependencies, configure the required Gemini API key, and launch the Streamlit interface using `python -m streamlit run app.py`. Refer to the Task 3 README for detailed setup and command-line instructions.

## Repository Structure

```text
Datheon_Python_-_Generative_AI_-_LangChain_Internship/
├── .gitignore
├── README.md
│
├── Task_1_SmartExtract/
│   ├── README.md
│   ├── main.py
│   ├── requirements.txt
│   ├── prompts/
│   ├── schemas/
│   ├── tests/
│   └── output/
│
├── Task_2_RetrieveAI/
│   ├── README.md
│   ├── app.py
│   ├── main.py
│   ├── requirements.txt
│   ├── ingestion/
│   ├── retrieval/
│   ├── prompts/
│   └── tests/
│
└── Task_3_NexusAI/
    ├── README.md
    ├── app.py
    ├── main.py
    ├── requirements.txt
    ├── agent/
    ├── tools/
    ├── data/
    └── tests/
```

The structure above highlights the main files and directories. Refer to each task's folder for its complete implementation.

## Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by the individual project
- Git
- A suitable API key for projects that use hosted language models
- Internet access for applications that require online model APIs or web search

### Clone the Repository

```bash
git clone https://github.com/kvmkashyap-stack/Datheon_Python_-_Generative_AI_-_LangChain_Internship.git
cd Datheon_Python_-_Generative_AI_-_LangChain_Internship
```

### Run Task 1 — SmartExtract

Create and activate a virtual environment from the repository root.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the Task 1 dependencies:

```powershell
python -m pip install -r Task_1_SmartExtract/requirements.txt
```

Configure the required API key in a local `.env` file according to the instructions in [`Task_1_SmartExtract/README.md`](./Task_1_SmartExtract/README.md).

Run the application:

```powershell
python Task_1_SmartExtract/main.py
```

### Run Task 2 — RetrieveAI

From the repository root, install the Task 2 dependencies:

```powershell
python -m pip install -r Task_2_RetrieveAI/requirements.txt
```

Configure the required API key according to [`Task_2_RetrieveAI/README.md`](./Task_2_RetrieveAI/README.md).

Launch the Streamlit application:

```powershell
python -m streamlit run Task_2_RetrieveAI/app.py
```

### Run Task 3 — NexusAI

From the repository root, install the Task 3 dependencies:

```powershell
python -m pip install -r Task_3_NexusAI/requirements.txt
```

Configure the required Gemini API key using the instructions in [`Task_3_NexusAI/README.md`](./Task_3_NexusAI/README.md).

**Launch the Streamlit interface:**

```powershell
python -m streamlit run Task_3_NexusAI/app.py
```

**Alternatively, run the command-line agent:**

```powershell
python Task_3_NexusAI/main.py
```

For task-specific installation, configuration, execution, and testing instructions, refer to the README inside each task folder.

## Security and Configuration

- Store API keys and other secrets in local environment variables or an untracked `.env` file.
- Never commit API keys, passwords, or private credentials.
- Keep virtual environments, caches, and unnecessary generated files out of version control.
- Use synthetic or appropriately anonymized data for demonstrations.
- Validate file inputs and restrict local file access appropriately.

## Learning Objectives

Through these projects, the internship aims to develop practical experience with:

- Python application development
- LLM integration and prompt engineering
- Schema validation and reliable structured outputs
- Retrieval-Augmented Generation and vector search
- AI agents and tool calling
- External tool integration and local file processing
- Interactive AI application development
- Software organization, testing, documentation, and Git/GitHub workflows

## Internship Submission

This repository serves as the project portfolio for internship evaluation. Each completed task includes its implementation and supporting documentation.

**Public repository:**  
https://github.com/kvmkashyap-stack/Datheon_Python_-_Generative_AI_-_LangChain_Internship

**Program information:**  
https://www.datheon.in/training/catalog/python-generative-ai-langchain-internship

---

**Author:** K. V. Maheedhara Kashyap

*Python | Agentic AI | Generative AI | LangChain | LLM Applications*
