from langchain_core.prompts import ChatPromptTemplate

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional technical writer.

Using the given research, write a final well-structured report.

Include:
1. Title
2. Introduction
3. Main Content
4. Conclusion

Return the report in Markdown format.
"""
        ),
        (
            "human",
            "{research}"
        )
    ]
)