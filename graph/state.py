from typing import TypedDict, List


class ResearchState(TypedDict):
    topic: str
    steps: List[str]
    research: List[str]
    reviews: List[str]
    final_report: str