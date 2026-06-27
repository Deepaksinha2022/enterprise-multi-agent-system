from copy import deepcopy

# deepcopy creates a new copy pointing to different
# memory location
# It is for ensuring that while execution is happening,
# no node accidentally 
# changes the state that another node is reading.

state = {
    "results": ["Doc1"]
}

new_state = deepcopy(state)

new_state["results"].append("Doc2")

print("Original:", state)
print("Copy:", new_state)