from dataclasses import dataclass
from typing import Optional


@dataclass
class FilteringConditionDTO:
    name: str
    min: Optional[float] = None
    max: Optional[float] = None
    equals: Optional[float] = None
