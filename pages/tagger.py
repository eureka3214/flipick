import streamlit as st
import fitz

st.set_page_config(page_title="FLIPICK",page_icon="🧊",layout="wide")

st.title("Filter with Fonts (WORKING)")


col1, col2 = st.columns([2,4],gap="medium")



def display_fonts(pdf_path):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[0]
        # for page in doc:
    txtpg = page.get_textpage()
    
    html = txtpg.extractHTML()
    xml = txtpg.extractXML()
    # st.code(xml,language='xml')
    # st.code(html,language='html')
    col2.markdown(html, unsafe_allow_html =True) 
    
        
    # doc.close()

 
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    display_fonts(uploaded_file)
