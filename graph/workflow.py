from langgraph.graph import StateGraph, END
from graph.state import ResearchState

from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.reviewer import ReviewerAgent
from agents.writer import WriterAgent

planner = PlannerAgent()
researcher = ResearchAgent()
reviewer = ReviewerAgent()
writer = WriterAgent()


def planner_node(state: ResearchState):
    plan = planner.plan(state["topic"])
    return {"steps": plan.steps}


def researcher_node(state: ResearchState):
    
    reports = []

    topic = state["topic"]

    for step in state["steps"]:

        reports.append(
            researcher.research(
                topic,
                step
            )
        )

    return {
        "research": reports
    }

    for step in state["steps"]:
        reports.append(researcher.research(step))

    return {"research": reports}


def reviewer_node(state: ResearchState):
    reviews = []

    for report in state["research"]:
        reviews.append(reviewer.review(report))

    return {"reviews": reviews}


def writer_node(state: ResearchState):

    research_text = "\n\n".join(state["research"])

    final_report = writer.write(research_text)

    return {"final_report": final_report}


builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("reviewer", reviewer_node)
builder.add_node("writer", writer_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "reviewer")
builder.add_edge("reviewer", "writer")
builder.add_edge("writer", END)

graph = builder.compile()