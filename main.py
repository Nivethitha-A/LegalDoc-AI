import os
from fastapi import FastAPI, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware

from backend.utils.pdf_reader import extract_text_from_pdf
from backend.models.clause_identifier import identify_clauses

# 🔐 import auth router + dependency
from backend.auth import router as auth_router, get_current_user

app = FastAPI()   # ✅ app MUST be defined FIRST

# ✅ Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ include auth routes AFTER app is created
app.include_router(auth_router)

os.makedirs("data", exist_ok=True)

@app.post("/analyze/")
async def analyze_pdf(
    file: UploadFile,
    user: str = Depends(get_current_user)
):
    pdf_path = os.path.join("data", file.filename)

    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(pdf_path)
    results = identify_clauses(text)

    return {
        "total_clauses_found": len(results),
        "clauses": results
    }
