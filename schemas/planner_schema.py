from pydantic import BaseModel
from typing import List


class PlannerOutput(BaseModel):
    steps: List[str]