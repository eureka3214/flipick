import streamlit as st
import fitz

def flags_decomposer(flags):
    """Make font flags human readable."""
    l = []
    if flags & 2 ** 0:
        l.append("superscript")
    if flags & 2 ** 1:
        l.append("italic")
    if flags & 2 ** 2:
        l.append("serifed")
    else:
        l.append("sans")
    if flags & 2 ** 3:
        l.append("monospaced")
    else:
        l.append("proportional")
    if flags & 2 ** 4:
        l.append("bold")
    return ", ".join(l)

def display_fonts(pdf_path, font_name, font_size, font_color):
    doc = fitz.open(stream=pdf_path.read(), filetype="pdf")
    page = doc[0]

    # read page text as a dictionary, suppressing extra spaces in CJK fonts
    blocks = page.get_text("dict", flags=11)["blocks"]
    font_filtered_data = []
    for b in blocks:  # iterate through the text blocks
        for l in b["lines"]:  # iterate through the text lines
            for s in l["spans"]:  # iterate through the text spans
                if (s["font"].lower() == font_name.lower() or font_name.lower() == "all") and \
                        (s["size"] == font_size or font_size == "all") and \
                        (s["color"] == font_color or font_color == "all"):
                    font_properties = {
                        "Text": s["text"],
                        "Font": s["font"],
                        "Size": s["size"],
                        "Color": s["color"]
                    }
                    font_filtered_data.append(font_properties)

    if len(font_filtered_data) > 0:
        st.table(font_filtered_data)
    else:
        st.write("No matching fonts found.")

st.title("PDF Font Checker")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
font_name = st.selectbox("Select Font Name", ["All", "Arial", "Times", "Helvetica", "Courier", "Symbol", "Other"])
font_size = st.selectbox("Select Font Size", ["All", 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72])
font_color = st.selectbox("Select Font Color", ["All", "#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", "#00ffff", "#ff00ff"])

if uploaded_file is not None:
    display_fonts(uploaded_file, font_name, font_size, font_color)
