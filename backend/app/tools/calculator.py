from langchain_core.tools import tool

from app.tools.schemas import CalculatorInput

# WHAT:
# Dedicated calculator tool.

# WHY:
# Each tool lives in its own file for better
# modularity, scalability and maintainability.

@tool(args_schema=CalculatorInput) 
# - decorator to register the function as a tool
# as ReAct agent cannot directly call functions, 
# we need to wrap the function with a tool decorator 
# WHAT:
# Registers the calculator tool with an input schema.
# WHY:
# Before executing the tool, LangChain validates
# the LLM-generated arguments against CalculatorInput.
# Invalid inputs are rejected before the Python function runs
def calculator(expression: str) -> str:
    """
    Evaluate arithmetic and mathematical expressions such as
    addition, subtraction, multiplication, division,
    percentages, parentheses, and decimal calculations.
    """
    return str(eval(expression))