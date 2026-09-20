from pathlib import Path

import yaml
from dotenv import load_dotenv
from openai import OpenAI

from app.supabase_client import supabase


load_dotenv()

client = OpenAI()


KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

EMBEDDING_MODEL = "text-embedding-3-small"
CHUNK_SIZE = 1500


def split_into_entries(text: str) -> list[tuple[dict, str]]:
    """
    Split a Markdown document into top-level sections.

    A section starts with a level-1 Markdown heading.
    A YAML metadata block inside that section identifies
    it as a structured knowledge entry.

    Sections without metadata are still preserved as
    document-level content.
    """

    lines = text.splitlines()

    sections: list[tuple[dict, str]] = []

    current_content: list[str] = []
    current_metadata: dict = {}

    def flush_section() -> None:
        nonlocal current_content
        nonlocal current_metadata

        content = "\n".join(current_content).strip()

        if content:
            sections.append(
                (
                    current_metadata,
                    content,
                )
            )

        current_content = []
        current_metadata = {}

    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        # A level-1 heading starts a new section.
        if stripped.startswith("# ") and not stripped.startswith("## "):
            flush_section()

            current_content = [line]

            index += 1
            continue

        # YAML metadata block.
        if stripped == "```yaml":
            yaml_lines: list[str] = []

            index += 1

            while index < len(lines):
                yaml_line = lines[index]

                if yaml_line.strip() == "```":
                    break

                yaml_lines.append(yaml_line)
                index += 1

            metadata = yaml.safe_load("\n".join(yaml_lines))

            if not isinstance(metadata, dict):
                raise ValueError(
                    "YAML metadata must contain a mapping/object."
                )

            current_metadata = metadata

            index += 1
            continue

        current_content.append(line)

        index += 1

    flush_section()

    return sections
def split_into_chunks(
    text: str,
    chunk_size: int = CHUNK_SIZE,
) -> list[str]:
    """
    Split Markdown into meaningful chunks while preserving heading hierarchy.

    Each chunk includes the headings that define its context.
    Large sections are further split by paragraphs.
    """

    lines = text.splitlines()

    chunks: list[str] = []

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
            flush_body()

            level = len(stripped) - len(stripped.lstrip("#"))

            heading_stack = {
                existing_level: heading
                for existing_level, heading in heading_stack.items()
                if existing_level < level
            }

            heading_stack[level] = stripped

        else:
            current_body.append(line)

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
    """Ingest one Markdown knowledge file into Supabase."""

    source = file_path.name
    category = file_path.stem

    print(f"Processing {source}...")

    content = file_path.read_text(encoding="utf-8")

    entries = split_into_entries(content)

    print(f"  Found {len(entries)} entries")

    # Remove existing chunks belonging to this file.
    supabase.table("knowledge_chunks").delete().eq(
        "source",
        source,
    ).execute()

    print("  Removed previous chunks")

    total_chunks = 0

    for entry_index, (metadata, entry_content) in enumerate(
        entries,
        start=1,
    ):
        chunks = split_into_chunks(entry_content)

        print(
            f"  Entry {entry_index}: "
            f"{metadata.get('name', metadata.get('degree', 'unnamed'))}"
            f" → {len(chunks)} chunks"
        )

        for chunk_index, chunk in enumerate(chunks, start=1):
            embedding = create_embedding(chunk)

            chunk_metadata = {
                **metadata,
                "entry_index": entry_index,
                "chunk_index": chunk_index,
            }

            supabase.table("knowledge_chunks").insert(
                {
                    "content": chunk,
                    "embedding": embedding,
                    "source": source,
                    "category": category,
                    "metadata": chunk_metadata,
                }
            ).execute()

            total_chunks += 1

            print(
                f"    Inserted chunk "
                f"{chunk_index}/{len(chunks)}"
            )

    print(f"  Inserted {total_chunks} chunks total")


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