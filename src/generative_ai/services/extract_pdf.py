
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
def extract_pdf(pdf):
        
        if pdf is not None:
            pdf_reader = PdfReader(pdf)
            raw_text= ''
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                     raw_text += text                  
                         
            text_splitter = RecursiveCharacterTextSplitter(        
                chunk_size = 1000,
                chunk_overlap  = 200,
                length_function = len,
            )
            chunks = text_splitter.split_text(raw_text)
            return chunks
