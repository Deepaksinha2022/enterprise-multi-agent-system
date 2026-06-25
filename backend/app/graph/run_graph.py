# WHAT: Executes the graph.

from app.graph.graph import graph

result = graph.invoke(
    {
        "message": ""
    }
)

print(result)

# # flow
# graph.invoke() receives the initial state.
# The compiled graph starts execution from START.
# The state is passed to the first node (hello_node).
# The node performs its task, updates the state, and returns it.
# LangGraph follows the defined edges to the next node (or END).
# When END is reached, invoke() returns the final updated state.