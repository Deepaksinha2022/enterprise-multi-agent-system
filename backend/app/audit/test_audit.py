import asyncio

# A UUID is a 128-bit globally unique identifier used to 
# uniquely identify an object or request.

import uuid

from datetime import datetime

from app.audit.models import AuditLog

from app.audit.audit_logger import write_audit_log

async def main():

    for i in range(30):

        log = AuditLog(
            user="deepak",
            agent_type="research_agent",
            action=f"web_search_{i}",
            input_hash=f"input_{i}",
            output_hash=f"output_{i}",
            duration=1.2 + i,
            timestamp=datetime.now(),
            trace_id=str(uuid.uuid4())
        )

        await write_audit_log(log)

asyncio.run(main())

# async → defines a coroutine.
# await → executes/waits for another coroutine.
# asyncio.run() → starts the event loop and runs the
# top-level coroutine.
