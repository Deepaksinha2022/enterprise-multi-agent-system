from pydantic import BaseModel
from datetime import datetime


class AuditLog(BaseModel):
    user: str
    agent_type: str
    action: str
    input_hash: str  # cryptograpy- dont store original 
                     # user's message privacy, store fingerprint
    output_hash: str # hash the LLM response
    duration: float  # time taken by the action - monitoring
    timestamp: datetime
    trace_id:str