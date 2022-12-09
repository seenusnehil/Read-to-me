import streamlit as st
import streamlit.components.v1 as stc
import pdfplumber
from PIL import Image

st.set_page_config(page_title='OCR',page_icon=':smiley:',initial_sidebar_state='collapsed')


def main():
    side_bar_list=['Home','Image','Pdf']
    menu_bar=st.sidebar.selectbox('Menu',side_bar_list)

    if menu_bar=='Home':
        st.subheader('Home Page')

        

    elif menu_bar=='Image':
        st.subheader('Upload Image')

        uploaded_image=st.file_uploader('Upload your Images',type=['png','jpeg','jpg'],accept_multiple_files=True)
        for i in uploaded_image:
            img=Image.open(i)
            st.image(image=img,use_column_width=True)
    elif menu_bar=='Pdf':
        st.subheader('Upload Pdf')

        uploaded_pdf=st.file_uploader('Upload your Pdf file',type='pdf',accept_multiple_files=False)
        # st.write(uploaded_pdf)

if __name__=='__main__':
    main()