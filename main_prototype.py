import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.title("Hello there!")
st.header("welcome to our prototype")
st.subheader("made by: Yukin dulu team")

st.write("Petunjuk Upload:")
st.write("Klik tombol browse file dibawah dan cari foto yang akan diupload")
st.write("Berikut contoh gambar yang diupload dan demonya: ")

selected_image = st.radio(
    "Pilih Contoh Demo: ",
    ("contoh 1", "contoh 2", "contoh 3")
)

if selected_image == "contoh 1":
    st.image("Contoh1.jpeg", caption="Demo Data: Contoh 1", use_container_width=200)
elif selected_image == "contoh 2":
    st.image("contoh2.jpeg", caption="Demo Data: Contoh 2", use_container_width=200)
elif selected_image == "contoh 3":
    st.image("contoh3.jpeg", caption="Demo Data: Contoh 3", use_container_width=200)

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