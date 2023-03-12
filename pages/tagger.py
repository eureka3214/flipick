import streamlit as st
import fitz

# Create a dictionary to store the tagged data
tagged_data = {}

# Define a function to tag the paragraphs
def tag_paragraphs(page):
    # Get the paragraphs in the page
    paragraphs = page.getText("text").split("\n\n")
    for i, para in enumerate(paragraphs):
        # Display the paragraph text and a dropdown to select the heading
        st.write(f"Paragraph {i+1}: {para}")
        heading = st.selectbox("Select Heading", ["", "Heading 1", "Heading 2", "Heading 3"])
        if heading:
            # Store the tagged data in the dictionary
            tagged_data.setdefault(heading, []).append({
                "text": para,
                "style": page.get_text_style(i)
            })

# Define the main function
def main():
    # Upload a PDF file
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if pdf_file is not None:
        # Open the PDF file using Pymupdf
        pdf_doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        # Display the number of pages in the PDF
        st.write(f"Number of Pages: {pdf_doc.page_count}")
        # Loop through each page in the PDF
        for i in range(pdf_doc.page_count):
            st.write(f"Page {i+1}")
            # Call the tag_paragraphs function to tag the paragraphs
            tag_paragraphs(pdf_doc[i])
        # Display the tagged data
        st.write(tagged_data)

if __name__ == "__main__":
    main()
