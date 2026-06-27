from copy import deepcopy


# WHAT:
# Demonstrates how deepcopy prevents mutation bugs.

# WHY:
# Each node gets its own independent copy of the state.


state = {
    "results": ["Doc1"]
}

node_a_state = deepcopy(state)
node_b_state = deepcopy(state)

node_a_state["results"].append("Planner Output")

print("Node A:", node_a_state)
print("Node B:", node_b_state)
print("Original:", state)