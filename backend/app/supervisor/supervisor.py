from app.supervisor.router import route_task

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

SUPERVISOR_PROMPT = """
You are a supervisor responsible for routing user tasks.

Choose exactly one agent.

research_agent:
- factual questions
- web search
- research
- information gathering

writer_agent:
- blogs
- emails
- essays
- reports
- summaries
- rewriting

code_agent:
- programming
- debugging
- algorithms
- code generation

Decision Rules:

- If the user is asking for information, explanations, facts, comparisons, or research, use research_agent.
- If the user is asking to write content such as blogs, emails, reports, or summaries, use writer_agent.
- If the user is asking to generate, debug, or explain source code or algorithms, use code_agent.
- - If the user asks to explain, teach, define, compare, research, or answer questions about a topic, use research_agent.
Return only one of:

research_agent
writer_agent
code_agent

Do not explain your answer.
"""

def supervisor(task: str):

    response = llm.invoke(
    SUPERVISOR_PROMPT + "\n\nTask: " + task
    )

    agent = response.content.strip()

    if agent not in [
        "research_agent",
        "writer_agent",
        "code_agent"
    ]:
        return route_task(task)

    return agent