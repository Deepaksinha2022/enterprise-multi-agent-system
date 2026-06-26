
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv

load_dotenv()
import asyncio

from langchain_core.messages import HumanMessage

from app.tools.registry import TOOLS

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# temperature = 0    → Almost always the same answer ✅
# temperature = 0.5  → Some variation
# temperature = 1.0  → More creative and random
# WHAT:
# Creates a ReAct agent using the LLM and the list 
# of available tools.
# WHY:
# The agent can now reason about a problem,
# decide whether to use
# calculator or web_search, observe the result, 
# and continue until
# it produces the final answer.

agent = create_react_agent(
    model=llm,
    tools=TOOLS
)

# WHAT:
# Async entry point for the agent.

# WHY:
# await can only be used inside an async function.


async def main():
    response = await agent.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content="What is the currency of Japan?"
                )
            ]
        }
    )

    print(response)


asyncio.run(main())

# HumanMessage → User
# AIMessage    → LLM - Thought + Action
# ToolMessage  → Tool - Observation
# SystemMessage→ Instructions to the LLM 
