import streamlit as st
import fitz

st.title("PDF Font Viewer")

# Upload PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Load PDF file using PyMuPDF
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    # Display number of pages in PDF
    st.write(f"Number of pages: {pdf_doc.page_count}")

    # Create empty list to store font names
    font_names = []

    # Iterate over pages in PDF
    for page in pdf_doc:
        st.write(f"Page {page.number + 1}")

        # Iterate over text blocks in page
        for block in page.get_fonts("text"):
            font_name = block[3]
            if font_name not in font_names:
                font_names.append(font_name)

    # Close PDF document
    pdf_doc.close()

    # Display font names in select box
    selected_font = st.selectbox("Select a font", font_names)
    st.write(f"You selected: {selected_font}")
