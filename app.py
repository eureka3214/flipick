import fitz
import streamlit as st

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
   
    text = ""
    for page in doc:
        txtpg = page.get_textpage()
        labels = page.get_page_labels()
        # pix = page.get_pixmap()
        # st.write(pix) 
        
        st.write(labels) 
    doc.close()