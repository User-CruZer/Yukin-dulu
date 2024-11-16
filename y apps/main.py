import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import numpy as np
import pandas as pd
import tensorflow as tf

@st.cache_resource
def model_cal():
    # Get the model
    densenetmodel = tf.keras.models.load_model('code/model/DenseNet121_final_model2.keras')
    incv3model = tf.keras.models.load_model('code/model/InceptionV3_final_model2.keras')
    return (densenetmodel, incv3model)

densenetmodel, incv3model = model_cal()

@st.cache_data
def predict_dl(x):
    # Load the image with the expected target size
    image = tf.keras.preprocessing.image.load_img(x, target_size=(224, 224))  # Adjust size based on your model's input

    # Convert the image to a numpy array
    image_array = tf.keras.preprocessing.image.img_to_array(image)

    # Normalize the pixel values to [0, 1] (if your model requires it)
    image_array = image_array / 255.0

    # Add a batch dimension (the model expects inputs as a batch of images)
    image_array = tf.expand_dims(image_array, axis=0)

    pred_densenet = densenetmodel.predict(image_array)
    pred_densenet = pred_densenet[:, 1]

    pred_incv3 = incv3model.predict(image_array)
    pred_incv3 = pred_incv3[:, 1]

    predicted_prob_all = (wDense*pred_densenet) + (wIncV3*pred_incv3)
    temp = predicted_prob_all > 0.5
    temp = temp.astype(int)
    predicted_class_all = classes[temp[0]]

    return (predicted_prob_all, predicted_class_all)
    

# Predicted probability from the weights
wDense=0.8500000000000001
wIncV3=0.1499999999999999
classes = ['Benign', 'Malignant']

st.title("Selamat Datang di SKI-NET")
st.text("Skin Cancer Detection Using Transfer Learning Neural Networks")
st.text("Dibuat Oleh: Yukindulu")

st.header("Prediksi Kanker Kulit")

st.subheader("Contoh Prediksi")

selected_image = st.radio(
    "Pilih gambar: ",
    ("Gambar 1", "Gambar 2", "Gambar 3")
)

if selected_image == "Gambar 1":
    selected_image_path = "y apps/example1.jpeg"
    st.image(selected_image_path, caption="Demo Data: Gambar 1", use_container_width=200)
elif selected_image == "Gambar 2":
    selected_image_path = "y apps/example2.jpeg"
    st.image(selected_image_path, caption="Demo Data: Gambar 2", use_container_width=200)
elif selected_image == "Gambar 3":
    selected_image_path = "y apps/example3.jpg"
    st.image(selected_image_path, caption="Demo Data: Gambar 3", use_container_width=200)

jal1 = st.button('Jalankan', key='b1')
if jal1:
    predicted_prob_all, predicted_class_all = predict_dl(selected_image_path)
    st.code(f'Hasil prediksi: {predicted_class_all}\nProbabilitas Malignant: {predicted_prob_all[0]}')

st.subheader("Upload Untuk Prediksi Kanker Kulit")

uploaded_file = st.file_uploader(
    "Unggah Gambar", accept_multiple_files=False, type=["png", "jpg"]
)

jal2 = st.button('Jalankan', key='b2')
if jal2:
    predicted_prob_all, predicted_class_all = predict_dl(uploaded_file)
    st.code(f'Hasil prediksi: {predicted_class_all}\nProbabilitas Malignant: {predicted_prob_all[0]}')