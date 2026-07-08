from app.core.messages import AgentMessage, Handoff

from app.core.protocol import TaskType

# Supervisor → Research
msg1 = AgentMessage(
    sender="Supervisor",
    receiver="ResearchAgent",
    task=TaskType.RESEARCH,
    payload="What is RAG?"
)

handoff1 = Handoff(
    target_agent="ResearchAgent",
    message=msg1
)

# Research → Writer
msg2 = AgentMessage(
    sender="ResearchAgent",
    receiver="WriterAgent",
    task=TaskType.WRITE_REPORT,
    payload="Research Summary"
)

handoff2 = Handoff(
    target_agent="WriterAgent",
    message=msg2
)

# Writer → Critic
msg3 = AgentMessage(
    sender="WriterAgent",
    receiver="CriticAgent",
    task=TaskType.CRITIQUE,
    payload="Draft Report"
)

handoff3 = Handoff(
    target_agent="CriticAgent",
    message=msg3
)

print(handoff1)
print(handoff2)
print(handoff3)