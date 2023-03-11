import fitz
import streamlit as st
import base64

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    # page = doc.loadPage(0) # Choose the first page
    for page in doc:
        pix = page.get_pixmap()
    image = pix.tobytes(output='png')
    return image

def displayPDF(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    base64_pdf = base64.b64encode(doc).decode('utf-8')


    # Opening file from file path
    # with open(file, "rb") as f:
    #     base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

if uploaded_pdf is not None:
    displayPDF(uploaded_pdf)
    # image = read_pdf(uploaded_pdf)
    # st.image(image, caption="PDF page", use_column_width=True)
  