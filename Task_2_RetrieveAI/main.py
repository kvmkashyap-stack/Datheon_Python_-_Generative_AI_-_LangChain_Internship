from pathlib import Path

from dotenv import load_dotenv

from ingestion.loader import load_document
from ingestion.chunker import split_documents
from retrieval.vector_store import create_vector_store
from retrieval.rag_chain import answer_question


def main():
    load_dotenv()

    print("=" * 50)
    print("          RetrieveAI - Document QA Agent")
    print("=" * 50)
    print("Supported files: PDF and TXT")
    print("Type 'exit' anytime to quit.\n")

    while True:
        file_input = input(
            "Agent: Enter the path to your document: "
        ).strip().strip('"')

        if file_input.lower() in {"exit", "quit"}:
            print("Agent: Goodbye!")
            return

        if not file_input:
            print("Agent: Please enter a valid file path.\n")
            continue

        file_path = Path(file_input).expanduser()

        try:
            documents = load_document(str(file_path))
            chunks = split_documents(documents)

            print(f"\nAgent: Loaded {len(documents)} document page(s).")
            print(f"Agent: Created {len(chunks)} text chunks.")
            print("Agent: Indexing your document...")

            create_vector_store(
                chunks,
                source_path=str(file_path.resolve()),
            )

            print("Agent: Document indexed successfully!")
            print("Agent: Ask me questions about your document.\n")

            while True:
                question = input("You: ").strip()

                if question.lower() in {"exit", "quit"}:
                    print("Agent: Goodbye!")
                    return

                if question.lower() in {"change file", "new file"}:
                    print()
                    break

                if not question:
                    continue

                try:
                    result = answer_question(question)

                    print(f"\nAnswer: {result['answer']}")

                    if result["sources"]:
                        print("Sources:")
                        for source in result["sources"]:
                            print(f"- {source}")

                    print()

                except Exception as exc:
                    print(f"\nAgent error: {exc}\n")

        except (FileNotFoundError, ValueError, EnvironmentError) as exc:
            print(f"\nAgent: {exc}\n")
        except Exception as exc:
            print(f"\nAgent: Could not process this document: {exc}\n")


if __name__ == "__main__":
    main()
