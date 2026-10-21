# Python + Generative AI & LangChain Internship

**Internship Organization:** Datheon  
**Role:** AI Engineer Intern — Python, Generative AI & LangChain  
**Batch:** 01 (NMIT)  
**Application ID:** DT-2026-L6RWR

---

## About This Repository

This repository contains the projects developed as part of the **Python + Generative AI & LangChain Internship at Datheon**.

The objective of this internship is to develop practical AI applications using Python, Large Language Models (LLMs), prompt engineering, structured output validation, Retrieval-Augmented Generation (RAG), vector databases, AI agents, tool calling, and interactive web applications.

Each task is organized in a separate directory containing its implementation, dependencies, and project-specific documentation.

## Internship Tasks

### Task 1 — SmartExtract: Structured Resume Information Extraction

**Status:** Completed

SmartExtract is a Python application that uses Google Gemini and LangChain to extract structured information from resume text. It applies prompt engineering and Pydantic validation to produce structured JSON output.

**Key features and technologies:**
- Python
- Google Gemini
- LangChain
- Prompt engineering
- Pydantic schema validation
- Structured JSON output
- Automated testing with pytest

**Project folder:** [`Task_1_SmartExtract/`](./Task_1_SmartExtract/)

**Documentation:** [`Task 1 — SmartExtract README`](./Task_1_SmartExtract/README.md)

### Task 2 — RetrieveAI: RAG Document Question Answering

**Status:** Completed

RetrieveAI is a document question-answering application built using Retrieval-Augmented Generation (RAG). Users can upload PDF or TXT documents through a Streamlit interface and ask questions about their contents.

The application retrieves relevant document chunks from a vector store and generates context-grounded responses with source citations.

**Key features and technologies:**
- Python
- LangChain document loaders
- Recursive text splitting
- Google Gemini embeddings and generation
- ChromaDB vector storage
- Retrieval-Augmented Generation
- Source citations and PDF page references
- Streamlit interface
- Automated testing with pytest

**Project folder:** [`Task_2_RetrieveAI/`](./Task_2_RetrieveAI/)

**Documentation:** [`Task 2 — RetrieveAI README`](./Task_2_RetrieveAI/README.md)

### Task 3 — NexusAI: Multi-Tool Autonomous AI Agent

**Status:** Completed

NexusAI is a multi-tool AI agent developed using LangChain and Google Gemini. It processes user queries, selects appropriate tools, and combines their results to generate useful responses.

The project includes a command-line interface and a modern, ChatGPT-style Streamlit conversational interface.

**Key features and technologies:**
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

- **Web Search:** Retrieves relevant information from web search results.
- **Calculator:** Evaluates supported mathematical expressions using a restricted AST-based implementation.
- **File Reader:** Reads supported local documents.

**Project folder:** [`Task_3_NexusAI/`](./Task_3_NexusAI/)

**Documentation:** [`Task 3 — NexusAI README`](./Task_3_NexusAI/README.md)

**Run the Streamlit interface:**

```powershell
python -m streamlit run Task_3_NexusAI/app.py
```

**Alternatively, run the command-line agent:**

```powershell
python Task_3_NexusAI/main.py
```

Refer to the Task 3 README for complete installation and configuration instructions.

### Task 4 — Vortex AI: Interactive Multi-Tool AI Agent

**Status:** Completed

Vortex AI is a browser-based AI assistant that integrates a LangChain-powered agent with a modern, ChatGPT-style Streamlit interface.

The application provides a conversational environment where users can submit prompts, view AI-generated responses, manage conversations, and upload supported files. The agent can use its configured tools to handle different types of requests.

**Key features and technologies:**
- Python
- Streamlit web application
- LangChain agent orchestration
- Google Gemini integration
- Real-time response streaming
- Chat history and session-state management
- New Chat and Clear Chat controls
- File upload interface
- Calculator tool
- Web-search tool
- File-reading tool
- Modular agent and tool architecture

**Available tools:**

- **Web Search:** Retrieves information using the configured web-search implementation.
- **Calculator:** Performs supported mathematical calculations.
- **File Reader:** Reads supported files through the configured file-reading implementation.

**Project folder:** [`Task_4_VortexAI/`](./Task_4_VortexAI/)

**Documentation:** [`Task 4 — Vortex AI README`](./Task_4_VortexAI/README.md)

**Launch the Streamlit application:**

```powershell
python -m streamlit run Task_4_VortexAI/app.py
```

Run this command from the repository root after installing the Task 4 dependencies and configuring the required API key.

The application is designed to run locally in a web browser. Public deployment is not required for local execution.

---

## Repository Structure

```text
Datheon_Python_-_Generative_AI_-_LangChain_Internship/
│
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
├── Task_3_NexusAI/
│   ├── README.md
│   ├── app.py
│   ├── main.py
│   ├── requirements.txt
│   ├── agent/
│   ├── tools/
│   ├── data/
│   └── tests/
│
└── Task_4_VortexAI/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── agent/
    ├── tools/
    └── tests/
```

*Note: This is a high-level overview. The actual files and directories may differ depending on each task's implementation. Consult the corresponding project directory for its complete structure.*

## Getting Started

### Prerequisites

Install or configure the following before running the projects:

- Python 3.10 or a version supported by the project's dependencies
- Git
- A Google Gemini API key for projects that use the hosted model
- Internet connectivity for model API requests and online search
- A modern web browser for Streamlit applications

Check your Python installation:

```powershell
python --version
```

Check pip:

```powershell
python -m pip --version
```

### Step 1 — Clone the Repository

Open a terminal and run:

```powershell
git clone https://github.com/kvmkashyap-stack/Datheon_Python_-_Generative_AI_-_LangChain_Internship.git
```

Navigate into the repository:

```powershell
cd Datheon_Python_-_Generative_AI_-_LangChain_Internship
```

### Step 2 — Create a Virtual Environment

Create a virtual environment for the project you want to run.

For example, to work on Task 4:

```powershell
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Using a virtual environment helps isolate dependencies from other Python projects.

### Step 3 — Configure Environment Variables

For projects that require Google Gemini, create a local `.env` file in the appropriate project directory, following that project's README.

A typical configuration may look like this:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Use the exact variable name expected by each project's code. Never replace the placeholder with a real key in the README or commit API credentials to GitHub.

### Step 4 — Install Task-Specific Dependencies

Each project has its own `requirements.txt` file. Install the dependencies for the project you intend to run rather than installing every project's dependencies unnecessarily.

#### Task 1 — SmartExtract

```powershell
python -m pip install -r Task_1_SmartExtract/requirements.txt
```

Run the application:

```powershell
python Task_1_SmartExtract/main.py
```

#### Task 2 — RetrieveAI

```powershell
python -m pip install -r Task_2_RetrieveAI/requirements.txt
```

Launch the Streamlit interface:

```powershell
python -m streamlit run Task_2_RetrieveAI/app.py
```

#### Task 3 — NexusAI

```powershell
python -m pip install -r Task_3_NexusAI/requirements.txt
```

Launch the Streamlit interface:

```powershell
python -m streamlit run Task_3_NexusAI/app.py
```

Alternatively, run the command-line agent:

```powershell
python Task_3_NexusAI/main.py
```

#### Task 4 — Vortex AI

```powershell
python -m pip install -r Task_4_VortexAI/requirements.txt
```

Launch the Streamlit interface:

```powershell
python -m streamlit run Task_4_VortexAI/app.py
```

After launching a Streamlit application, open the local URL displayed in the terminal. The default address is commonly `http://localhost:8501`.

### Step 5 — Test the Projects

Run the tests available in the relevant project. For example, if the project uses pytest:

```powershell
python -m pytest Task_1_SmartExtract/tests -q
```

```powershell
python -m pytest Task_2_RetrieveAI/tests -q
```

```powershell
python -m pytest Task_3_NexusAI/tests -q
```

```powershell
python -m pytest Task_4_VortexAI/tests -q
```

These commands assume that each directory exists and contains tests. Adjust the paths to match the actual repository structure.

For complete instructions, dependencies, configuration details, and troubleshooting, refer to each task's README.

## Security and Configuration

- Store API keys and credentials in environment variables or an untracked `.env` file.
- Never commit private keys, passwords, or sensitive credentials.
- Exclude virtual environments, Python caches, and unnecessary generated files from version control.
- Validate uploaded files and restrict file access to the intended locations.
- Avoid executing arbitrary code from user-provided inputs.
- Be mindful of information sent to external model APIs and search services.
- Use synthetic or appropriately anonymized data for demonstrations.

## Learning Objectives

The internship projects demonstrate practical work with:

- Python application development
- Large Language Model integration
- Prompt engineering
- Structured output generation and Pydantic validation
- Retrieval-Augmented Generation and vector search
- Document ingestion and question answering
- AI agents and tool calling
- Web search and mathematical computation
- File processing and document interaction
- Streamlit-based conversational applications
- Session-state and conversation management
- Software testing and modular application design
- Git, GitHub, and technical documentation

## Internship Submission

This repository serves as the project portfolio for the Python + Generative AI & LangChain Internship at Datheon.

It contains four projects covering structured information extraction, document question answering, multi-tool AI agents, and an interactive conversational AI application.

Each task is organized separately to make its implementation, dependencies, execution instructions, and supporting documentation easier to review.

**Public repository:**  
[Datheon Python + Generative AI & LangChain Internship](https://github.com/kvmkashyap-stack/Datheon_Python_-_Generative_AI_-_LangChain_Internship)

**Program information:**  
[Datheon — Python, Generative AI & LangChain Internship](https://www.datheon.in/training/catalog/python-generative-ai-langchain-internship)

---

**Author:** K. V. Maheedhara Kashyap

*Python | Generative AI | LangChain | RAG | AI Agents | LLM Applications*
