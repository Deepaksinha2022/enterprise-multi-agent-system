from app.tools.calculator import calculator
from app.tools.web_search import web_search

# WHAT:
# Central registry of all tools.

# WHY:
# Provides one place to register enterprise tools.

TOOLS = [
    calculator,
    web_search,
]