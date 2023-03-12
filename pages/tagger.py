import streamlit as st
import fitz

def tag_paragraphs(headings, paragraphs):
    tagged_data = {}
    for i, heading in enumerate(headings):
        tagged_data[heading] = paragraphs[i]
    return tagged_data

st.title("Tagger Application")

# Input headings
st.header("Enter the headings:")
headings = []
for i in range(3): # change the number of headings as per your requirement
    heading = st.text_input(f"Heading {i+1}")
    headings.append(heading)

# Input paragraphs
st.header("Enter the paragraphs:")
paragraphs = []
for i in range(3): # change the number of paragraphs as per your requirement
    paragraph = st.text_area(f"Paragraph {i+1}")
    paragraphs.append(paragraph)

# Tag paragraphs with headings
if st.button("Tag paragraphs"):
    tagged_data = tag_paragraphs(headings, paragraphs)
    st.write(tagged_data)
