# Legal Clause Identification System

An AI-powered web application that analyzes legal PDF documents and automatically identifies key contractual clauses using Natural Language Processing. The system allows users to upload legal documents and detect important clauses such as Governing Law, Termination, Confidentiality, and Limitation of Liability.

---

## Features

- Secure **User Authentication (JWT-based login and registration)**
- Upload and analyze **legal PDF documents**
- Automatic detection of key contractual clauses
- Display **confidence scores** for detected clauses
- Downloadable **analysis report**
- Simple web dashboard for document analysis

---

## Dataset

This project utilizes the **CUAD (Contract Understanding Atticus Dataset)**, a dataset designed for legal contract analysis.

Reference:
**CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review**

From the original CUAD dataset, a **subset of clause categories** was created for this project to focus on commonly occurring contractual clauses.

Selected clause categories:

- Governing Law
- Termination
- Confidentiality
- Limitation of Liability
- License Grant
- Non-Compete
- Assignment
- IP Ownership
- Payment Terms

The dataset was preprocessed and structured into a custom training dataset (`cuad_clause_dataset.csv`) used to train the clause classification model.

---

## Model

The system uses a **fine-tuned LegalBERT transformer model** for multi-label classification of legal clauses.

Pipeline:

PDF Document → Text Extraction → Sentence Processing → LegalBERT Model → Clause Prediction → Results Display

Each sentence from the legal document is analyzed and classified into one or more clause categories based on confidence scores.

---

## Technologies Used

### Backend
- FastAPI (Python)

### Frontend
- HTML
- CSS
- JavaScript

### Machine Learning
- HuggingFace Transformers
- LegalBERT

### Other Tools
- JWT Authentication
- PDF Text Extraction

---

## Project Structure
```

LegalDoc-AI/
│
├── legalbert-pretrained/
│ ├── config.json
│ ├── tokenizer_config.json
│ ├── tokenizer.json
│ └── model.safetensors
│
├── main.py
├── model.py
├── clause_identifier.py
├── pdf_utils.py
├── auth.py
├── labels.py
│
├── cuad_clause_dataset.csv
│
├── login.html
├── register.html
├── dashboard.html
├── styles.css
├── dashboard.css
├── app.js
│
├── legal_agreement.pdf
├── legal-mou.pdf
│
└── requirements.txt

```

---

## Model File

Due to GitHub file size limitations, the fine-tuned model file (`model.safetensors`) is hosted externally.

Download the model and place it inside:
legalbert-pretrained/model.safetensors


Google Drive Link:
(Add your link here)

---

## Installation

Clone the repository:
```
git clone "https://github.com/Nivethitha-A/LegalDoc-AI"
```

Create virtual environment:

```
python -m venv venv
```


Activate environment (Windows):

```
venv\Scripts\activate
```


Install dependencies:

```
pip install -r requirements.txt
```


Run backend server:

```
uvicorn main:app --reload
```


Open the frontend by launching:


login.html


---

## Use Cases

- Automated contract analysis
- Legal document review
- Contract clause identification
- Legal research and education

---

## License

This project is developed for academic and research purposes.
