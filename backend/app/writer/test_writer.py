from app.writer.writer_agent import (
    write_report,
    reflect_report
)

research_tasks = [
    """
    LangGraph is a framework for building stateful multi-agent AI applications.
    It supports checkpoints, memory, human-in-the-loop, and agent orchestration.
    """,

    """
    Retrieval-Augmented Generation (RAG) combines information retrieval with
    large language models to improve factual accuracy by retrieving relevant
    documents before generation.
    """,

    """
    Redis is an in-memory data store used for caching, session management,
    pub/sub messaging, and fast key-value storage.
    """
]

for i, research in enumerate(research_tasks, 1):

    print("=" * 60)
    print(f"TASK {i}")

    draft = write_report(research)
    refined = reflect_report(research)

    print("\n----- DRAFT -----")
    print(draft)

    print("\n----- REFINED -----")
    print(refined)

    print("\nQuality Score")
    print("Draft   : ____ /10")
    print("Refined : ____ /10")