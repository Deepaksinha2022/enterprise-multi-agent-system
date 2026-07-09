from app.aggregator.aggregator_agent import AggregatorAgent

agent = AggregatorAgent()

responses = [
    ("RAG uses vector databases.", 0.95),
    ("RAG stores data in SQL only.", 0.45),
    ("RAG combines retrieval with generation.", 0.90),
]

print(agent.aggregate(responses))