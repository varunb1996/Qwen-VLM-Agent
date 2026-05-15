import streamlit as st
import requests

st.title(
    "Agentic Vision Language AI Assistant"
)

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

question = st.text_input(
    "Ask a question about the image"
)

if st.button("Analyze"):

    if uploaded_file is not None:

        files = {
            "file": uploaded_file
        }

        data = {
            "question": question
        }

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            files=files,
            data=data
        )

        st.write(
            response.json()
        )