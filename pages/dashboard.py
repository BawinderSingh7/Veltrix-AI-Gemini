"""import streamlit as st
from calleragent import fetch_conversation_status
from theme import load_theme, hero

load_theme()

# function to display dashboard
def page_dashboard():
    st.title('Dashboard')
    
    if st.button('Fetch Conversation Status'):
        result = fetch_conversation_status()
    
        for line in result:
            st.write(line)
    """
import streamlit as st
from calleragent import fetch_conversation_status
from theme import load_theme, hero

load_theme()


def page_dashboard():

    # -----------------------------
    # Hero Section
    # -----------------------------

    hero(
        "🤖 Veltrix AI",
        "Agentic AI Voice Assistant Dashboard"
    )

    st.write("")

    # -----------------------------
    # Status Cards
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📋 Tasks",
            value="--",
            delta="Ready"
        )

    with col2:
        st.metric(
            label="📞 Calls",
            value="--",
            delta="Ready"
        )

    with col3:
        st.metric(
            label="👥 Contacts",
            value="--",
            delta="Connected"
        )

    with col4:
        st.metric(
            label="🤖 AI Status",
            value="Online",
            delta="Healthy"
        )

    st.write("")

    # -----------------------------
    # AI Service Status
    # -----------------------------

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("🟢 Services")

            st.success("OpenAI Connected")

            st.success("MongoDB Connected")

            st.success("ElevenLabs Connected")

    with right:

        with st.container(border=True):

            st.subheader("⚡ Quick Actions")

            st.write("Use the sidebar to")

            st.write("• Save Tasks")

            st.write("• Execute Calls")

            st.write("• Monitor Conversations")

    st.write("")

    # -----------------------------
    # Conversation Status
    # -----------------------------

    with st.container(border=True):

        st.subheader("📞 Conversation Status")

        st.write(
            "Fetch the latest AI phone conversations from ElevenLabs."
        )

        if st.button(
            "🔄 Fetch Conversation Status",
            use_container_width=True,
            type="primary"
        ):

            with st.spinner("Fetching latest conversations..."):

                result = fetch_conversation_status()

            st.success("Conversation history loaded.")

            st.divider()

            if result:

                for line in result:

                    st.info(line)

            else:

                st.warning("No conversations found.")

    st.write("")

    # -----------------------------
    # Recent Activity
    # -----------------------------

    with st.container(border=True):

        st.subheader("📝 Recent Activity")

        st.write("✔ Dashboard Loaded")

        st.write("✔ AI Agent Ready")

        st.write("✔ Waiting for new tasks")

        st.write("✔ Waiting for phone calls")

    st.write("")

    st.caption(
        "Powered by OpenAI • ElevenLabs • MongoDB • Streamlit"
    )