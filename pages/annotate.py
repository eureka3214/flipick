import streamlit as st
import fitz

# Define function to extract text from PDF document using PyMuPDF
def extract_text_from_pdf(pdf_file):
    with fitz.open(pdf_file) as doc:
        text = ""
        for page in doc:
            text += page.getText()
    return text

# Create Streamlit app

    # Set page title
st.set_page_config(page_title="PDF Text Extractor")

# Set page layout
st.title("PDF Text Extractor")
st.write("Upload a PDF file to extract all text contents from the document.")

# Allow user to upload a file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# If file is uploaded
if uploaded_file is not None:
    # Extract text from PDF document
    text = extract_text_from_pdf(uploaded_file)

    # Display text in an expandable widget based on layout hierarchy
    with st.expander("Layout Hierarchy"):
        st.write(text)
