import fitz
import streamlit as st

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    toc = doc.get_toc()
    
    for t in toc:
        toc[1][1] += " modified by set_toc"  
    doc.set_toc(toc)
    st.write(toc) 
    for page in doc:
        txtpg = page.get_textpage()
        
        # pix = page.get_pixmap()
        # st.write(pix) 
        
        
    doc.close()