from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional


class Scatter(BaseModel):
    x: List[float]|float = Field(..., description="A list of floats")
    y: List[float]|float = Field(..., description="A list of floats")
    s: Optional[List[float]] = Field(default=None, description="A value")

    # class InpModel(BaseModel):
    #     x: List[float] = Field(..., description="A list of floats")
    #     y: List[int] = Field(..., description="A list of integers")
    #
    # inp: InpModel = Field(..., description="An object with x and y fields")
    # bobi: str = Field(..., description="A string field")