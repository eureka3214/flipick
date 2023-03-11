# import fitz
# import streamlit as st

# uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])

# if uploaded_pdf is not None:
#     doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
   
#     text_blocks = []
#     for page in doc:
#         txtpg = page.get_textpage()
#         blocks = txtpg.extractBLOCKS()
#         text_blocks.append(blocks)
        
#     doc.close()

#     for block in text_blocks:
#         container = st.expander(str(block[0][4]))
#         with container:
#             st.write(block[4])
#         # container.radio(label=block[0][4], options=[block[0][5]])
#         # if container.radio_selected:
#         #         bbox = block[0]
#         #         st.write(f"Bbox coordinates: {bbox}")

          
#         # # st.write(f"Page {page_num + 1}")
#         # for block_num, block in enumerate(blocks):
#         #     container = st.container()
#         #     container.radio(label=block["lines"][0]["spans"][0]["text"], options=[block_num])
#         #     if container.radio_selected:
#         #         bbox = block["bbox"]
#         #         st.write(f"Bbox coordinates: {bbox}")
