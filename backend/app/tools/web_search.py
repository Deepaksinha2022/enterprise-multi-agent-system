from langchain_core.tools import tool

from app.tools.schemas import WebSearchInput

import asyncio
# WHAT:
# Async version of the web search tool.

# WHY:
# Real web searches are network operations.
# Async allows the agent to perform other work
# while waiting for the network response.

@tool(args_schema=WebSearchInput)
async def web_search(query: str) -> str:
    """
    Search for factual, current, or external information
    that cannot be reliably answered from the model's
    internal knowledge.
    """
    await asyncio.sleep(2) # simulate a network/API call
    return {
    "query": query,
    "result": "Japanese Yen",
    "source": "Mock Search"
    }
# WHAT:
# Returns structured data instead of plain text.

# WHY:
# Structured outputs are easier for LLMs,
# downstream tools, APIs and UIs to consume

# LLM dont understand python code they use schema,
# tool description,tool name
# exact description lets LLM know when this tool should be
# selected
