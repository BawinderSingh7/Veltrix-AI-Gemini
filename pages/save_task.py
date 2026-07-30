
import streamlit as st
import time
from aiagent import agentic_save
from streamlit_mic_recorder import speech_to_text
from theme import load_theme, hero

load_theme()

def page_tasks():

    st.set_page_config(
        page_title="Veltrix AI - Save Task",
        page_icon="🤖",
        layout="wide"
    )

    # --------------------------
    # Custom CSS
    # --------------------------

    st.markdown("""
    <style>

    .stApp{
        background:#0f172a;
    }

    h1{
        color:white;
    }

    p{
        color:#cbd5e1;
    }

    div[data-testid="stChatMessage"]{
        border-radius:15px;
        padding:10px;
    }

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        max-width:900px;
    }

    </style>
    """, unsafe_allow_html=True)

    # --------------------------
    # Header
    # --------------------------

    st.markdown(
        """
        <h1 style='text-align:center;'>
        🤖 Veltrix AI
        </h1>

        <p style='text-align:center;font-size:18px;'>
        AI Powered Task Delegation Assistant
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # --------------------------
    # Session State
    # --------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # --------------------------
    # Previous Chat
    # --------------------------

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --------------------------
    # Voice Input
    # --------------------------

    st.markdown("### 🎤 Voice Input")

    voice_text = speech_to_text(
        language="en",
        just_once=True,
        use_container_width=True,
        key="voice"
    )

    if voice_text:
        st.session_state.voice_input = voice_text

    default_text = st.session_state.get("voice_input", "")

    # --------------------------
    # Input Area
    # --------------------------

    st.markdown("### 📝 Write a Task")

    user_input = st.text_area(
        "",
        value=default_text,
        placeholder="Example: Call Jashan tomorrow at 5 PM regarding project discussion.",
        height=120,
        label_visibility="collapsed"
    )

    col1, col2 = st.columns([6,1])

    with col2:
        send = st.button(
            "➤ Send",
            use_container_width=True,
            type="primary"
        )

    # --------------------------
    # Process Task
    # --------------------------

    if send and user_input.strip():

        user_message = {
            "role": "user",
            "content": user_input
        }

        st.session_state.messages.append(user_message)

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("🤖 Veltrix AI is thinking..."):

            input_list = [
                {
                    "role": "user",
                    "content": user_input
                }
            ]

            result = agentic_save(input_list=input_list)

        assistant_message = {
            "role": "assistant",
            "content": result
        }

        st.session_state.messages.append(assistant_message)

        with st.chat_message("assistant"):

            placeholder = st.empty()

            text = ""

            for ch in result:
                text += ch
                placeholder.markdown(text)
                time.sleep(0.01)

        # Clear voice text after sending
        if "voice_input" in st.session_state:
            del st.session_state["voice_input"]

    st.divider()

    st.caption(
        "Powered by OpenAI • ElevenLabs • MongoDB • Streamlit"
    )