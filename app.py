import fitz
import streamlit as st

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    cat = doc.get_toc()
    # st.write(doc.xref_object(cat))
    st.write(cat)
    text = ""
    for page in doc:
        txtpg = page.get_textpage()
        pix = page.get_xobjects()
        # st.image(pix)
        st.write(pix) 
        
        # st.write(txtpg.extractDICT()) 
    doc.close()