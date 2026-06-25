# WHAT: Builds the LangGraph workflow.
# WHY: Connects nodes together.

from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState
from app.graph.nodes import hello_node

# create a langgraph workflow builder that uses 
# GraphState as the shared state object.
# holdes all nodes,edges and shared state for the workflow.
builder = StateGraph(GraphState)

builder.add_node("hello", hello_node)

builder.add_edge(START, "hello")
builder.add_edge("hello", END)

graph = builder.compile()