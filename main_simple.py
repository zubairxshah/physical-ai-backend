from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from pathlib import Path
import json

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# In-memory storage (simple alternative to Qdrant)
documents_store = []

class QueryRequest(BaseModel):
    question: str
    selected_text: str = ""

class QueryResponse(BaseModel):
    answer: str
    sources: list[str] = []

def chunk_text(text: str, chunk_size: int = 1000) -> list[str]:
    """Split text into chunks"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        if chunk.strip():
            chunks.append(chunk.strip())
        start += chunk_size - 200  # 200 char overlap
    return chunks

@app.get("/")
async def root():
    return {"message": "Physical AI Book Backend API", "status": "running"}



@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """Query using simple keyword matching + GPT"""
    try:
        # Build prompt
        system_prompt = """You are an AI assistant for the Physical AI and Humanoid Robotics book. 
Answer questions about physical AI, robotics, humanoid robots, sensors, actuators, AI/ML, computer vision, 
NLP, industrial robotics, service robots, medical robotics, ethics, and future trends. Be concise and helpful."""
        
        user_prompt = request.question
        if request.selected_text:
            user_prompt = f"Selected text: {request.selected_text}\n\nQuestion: {request.question}"
        
        # Get answer from OpenAI
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        answer = response.choices[0].message.content
        
        return QueryResponse(answer=answer, sources=["General Knowledge"])
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok", "documents": len(documents_store)}
