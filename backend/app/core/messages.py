from dataclasses import dataclass
# dataclass reduces boilerplate by automatically generating
#  common methods like __init__ and __repr__."

from typing import Any

@dataclass
class AgentMessage:
    sender: str
    receiver: str
    task: str
    payload: Any

# different agents sends different payload so any

@dataclass
class Handoff:
    target_agent: str
    message: AgentMessage

# AgentMessage → Communication data.
# Handoff → Workflow transition.

# handoff increases the cohesion as their is no direct calling
# instead handoff request describes who should execute the
#  next task , doesnt execute anything