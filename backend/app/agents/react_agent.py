from langchain_core.tools import tool

from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv

load_dotenv()

# Loads all environment variables from the .env file.
# Makes GROQ_API_KEY available to ChatGroq automatically.

# why tool - as a ReACt agent cannot itself perform calculations
@tool # - decorator to register the function as a tool
# as ReAct agent cannot directly call functions, 
# we need to wrap the function with a tool decorator 
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """
    return str(eval(expression))

# Second tool for web search
@tool
def web_search(query: str) -> str:
    """
    Mock web search.
    """
    return f"Search results for: {query}"

# LLM model will act as a brain of agent
# it decides whether to answer directly or call one of tools
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# temperature = 0    → Almost always the same answer ✅
# temperature = 0.5  → Some variation
# temperature = 1.0  → More creative and random

## WHAT:
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
    tools=[calculator, web_search]
)

from langchain_core.messages import HumanMessage

# invoke() executes the entire agent or graph.
response = agent.invoke(
    {
        "messages": [
            HumanMessage(
    content="Search for the currency of Japan and calculate (250 + 350) / 2."
        )
        ]
    }
)

print(response)

# HumanMessage → User
# AIMessage    → LLM - Thought + Action
# ToolMessage  → Tool - Observation
# SystemMessage→ Instructions to the LLM 