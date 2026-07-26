from utils.llm import llm
from prompts.writer_prompt import writer_prompt
from utils.logger import logger


class WriterAgent:

    def __init__(self):

        self.chain = writer_prompt | llm

    def write(self, research):

        logger.info("Writer Started")

        response = self.chain.invoke(
            {
                "research": research
            }
        )

        logger.info("Writer Finished")

        return response.content