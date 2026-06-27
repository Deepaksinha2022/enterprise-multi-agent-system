from copy import deepcopy


# WHAT:
# Verify that each node works on an independent copy.

# WHY:
# Ensure no mutation bugs occur.


initial_state = {
    "results": []
}

# Node 1
state1 = deepcopy(initial_state)
state1["results"].append("Planner")

# Node 2
state2 = deepcopy(state1)
state2["results"].append("Retriever")

# Node 3
state3 = deepcopy(state2)
state3["results"].append("Web Search")

# Node 4
state4 = deepcopy(state3)
state4["results"].append("Validator")

# Node 5
state5 = deepcopy(state4)
state5["results"].append("LLM")

print("Initial :", initial_state)
print("Node1   :", state1)
print("Node2   :", state2)
print("Node3   :", state3)
print("Node4   :", state4)
print("Node5   :", state5)