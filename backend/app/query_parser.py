import json

from openai import OpenAI


client = OpenAI()

MODEL = "gpt-5-mini"


SYSTEM_PROMPT = """
You are a query parser for a personal portfolio knowledge base.

Your job is to analyze the user's question and extract structured filters
that can be used to retrieve relevant knowledge.

Supported filter types:

- profile
- education
- experience
- project

Supported filters:

- type
- technology
- company
- institution

Return ONLY valid JSON with this exact structure:

{
  "semantic_query": "string",
  "filters": {
    "type": null,
    "technology": null,
    "company": null,
    "institution": null,
    "year": null
  }
}

Rules:

- semantic_query should preserve the meaning of the user's question.
- Only set a filter when the question clearly asks for it.
- Use null when a filter is not applicable.
- For "projects", use type = "project".
- Only set type = "project" when the user explicitly asks about projects.
- Only set type = "experience" when the user explicitly asks about professional
  experience, work experience, jobs, internships, or employment.
- If the user asks whether Mohamed has experience with a technology, do not
  assume they mean professional experience. Search across projects and
  experiences unless the question explicitly specifies one.
- For education-related questions, use type = "education".
- For questions about Mohamed generally, do not automatically set type.
- Extract technologies such as Spring Boot, React, Vue.js, Python, etc.
- Do not invent technologies, companies, or institutions.
- Keep technology names as they appear in the question when possible.\
- If the user asks about a specific calendar year, extract that year as an integer.
- For example, "Where did Mohamed work in 2024?" should produce year = 2024.
- Only extract a year when the question clearly refers to that calendar year.
"""


def parse_query(query: str) -> dict:
    response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input=query,
    )

    return json.loads(response.output_text)