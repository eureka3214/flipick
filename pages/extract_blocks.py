import fitz
import streamlit as st

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    # toc = doc.get_toc()
    
    # # for t in toc:
    # #     t += " modified by set_toc"  
    # # doc.set_toc(toc)
    # st.write(toc)
    # doc.close() 
    checkbox_key = 0
    for page in doc:
        txtpg = page.get_textpage()
        
        blocks = txtpg.extractBLOCKS()
        for block in blocks:
            container = st.expander(str(block[4]))
            checkbox_key += 1
            container.checkbox("select to group", label_visibility="hidden", key=checkbox_key)
            with container:
               
                st.write(block)
        # st.markdown(html, unsafe_allow_html =True) 
        
        
    doc.close()
