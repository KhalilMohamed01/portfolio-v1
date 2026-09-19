from openai import OpenAI

from app.supabase_client import supabase


client = OpenAI()

EMBEDDING_MODEL = "text-embedding-3-small"


def search_knowledge(
    query: str,
    match_count: int = 20,
    filter_type: str | None = None,
    filter_technology: str | None = None,
) -> list[dict]:
    embedding_response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query,
    )

    query_embedding = embedding_response.data[0].embedding

    response = supabase.rpc(
        "match_knowledge_chunks",
        {
            "query_embedding": query_embedding,
            "match_count": match_count,
            "filter_type": filter_type,
            "filter_technology": filter_technology,
        },
    ).execute()

    return response.data