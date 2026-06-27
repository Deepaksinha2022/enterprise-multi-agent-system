# WHAT: Shared data passed between all nodes.
# WHY: Every node reads and updates this state.

from typing import TypedDict

from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from app.graph.reducers import add_results


 # typing → Python module used for type hints.
 # TypedDict → Defines the expected structure of a dictionary.
 # GraphState → Your project's shared state 
 # object that is passed between LangGraph nodes.

# WHAT:
# Defines the complete shared state for our graph.

# WHY:
# Every node will read and update this state.

class GraphState(TypedDict):
    messages: Annotated[list, add_messages]
    task: str
    results: Annotated[list,add_results]
    errors: list
    metadata: dict

# ypedDict defines the expected structure and 
# data types of the shared state. GraphState is
# our TypedDict that is passed between nodes.
# Although a normal dictionary can be used,
# TypedDict provides type safety, catches key typos,
# and makes the shared state easier to maintain in 
# large workflows.