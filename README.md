# Legal Document Summarizer & Clause Identifier

---

## Overview

This project is an AI-powered system that simplifies understanding of legal documents. It performs:

- Automatic **text extraction** from legal PDFs
- **Clause identification** using LegalBERT
- **Multi-label classification** with confidence scores
- **Legal document summarization**
- **English → Tamil translation**
- **Audio (voice) output** of summarized content

---

## Features

- Upload legal documents (PDF format)
- Sentence-level clause detection
- Highlight key clauses with confidence scores
- Summarize documents automatically
- Multilingual support (English → Tamil)
- Voice output for accessibility
- Supports multiple legal document types (contracts, MOUs, agreements, etc.)

---

## Tech Stack

- **Python, PyTorch, Transformers (HuggingFace)**
- **LegalBERT model for clause classification**
- **NLTK** for sentence tokenization
- **PyMuPDF** for PDF text extraction
- **Google Translate API** for translation
- **gTTS (Google Text-to-Speech)** for audio output
- **Google Colab** for development and training
- **Google Drive** for dataset & model storage

---

## Dataset

- CUAD dataset subset used for training (key 10–15 clauses)
- Total training samples: 8,410
- Multi-label clause classification

---

## Usage

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/legal-doc-summarizer.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```
Run the demo notebook:

```bash
cd notebooks
```
## Open Colab or Jupyter Notebook
Upload a legal PDF and get:

Clause detection + confidence

Summarized document

Tamil translation

Audio output

## Future Developments
Support more Indian and global languages

Mobile app with offline audio summaries

Enhanced clause ranking and importance highlighting

Cloud deployment with secure access control


