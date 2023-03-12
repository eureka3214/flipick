import streamlit as st
import fitz

def tag_paragraphs(headings, paragraphs):
    tagged_data = {}
    for i, heading in enumerate(headings):
        tagged_data[heading] = paragraphs[i]
    return tagged_data

st.title("Tagger Application")

uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    page = doc[0]
        # for page in doc:
    txtpg = page.get_textpage()

    
    html = txtpg.extractHTML()

    html_tag = f"<div>{html}</div>"
    js_function = """
        <script>
            var headings = document.getElementsByTagName("h2");
            for (var i = 0; i < headings.length; i++) {
                headings[i].addEventListener("click", function() {
                    var id = this.innerText.toLowerCase().replace(/ /g, "-");
                    var p = document.getElementById("p" + id);
                    p.style.display = (p.style.display === "none" ? "block" : "none");
                });
            }
        </script>
        """
    st.markdown(html_tag + js_function, unsafe_allow_html =True) 

# Input headings
st.sidebar.header("Enter the headings:")
headings = []
for i in range(3): # change the number of headings as per your requirement
    heading = st.sidebar.text_input(f"Heading {i+1}")
    headings.append(heading)

# Input paragraphs
st.sidebar.header("Enter the paragraphs:")
paragraphs = []
for i in range(3): # change the number of paragraphs as per your requirement
    paragraph = st.sidebar.text_area(f"Paragraph {i+1}")
    paragraphs.append(paragraph)

# Tag paragraphs with headings
if st.sidebar.button("Tag paragraphs"):
    tagged_data = tag_paragraphs(headings, paragraphs)
    st.write(tagged_data)
