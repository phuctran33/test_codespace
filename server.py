from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()

# Cho phép frontend gọi API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# HuggingFace model dịch EN -> VI
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-vi")

class TranslateRequest(BaseModel):
    text: str

@app.post("/translate")
def translate(req: TranslateRequest):
    text = (req.text or "").strip()
    if not text:
        return {"error": "Missing text"}

    out = translator(text, max_length=256)
    return {"translated": out[0]["translation_text"]}
