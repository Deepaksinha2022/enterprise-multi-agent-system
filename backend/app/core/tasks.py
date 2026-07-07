from app.core.celery_app import celery_app

@celery_app.task
def add(x: int, y: int) -> int:
    return x + y

# delay is used to send the task to the broker, 
# which will hold it until a worker picks it up

import asyncio

from app.core.celery_app import celery_app
from app.agents.research_agent import ResearchAgent

@celery_app.task
def run_research(query: str):
    agent = ResearchAgent()
    return asyncio.run(agent.research(query))
