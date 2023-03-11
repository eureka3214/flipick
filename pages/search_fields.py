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


def get_text_at_coords(pdf, block_coords):
    # Loop through each block coordinate
    for block_coord in block_coords:
        # Get the page number and rectangle coordinates for this block
        page_num, rect_tl, rect_br = block_coord

        # Get the page object for this page number
        page = pdf[page_num]

        # Get the text in the rectangle
        text = page.get_text("text", clip=rect_tl + rect_br)

        # Display the text on the screen
        st.write(f"Page {page_num}: {text.strip()}")


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
            bc = []
            # Display the block coordinates on the page
            for block_coord in block_coords:
                st.write(f"Page {block_coord[0]}, Block {block_coord[1]} - {block_coord[2]}")
                parts = block_coord_str.split(" ")
                page_num = block_coord[0]
                rect_tl = block_coord[1]
                rect_br = block_coord[2]
                bc.append((page_num, rect_tl, rect_br))


            get_text_at_coords(pdf, bc)
        # Get the user's block coordinates
        # block_coords_str = st.text_input("Enter block coordinates (e.g. '0 (10, 20) (100, 200)'):")

        # If the user has entered block coordinates
        # if block_coords_str:
        #     # Parse the block coordinates string into a list of tuples
        #     block_coords = []
        #     for block_coord_str in block_coords_str.split(";"):
        #         parts = block_coord_str.split(" ")
        #         page_num = int(parts[0])
        #         rect_tl = eval(parts[1])
        #         rect_br = eval(parts[2])
        #         block_coords.append((page_num, rect_tl, rect_br))

        #     # Get the text at the block coordinates and display it on the screen
        #     get_text_at_coords(pdf, block_coords)

app()