from langgraph.checkpoint.sqlite import SqliteSaver

from app.graph.graph import build_graph

from langgraph.types import Command

with SqliteSaver.from_conn_string("checkpoints.db") as checkpointer:

    graph = build_graph(
        checkpointer
    )

    config = {
        "configurable": {
            "thread_id": "kill-demo"
        }
    }

    result = graph.invoke(
    Command(resume="approved"),
    config=config,
    )

    # What is Command?
    # Command is a special instruction sent to LangGraph.

print(result)