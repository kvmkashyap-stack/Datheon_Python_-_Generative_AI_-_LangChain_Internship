
import uuid
from pathlib import Path

import streamlit as st

from agent.executor import ask_agent, build_agent
from tools.file_reader import DATA_DIR


# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="NexusAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# Custom styling
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background: #212121;
        color: #ececec;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 1000px;
        padding-top: 1.5rem;
        padding-bottom: 7rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #171717;
        border-right: 1px solid #303030;
    }

    [data-testid="stSidebar"] > div {
        padding-top: 1.4rem;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #d4d4d4;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        border: 1px solid #424242;
        background: #262626;
        color: #eeeeee;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #353535;
        border-color: #777777;
        color: white;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        background: transparent;
        border: none;
        padding: 1rem 0.4rem;
    }

    [data-testid="stChatMessageContent"] {
        color: #ececec;
        line-height: 1.75;
    }

    /* Chat input container */
    [data-testid="stChatInput"] {
    background: #ffffff !important;
    border: 1px solid #d1d5db !important;
    border-radius: 24px !important;
    padding: 5px 8px !important;
}

[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] textarea:focus {
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
    caret-color: #111111 !important;
    background: #ffffff !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #666666 !important;
    -webkit-text-fill-color: #666666 !important;
    opacity: 1 !important;
}

    /* File uploader */
    [data-testid="stFileUploader"] {
        border-radius: 12px;
    }

    /* Expanders */
    [data-testid="stExpander"] {
        background: #262626;
        border: 1px solid #3b3b3b;
        border-radius: 12px;
    }

    /* Dividers and muted text */
    hr {
        border-color: #343434;
    }

    .muted-text {
        color: #a0a0a0;
        font-size: 0.88rem;
    }

    .brand-title {
        font-size: 1.45rem;
        font-weight: 700;
        letter-spacing: -0.7px;
        color: #ffffff;
    }

    .brand-subtitle {
        color: #a0a0a0;
        font-size: 0.82rem;
        margin-top: -8px;
    }

    .welcome-title {
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        font-weight: 650;
        letter-spacing: -1.2px;
        text-align: center;
        color: #f5f5f5;
        margin-top: 12vh;
        margin-bottom: 0.5rem;
    }

    .welcome-subtitle {
        text-align: center;
        color: #a5a5a5;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    /* Keep the footer subtle */
    .footer-note {
        text-align: center;
        color: #777777;
        font-size: 0.75rem;
        padding-top: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Session state
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    # Maps original filename -> safe internal filename
    st.session_state.uploaded_files = {}


@st.cache_resource
def get_agent():
    return build_agent()


def save_uploaded_file(uploaded_file):
    """Save a supported document with a generated safe filename."""
    suffix = Path(uploaded_file.name).suffix.lower()
    allowed_types = {".pdf", ".txt"}

    if suffix not in allowed_types:
        raise ValueError("Only PDF and TXT files are supported.")

    if uploaded_file.size > 1_000_000:
        raise ValueError("Maximum file size is 1 MB.")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    stored_name = f"{uuid.uuid4().hex}{suffix}"
    destination = DATA_DIR / stored_name
    destination.write_bytes(uploaded_file.getvalue())

    return stored_name


# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand-title">🧠 NexusAI</div>
        <div class="brand-subtitle">Your AI workspace</div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button("＋   New chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("**TOOLS**")
    st.markdown("🌐  Web search")
    st.markdown("🧮  Calculator")
    st.markdown("📄  Document reader")

    st.divider()

    st.markdown("**YOUR DOCUMENTS**")

    if st.session_state.uploaded_files:
        for original_name in st.session_state.uploaded_files:
            st.markdown(f"📎 `{original_name}`")
    else:
        st.markdown(
            '<div class="muted-text">Your uploaded files will appear here.</div>',
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown(
        '<div class="muted-text">Powered by Gemini · Built with Streamlit</div>',
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# Main header
# --------------------------------------------------
header_left, header_right = st.columns([5, 1])

with header_left:
    st.markdown("### NexusAI")
    st.caption("A multi-tool AI agent for research, reasoning, and documents.")

with header_right:
    st.markdown(
        '<div style="text-align:right; color:#a0a0a0; padding-top:12px;">'
        "● Ready</div>",
        unsafe_allow_html=True,
    )

st.divider()


# --------------------------------------------------
# Welcome screen
# --------------------------------------------------
if not st.session_state.messages:
    st.markdown(
        """
        <div class="welcome-title">What can I help you with?</div>
        <div class="welcome-subtitle">
            Search the web, solve calculations, or ask questions about your files.
        </div>
        """,
        unsafe_allow_html=True,
    )

    card1, card2, card3 = st.columns(3)

    with card1:
        st.markdown("#### 🌐 Research")
        st.markdown(
            '<div class="muted-text">Find information and explore topics using web search.</div>',
            unsafe_allow_html=True,
        )

    with card2:
        st.markdown("#### 🧮 Calculate")
        st.markdown(
            '<div class="muted-text">Solve mathematical expressions with the calculator tool.</div>',
            unsafe_allow_html=True,
        )

    with card3:
        st.markdown("#### 📄 Your files")
        st.markdown(
            '<div class="muted-text">Upload PDF or TXT documents and ask questions about them.</div>',
            unsafe_allow_html=True,
        )


# --------------------------------------------------
# Conversation history
# --------------------------------------------------
for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "🧠"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

        if message.get("tool_logs"):
            with st.expander("View agent execution logs"):
                for log in message["tool_logs"]:
                    st.code(log, language="text")


# --------------------------------------------------
# Chat input with attachment support
# --------------------------------------------------
chat_input = st.chat_input(
    "Message NexusAI...",
    accept_file="multiple",
    file_type=["pdf", "txt"],
)

if chat_input:
    prompt = (chat_input.text or "").strip()
    attachments = chat_input.files or []
    newly_uploaded = []

    # Save uploaded files
    for uploaded_file in attachments:
        try:
            stored_name = save_uploaded_file(uploaded_file)
            st.session_state.uploaded_files[uploaded_file.name] = stored_name
            newly_uploaded.append(uploaded_file.name)
        except Exception as exc:
            st.error(f"Could not upload {uploaded_file.name}: {exc}")

    if newly_uploaded:
        names = ", ".join(newly_uploaded)
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": f"Successfully uploaded: {names}",
            }
        )

    # Process prompt
    if prompt:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user", avatar="🧑"):
            st.markdown(prompt)

        # Give the agent both original and internal filenames.
        file_context = ""
        if st.session_state.uploaded_files:
            file_details = "\n".join(
                f"- User filename: {original_name}; "
                f"filename for the document reader tool: {stored_name}"
                for original_name, stored_name
                in st.session_state.uploaded_files.items()
            )

            file_context = (
                "\n\nUploaded documents available in the data directory:\n"
                f"{file_details}\n"
                "If the question is about an uploaded document, use the "
                "document reader tool with its exact internal filename. "
                "Do not claim to have read a file unless you used the tool."
            )

        try:
            agent = get_agent()

            with st.chat_message("assistant", avatar="🧠"):
                with st.spinner("NexusAI is thinking..."):
                    answer = ask_agent(agent, prompt + file_context)

                st.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                }
            )

        except Exception as exc:
            error_message = f"NexusAI encountered an error: {exc}"
            st.error(error_message)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message,
                }
            )

    elif newly_uploaded:
        st.info("Your files are ready. Ask NexusAI a question about them.")

    st.rerun()

st.markdown(
    '<div class="footer-note">NexusAI can make mistakes. Verify important information.</div>',
    unsafe_allow_html=True,
)
