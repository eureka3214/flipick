import streamlit as st
import fitz


def get_block_coords(page, search_text):
    # Find all instances of the search_text on the page
    instances = page.search_for(search_text)

    # Get the block coordinates for each instance
    block_coords = []
    for inst in instances:
        # Get the rectangle coordinates for this instance
        rect = fitz.Rect(inst)

        # Convert the rectangle coordinates to block coordinates
        block_coords.append((page.number, rect.tl, rect.br))

    return block_coords


# Define the Streamlit app
def app():
    # Upload a PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    # Get the user's search text
    search_text = st.text_input("Search for text:")

    # If a PDF file has been uploaded
    if uploaded_file is not None:
        # Open the PDF file using PyMuPDF
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        # Loop through each page of the PDF file
        for page in pdf:
            # Get the block coordinates for the search text on this page
            block_coords = get_block_coords(page, search_text)

            # Display the block coordinates on the page
            for block_coord in block_coords:
                st.write(f"Page {block_coord[0]}, Block {block_coord[1]} - {block_coord[2]}")

app()