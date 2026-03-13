import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from nltk.tokenize import sent_tokenize
import numpy as np

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 🔁 UPDATE THIS PATH TO YOUR FINETUNED MODEL
MODEL_PATH = "legalbert-finetuned"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.to(DEVICE)
model.eval()

# 🔁 MUST MATCH YOUR TRAINING
LABELS = [
    "Governing Law",
    "Termination",
    "Confidentiality",
    "Limitation Of Liability",
    "License Grant",
    "Non-Compete",
    "Assignment",
    "IP Ownership",
    "Payment Terms"
]

THRESHOLD = 0.5  # you can tune this later

def identify_clauses(text: str):
    sentences = sent_tokenize(text)
    results = []

    for sent in sentences:
        inputs = tokenizer(
            sent,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        )

        inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.sigmoid(outputs.logits).cpu().numpy()[0]

        for i, prob in enumerate(probs):
            if prob >= THRESHOLD:
                results.append({
                    "sentence": sent,
                    "clause": LABELS[i],
                    "confidence": round(float(prob), 3)
                })

    return results
