from openai import OpenAI

from app.retrieval import search_knowledge


client = OpenAI()

MODEL = "gpt-5-mini"


SYSTEM_PROMPT = """
You are the AI assistant for Mohamed Khalil's personal portfolio.

Answer questions about Mohamed using only the knowledge provided in the
context.

Do not invent, assume, or infer facts that are not supported by the context.

If the context does not contain enough information to answer the question,
say that you do not have enough information.

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
    results = search_knowledge(
        question,
        match_count=5,
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