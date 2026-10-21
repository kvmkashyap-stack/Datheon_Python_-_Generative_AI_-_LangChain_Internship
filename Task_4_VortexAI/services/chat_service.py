
from collections.abc import Iterator

from database.db import SessionLocal
from database.chat_repository import (
    add_message,
    create_conversation,
    get_conversation,
    get_messages,
)
from agent.executor import build_agent


class ChatService:
    """Connect the LangChain agent with persistent conversation history."""

    def __init__(self):
        self.agent = build_agent()

    def create_chat(self) -> int:
        with SessionLocal() as db:
            conversation = create_conversation(db)
            return conversation.id

    def get_history(self, conversation_id: int) -> list[dict[str, str]]:
        with SessionLocal() as db:
            conversation = get_conversation(db, conversation_id)

            if conversation is None:
                return []

            return [
                {"role": message.role, "content": message.content}
                for message in get_messages(db, conversation_id)
            ]

    def stream_response(
        self, conversation_id: int, question: str
    ) -> Iterator[str]:
        """Stream an answer when supported; persist both completed messages."""

        question = question.strip()
        if not question:
            return

        # Load the existing conversation before saving the new question.
        history = self.get_history(conversation_id)

        with SessionLocal() as db:
            if get_conversation(db, conversation_id) is None:
                raise ValueError("Conversation not found.")

            add_message(db, conversation_id, "user", question)

        messages = [
            {"role": item["role"], "content": item["content"]}
            for item in history[-20:]
        ]
        messages.append({"role": "user", "content": question})

        answer_parts: list[str] = []

        try:
            # LangChain agents expose a stream API. Stream model message chunks
            # when available, while allowing tool execution to complete.
            for event in self.agent.stream(
                {"messages": messages},
                stream_mode="messages",
            ):
                chunk, metadata = event

                if metadata.get("langgraph_node") != "model":
                    continue

                content = getattr(chunk, "content", "")

                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    text = "".join(
                        block.get("text", "")
                        for block in content
                        if isinstance(block, dict)
                        and block.get("type") == "text"
                    )
                else:
                    text = ""

                if text:
                    answer_parts.append(text)
                    yield text

            answer = "".join(answer_parts).strip()

            if not answer:
                answer = "The agent did not return a final answer."
                yield answer

        except Exception:
            # Do not store a fabricated assistant response.
            raise

        with SessionLocal() as db:
            add_message(db, conversation_id, "assistant", answer)
