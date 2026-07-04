import asyncio
import time

from app.supervisor.supervisor import execute_parallel

from app.agents.research_agent import ResearchAgent

from app.code.code_agent import solve_task

research_agent = ResearchAgent()


async def serial(task):

    research = await research_agent.research(task)

    code = await solve_task(task)

    return research, code


async def benchmark():

    task = "Explain LangGraph and write Python code to implement BFS."

    start = time.perf_counter()

    await serial(task)

    serial_time = time.perf_counter() - start

    start = time.perf_counter()

    await execute_parallel(task)

    parallel_time = time.perf_counter() - start

    print(f"Serial   : {serial_time:.2f} sec")
    print(f"Parallel : {parallel_time:.2f} sec")


asyncio.run(benchmark())