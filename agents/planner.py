from utils.llm import llm
from prompts.planner_prompt import planner_prompt
from schemas.planner_schema import PlannerOutput


class PlannerAgent:

    def __init__(self):
        self.chain = planner_prompt | llm.with_structured_output(PlannerOutput)

    def plan(self, topic):
        return self.chain.invoke(
            {
                "topic": topic
            }
        )