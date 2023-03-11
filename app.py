import fitz
import streamlit as st

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

if uploaded_pdf is not None:
    with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.getText()
        st.write(text)
