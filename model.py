import torch
import torch.nn.functional as F
from transformers import BertTokenizer, BertForSequenceClassification
from backend.labels import LABEL_COLUMNS

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BertTokenizer.from_pretrained("legalbert-finetuned")
model = BertForSequenceClassification.from_pretrained(
    "legalbert-finetuned",
    num_labels=len(LABEL_COLUMNS)
).to(device)

model.eval()

THRESHOLD = 0.5

def predict_clauses(sentences):
    results = []

    for sent in sentences:
        inputs = tokenizer(
            sent,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        ).to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.sigmoid(outputs.logits)[0]

        for i, score in enumerate(probs):
            if score.item() >= THRESHOLD:
                results.append({
                    "sentence": sent,
                    "clause": LABEL_COLUMNS[i],
                    "probability": round(score.item(), 4)
                })

    return results
