import streamlit as st
import fitz





if __name__ == '__main__':
    def find_text_in_pdf(pdf_file, search_text):
    doc = fitz.open(pdf_file)
    blocks = []
    for page in doc:
        block = page.search_for(search_text)
        if block:
            blocks.append((page.number, block))
    return blocks
    
    st.title('PDF Text Search')
    pdf_file = st.file_uploader('Upload PDF', type=['pdf'])
    if pdf_file is not None:
        search_text = st.text_input('Enter Text to Search')
        if search_text:
            blocks = find_text_in_pdf(pdf_file, search_text)
            if blocks:
                st.write(f'Found {len(blocks)} Occurrences of "{search_text}" in PDF')
                for block in blocks:
                    st.write(f'Page {block[0]}: {block[1]}')
            else:
                st.write(f'No Occurrences of "{search_text}" Found in PDF')
        else:
            st.write('Please Enter Text to Search')
