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
    radio_pg_key = 0
    radio_header_key = 0
    radio_Subheader_key = 0

    for page in doc:
        txtpg = page.get_textpage()
        
        blocks = txtpg.extractBLOCKS()
        for block in blocks:
            container = st.expander(str(block[4]))
            radio_pg_key += 1
            radio_header_key += 1
            radio_Subheader_key += 1

            container.radio("Paragraph", label_visibility="visible", key=radio_pg_key)
            container.radio("Header", label_visibility="visible", key=radio_Subheader_key)
            container.radio("subheader", label_visibility="visible", key=radio_Subheader_key)

            with container:
               
                st.write(block)
        # st.markdown(html, unsafe_allow_html =True) 
        
        
    doc.close()
