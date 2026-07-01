from app.supervisor.supervisor import supervisor

from app.supervisor.supervisor import supervisor

tasks = [
    "Write a blog on AI",
    "Generate Python code for BFS",
    "Research LangGraph",
    "Summarize this document",
    "Debug my FastAPI application",
    "Compare AWS and Azure",
    "Write a professional email",
    "Explain reinforcement learning",
    "Implement binary search in Python",
    "Create a project report"
        ]

for task in tasks:
    print(f"Task: {task}")
    print(f"Agent: {supervisor(task)}")
    print("-" * 40)