from app.tools.schemas import CalculatorInput


# WHAT:
# Converts the Pydantic model into JSON Schema.

# WHY:
# LangChain internally sends this schema to the LLM so it
# knows what arguments a tool expects.


print(CalculatorInput.model_json_schema())