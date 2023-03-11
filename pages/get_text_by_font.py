import streamlit as st
import fitz # PyMuPDF library

# Define function to extract text from PDF using PyMuPDF
def extract_text(pdf_path):
    pdf_doc = fitz.open(stream=pdf_path.read(), filetype="pdf")

    # with fitz.open(pdf_path) as doc:
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Define function to apply font to text
def apply_font(text, font_name):
    font = f"fonts/{font_name}.ttf" # Assuming the font files are stored in a 'fonts' subdirectory
    style = fitz.TextStyle(font=font)
    styled_text = ""
    for line in text.split("\n"):
        styled_text += f"<span style='font-family:{font_name};'>{line}</span>\n"
    return styled_text

# Streamlit app
st.title("PDF Text with Custom Font")

# File upload widget
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Font select box
font_options = ["Arial", "Calibri", "Georgia", "Times New Roman"]
font_name = st.selectbox("Select a font", options=font_options)

# If file is uploaded and font is selected
if uploaded_file is not None and font_name is not None:
    # Extract text from PDF
    text = extract_text(uploaded_file)
    # Apply font to text
    styled_text = apply_font(text, font_name)
    # Display styled text
    st.write(styled_text, unsafe_allow_html=True)
