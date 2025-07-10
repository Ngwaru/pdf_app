import os
import streamlit as st
from PyPDF2 import PdfFileMerger, PdfWriter, PdfReader
from PIL import Image

st.title("PDF Manupulation App")
st.caption("Merge, Split pdf and change Images to PDF")

with st.sidebar:
    uploaded_files = st.file_uploader("PDF Files", type='pdf', accept_multiple_files=True)
    if st.button("Upload Files"):
        if not uploaded_files:
            st.write("Upload Files")
        else:
            