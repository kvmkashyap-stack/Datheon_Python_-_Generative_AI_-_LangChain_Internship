
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database.db import Base
from database.chat_repository import (
    add_message,
    create_conversation,
    delete_all_conversations,
    delete_conversation,
    get_conversation,
    get_messages,
    list_conversations,
)


@pytest.fixture
def db():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    TestingSession = sessionmaker(bind=engine)

    with TestingSession() as session:
        yield session

    Base.metadata.drop_all(bind=engine)
    engine.dispose()


def test_create_conversation(db):
    chat = create_conversation(db)

    assert chat.id is not None
    assert chat.title == "New Chat"


def test_save_and_retrieve_messages(db):
    chat = create_conversation(db)

    add_message(db, chat.id, "user", "Hello Vortex")
    add_message(db, chat.id, "assistant", "Hello! How can I help?")

    messages = get_messages(db, chat.id)

    assert len(messages) == 2
    assert messages[0].role == "user"
    assert messages[1].content == "Hello! How can I help?"


def test_conversation_title_updates(db):
    chat = create_conversation(db)

    add_message(db, chat.id, "user", "Explain LangChain")

    updated_chat = get_conversation(db, chat.id)
    assert updated_chat.title == "Explain LangChain"


def test_list_conversations(db):
    create_conversation(db, "Chat One")
    create_conversation(db, "Chat Two")

    chats = list_conversations(db)

    assert len(chats) == 2


def test_delete_conversation(db):
    chat = create_conversation(db)
    add_message(db, chat.id, "user", "Delete this chat")

    assert delete_conversation(db, chat.id) is True
    assert get_conversation(db, chat.id) is None


def test_delete_all_conversations(db):
    create_conversation(db, "First")
    create_conversation(db, "Second")

    deleted_count = delete_all_conversations(db)

    assert deleted_count == 2
    assert list_conversations(db) == []


def test_reject_invalid_role(db):
    chat = create_conversation(db)

    with pytest.raises(ValueError):
        add_message(db, chat.id, "system", "Invalid role")
