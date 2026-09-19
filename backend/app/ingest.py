from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from app.supabase_client import supabase


load_dotenv()

client = OpenAI()


KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

EMBEDDING_MODEL = "text-embedding-3-small"
CHUNK_SIZE = 1500


def split_into_chunks(text: str, chunk_size: int = CHUNK_SIZE) -> list[str]:
    """
    Split Markdown into meaningful chunks while preserving heading hierarchy.

    Each chunk includes the headings that define its context.
    Large sections are further split by paragraphs.
    """

    lines = text.splitlines()

    chunks: list[str] = []

    # Stores the current heading for each Markdown level.
    # Example:
    # {
    #     1: "# SAD Marketing",
    #     2: "## Final-Year Engineering Internship",
    #     3: "### Project",
    # }
    heading_stack: dict[int, str] = {}

    current_body: list[str] = []

    def get_heading_context() -> str:
        """Return the current heading hierarchy."""
        return "\n\n".join(
            heading_stack[level]
            for level in sorted(heading_stack)
        )

    def flush_body() -> None:
        """Turn the current body into one or more chunks."""
        nonlocal current_body

        body = "\n".join(current_body).strip()

        if not body:
            current_body = []
            return

        context = get_heading_context()

        paragraphs = [
            paragraph.strip()
            for paragraph in body.split("\n\n")
            if paragraph.strip()
        ]

        current_chunk = context

        for paragraph in paragraphs:
            candidate = (
                f"{current_chunk}\n\n{paragraph}"
                if current_chunk
                else paragraph
            )

            if len(candidate) <= chunk_size:
                current_chunk = candidate
            else:
                if current_chunk:
                    chunks.append(current_chunk)

                current_chunk = (
                    f"{context}\n\n{paragraph}"
                    if context
                    else paragraph
                )

        if current_chunk:
            chunks.append(current_chunk)

        current_body = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#"):
            # Finish the content belonging to the previous heading.
            flush_body()

            # Determine heading level.
            level = len(stripped) - len(stripped.lstrip("#"))

            # Remove deeper heading levels.
            heading_stack = {
                existing_level: heading
                for existing_level, heading in heading_stack.items()
                if existing_level < level
            }

            # Add the new heading.
            heading_stack[level] = stripped

        else:
            current_body.append(line)

    # Flush the final content.
    flush_body()

    return chunks

def create_embedding(text: str) -> list[float]:
    """Create an embedding for a knowledge chunk."""

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )

    return response.data[0].embedding


def ingest_file(file_path: Path) -> None:
    """Ingest one Markdown file into Supabase."""

    source = file_path.name
    category = file_path.stem

    print(f"Processing {source}...")

    content = file_path.read_text(encoding="utf-8")

    chunks = split_into_chunks(content)

    print(f"  Found {len(chunks)} chunks")

    # Remove existing chunks belonging to this file.
    supabase.table("knowledge_chunks").delete().eq(
        "source",
        source,
    ).execute()

    print("  Removed previous chunks")

    for index, chunk in enumerate(chunks, start=1):
        embedding = create_embedding(chunk)

        supabase.table("knowledge_chunks").insert(
            {
                "content": chunk,
                "embedding": embedding,
                "source": source,
                "category": category,
                "metadata": {
                    "chunk_index": index,
                },
            }
        ).execute()

        print(f"  Inserted chunk {index}/{len(chunks)}")


def main() -> None:
    """Ingest every Markdown knowledge file."""

    files = sorted(KNOWLEDGE_DIR.glob("*.md"))

    if not files:
        raise RuntimeError("No Markdown files found.")

    print(f"Found {len(files)} knowledge files")

    for file_path in files:
        ingest_file(file_path)

    print("Ingestion complete.")


if __name__ == "__main__":
    main()