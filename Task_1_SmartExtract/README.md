# SmartExtract — LLM-Based Structured Information Extraction

## 1. Project Overview

SmartExtract is a Python-based Generative AI application that extracts structured information from unstructured resume text using Google Gemini and LangChain.

Organizations often receive resumes containing information in different formats. Manually extracting candidate details can be time-consuming and inconsistent. SmartExtract addresses this problem by converting resume text into structured, validated JSON.

The application combines prompt engineering, few-shot prompting, LLM-based extraction, and Pydantic validation to produce consistent output while handling missing information.

## 2. Problem Statement

Extracting candidate information from unstructured resumes manually can be repetitive and error-prone. The objective of this project is to develop a Python application that accepts resume text, identifies relevant information, validates the extracted data, and produces a structured JSON result.

## 3. Key Features

- **LLM-based extraction:** Uses Google Gemini through LangChain.
- **Prompt engineering:** Uses explicit instructions to guide information extraction.
- **Few-shot prompting:** Provides examples of expected input and output to guide the model.
- **Structured output:** Uses Pydantic models to define the expected data structure.
- **Data validation:** Validates field types, email addresses, and non-negative experience values.
- **Missing-field handling:** Uses `null` for missing scalar fields and empty lists for missing collections.
- **JSON export:** Saves extracted information to `output/resume.json`.
- **Automated testing:** Uses pytest to test prompt behavior and schema validation.

## 4. Extracted Information

The application supports extracting the following resume fields:

- Candidate name
- Email address
- Phone number
- Skills
- Years of experience
- Education details, including degree, institution, and graduation year
- Projects



## 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| Google Gemini | Large Language Model used for information extraction |
| LangChain | Prompt templates, few-shot prompting, and LLM integration |
| Pydantic | Schema definition and data validation |
| python-dotenv | Loading API credentials from environment variables |
| pytest | Automated testing |
| JSON | Structured output format |

## 6. How It Works

1. **Input:** The user pastes resume text into the command-line application.
2. **Prompt construction:** LangChain combines system instructions, few-shot examples, and the supplied resume text.
3. **LLM processing:** Google Gemini processes the prompt and extracts relevant information.
4. **Structured output:** LangChain's structured-output integration maps the model response to the `ResumeData` Pydantic schema.
5. **Validation:** Pydantic validates the extracted fields against the defined schema.
6. **Export:** The application serializes the validated result to JSON and saves it to `output/resume.json`.

## 7. Data Validation and Missing Information

SmartExtract uses Pydantic models to define the expected output structure.

- Missing scalar values are represented as `null`.
- Missing list values default to empty lists.
- Invalid email addresses are rejected during validation.
- Negative experience values are rejected by the schema.
- The prompt instructs the model to extract only information supported by the supplied resume and not invent missing details.

**Note:** Schema validation checks the output's structure and constraints. It cannot independently guarantee that every extracted fact is correct, so model-generated results should still be reviewed when accuracy is important.



## 8. Project Structure

```text
Task_1_SmartExtract/
├── main.py
├── requirements.txt
├── README.md
├── prompts/
│   └── resume_prompt.py
├── schemas/
│   ├── __init__.py
│   └── resume.py
├── tests/
│   ├── __init__.py
│   ├── test_prompt.py
│   └── test_schema.py
└── output/
    └── resume.json
```

### File Descriptions

- `main.py` — Runs the extraction workflow, accepts resume text, and saves the validated JSON output.
- `prompts/resume_prompt.py` — Defines the extraction instructions and few-shot examples.
- `schemas/resume.py` — Defines the Pydantic models for resume information.
- `tests/test_prompt.py` — Tests prompt construction and instructions.
- `tests/test_schema.py` — Tests schema defaults and validation constraints.
- `output/resume.json` — Stores the extracted resume data.
- `requirements.txt` — Lists the Python dependencies needed to run the project.



## 9. Installation and Setup

### Prerequisites

- Python 3.12 or a compatible Python version
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/kvmkashyap-stack/Datheon_Python_-_Generative_AI_-_LangChain_Internship.git
cd Datheon_Python_-_Generative_AI_-_LangChain_Internship/Task_1_SmartExtract
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

Create a `.env` file inside the `Task_1_SmartExtract` directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace the placeholder with your actual API key. Never commit the `.env` file or expose your API key in source code.

### 5. Run the Application

```bash
python main.py
```

Paste the resume / linkedin posts text when prompted. The application will display the extracted JSON and save it to `output/resume.json`.



## 10. Running Tests

The project includes automated tests for prompt construction and Pydantic schema validation.

Run the tests from the `Task_1_SmartExtract` directory:

```bash
python -m pytest tests -v
```

The current test suite contains six tests covering:

- Prompt construction with resume text
- Instructions against inventing missing information
- Valid resume data
- Default values for missing fields
- Rejection of negative experience values
- Rejection of invalid email addresses

**Verified result:** All six tests passed.

## 11. Limitations

- Extraction quality depends on the quality and completeness of the input text and the language model's response.
- The application currently focuses on resume text rather than directly parsing PDF or Word files.
- A valid Google Gemini API key and an available model endpoint are required for live extraction.
- Pydantic validates the output structure and constraints but cannot guarantee the factual accuracy of extracted information.
- The current implementation saves results to a single output file, `output/resume.json`, which is overwritten by subsequent runs.

## 12. Future Improvements

- Support direct PDF and DOCX resume uploads.
- Add batch processing for multiple resumes.
- Add more comprehensive validation and error-handling tests.
- Allow users to specify output filenames to preserve multiple extraction results.
- Expand the schema to support additional candidate information.

## 13. Author

**K. V. Maheedhara Kashyap**

GitHub: [kvmkashyap-stack](https://github.com/kvmkashyap-stack)

---

*Developed as part of the Datheon Python, Generative AI, and LangChain internship tasks.*