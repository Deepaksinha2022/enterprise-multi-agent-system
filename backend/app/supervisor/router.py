RESEARCH_AGENT = "research_agent"
WRITER_AGENT = "writer_agent"
CODE_AGENT = "code_agent"

def route_task(task: str):

    task = task.lower()

    if "code" in task:
        return CODE_AGENT

    if "write" in task:
        return WRITER_AGENT

    return RESEARCH_AGENT