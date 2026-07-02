from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

WRITER_PROMPT = """
You are a professional technical writer.

Your task is to convert the research into a clear, well-structured report.

Structure:

1. Title
2. Executive Summary
3. Main Findings
4. Conclusion

Use clear and concise language.
"""

def write_report(research_output: str):

    response = llm.invoke(
        WRITER_PROMPT +
        "\n\nResearch:\n" +
        research_output
    )

    return response.content.strip()


REFLECTION_PROMPT = """
Review the report for:

- factual correctness
- clarity
- completeness
- structure

Do not introduce new facts.
Do not invent information.
Only improve the wording, organization, and clarity using the provided report.
Suggest improvements only.
"""

def critique_report(report: str):

    response = llm.invoke(
        REFLECTION_PROMPT +
        "\n\nReport:\n" +
        report
    )

    return response.content.strip()


def refine_report(report: str, critique: str):

    response = llm.invoke(
        f"""
Improve the following report using the review comments.

Report:
{report}

Review:
{critique}

Return only the improved report.
"""
    )

    return response.content.strip()


def reflect_report(research_output: str):

    draft = write_report(research_output)

    critique = critique_report(draft)

    refined = refine_report(
        draft,
        critique
    )

    return refined

