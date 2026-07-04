from langchain_ollama import ChatOllama

import subprocess

import tempfile

import os

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

CODE_PROMPT = """
You are an expert Python developer.

Generate only executable Python code.

Do not include explanations.
Do not include markdown.
Return only Python code.
"""

DEBUG_PROMPT = """
You are an expert Python debugger.

The following Python program failed.

Fix the code using the error message.

Return only corrected Python code.
"""

def clean_code(code: str):

    return (
        code
        .replace("```python", "")
        .replace("```", "")
        .strip()
    )

async def generate_code(task: str):

    response = await llm.ainvoke(
        CODE_PROMPT +
        "\n\nTask:\n" +
        task
    )

    return response.content.strip()


def execute_code(code: str):

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False
    ) as f:

        f.write(code)

        filename = f.name

    result = subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{filename}:/app/code.py",
            "python:3.11",
            "python",
            "/app/code.py"
        ],
        capture_output=True,
        text=True
    )
    os.remove(filename)

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }


async def debug_code(code: str, error: str):

    response = await llm.ainvoke(
        DEBUG_PROMPT +
        f"""

Code:
{code}

Error:
{error}
"""
    )

    return clean_code(response.content)

async def solve_task(task: str, max_iterations: int = 3):

    code = await generate_code(task)

    for _ in range(max_iterations):

        result = execute_code(code)

        if result["returncode"] == 0:
            return code, result

        code = await debug_code(
            code,
            result["stderr"]
        )

    return code, result