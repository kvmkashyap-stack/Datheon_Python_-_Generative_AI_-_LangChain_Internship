
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, Text, select
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from database.db import Base


def utc_now():
    return datetime.now(timezone.utc)


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), default="New Chat")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation",
        cascade="all, delete-orphan",
        order_by="Message.id",
    )


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id", ondelete="CASCADE"), index=True
    )
    role: Mapped[str] = mapped_column(String(20))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now
    )

    conversation: Mapped[Conversation] = relationship(
        back_populates="messages"
    )


def create_conversation(db: Session, title: str = "New Chat") -> Conversation:
    conversation = Conversation(title=title)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation


def list_conversations(db: Session) -> list[Conversation]:
    statement = select(Conversation).order_by(
        Conversation.updated_at.desc(), Conversation.id.desc()
    )
    return list(db.scalars(statement).all())


def get_conversation(db: Session, conversation_id: int):
    return db.get(Conversation, conversation_id)


def get_messages(db: Session, conversation_id: int) -> list[Message]:
    statement = (
        select(Message)
        .where(Message.conversation_id == conversation_id)
        .order_by(Message.id)
    )
    return list(db.scalars(statement).all())


def add_message(
    db: Session,
    conversation_id: int,
    role: str,
    content: str,
) -> Message:
    if role not in {"user", "assistant"}:
        raise ValueError("role must be 'user' or 'assistant'")

    conversation = db.get(Conversation, conversation_id)
    if conversation is None:
        raise ValueError("Conversation not found")

    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content,
    )
    conversation.updated_at = utc_now()

    if role == "user" and conversation.title == "New Chat":
        cleaned = " ".join(content.split())
        if cleaned:
            conversation.title = (
                cleaned[:197] + "..." if len(cleaned) > 200 else cleaned
            )

    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def delete_conversation(db: Session, conversation_id: int) -> bool:
    conversation = db.get(Conversation, conversation_id)
    if conversation is None:
        return False

    db.delete(conversation)
    db.commit()
    return True


def delete_all_conversations(db: Session) -> int:
    conversations = list_conversations(db)
    count = len(conversations)

    for conversation in conversations:
        db.delete(conversation)

    db.commit()
    return count
