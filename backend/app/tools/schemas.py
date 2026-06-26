from pydantic import BaseModel
# Pydantic is a Python library used for data validation 
# and type enforcement.
# A schema is a blueprint or 
# structure that defines what data is expected.
# WHAT:
# Defines input schemas for every tool.

# WHY:
# Every tool should clearly specify what input it accepts.
# LangChain converts these into JSON Schemas for the LLM.


class CalculatorInput(BaseModel):
    expression: str


class WebSearchInput(BaseModel):
    query: str


class SQLInput(BaseModel):
    query: str


class WeatherInput(BaseModel):
    city: str


class EmailInput(BaseModel):
    recipient: str
    subject: str
    body: str