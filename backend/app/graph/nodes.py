# WHAT: A node performs one task and updates the state.

from app.graph.state import GraphState

from langgraph.types import interrupt

# interrupt stop execution here. Save the current checkpoint
# Return control to the caller
def hello_node(state: GraphState) -> GraphState:

    resume_value = interrupt("Paused after hello node.")

    print(f">>> Resumed with: {resume_value}")

    return state

def second_node(state:GraphState) -> GraphState:
   
   print("Second node executed")

   return state