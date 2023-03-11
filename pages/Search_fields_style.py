import streamlit as st
import fitz


def get_block_style(block):
    style = {
        'fontname': block.get_fontname(),
        'fontsize': block.get_fontsize(),
        'color': block.get_color(),
        'bgcolor': block.get_bgcolor(),
        'lineheight': block.get_lineheight(),
        'linewidth': block.get_linewidth(),
        'bbox': block.rect
    }
    return style


def find_text_in_pdf(pdf_file, search_text):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    blocks = []
    for page in doc:
        block = page.search_for(search_text)
        if block:
            for b in block:
                style = get_block_style(b)
                blocks.append((page.number, b, style))
    return blocks


if __name__ == '__main__':
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
                    st.json(block[2])
            else:
                st.write(f'No Occurrences of "{search_text}" Found in PDF')
        else:
            st.write('Please Enter Text to Search')
