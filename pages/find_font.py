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

    # Iterate over pages in PDF
    for page in pdf_doc:
        st.write(f"Page {page.number + 1}")

        # Iterate over text blocks in page
        for block in page.get_fonts("text"):
            text = block[4]
            font_name = block[5]
            font_size = block[6]
            st.write(block)
            # Display font name and size
            # st.write(f"{text} - Font: {font_name}, Size: {font_size}")

    # Close PDF document
    pdf_doc.close()
