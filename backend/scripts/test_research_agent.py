from app.agents.research_agent import ResearchAgent

agent = ResearchAgent()

topics = [
    "Latest AI trends",
    "Quantum Computing",
    "Climate Change",
    "Electric Vehicles",
    "SpaceX Starship"
]

for topic in topics:
    print(f"\n{'='*60}")
    print(f"Topic: {topic}")

    result = agent.research(topic)

    print(f"Summary Length: {len(result['summary'])}")
    print(f"Sources Returned: {len(result['sources'])}")