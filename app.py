import os
import streamlit as st
from PyPDF2 import PdfFileMerger, PdfWriter, PdfReader
from PIL import Image

def write_uploaded_folders(uploaded_files):
    os.makedirs("./currrent_working_dir", exist_ok=True)
    for f in uploaded_files:
        current_path = os.path.join("./currrent_working_dir", f.name)
        with open(current_path, "wb") as current_file:
            current_path.write(f.getbuffer())

st.title("PDF Editing App")
st.caption("Merge, Split pdf and change Images to PDF")



with st.sidebar:
    uploaded_files = st.file_uploader("PDF Files", type='pdf', accept_multiple_files=True)
    if st.button("Upload Files"):
        if not uploaded_files:
            st.write("Upload Files")
        else:
            write_uploaded_folders(uploaded_files)

if st.button("Split PDF to pages"):
    pass

if st.button("Merge PDF pages"):
    pass

if st.button("Image to PDF"):
    pass


if st.button("PDF to Word"):
    pass