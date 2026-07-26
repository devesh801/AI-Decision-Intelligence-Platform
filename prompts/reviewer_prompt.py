from langchain_core.prompts import ChatPromptTemplate

reviewer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior Research Reviewer.

Your job is to review the research provided by the researcher.

Check the following:
1. Accuracy
2. Completeness
3. Clarity
4. Missing Information
5. Suggestions for Improvement

Finally, provide an overall score out of 10.
"""
        ),
        (
            "human",
            "{research}"
        )
    ]
)