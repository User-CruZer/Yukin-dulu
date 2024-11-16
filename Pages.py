import streamlit as st

pages = {
    "Main": [
        st.Page("main_prototype.py", title="Main Prototype"),
        st.Page("about.py", title="About!"),
    ],
}

pg = st.navigation(pages)
pg.run()