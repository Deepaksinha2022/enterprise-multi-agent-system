from app.graph.state import GraphState

from app.graph.reducers import add_results
# WHAT:
# Creates an initial graph state.

# WHY:
# Every LangGraph execution starts with an initial state.


state: GraphState = {
    "messages": [],
    "task": "",
    "results": [],
    "errors": [],
    "metadata": {}
}

# Node 1 - Planner
state["task"] = "Find HR Leave Policy"

# Node 2 - Retriever
state["results"].append("HR Leave Policy Document")

# Node 3 - Web Search
state["results"].append("Government Leave Rules")

# Node 4 - Validator
state["metadata"]["validated"] = True

# Node 5 - Final LLM
state["messages"].append("Final Answer Generated")

print(state)