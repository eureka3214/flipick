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

    # Create empty dictionary to store text by font
    text_by_font = {}

    # Iterate over pages in PDF
    for page in pdf_doc:
        st.write(f"Page {page.number + 1}")

        # Iterate over text blocks in page
        for block in page.get_text("dict")["blocks"]:
            font_name = block["font"]
            if font_name not in font_names:
                font_names.append(font_name)
                text_by_font[font_name] = []

            # Extract text using selected font
            if font_name == selected_font:
                text = block["text"].strip()
                if text:
                    text_by_font[font_name].append(text)

    # Close PDF document
    pdf_doc.close()

    # Display font names in select box
    selected_font = st.selectbox("Select a font", font_names)

    # Display text for selected font
    if selected_font in text_by_font:
        st.write(f"Text for {selected_font}:")
        for text in text_by_font[selected_font]:
            st.write(text)
    else:
        st.write(f"No text found for {selected_font}.")
