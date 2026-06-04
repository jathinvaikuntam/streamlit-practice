import streamlit as st

st.title("Image Viewer")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.image(uploaded_file)