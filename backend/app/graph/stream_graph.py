# WHAT: Executes the graph step by step.

from app.graph.graph import graph

# graph streaming allows you to see the state of
# the graph at each step of execution.

for step in graph.stream(
    {
        "message": ""
    }
):
    print(step)

# graph.invoke() executes the entire workflow and 
# returns only the final state after reaching END. 
# graph.stream() also executes the workflow,
# but returns the output after each node executes, 
# allowing us to observe the state transition step by step 
# for debugging and monitoring.