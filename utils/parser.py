import PyPDF2
from docx import Document
import os

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1]

    # PDF FILE
    if ext == ".pdf":
        text = ""
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text

    # DOCX FILE
    elif ext == ".docx":
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    return "Unsupported file type"