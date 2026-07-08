from enum import Enum
# enum restricts value to a predefined set
# An Enum is a collection of named constant values that restricts
# a variable to a predefined set of valid options.

class TaskType(str, Enum):
    RESEARCH = "research"
    WRITE_REPORT = "write_report"
    CRITIQUE = "critique"
    REFINE = "refine"
    GENERATE_CODE = "generate_code"