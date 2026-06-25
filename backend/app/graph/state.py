# WHAT: Shared data passed between all nodes.
# WHY: Every node reads and updates this state.

from typing import TypedDict
 # typing → Python module used for type hints.
 # TypedDict → Defines the expected structure of a dictionary.
 # GraphState → Your project's shared state 
 # object that is passed between LangGraph nodes.

class GraphState(TypedDict):
    message: str

# ypedDict defines the expected structure and 
# data types of the shared state. GraphState is
# our TypedDict that is passed between nodes.
# Although a normal dictionary can be used,
# TypedDict provides type safety, catches key typos,
# and makes the shared state easier to maintain in 
# large workflows.