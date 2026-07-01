from app.audit.models import AuditLog

import json

# Making the function asynchronous prevents blocking the request
# while waiting for I/O.
async def write_audit_log(log: AuditLog):
    with open(
        "audit.log",
        "a"
    ) as f:

        f.write(
            json.dumps(
                log.model_dump(),
                default=str
            )
            + "\n"
        )

# model_dump() converts a Pydantic model into a Python dict.
# json.dumps work with dict not python object