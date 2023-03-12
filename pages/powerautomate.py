import streamlit as st
import io
import layoutparser as lp
from pdf2image import convert_from_bytes
from PIL import Image


def visualize_layouts(pdf_file):
    # Convert PDF to bytes
    pdf_bytes = io.BytesIO(pdf_file.read())
    
    # Convert bytes to image
    pil_images = convert_from_bytes(pdf_bytes.read())
    
    # Extract layouts
    layouts = lp.Detectron2LayoutModel('lp://PubLayNet-faster_rcnn').detect(pil_images)
    
    # Display layouts
    for page_layout in layouts:
        page_image = pil_images[page_layout.page_number]
        st.image(page_image, use_column_width=True)
        for block in page_layout.blocks:
            st.write(f'Block {block.id} ({block.type}):')
            st.write(block)
            st.image(block.crop(page_image), use_column_width=True)


# Streamlit app
st.title('PDF Layout Visualizer')

pdf_file = st.file_uploader('Upload a PDF file', type='pdf')
if pdf_file is not None:
    visualize_layouts(pdf_file)
