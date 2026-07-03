from app.code.code_agent import (
    solve_task
)

task = """
Write a Python function to divide two numbers.
The function should print the result.
Intentionally make a mistake in the code.
"""

code, result = solve_task(task)

print("========== FINAL CODE ==========")
print(code)

print("\n========== STDOUT ==========")
print(result["stdout"])

print("\n========== STDERR ==========")
print(result["stderr"])

print("\n========== RETURN CODE ==========")
print(result["returncode"])