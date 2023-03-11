import fitz
import streamlit as st

uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])


variables_dict = {}

# add a button to create a new variable and add it to the dictionary
if st.button("Add" ,key="add variables"):
    # prompt the user for a name for the variable
    var_name = st.text_input("Enter a name for the variable:")
    if var_name:
        # create a new variable with the name entered by the user
        exec(f"{var_name} = ''")
        # add the variable to the dictionary
        variables_dict[var_name] = []
if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")


    # create an empty dictionary to hold the variables
    

    for page in doc:
        txtpg = page.get_textpage()

        blocks = txtpg.extractBLOCKS()
        for block in blocks:
            container = st.expander(str(block))
            container.checkbox("select to group", label_visibility="hidden", key=str(block[5]))
            with container:
                # add a dropdown to select the variable to add the block to
                var_selection = st.selectbox("Add to variable:", key=str(block[4]), options=list(variables_dict.keys()))
                # add the block to the selected variable
                if st.button("Add block"):
                    variables_dict[var_selection].append(block[4])

                st.write(block[4])
        # st.markdown(html, unsafe_allow_html =True)

    doc.close()
