from typing import List, Union, Tuple
from typing_extensions import TypedDict
from pydantic import BaseModel

# Base Model
class Query(TypedDict):
    qid: str
    query: str


class Document(TypedDict):
    docno: str
    body: str


class Result(Query):
    docno: str
    score: float


class T5Model(Result):
    rank: int
    text: str


class DocumentText(TypedDict):
    docno: int
    text: str


class ApiResponse(BaseModel):
    result: List
    code: str

# Interactive Feature Props


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


class InteractiveFeatureProps(BaseModel):
    # Array of objects, in Python it's a list of dictionaries
    example: List[dict]
    parameters: List[IParameters]
    input: List[IColumns]
    output: List[IColumns]


class MultiInteractiveFeatureProps(BaseModel):
    options: dict
    parameters: List[IParameters]
