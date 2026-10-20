# Python + Generative AI & LangChain Internship

**Internship Organization:** Datheon  
**Role:** AI Engineer Intern — Python, Generative AI & LangChain  
**Batch:** 01 (NMIT)  
**Application ID:** DT-2026-L6RWR

## About This Repository

This repository contains the projects developed as part of the Python + Generative AI & LangChain Internship at Datheon. The goal is to build practical, real-world applications using Python, Large Language Models (LLMs), prompt engineering, structured output validation, Retrieval-Augmented Generation (RAG), vector databases, AI agents, and interactive applications.

Each task is maintained in a separate folder with its own source code, dependencies, tests where applicable, and detailed README documentation.

## Internship Tasks

### Task 1 — SmartExtract: Structured Resume Information Extraction

**Status:** Completed

SmartExtract is a Python application that uses a generative AI model and LangChain to extract structured information from resume text. It validates the generated data using Pydantic and produces JSON output.

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

### Task 2 — RetrieveAI: Document Question Answering with RAG

**Status:** Completed

RetrieveAI is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF or text documents and ask questions about their contents. It loads documents, splits them into chunks, generates vector embeddings, stores them in a vector database, and retrieves relevant context to generate answers grounded in the provided documents. The application also provides source citations to help users identify the documents used to answer their questions.

**Key concepts and technologies:**
- Python
- Google Gemini
- LangChain
- Retrieval-Augmented Generation (RAG)
- PDF and text document loaders
- Recursive text splitting and chunking
- Vector embeddings
- ChromaDB
- Context-based question answering
- Source and page citations
- Streamlit interactive web application
- Automated testing with pytest

**Project folder:** [`Task_2_RetrieveAI/`](./Task_2_RetrieveAI/)

**Documentation:** [`Task 2 README`](./Task_2_RetrieveAI/README.md)

**Expected outcome:** A working document Q&A application that answers user questions using retrieved context from uploaded documents and displays source information.

### Task 3 — AI Agent with Tools

**Status:** Planned

Build an AI agent that can select and use tools to solve multi-step tasks, such as web research, mathematical calculations, and reading local files.

**Planned concepts and technologies:**
- LangChain agents or tool/function calling
- Tool definitions and execution
- DuckDuckGo or Tavily search
- Python calculator
- Local file reader
- Agent execution and observation handling

**Expected outcome:** A console-based AI agent that uses appropriate tools to respond to compound queries.

### Task 4 — Interactive Generative AI Web Application

**Status:** Planned

Create a web interface around a RAG pipeline or AI agent, providing a conversational experience with chat history and streamed responses.

**Planned concepts and technologies:**
- Streamlit
- Interactive chat components
- Session state management
- Streaming model responses
- LangChain integration

**Expected outcome:** A locally running web application for interactive conversations with an AI-powered system.

## Repository Structure

```text
Datheon_Python_-_Generative_AI_-_LangChain_Internship/
├── .gitignore
├── README.md
├── Task_1_SmartExtract/
│   ├── README.md
│   ├── main.py
│   ├── requirements.txt
│   ├── prompts/
│   ├── schemas/
│   ├── tests/
│   └── output/
└── Task_2_RetrieveAI/
    ├── README.md
    ├── app.py
    ├── main.py
    ├── requirements.txt
    ├── ingestion/
    ├── retrieval/
    ├── prompts/
    └── tests/
```

As additional tasks are completed, their folders and documentation will be added to this repository.

## Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by the individual project
- Git
- A suitable API key for projects that use hosted language models

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

With the virtual environment activated, install the Task 2 dependencies:

```powershell
python -m pip install -r Task_2_RetrieveAI/requirements.txt
```

Configure the required API key in a local `.env` file according to the instructions in [`Task_2_RetrieveAI/README.md`](./Task_2_RetrieveAI/README.md).

Run the Streamlit application:

```powershell
python -m streamlit run Task_2_RetrieveAI/app.py
```

For task-specific installation, configuration, execution, and testing instructions, refer to the README inside each task folder.

## Security and Configuration

- Store API keys and other secrets in local environment variables or an untracked `.env` file.
- Never commit API keys, passwords, or private credentials.
- Keep virtual environments and generated files out of version control when appropriate.
- Use synthetic or appropriately anonymized data for demonstrations.

## Learning Objectives

Through these projects, the internship aims to develop practical experience with:

- Python application development
- LLM integration and prompt engineering
- Schema validation and reliable structured outputs
- Retrieval-Augmented Generation and vector search
- AI agents and tool calling
- Interactive AI application development
- Software organization, testing, documentation, and Git/GitHub workflows

## Internship Submission

This repository is intended to serve as the project portfolio for internship evaluation. Each completed task will include its implementation and supporting documentation.

**Public repository:**  
https://github.com/kvmkashyap-stack/Datheon_Python_-_Generative_AI_-_LangChain_Internship

**Program information:**  
https://www.datheon.in/training/catalog/python-generative-ai-langchain-internship

---

**Author:** K. V. Maheedhara Kashyap

*Python | Generative AI | LangChain | LLM Applications*
