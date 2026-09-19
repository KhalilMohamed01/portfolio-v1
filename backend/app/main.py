import os
from fastapi import FastAPI
from dotenv import load_dotenv
from openai import OpenAI
from app.supabase_client import supabase
from app.retrieval import search_knowledge
from app.rag import generate_answer
from app.query_parser import parse_query

load_dotenv()


app = FastAPI(title="Medk Portfolio API")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/test-supabase")
def test_supabase():
    response = (
        supabase
        .table("knowledge_chunks")
        .select("id")
        .limit(1)
        .execute()
    )

    return {
        "connected": True,
        "rows": response.data,
    }

@app.get("/api/test-retrieval")
def test_retrieval(q: str):
    results = search_knowledge(q, match_count=20)
    return {"results": results}

@app.get("/api/test-query-parser")
def test_query_parser(q: str):
    return parse_query(q)

@app.get("/api/ask")
def ask(q: str):
    answer = generate_answer(q)

    return {
        "question": q,
        "answer": answer,
    }