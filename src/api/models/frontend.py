"""
Models for generating front end components.
"""
from typing import List, Union

from pydantic import BaseModel


# Interfaces
class IColumns(BaseModel):
    name: str
    width: int = None  # Optional, defaults to None if not provided


class IParameters(BaseModel):
    name: str
    id: str
    type: str
    choices: List[str] = None  # Optional, defaults to None if not provided
    default: Union[str, int, float]  # Can be either string or integer or float
    read_only: bool = False


# Props
class InteractiveFeatureProps(BaseModel):
    example: List[dict]
    parameters: List[IParameters]
    input: List[IColumns]
    output: List[IColumns]


class MultiInteractiveFeatureProps(BaseModel):
    options: dict
    parameters: List[IParameters]


# Respond
class ApiResponse(BaseModel):
    result: List
    code: str
