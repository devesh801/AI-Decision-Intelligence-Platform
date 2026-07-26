from utils.llm import llm
from prompts.researcher_prompt import researcher_prompt
from tools.search_tool import search_web
from utils.logger import logger


class ResearchAgent:

    def __init__(self):

        self.chain = researcher_prompt | llm

    def research(self, topic, section):

        logger.info(f"Research Started : {section}")

        # Create a focused search query
        query = f"{section} about {topic}"

        search_results = search_web(query)

        context = ""

        for item in search_results:
            context += item["content"] + "\n\n"

        response = self.chain.invoke(
            {
                "topic": topic,
                "section": section,
                "context": context
            }
        )

        logger.info(f"Research Finished : {section}")

        return response.content