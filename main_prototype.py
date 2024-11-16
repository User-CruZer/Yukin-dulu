import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.title("Hello there!")
st.header("welcome to our prototype")
st.subheader("made by: Yukin dulu team")

st.write("Petunjuk Upload:")
st.write("Klik tombol browse file dibawah dan cari foto yang akan diupload")
st.write("pastikan Foto yang anda upload sejenis dengan gambar berikut:")

col1, col2, col3 = st.columns([1, 1, 1])  

with col1:
    st.image("Contoh1.jpeg", caption="contoh 1")

with col2:
    st.image("contoh2.jpeg", caption="contoh 2")

with col3:
    st.image("contoh3.jpeg", caption="contoh 3")

uploaded_files = st.file_uploader(
    "insert an image", accept_multiple_files=True, type=["png", "jpg"]
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Open and display each image
            image = Image.open(uploaded_file)
            st.image(image, caption=f"Uploaded: {uploaded_file.name}", use_container_width=True)
        except Exception as e:
            st.error(f"An error occurred with {uploaded_file.name}: {e}")

submitter =  f"{uploaded_files}", st.button("submit image", use_container_width= True)


# ChatGpt Masih Error
chatgpt_url = "https://chat.openai.com/"
iframe_code = f"""
    <iframe src="{chatgpt_url}" width="100%" height="800px" frameborder="0"></iframe>
"""
components.html(iframe_code, height=200)