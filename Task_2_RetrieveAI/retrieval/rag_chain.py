import re

from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.rag_prompt import RAG_PROMPT
from retrieval.vector_store import load_vector_store


ABSTENTION = (
    "I couldn't find sufficient information in the provided documents."
)


def answer_question(
    question: str,
    persist_directory: str = "chroma_db",
) -> dict:
    """Answer a question using the selected document's vector store."""

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    vector_store = load_vector_store(
        persist_directory=persist_directory
    )
    documents = vector_store.similarity_search(question, k=4)

    if not documents:
        return {"answer": ABSTENTION, "sources": []}

    context_parts = []
    source_map = {}

    for index, document in enumerate(documents, start=1):
        source = document.metadata.get("source", "Unknown source")
        page = document.metadata.get("page")

        if page is not None:
            citation = f"{source}, page {int(page) + 1}"
        else:
            citation = f"{source} (page number unavailable)"

        context_parts.append(
            f"[{index}] Source: {citation}\n{document.page_content}"
        )
        source_map[str(index)] = citation

    context = "\n\n".join(context_parts)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )

    response = llm.invoke(
        RAG_PROMPT.format_messages(
            context=context,
            question=question,
        )
    )

    answer = response.content

    if not isinstance(answer, str):
        answer = str(answer)

    if ABSTENTION.lower() in answer.lower():
        return {"answer": ABSTENTION, "sources": []}

    cited_numbers = set(re.findall(r"\[(\d+)\]", answer))

    # Do not return an uncited answer as if it were grounded.
    if not cited_numbers or not cited_numbers.issubset(source_map.keys()):
        return {"answer": ABSTENTION, "sources": []}

    sources = [
        source_map[number]
        for number in sorted(cited_numbers, key=int)
    ]

    return {"answer": answer, "sources": sources}
