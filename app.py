import os
import streamlit as st
from PyPDF2 import PdfMerger, PdfWriter, PdfReader
from PIL import Image
from pdf2docx import Converter

class Item_To_Change():
    def __init__(self, pdf_files, pic_files=None):
        self.pdf_files = pdf_files
        self.pic_files = pic_files



    def splitting(self):
        os.makedirs(".\\output", exist_ok=True)
        output_path = ".\\output"
        for file in self.pdf_files:
            # if file.endswith(".pdf"):
            #     path_to_open = os.path.join(output_path, file)
            with open(file, "rb") as og_file:
                Reader = PdfReader(og_file)
                for page_num in range(len(Reader.pages)):
                    pdf_writer = PdfWriter()
                    pdf_writer.add_page(Reader.pages[page_num])
                    with open(f"{output_path}\\page_num_{page_num}.pdf", "wb") as new_file:
                        pdf_writer.write(new_file)
    def merge_pdf(self):
        os.makedirs(".\\output", exist_ok=True)
        output_path = ".\\output"
        merger = PdfMerger(strict=False)
        for file in self.pdf_files:
            merger.append(file)
        merger.write(f"{output_path}\\new_file.pdf")
        merger.close()

    def pdf_to_image(self):
        os.makedirs(".\\output", exist_ok=True)
        output_path = ".\\output"
        for pic_file in self.pic_files:
            pic_name = pic_file.split("\\")[-1].split('.')[-2]
            image_content = Image.open(pic_file)
            image_content_converted = image_content.convert("RGB")
            image_content_converted.save(f"{output_path}\\{pic_name}.pdf")

    def pdf_to_word(self):
        os.makedirs(".\\output", exist_ok=True)
        output_path = ".\\output"
        
        for file in self.pdf_files:
            file_name = file.split("\\")[-1].split('.')[-2]
            converter_one = Converter(file)
            converter_one.convert(f"{output_path}\\{file_name}.docx")




def write_uploaded_folders(uploaded_files):
    os.makedirs(".\\currrent_working_dir", exist_ok=True)
    pdf_paths = []
    for f in uploaded_files:
        current_path = os.path.join(".\\currrent_working_dir", f.name)
        pdf_paths.append(current_path)
        with open(current_path, "wb") as current_file:
            current_file.write(f.getbuffer())

    return pdf_paths
def get_pic_files(uploaded_files):
    os.makedirs(".\\currrent_working_dir", exist_ok=True)
    pic_paths = []
    for f in uploaded_files:
        if f.name.split(".")[-1] in ('png', 'jpg', 'jpeg'):
            current_path = os.path.join(".\\currrent_working_dir", f.name)
            pic_paths.append(current_path)
            with open(current_path, "wb") as current_file:
                current_file.write(f.getbuffer())
    return pic_paths

st.title("PDF Editing App")
st.caption("Merge, Split pdf and change Images to PDF")




uploaded_files = st.file_uploader("PDF Files", accept_multiple_files=True) 
if st.button("Split PDF to pages"):
    if not uploaded_files:
        st.write("Upload Files")
    else:
        pdfs = write_uploaded_folders(uploaded_files)
        
        item_to_work_on = Item_To_Change(pdfs)
        item_to_work_on.splitting()
            
elif st.button("Merge PDF pages"):
    if not uploaded_files:
        st.write("Upload Files")
    else:
        pdfs = write_uploaded_folders(uploaded_files)
        
        item_to_work_on = Item_To_Change(pdfs)
        item_to_work_on.merge_pdf()
            
elif st.button("Image to PDF"):
    if not uploaded_files:
        st.write("Upload Files")
    else:
        pic_files = get_pic_files(uploaded_files)
        
        item_to_work_on = Item_To_Change(pic_files, pic_files)
        item_to_work_on.pdf_to_image()
    


elif st.button("PDF to Word"):
    if not uploaded_files:
        st.write("Upload Files")
    else:
        pic_files = write_uploaded_folders(uploaded_files)
        
        item_to_work_on = Item_To_Change(pic_files, pic_files)
        item_to_work_on.pdf_to_word()
    