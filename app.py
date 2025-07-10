import os
import streamlit as st
from PyPDF2 import PdfFileMerger, PdfWriter, PdfReader
from PIL import Image

class Item_To_Change():
    def __init__(self, pdf_files):
        self.pdf_files = pdf_files


    def splitting(self):
        os.makedirs("./output", exist_ok=True)
        output_path = "./output"
        for file in os.listdir(os.cwd()):
            if file.endswith(".pdf"):

                with open(output_path, "rb") as og_file:
                    Reader = PdfReader(og_file)
                    for page_num in range(Reader.pages):
                        pdf_writer = PdfWriter()
                        pdf_writer.add_page(Reader.pages[page_num])
                        with open(f"{file}_page_num_{page_num}.pdf", "wb") as new_file:
                            pdf_writer.write(new_file)




def write_uploaded_folders(uploaded_files):
    os.makedirs("./currrent_working_dir", exist_ok=True)
    pdf_paths = []
    for f in uploaded_files:
        current_path = os.path.join("./currrent_working_dir", f.name)
        pdf_paths.add(current_path)
        with open(current_path, "wb") as current_file:
            current_file.write(f.getbuffer())

    return pdf_paths

st.title("PDF Editing App")
st.caption("Merge, Split pdf and change Images to PDF")



with st.sidebar:
    uploaded_files = st.file_uploader("PDF Files", type='pdf', accept_multiple_files=True)
    if st.button("Upload Files"):
        if not uploaded_files:
            st.write("Upload Files")
        else:
            pdfs = write_uploaded_folders(uploaded_files)
            item_to_work_on = Item_To_Change(pdfs)

if st.button("Split PDF to pages"):
    item_to_work_on.splitting()
    

if st.button("Merge PDF pages"):
    pass

if st.button("Image to PDF"):
    pass


if st.button("PDF to Word"):
    pass