import pdfplumber
from nltk.tokenize import sent_tokenize

def extract_sentences_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

    sentences = sent_tokenize(text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    return sentences
