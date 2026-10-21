
import uuid
from pathlib import Path

import streamlit as st

from database.db import init_db, SessionLocal
from database.chat_repository import (
    create_conversation,
    list_conversations,
    get_conversation,
    delete_conversation,
)
from services.chat_service import ChatService
from tools.file_reader import DATA_DIR


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Vortex AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_db()


# =========================================================
# CHATGPT-STYLE LIGHT THEME
# =========================================================

st.markdown(
    """
    <style>
    /* Main page */
    .stApp {
        background: #ffffff !important;
        color: #202123 !important;
    }

    [data-testid="stHeader"] {
        background: #ffffff !important;
    }

    [data-testid="stMain"] {
        background: #ffffff !important;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 8rem;
    }

    /* Always give the sidebar a visible light background */
    [data-testid="stSidebar"] {
        background: #f9f9f9 !important;
        border-right: 1px solid #e5e5e5 !important;
        min-width: 250px;
    }

    [data-testid="stSidebar"] > div:first-child {
        background: #f9f9f9 !important;
    }

    [data-testid="stSidebar"] * {
        color: #202123;
    }

    /* Branding */
    .vortex-brand {
        font-size: 1.4rem;
        font-weight: 750;
        color: #202123 !important;
        padding: 0.4rem 0 0;
    }

    .vortex-subtitle {
        font-size: 0.82rem;
        color: #6b6b6b !important;
        margin-bottom: 1rem;
    }

    .sidebar-heading {
        font-size: 0.75rem;
        font-weight: 700;
        color: #777777 !important;
        letter-spacing: 0.06em;
        margin-top: 0.5rem;
        margin-bottom: 0.6rem;
    }

    /* Buttons */
    .stButton > button {
        background: transparent !important;
        color: #202123 !important;
        border: 1px solid transparent !important;
        border-radius: 10px !important;
        min-height: 2.5rem;
        text-align: left;
        transition: background 0.15s ease;
    }

    .stButton > button:hover {
        background: #eaeaea !important;
        border-color: #eaeaea !important;
        color: #111111 !important;
    }

    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        background: #ffffff !important;
        border: none !important;
        padding: 1rem 0.25rem !important;
    }

    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] div,
    [data-testid="stChatMessage"] span {
        color: #202123;
    }

    /* Message composer */
    [data-testid="stChatInput"] {
        background: #ffffff !important;
        border: 1px solid #d9d9e3 !important;
        border-radius: 24px !important;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.07) !important;
    }

    [data-testid="stChatInput"]:focus-within {
        border-color: #b8b8c5 !important;
        box-shadow: 0 3px 14px rgba(0, 0, 0, 0.09) !important;
    }

    [data-testid="stChatInput"] textarea {
        color: #202123 !important;
        -webkit-text-fill-color: #202123 !important;
        caret-color: #202123 !important;
        background: transparent !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #777777 !important;
        -webkit-text-fill-color: #777777 !important;
        opacity: 1 !important;
    }

    [data-testid="stChatInput"] button {
        color: #202123 !important;
    }

    /* Welcome screen */
    .welcome {
        text-align: center;
        padding-top: 15vh;
        padding-bottom: 1.5rem;
    }

    .welcome h1 {
        color: #202123 !important;
        font-size: 2.25rem;
        font-weight: 650;
        letter-spacing: -1px;
    }

    .welcome p {
        color: #666666 !important;
        font-size: 1rem;
    }

    /* Suggestion cards */
    .stButton > button[kind="secondary"] {
        border: 1px solid #e5e5e5 !important;
    }

    /* Dividers */
    hr {
        border-color: #e5e5e5 !important;
    }

    /* File upload */
    [data-testid="stFileUploader"] {
        background: #ffffff !important;
        color: #202123 !important;
    }

    /* Hide Streamlit footer */
    footer {
        visibility: hidden;
    }

    /* Status text */
    .muted {
        color: #777777 !important;
        font-size: 0.82rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SERVICE
# =========================================================

@st.cache_resource
def get_chat_service():
    return ChatService()


service = get_chat_service()


# =========================================================
# SESSION STATE
# =========================================================

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = {}

if "suggested_prompt" not in st.session_state:
    st.session_state.suggested_prompt = None


# =========================================================
# HELPERS
# =========================================================

def create_new_chat():
    with SessionLocal() as db:
        conversation = create_conversation(db)
        st.session_state.conversation_id = conversation.id


def save_uploaded_file(uploaded_file):
    suffix = Path(uploaded_file.name).suffix.lower()

    if suffix not in {".pdf", ".txt"}:
        raise ValueError("Only PDF and TXT files are supported.")

    if uploaded_file.size > 1_000_000:
        raise ValueError("Maximum file size is 1 MB per file.")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    stored_name = f"{uuid.uuid4().hex}{suffix}"
    destination = DATA_DIR / stored_name
    destination.write_bytes(uploaded_file.getvalue())

    return stored_name


def get_chat_files(chat_id):
    return st.session_state.uploaded_files.get(chat_id, {})


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown(
        '<div class="vortex-brand">⚡ Vortex AI</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="vortex-subtitle">Your AI workspace</div>',
        unsafe_allow_html=True,
    )

    if st.button(
        "＋  New chat",
        key="create_new_chat",
        use_container_width=True,
    ):
        create_new_chat()
        st.rerun()

    st.divider()

    st.markdown(
        '<div class="sidebar-heading">YOUR CHATS</div>',
        unsafe_allow_html=True,
    )

    with SessionLocal() as db:
        conversations = list_conversations(db)
        chat_items = [
            (chat.id, chat.title or "New Chat")
            for chat in conversations
        ]

    if not chat_items:
        st.caption("No conversations yet.")

    for chat_id, title in chat_items:
        display_title = title[:24] + ("…" if len(title) > 24 else "")
        is_current = chat_id == st.session_state.conversation_id

        open_col, delete_col = st.columns([5, 1], gap="small")

        with open_col:
            button_label = f"●  {display_title}" if is_current else display_title

            if st.button(
                button_label,
                key=f"select_{chat_id}",
                use_container_width=True,
                help=title,
            ):
                st.session_state.conversation_id = chat_id
                st.rerun()

        with delete_col:
            if st.button(
                "🗑",
                key=f"remove_{chat_id}",
                help="Delete this chat",
            ):
                with SessionLocal() as db:
                    delete_conversation(db, chat_id)

                st.session_state.uploaded_files.pop(chat_id, None)

                if st.session_state.conversation_id == chat_id:
                    st.session_state.conversation_id = None

                st.rerun()

    st.divider()

    st.markdown(
        '<div class="sidebar-heading">CAPABILITIES</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="muted">🌐 Web search</div>'
        '<div class="muted">🧮 Calculator</div>'
        '<div class="muted">📄 PDF and TXT documents</div>',
        unsafe_allow_html=True,
    )


# =========================================================
# SELECT OR CREATE A CHAT
# =========================================================

if st.session_state.conversation_id is not None:
    with SessionLocal() as db:
        selected = get_conversation(
            db, st.session_state.conversation_id
        )

    if selected is None:
        st.session_state.conversation_id = None

if st.session_state.conversation_id is None:
    st.markdown(
        """
        <div class="welcome">
            <h1>What can I help you with?</h1>
            <p>Start a new chat to begin your conversation.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.stop()

conversation_id = st.session_state.conversation_id


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

history = service.get_history(conversation_id)

if not history:
    st.markdown(
        """
        <div class="welcome">
            <h1>What can I help you with?</h1>
            <p>Ask anything, solve a problem, or explore your documents.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌐  Search the web", use_container_width=True):
            st.session_state.suggested_prompt = (
                "Search the web for the latest AI news."
            )
            st.rerun()

    with col2:
        if st.button("🧮  Solve a calculation", use_container_width=True):
            st.session_state.suggested_prompt = "Calculate 125 * 48."
            st.rerun()

    with col3:
        if st.button("📄  Ask about a file", use_container_width=True):
            st.session_state.suggested_prompt = (
                "Summarize my uploaded document."
            )
            st.rerun()

else:
    for message in history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# =========================================================
# MESSAGE COMPOSER + FILE UPLOAD
# =========================================================

chat_input = st.chat_input(
    "Message Vortex AI...",
    accept_file="multiple",
    file_type=["pdf", "txt"],
)

prompt = st.session_state.suggested_prompt
st.session_state.suggested_prompt = None

uploaded_now = []

if chat_input is not None:
    prompt = (chat_input.text or "").strip()

    for uploaded_file in (chat_input.files or []):
        try:
            stored_name = save_uploaded_file(uploaded_file)

            files_for_chat = st.session_state.uploaded_files.setdefault(
                conversation_id, {}
            )
            files_for_chat[uploaded_file.name] = stored_name

            uploaded_now.append(uploaded_file.name)

        except (ValueError, OSError) as exc:
            st.error(f"Upload failed: {exc}")

# Show current chat's attachments.
files_for_chat = get_chat_files(conversation_id)

if files_for_chat:
    with st.expander(
        f"📎 Documents attached to this chat ({len(files_for_chat)})",
        expanded=False,
    ):
        for filename in files_for_chat:
            st.write(f"📄 {filename}")

# If a file was submitted without a question, ask the agent to summarize it.
if uploaded_now and not prompt:
    prompt = "Please summarize the document I just uploaded."


# =========================================================
# SEND MESSAGE AND STREAM RESPONSE
# =========================================================

if prompt and prompt.strip():
    prompt = prompt.strip()

    current_files = get_chat_files(conversation_id)

    # Tell the existing agent which uploaded filenames its file tool can read.
    if current_files:
        file_listing = "\n".join(
            f"- {original_name}: {stored_name}"
            for original_name, stored_name in current_files.items()
        )

        agent_prompt = (
            f"{prompt}\n\n"
            "Documents attached to this conversation are listed below. "
            "For questions about these documents, call the file reader tool "
            "using the exact stored filename. Read the document before "
            "answering and do not pretend to have read it if the tool fails.\n"
            f"{file_listing}"
        )
    else:
        agent_prompt = prompt

    with st.chat_message("user"):
        st.markdown(prompt)

        for filename in uploaded_now:
            st.caption(f"📎 {filename}")

    with st.chat_message("assistant"):
        try:
            st.write_stream(
                service.stream_response(
                    conversation_id,
                    agent_prompt,
                )
            )

        except Exception as exc:
            st.error(
                "I couldn't generate a response. Check the terminal for "
                "the underlying error."
            )
            st.caption(str(exc))
