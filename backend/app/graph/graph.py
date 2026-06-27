# WHAT: Builds the LangGraph workflow.
# WHY: Connects nodes together.

from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState

from app.graph.nodes import hello_node,second_node


def build_graph(checkpointer=None):
    
    builder = StateGraph(GraphState)

    builder.add_node("hello", hello_node)

    builder.add_node("second", second_node)

    builder.add_edge(START, "hello")

    builder.add_edge("hello", "second")

    builder.add_edge("second", END)

    return builder.compile(
        checkpointer=checkpointer
    )

# WHAT:
# Compile the graph with checkpoint support.

# WHY:
# Enables LangGraph to automatically save and restore state.
