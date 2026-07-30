import streamlit as st
from calleragent import execute_pending_calls
from database import tasks_collection
from theme import load_theme, hero

load_theme()


def page_execute_calls():

    # -----------------------------------
    # Hero
    # -----------------------------------

    hero(
        "📞 Execute Calls",
        "Start AI voice calls for pending reminders"
    )

    st.write("")

    # -----------------------------------
    # Quick Stats
    # -----------------------------------

    total = tasks_collection.count_documents({})
    pending = tasks_collection.count_documents({"status": "Pending"})
    completed = tasks_collection.count_documents({"status": "Completed"})

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📋 Total Tasks", total)

    with col2:
        st.metric("⏳ Pending", pending)

    with col3:
        st.metric("✅ Completed", completed)

    st.write("")

    # -----------------------------------
    # Task Board
    # -----------------------------------

    st.subheader("📋 Pending Task Board")

    tasks = list(tasks_collection.find())

    if len(tasks) == 0:

        st.info("No tasks found.")

    else:

        for task in tasks:

            with st.container(border=True):

                c1, c2 = st.columns([4,1])

                with c1:

                    st.markdown(f"### {task['title']}")

                    st.write(f"👤 **Contact:** {task['name']}")

                    st.write(f"⚡ **Action:** {task['action']}")

                    if task["status"] == "Pending":
                        st.warning("⏳ Pending")

                    elif task["status"] == "Completed":
                        st.success("✅ Completed")

                    else:
                        st.info(task["status"])

                with c2:

                    st.write("")

                    st.write("")

                    if task["status"] == "Pending":
                        st.button(
                            "📞 Ready",
                            disabled=True,
                            key=str(task["_id"])
                        )

                    else:
                        st.button(
                            "✔ Done",
                            disabled=True,
                            key=str(task["_id"])
                        )

    st.write("")

    # -----------------------------------
    # Execute Calls
    # -----------------------------------

    st.divider()

    st.subheader("🚀 Execute Pending Calls")

    st.write(
        "Click the button below to let Veltrix AI call every pending contact."
    )

    if st.button(
        "📞 Start Pending Calls",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner("Calling contacts..."):

            result = execute_pending_calls()

        st.success("Execution Finished")

        st.divider()

        for line in result:

            st.info(line)

    st.write("")

    st.caption(
        "Powered by OpenAI • ElevenLabs • MongoDB • Streamlit"
    )