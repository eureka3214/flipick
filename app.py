import fitz
import streamlit as st

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    # page = doc.loadPage(0) # Choose the first page
    for page in doc:
        pix = page.getPixmap()
    image = pix.getImageData("png")
    return image

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

if uploaded_pdf is not None:
    image = read_pdf(uploaded_pdf)
    st.image(image, caption="PDF page", use_column_width=True)
    # doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    # cat = doc.get_toc(simple=False)
    # st.write(doc.xref_object(cat))
    # st.write(cat)
    # text = ""
    # for page in doc:
    #     txtpg = page.get_textpage()
    #     cont = page.read_contents()
    #     # st.image(cont)
    #     st.write(cont) 
        
        # st.write(txtpg.extractDICT()) 
    # doc.close()