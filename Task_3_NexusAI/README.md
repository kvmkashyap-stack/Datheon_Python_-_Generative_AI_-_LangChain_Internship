# Task 3: NexusAI — Multi-Tool Autonomous AI Agent

NexusAI is a multi-tool autonomous AI agent built using LangChain and Google Gemini. It can understand user queries, decide which tools to use, and generate responses using real-time web search, Python-based mathematical calculations, and local document reading.

The project also includes a Streamlit chat interface with a modern, ChatGPT-style layout, allowing users to interact with the agent and upload supported documents through the interface.

## Features

- **Autonomous Tool Selection:** Uses a LangChain agent to determine which tool is appropriate for a given user query.
- **Real-Time Web Search:** Searches the web using DuckDuckGo to retrieve relevant information for current or general knowledge queries.
- **Mathematical Calculator:** Evaluates mathematical expressions using a restricted Python AST-based calculator rather than unrestricted code execution.
- **Local File Reader:** Reads supported local files, including TXT, PDF, Markdown, CSV, and JSON, from the designated data directory.
- **Document Upload:** Allows users to upload PDF and TXT documents through the Streamlit interface.
- **Conversational Chat Interface:** Provides a ChatGPT-style interface with chat history and a message input area.
- **Gemini Integration:** Uses Google's Gemini model to understand questions, select tools, and generate responses.
- **Tool Execution Logs:** Displays tool execution information in the terminal to help with debugging and understanding the agent's behavior.
- **Automated Testing:** Includes unit tests for the calculator, file reader, and web search tools.
- **Environment Variable Support:** Keeps API credentials in a local `.env` file rather than hardcoding secrets into the source code.

## Tech Stack

- Python
- LangChain
- Google Gemini
- LangChain Google GenAI
- LangChain Community
- DuckDuckGo Search (`ddgs`)
- Streamlit
- PyPDF
- Python Dotenv
- Pytest

## Prerequisites

Before running NexusAI, ensure that you have:

- Python installed on your system.
- Git installed if you are cloning the repository.
- A Google Gemini API key.
- An active internet connection for Gemini API requests and web searches.
- A terminal or IDE such as Visual Studio Code.

## Setup

### Step 1: Navigate to the Project Directory

Open your terminal and navigate to the NexusAI project folder.

If you are working from the internship repository:

```bash
cd Task_3_NexusAI
```

If you have the project in a separate local directory:

```bash
cd NexusAI
```

Make sure you are inside the directory containing `app.py`, `main.py`, and `requirements.txt`.

### Step 2: Create a Virtual Environment

Create an isolated Python environment to install the project's dependencies.

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**Linux or macOS:**

```bash
source .venv/bin/activate
```

After activation, your terminal should display the virtual environment name.

### Step 4: Install Dependencies

Install all required packages from `requirements.txt`.

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Configure the Gemini API Key

Create a `.env` file in the project root directory.

The project includes a `.env.example` template. Copy it to `.env`:

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

**Linux or macOS:**

```bash
cp .env.example .env
```

Open `.env` and add your Gemini API key using the variable name expected by the application. For example, if the code reads `GOOGLE_API_KEY`:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your actual API key. Check `.env.example` and the application's configuration code to confirm the exact environment variable name.

**Security note:** Never commit or upload your `.env` file or expose your API key in source code, screenshots, logs, or public repositories.

### Step 6: Prepare the Data Directory

NexusAI uses a `data/` directory for local documents that the file-reading tool is allowed to access.

Create the directory if it does not already exist:

```powershell
New-Item -ItemType Directory -Force data
```

Place any supported local documents you want the agent to read inside this directory.

Supported formats include:

- `.txt` — Plain text files
- `.pdf` — PDF documents
- `.md` — Markdown files
- `.csv` — CSV files
- `.json` — JSON files

The file reader is designed to access documents within the configured data directory rather than arbitrary paths on the computer.

For PDF and TXT documents, you can also use the upload feature in the Streamlit interface.

## Running the Application

NexusAI provides two ways to interact with the agent: a Streamlit graphical interface and a command-line interface.

### Option 1: Run the Streamlit Web Interface

Start the application using:

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal, typically:

```text
http://localhost:8501
```

Open the URL in your browser.

#### Using the Chat Interface

1. Open the NexusAI web interface.
2. Enter a question in the message input field.
3. Submit the message.
4. The agent analyzes the query and determines whether a tool is needed.
5. If necessary, the agent invokes the appropriate tool.
6. The tool's result is used to generate the final response.
7. Continue the conversation using the same chat interface.

#### Uploading Documents

1. Locate the file-upload control in the interface.
2. Select a supported PDF or TXT file from your computer.
3. Wait for the upload to complete.
4. Ask the agent a question related to the uploaded document.
5. The application processes the uploaded file according to its configured document-handling workflow.

The local file reader's directory restrictions and the web interface's upload handling are separate implementation details. Uploading a document does not automatically imply that it becomes permanently indexed or available to every tool unless the application explicitly implements that behavior.

### Option 2: Run the Command-Line Interface

To interact with NexusAI directly in the terminal, run:

```bash
python main.py
```

Enter your query when prompted.

Example questions:

```text
Who is Virat Kohli?
```

```text
Calculate (125 * 8) + 450.
```

```text
Search the web for the latest developments in artificial intelligence.
```

```text
Read the document named notes.txt.
```

The agent determines which available tool is appropriate for the query and returns a response.

Use the command or exit instruction supported by the CLI implementation to end the session.

## Available Tools

### 1. Web Search Tool

The web search tool uses DuckDuckGo to retrieve relevant search results.

**Purpose:**
- Search for information available on the web.
- Retrieve useful search-result snippets and links.
- Support questions that require external information.

**Example:**

```text
Search for recent developments in generative AI.
```

The agent can invoke the search tool and use its results to formulate an answer.

**Limitations:**
- Search results depend on web availability and the quality of indexed information.
- Search snippets may not contain the full content of a webpage.
- Results should be independently verified for critical decisions.

### 2. Mathematical Calculator Tool

The calculator evaluates mathematical expressions using a restricted Abstract Syntax Tree (AST) approach.

**Purpose:**
- Perform arithmetic operations.
- Evaluate supported mathematical expressions.
- Avoid unrestricted execution of arbitrary Python code.

**Example expressions:**

```text
125 * 8
```

```text
(450 + 250) / 7
```

```text
2 ** 10
```

Only the operations supported by the calculator implementation are available. Unsupported expressions should be rejected rather than executed as arbitrary code.

### 3. Local File Reader Tool

The file reader retrieves content from supported files stored in the configured local data directory.

**Purpose:**
- Read document content.
- Provide file information to the agent.
- Help answer questions based on local documents.

**Example:**

Place a file named `notes.txt` inside the `data/` directory, then ask:

```text
Read notes.txt and summarize its main points.
```

The agent can use the file-reading tool to retrieve the document content and formulate a response.

Supported file types include TXT, PDF, Markdown, CSV, and JSON, subject to the reader's implementation.

**Security considerations:**
- File access is restricted to the configured data directory.
- Unsupported file formats should be rejected.
- Large files may be subject to implementation-specific size or content limits.

## Agent Workflow

NexusAI follows a tool-using agent workflow.

1. **User Input:** The user submits a natural-language question.
2. **Query Analysis:** The Gemini model interprets the user's request.
3. **Tool Selection:** The LangChain agent determines whether a tool is required.
4. **Tool Execution:** The selected tool performs the requested operation.
5. **Result Processing:** The tool output is passed back to the agent.
6. **Response Generation:** The model produces a final response based on the question and available results.
7. **User Output:** The answer is displayed in the Streamlit interface or terminal.

The agent can select different tools depending on the query. A mathematical question may use the calculator, a question requiring external information may use web search, and a question about a local document may use the file reader.

## Run Automated Tests

NexusAI includes automated tests for its core tools.

Run all tests from the project root:

```bash
python -m pytest tests -v
```

The test suite covers:

- Calculator functionality and supported mathematical expressions.
- File reader behavior and file-handling restrictions.
- Web search tool behavior.

To run individual test files:

**Calculator tests:**

```bash
python -m pytest tests/test_calculator.py -v
```

**File reader tests:**

```bash
python -m pytest tests/test_file_reader.py -v
```

**Web search tests:**

```bash
python -m pytest tests/test_web_search.py -v
```

A successful test run should report that the tests have passed. Some web search or API integration behavior may depend on the test setup and network availability.

## Project Structure

```text
Task_3_NexusAI/
│
├── agent/
│   ├── __init__.py
│   └── executor.py
│
├── tools/
│   ├── __init__.py
│   ├── web_search.py
│   ├── calculator.py
│   └── file_reader.py
│
├── data/
│   └── (local documents)
│
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_file_reader.py
│   └── test_web_search.py
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
└── app.py
```

### Important Files

- `app.py` — Streamlit graphical interface and chat interaction.
- `main.py` — Command-line entry point.
- `agent/executor.py` — Configures and executes the LangChain agent.
- `tools/web_search.py` — Implements web search functionality.
- `tools/calculator.py` — Implements restricted mathematical calculations.
- `tools/file_reader.py` — Implements local document reading.
- `tests/` — Automated tests for the core tools.
- `requirements.txt` — Python dependency list.
- `.env.example` — Template for required environment variables.
- `.gitignore` — Excludes local files and environment-specific artifacts from version control.
- `data/` — Directory for documents used by the local file reader.

## Troubleshooting

### 1. Gemini API Key Error

**Possible cause:** The API key is missing, invalid, or loaded under the wrong environment variable.

**Solution:**
- Check the `.env` file.
- Verify the variable name expected by the application.
- Confirm that the API key is valid.
- Restart the application after updating environment variables.

### 2. Module Not Found

**Possible cause:** Dependencies have not been installed in the active virtual environment.

**Solution:**

```bash
pip install -r requirements.txt
```

Ensure that the correct virtual environment is activated before running the application.

### 3. Web Search Failure

**Possible cause:** Network connectivity issues, search-service limitations, or changes to the search library.

**Solution:**
- Check your internet connection.
- Verify that the required search dependency is installed.
- Retry the query.
- Inspect the terminal output for the underlying error.

### 4. File Not Found

**Possible cause:** The file is missing or outside the permitted data directory.

**Solution:**
- Confirm that the file exists.
- Check the filename and extension.
- Place the file in the configured `data/` directory.
- Verify the path and access restrictions implemented in `tools/file_reader.py`.

### 5. Streamlit Does Not Start

**Possible cause:** Missing dependencies, an incorrect working directory, or a port conflict.

**Solution:**

```bash
python -m streamlit run app.py
```

Confirm that you are in the project directory and that the virtual environment is active. If the default port is occupied, use a different available port supported by Streamlit.

### 6. Tests Fail

**Possible cause:** Missing dependencies, unexpected test data, or differences between the implementation and test assumptions.

**Solution:**

```bash
python -m pip install -r requirements.txt
python -m pytest tests -v
```

Review the error output and address the specific failing test.

## Limitations

- Requires a valid Google Gemini API key.
- Requires internet access for Gemini API requests and web search.
- Web search results may be incomplete, outdated, or unavailable.
- The calculator supports only the operations implemented in its restricted expression evaluator.
- The local file reader supports only the file formats implemented in the project.
- Large documents may require additional handling to avoid context-length limitations.
- The agent's answers depend on the quality of the model's reasoning and the results returned by its tools.
- Uploaded documents are not necessarily persistent across application restarts unless persistence is explicitly implemented.
- The application is intended as an educational and development project; tool outputs should be verified before being used for critical decisions.

## Future Improvements

- Add additional tools such as a database query tool or a dedicated document retrieval tool.
- Improve tool execution tracing and error reporting.
- Add configurable conversation memory.
- Introduce stronger document upload validation and file-size controls.
- Add support for more document formats.
- Improve response formatting and source attribution for web search results.
- Add integration tests for the complete agent workflow.
- Deploy the application to a hosted environment.

## Conclusion

NexusAI demonstrates how a tool-using autonomous AI agent can combine a large language model with external search, mathematical computation, and local document access.

By integrating LangChain, Google Gemini, DuckDuckGo, and Streamlit, the project provides both a command-line interface and a graphical chat experience for interacting with multiple tools through natural language.
