from typing import Any

# WHAT:
# Custom reducer for the results field.

# WHY:
# Instead of replacing the previous list,
# merge new results into the existing list.


def add_results(existing: list[Any], new: list[Any]) -> list[Any]:
    return existing + new