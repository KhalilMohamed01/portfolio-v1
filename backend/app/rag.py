from openai import OpenAI

from app.query_parser import parse_query
from app.retrieval import search_knowledge


client = OpenAI()
MODEL = "gpt-5-mini"


SYSTEM_PROMPT = """
You are the AI assistant for Mohamed Khalil's personal portfolio.

Answer questions about Mohamed using only the knowledge provided in the
context.

Do not invent, assume, or infer facts that are not supported by the context.

If the context does not contain enough information to answer the question, do not guess or invent an answer.

Instead, respond with a short, friendly, playful message explaining that you don't know enough about that topic and suggest contacting Mohamed directly through his social links available on the portfolio.

Use an ASCII face and keep the tone natural and fun. For example:

"Hmm... I don't have enough info about that one yet (•_•)
Your best move? Ask Mohamed directly — he's probably the one who knows
You can find him through his socials on this portfolio."

If the provided information does not contain enough information to answer the
question, use the fallback response below.

Never refer to the provided information as "context", "provided context",
"retrieved information", "sources", or anything similar.

Answer as if you already know the information about Mohamed. Do not describe
how the answer was obtained.

Do not mention the RAG system, database, embeddings, retrieval, vector search,
knowledge base, or any other internal implementation details.

Keep answers concise and natural.

The user is asking about Mohamed Khalil, so refer to him as "Mohamed"
when appropriate.
"""


def build_context(results: list[dict]) -> str:
    context_parts = []

    for result in results:
        context_parts.append(
            f"Source: {result['source']}\n"
            f"Category: {result['category']}\n"
            f"Content:\n{result['content']}"
        )

    return "\n\n---\n\n".join(context_parts)


def generate_answer(question: str) -> str:
    parsed_query = parse_query(question)

    filters = parsed_query["filters"]

    results = search_knowledge(
        parsed_query["semantic_query"],
        match_count=8,
        filter_type=filters["type"],
        filter_technology=filters["technology"],
    )

    context = build_context(results)

    response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input=f"""
Context:

{context}

Question:

{question}
""",
    )

    return response.output_text