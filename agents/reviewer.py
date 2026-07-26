from utils.llm import llm
from prompts.reviewer_prompt import reviewer_prompt
from utils.logger import logger


class ReviewerAgent:

    def __init__(self):

        self.chain = reviewer_prompt | llm

    def review(self, report):

        logger.info("Reviewer Started")

        response = self.chain.invoke(
    {
        "research": report
    }
)

        logger.info("Reviewer Finished")

        return response.content