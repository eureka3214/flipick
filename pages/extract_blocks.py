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
    radio_title_key = 0
  

    for page in doc:
        txtpg = page.get_textpage()
        
        blocks = txtpg.extractBLOCKS()
        for block in blocks:
            container = st.expander(str(block[4]))
            radio_title_key += 1
            container.radio("Content Option", options=["header", "subheader","paragraph"],label_visibility="visible", key=radio_title_key)
            
            with container:
               
                st.write(block)
        # st.markdown(html, unsafe_allow_html =True) 
        
        
    doc.close()
