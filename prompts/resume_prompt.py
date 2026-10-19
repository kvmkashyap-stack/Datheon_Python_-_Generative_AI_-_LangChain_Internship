from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "Extract resume information from:\n{resume_text}"),
        ("ai", "{output}"),
    ]
)

examples = [
    {
        "resume_text": (
            "I am Rahul. I have 2 years of experience "
            "with Python and FastAPI."
        ),
        "output": (
            '{"name": "Rahul", "email": null, '
            '"phone": null, "skills": ["Python", "FastAPI"], '
            '"experience_years": 2, "education": [], '
            '"projects": []}'
        ),
    },
    {
        "resume_text": (
            "My name is Priya. I know Java and SQL. "
            "I graduated from ABC University in 2024."
        ),
        "output": (
            '{"name": "Priya", "email": null, '
            '"phone": null, "skills": ["Java", "SQL"], '
            '"experience_years": null, '
            '"education": [{"degree": null, '
            '"institution": "ABC University", '
            '"graduation_year": 2024}], "projects": []}'
        ),
    },
]


few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)


resume_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a structured resume/linkedin post/information extractor. "
            "Extract information supported by the resume/ linkedin posts. "
            "Never invent missing information. "
            "Use null for missing scalar values and empty lists "
            "for missing collections. Follow the requested schema.",
        ),
        few_shot_prompt,
        (
            "human",
            "Extract structured information from this resume/linkedin post:\n"
            "{resume_text}",
        ),
    ]
)
