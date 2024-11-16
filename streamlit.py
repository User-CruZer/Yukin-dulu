import streamlit as st
import streamlit.components.v1 as components

st.sidebar.write("# About!")
st.sidebar.write("waiting for season 2 for real") # Ketik disini mad

st.title("Hello there")
st.subheader("Welcome Woy Brader!")
st.subheader("To cancer detection made by yukin dulu team")

uploaded_files = st.file_uploader(
    "insert an image", accept_multiple_files=True, type=["png", "jpg"]
)

submitter =  f"{uploaded_files}", st.button("submit image", use_container_width= True)


# ChatGpt Masih Error
chatgpt_url = "https://chat.openai.com/"
iframe_code = f"""
    <iframe src="{chatgpt_url}" width="100%" height="800px" frameborder="0"></iframe>
"""
components.html(iframe_code, height=200)