# Task 4 — Vortex AI: Interactive AI Agent with Streamlit

## 1. Project Overview

**Vortex AI** is an interactive, browser-based AI assistant built using Python, Streamlit, LangChain, and Google Gemini. It combines a multi-tool AI agent with a modern conversational interface inspired by ChatGPT.

The application allows users to ask questions, receive AI-generated responses, use integrated tools, upload documents, and maintain multiple conversations through a chat interface.

Unlike a basic chatbot that only generates text, Vortex AI uses an agent-based architecture that can select and invoke available tools to help solve different types of problems.

The application runs locally in a web browser and supports conversational interaction, chat history, session-state management, and streaming responses.

### Project Objectives

- Integrate an AI agent into an interactive web application.
- Build a modern conversational interface using Streamlit.
- Support real-time streaming of AI-generated responses.
- Maintain conversation history during a user session.
- Provide access to useful tools through the AI agent.
- Allow users to upload documents directly through the interface.
- Implement chat management features such as New Chat and Clear Chat.
- Provide a simple, responsive interface for interacting with the AI assistant.

## 2. Problem Statement

AI agents are often developed as command-line applications or standalone Python scripts. Although these implementations demonstrate the underlying intelligence, they do not always provide a convenient interface for everyday users.

A command-line interface requires users to interact through a terminal, makes conversation history difficult to navigate, and offers limited support for managing multiple conversations or uploading documents.

The objective of this project is to transform an AI agent pipeline into a user-friendly browser application with a conversational interface, streaming output, session management, and tool integration.

### Proposed Solution

Vortex AI addresses these limitations by combining a LangChain-powered AI agent with a Streamlit web interface.

Users can submit prompts, view responses as they are generated, start new conversations, clear existing chat history, and upload supported files through the interface. The agent can also use its configured tools when appropriate.

## 3. Key Features

### 3.1 Interactive Chat Interface

- Chat-style interface for sending prompts and receiving responses.
- Separate visual presentation for user messages and AI responses.
- Input area for submitting questions.
- Conversation display that updates as the interaction progresses.
- Layout inspired by modern AI chat applications.

### 3.2 Real-Time Streaming Responses

The application supports streaming AI responses so that users can see output as it becomes available instead of waiting for the entire response to finish.

Streaming improves the perceived responsiveness of the application and provides a more natural conversational experience.

### 3.3 Conversation History

- Maintains messages within the active session.
- Displays previous messages in the current conversation.
- Preserves conversation context for follow-up questions when supported by the agent implementation.
- Separates conversation display and agent execution logic.

Conversation history is managed through Streamlit session state.

### 3.4 New Chat

The New Chat feature allows users to start a fresh conversation without continuing the previous conversation's message history.

A new conversation begins with an empty message list, providing a clean workspace for a different topic.

### 3.5 Clear Chat

The Clear Chat feature allows users to clear the messages in the active conversation.

This helps users reset the current interaction without manually removing individual messages.

### 3.6 Multi-Tool AI Agent

Vortex AI integrates an AI agent that can select from its configured tools to help answer user requests.

The available tools include:

- **Web Search:** Retrieves relevant information from web search results.
- **Calculator:** Performs supported mathematical calculations.
- **File Reader:** Reads supported local files and provides their contents to the agent.

Tool execution depends on the user's prompt, the agent's decisions, and the capabilities of the configured tools.

### 3.7 File Upload Support

The interface provides a file-upload control so users can select files from their own devices.

This enables document-based interaction without requiring users to manually place every document in a predefined project folder.

The types of files that can be processed depend on the upload handling and file-reading logic implemented in the application.

### 3.8 Session-State Management

Streamlit session state is used to maintain application data between interactions, including conversation messages and other session-specific values.

This helps prevent the chat interface from losing its active conversation whenever Streamlit reruns the application.

### 3.9 Modular Architecture

The project separates the web interface, agent execution logic, and individual tools into different modules.

This improves readability, simplifies debugging, and makes it easier to extend the application with additional tools or interface features.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application programming language |
| Streamlit | Browser-based interactive user interface |
| LangChain | Agent orchestration and tool integration |
| Google Gemini | Large language model for AI responses |
| `langchain-google-genai` | Integration between LangChain and Google Gemini |
| Python-dotenv | Loading environment variables from a `.env` file |
| DuckDuckGo search integration | Web-search functionality, depending on the configured implementation |
| Pytest | Automated testing, if included in the project |

## 5. System Architecture

Vortex AI follows a modular architecture that separates the user interface from the agent and its tools.

```text
User
  |
  v
Streamlit Chat Interface
  |
  +--> Prompt Input
  |
  +--> Conversation History
  |
  +--> File Upload
  |
  v
Agent Execution Layer
  |
  v
LangChain AI Agent
  |
  +--> Google Gemini
  |
  +--> Web Search Tool
  |
  +--> Calculator Tool
  |
  +--> File Reader Tool
  |
  v
Response Processing / Streaming
  |
  v
Chat Interface Displays Response
```

### Component Responsibilities

**1. Streamlit Interface**

Receives user prompts, displays messages, manages chat controls, and handles file uploads.

**2. Agent Execution Layer**

Connects the interface to the LangChain agent and coordinates the processing of user requests.

**3. Language Model**

Google Gemini generates responses and helps the agent determine when a configured tool may be useful.

**4. Tool Layer**

Provides specific capabilities, including mathematical calculations, file reading, and web searching.

**5. Session Management**

Maintains conversation data and relevant state throughout the active Streamlit session.

## 6. Application Workflow

The application follows the workflow below when a user submits a prompt.

### Step 1: Launch the Application

The user starts the Streamlit application from the project directory. Streamlit launches a local web server and provides a browser interface.

### Step 2: Enter a Prompt

The user types a question or instruction into the chat input area and submits it.

### Step 3: Update Conversation State

The application adds the user's message to the active conversation and prepares the relevant conversation context.

### Step 4: Execute the AI Agent

The agent receives the user's request and processes it using the configured language model and available tools.

### Step 5: Invoke Tools When Required

Depending on the request, the agent may use the calculator, web-search functionality, or file-reading functionality.

### Step 6: Generate the Response

The agent produces a response based on the prompt, the model's output, and any relevant tool results.

### Step 7: Stream and Display the Response

The interface displays the generated response progressively when streaming is supported by the configured execution path.

### Step 8: Preserve Conversation History

The messages are maintained in session state so the user can continue the conversation with follow-up questions.

### Step 9: Manage Conversations

The user can start a new chat or clear the current conversation using the available interface controls.

## 7. Project Structure

The following is the intended logical structure of the application. Keep the paths aligned with the files present in your actual project.

```text
Task_4_VortexAI/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── agent/
│   ├── __init__.py
│   └── executor.py
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── file_reader.py
│   └── web_search.py
│
└── tests/
    └── ...
```

### File Descriptions

| File or directory | Responsibility |
|---|---|
| `app.py` | Streamlit application entry point and chat interface |
| `requirements.txt` | Python dependencies required by the application |
| `.env` | Stores local environment variables and API credentials |
| `.gitignore` | Excludes secrets, virtual environments, caches, and generated files from Git |
| `agent/` | Contains the AI agent implementation |
| `agent/executor.py` | Configures the language model, tools, and agent execution |
| `tools/calculator.py` | Implements the calculator functionality |
| `tools/file_reader.py` | Implements supported file-reading functionality |
| `tools/web_search.py` | Implements web-search functionality |
| `tests/` | Contains automated tests, if included |

**Note:** The structure above is a documentation template. If your repository contains additional files or different filenames, document the actual structure rather than creating unnecessary files.

## 8. Prerequisites

Before running Vortex AI, ensure that the following are available:

- Python 3.10 or another version supported by the installed dependencies.
- Git, if cloning the repository.
- A Google Gemini API key.
- Internet connectivity for model API requests and web search.
- A terminal such as Windows PowerShell.
- A modern web browser.

Check your Python installation:

```powershell
python --version
```

Check that pip is available:

```powershell
python -m pip --version
```

## 9. Installation and Setup

### Step 1: Open the Project Directory

Navigate to the directory containing the Vortex AI application.

For example:

```powershell
cd "C:\Users\mahee\OneDrive\Desktop\Task_4_VortexAI"
```

Use the actual path where your project is stored.

### Step 2: Create a Virtual Environment

Create an isolated Python environment for the project.

```powershell
python -m venv .venv
```

A virtual environment keeps the project's dependencies separate from other Python projects.

### Step 3: Activate the Virtual Environment

On Windows PowerShell, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because of its execution policy, use an appropriate permitted activation method for your environment rather than changing system-wide security settings unnecessarily.

After activation, the terminal should display the environment name, typically `(.venv)`.

### Step 4: Install Dependencies

Install the dependencies listed in `requirements.txt`:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If installation fails, check the Python version and the compatibility of the package versions specified in the requirements file.

### Step 5: Configure the API Key

Create or update the `.env` file in the project root.

Add the Google Gemini API key using the environment variable expected by the application.

For example:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace the placeholder with your actual API key.

**Security precautions:**

- Never commit the `.env` file to a public repository.
- Never place API keys directly in source code.
- Ensure `.env` is listed in `.gitignore`.
- If an API key is accidentally exposed, revoke it and create a replacement.

### Step 6: Verify the Configuration

Before starting the application, confirm that:

1. The virtual environment is active.
2. Dependencies are installed.
3. The `.env` file is configured correctly.
4. The application loads the expected environment variable.
5. The configured Gemini model is available to your API account.

## 10. Running the Application

Once the installation and configuration are complete, start the application.

### Step 1: Navigate to the Project Root

```powershell
cd "C:\Users\mahee\OneDrive\Desktop\Task_4_VortexAI"
```

### Step 2: Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If the environment is already active, this step can be skipped.

### Step 3: Start Streamlit

```powershell
streamlit run app.py
```

Alternatively:

```powershell
python -m streamlit run app.py
```

### Step 4: Open the Browser

Streamlit normally displays a local address in the terminal, commonly:

```text
http://localhost:8501
```

Open the displayed local URL in your browser if it does not open automatically.

### Step 5: Interact with Vortex AI

Once the application loads:

1. Enter a question in the chat input.
2. Submit the prompt.
3. Observe the generated response.
4. Ask follow-up questions within the conversation.
5. Try requests that use the available tools.
6. Upload a supported document using the file-upload control.
7. Use New Chat to begin another conversation.
8. Use Clear Chat to clear the active conversation.

The application runs locally. A public deployment is not required to use it on your own computer.

## 11. Testing and Validation

Testing should verify the interface, agent, tool integrations, session behavior, and error handling.

### 11.1 Interface Testing

Verify that:

- The application launches without errors.
- The chat input accepts user messages.
- User and assistant messages appear in the correct order.
- The interface remains usable after multiple prompts.
- The New Chat and Clear Chat controls behave as intended.

### 11.2 Agent Testing

Verify that:

- A basic conversational prompt produces a response.
- Follow-up prompts are handled appropriately.
- The configured model can be reached using the supplied API credentials.
- Tool execution occurs when relevant to a request.
- Tool failures do not crash the entire application unnecessarily.

### 11.3 Calculator Testing

Try a simple calculation such as:

```text
What is 125 multiplied by 8?
```

Verify that the agent uses the calculator when appropriate and returns the correct result.

### 11.4 Web Search Testing

Ask a question that requires current or externally retrieved information.

Verify that the web-search tool runs successfully and that its results are incorporated appropriately into the response.

Search results can vary depending on network availability and the search provider.

### 11.5 File-Reading Testing

Upload a supported document and try asking a question about its contents.

Verify that the configured file-processing implementation can access the file and that the agent uses the available document content appropriately.

### 11.6 Session-State Testing

Send multiple prompts in the same session and confirm that previous messages remain visible.

Then test New Chat and Clear Chat to ensure the expected conversation reset occurs.

### 11.7 Automated Tests

If the repository contains automated tests, run them from the project root:

```powershell
pytest -q
```

If Pytest is not installed and is part of your testing setup, install it in the active virtual environment:

```powershell
pip install pytest
```

Only report tests as passing when they have actually been executed successfully.

## 12. Error Handling and Troubleshooting

### Problem 1: Missing API Key

**Possible cause:** The API key is missing or the environment variable name does not match the application configuration.

**Solution:**

- Check the `.env` file.
- Confirm the expected environment variable name.
- Ensure the application loads environment variables before initializing the model.
- Restart Streamlit after configuration changes.

### Problem 2: Dependency Installation Failure

**Possible cause:** Incompatible package versions, network issues, or an unsupported Python version.

**Solution:**

```powershell
python --version
python -m pip install -r requirements.txt
```

Review the installation error and use dependency versions compatible with the project's code.

### Problem 3: Streamlit Command Not Found

**Possible cause:** Streamlit is not installed in the active environment or the wrong Python environment is being used.

**Solution:**

```powershell
python -m streamlit run app.py
```

If the module is unavailable, install the dependencies listed in `requirements.txt`.

### Problem 4: AI Response Fails

**Possible cause:** Invalid API credentials, network connectivity issues, model access restrictions, or API quota limits.

**Solution:**

- Verify the API key.
- Check network connectivity.
- Confirm model availability.
- Review the terminal output for the underlying error.

### Problem 5: Tool Execution Fails

**Possible cause:** Invalid input, a tool dependency issue, an unavailable search service, or an exception inside a tool.

**Solution:**

- Test the affected tool independently.
- Validate input before executing the tool.
- Handle tool exceptions appropriately.
- Ensure the agent is configured with the intended tools.

### Problem 6: Chat History Is Lost

**Possible cause:** Session-state initialization or conversation-reset logic is clearing messages unexpectedly.

**Solution:**

- Initialize the conversation state only when the relevant key is absent.
- Avoid resetting the active conversation during ordinary reruns.
- Clear state only when the user requests a reset or starts a new conversation.

### Problem 7: Uploaded File Cannot Be Read

**Possible cause:** An unsupported file type, an incorrect file-handling path, or an issue in the file reader.

**Solution:**

- Verify the supported file types.
- Check the upload-processing implementation.
- Validate file content before passing it to the agent.
- Display a clear error when processing fails.

## 13. Security and Privacy Considerations

- Keep API keys and credentials outside the source code.
- Exclude `.env` and virtual-environment directories from version control.
- Validate uploaded files before processing them.
- Restrict file access to the intended files and directories.
- Avoid executing arbitrary commands or untrusted code from user input.
- Use appropriate exception handling for API and tool failures.
- Be mindful of the information sent to external model and search services.
- Do not assume session-state conversation history is persistent storage; it is generally session-scoped.

## 14. Limitations

The current application has the following general considerations:

- AI-generated responses can contain incorrect information.
- Tool results depend on the configured tools and external service availability.
- API usage may be subject to quotas, rate limits, or costs.
- Conversation history maintained in session state is not necessarily saved permanently.
- File processing depends on the supported formats and file-reader implementation.
- Streaming behavior depends on the model integration and the agent's execution path.
- A locally running application is not automatically accessible as a publicly hosted service.
- Persistent conversation storage, multi-user authentication, and production deployment require additional implementation if needed.

## 15. Future Improvements

Possible improvements include:

1. **Persistent Chat History:** Store conversations in a database so users can access them across sessions.
2. **Conversation Management:** Add conversation renaming, deletion, and restoration.
3. **Expanded File Support:** Support additional document formats and larger files with suitable validation.
4. **Document Question Answering:** Add retrieval-augmented generation (RAG) for searching larger document collections.
5. **Improved Source Attribution:** Display sources or references when answers use external search results or documents.
6. **Additional Tools:** Integrate more tools for productivity, data analysis, and information retrieval.
7. **Error Reporting:** Improve user-facing error messages and diagnostic logging.
8. **Interface Enhancements:** Refine responsive layouts, loading indicators, accessibility, and chat controls.
9. **Automated Testing:** Expand unit and integration tests for the agent, tools, and interface logic.
10. **Deployment:** Package and deploy the application to an appropriate hosting platform if public access is required.

## 16. Learning Outcomes

This project demonstrates practical experience with:

- Building a browser-based AI application using Streamlit.
- Integrating Google Gemini with LangChain.
- Designing an agent that can use multiple tools.
- Connecting a user interface to a Python agent pipeline.
- Managing conversation state and chat history.
- Implementing interactive chat controls.
- Supporting file uploads and tool-based information retrieval.
- Handling configuration through environment variables.
- Organizing application logic into reusable modules.
- Running and validating a local AI application.

## 17. Conclusion

Vortex AI demonstrates how a tool-enabled AI agent can be transformed into a user-friendly conversational web application.

By combining Streamlit, LangChain, Google Gemini, and custom tools, the project brings together conversational AI, tool execution, session management, file uploads, and a modern chat interface in a single local application.

The project provides a foundation for developing more advanced AI assistants with persistent conversations, richer document processing, expanded tool capabilities, and production-ready deployment.

## 18. Author

**Project:** Vortex AI  
**Task:** Task 4 — AI Agent Web Application  
**Technology:** Python, Stream
