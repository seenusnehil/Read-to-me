import streamlit as st
from PIL import Image
import pdfplumber
import numpy as np
@st.cache
def load_image(img):
    image=Image.open(img)

    return image

# @st.cache
# def load_pdf(file):
#     pdf_images=[]
   
#     with pdfplumber.open(file) as pdf:
#         for i in range(len(pdf.pages)):
#             image=pdf.pages[i].to_image(resolution=150)
#             test=Image.open(image)
#             print(test)
#             pdf_images.append(image)
    
#     return pdf_images


if __name__=='__main__':
    load_pdf("/home/revanth/Downloads/Form11_ PF Declaration.pdf")