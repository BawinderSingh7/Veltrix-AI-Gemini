# Application File
import json
from database import save_contacts
from pages.save_task import page_tasks
from pages.execute_calls import page_execute_calls
from pages.dashboard import page_dashboard
import streamlit as st

st.set_page_config(
    page_title="Veltrix AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Save contacts in the database
    #save_contacts()

    pg = st.navigation(
        [
            st.Page(page_tasks, title="Save Tasks"),
            st.Page(page_execute_calls, title="Execute Calls"),
            st.Page(page_dashboard, title="Dashboard"),
        ]
    )

    pg.run()

if __name__ == "__main__":
    main()