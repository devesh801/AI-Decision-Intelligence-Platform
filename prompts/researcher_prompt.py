from langchain_core.prompts import ChatPromptTemplate

researcher_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert research analyst.

Your task is to write ONLY the requested section of the research report.

Rules:
- Focus only on the given section.
- Use the provided web information as the primary source.
- Stay strictly related to the main topic.
- Do not include information unrelated to the topic.
- Write in a professional and factual style.
- Do not repeat content from other sections.
- Use clear paragraphs and headings.
"""
        ),
        (
            "human",
            """
Main Topic:
{topic}

Research Section:
{section}

Web Information:
{context}

Write a detailed section only for:
{section}
"""
        )
    ]
)