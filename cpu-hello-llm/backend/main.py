from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="CPU Hello LLM", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    # CPU-only "toy" model: transform prompt deterministically
    text = req.prompt.strip()
    if not text:
        return {"reply": "Please provide a prompt."}
    # simple pretend "generation": title-case + add a suffix
    reply = text.capitalize() + " — acknowledged (CPU demo)."
    return {"reply": reply}
