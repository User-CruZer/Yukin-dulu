import streamlit as st

pages = {
    "Main": [
        st.Page("main.py", title="SKI-NET v0.1"),
        st.Page("about.py", title="Tentang SKI-NET"),
    ]
}

pg = st.navigation(pages)
pg.run()