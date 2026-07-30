import streamlit as st
from theme import load_theme

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Veltrix AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Load Theme
# --------------------------------------------------

load_theme()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;padding-bottom:15px;">
            <h2>🤖 Veltrix AI</h2>
            <p style="color:#94A3B8;">
                Agentic AI Assistant
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.success("🟢 AI Online")

    st.info("OpenAI Connected")

    st.info("MongoDB Connected")

    st.info("ElevenLabs Connected")

    st.divider()

    st.caption("Version 1.0")

# --------------------------------------------------
# Home Page
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>🤖 Veltrix AI</h1>
        <p>AI Powered Task Delegation & Voice Calling Assistant</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📋 Tasks", "--")

with col2:
    st.metric("📞 Calls", "--")

with col3:
    st.metric("🤖 Status", "Online")

st.divider()

st.info("👈 Select a page from the left sidebar to begin.")

st.caption("Powered by OpenAI • ElevenLabs • MongoDB • Streamlit")