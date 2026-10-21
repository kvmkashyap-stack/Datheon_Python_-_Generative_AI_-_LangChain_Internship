import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.resume_prompt import resume_prompt
from schemas.resume import ResumeData

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from the .env file")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key=api_key,
)

structured_llm = llm.with_structured_output(
    ResumeData, method="json_schema",
)

chain = resume_prompt | structured_llm

resume_text = input(
    "Paste the resume/linkedin post text here:\n"
).strip()


if not resume_text:
    print("Error: Resume text cannot be empty.")
    raise SystemExit(1)


try:
    result = chain.invoke({"resume_text": resume_text})

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "resume.json"

    output_file.write_text(
        result.model_dump_json(indent=2),
        encoding="utf-8",
    )

    print("\nValidated Resume JSON:\n")
    print(result.model_dump_json(indent=2))

    print(f"\nJSON saved successfully to: {output_file}")


except Exception as error:
    print("Error: Resume extraction failed.")
    print(f"Details: {error}")
    raise SystemExit(1)
