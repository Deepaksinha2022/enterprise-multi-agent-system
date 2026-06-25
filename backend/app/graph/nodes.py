# WHAT: A node performs one task and updates the state.

from app.graph.state import GraphState

def hello_node(state: GraphState) -> GraphState:
    # state: GraphState → indicates the function 
    # takes a GraphState object as input.
    # -> indicates the function returns a GraphState object.
    state["message"] = "Hello Langgraph!"
    return state