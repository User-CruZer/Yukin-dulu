import streamlit as st

pages = {
    "Main": [
        st.Page("streamlit.py", title="Main Prototype"),
        st.Page("about.py", title="About!"),
    ],
}

pg = st.navigation(pages)
pg.run()