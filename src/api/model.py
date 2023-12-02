from typing import List, TypedDict, Union, Tuple
from pydantic import BaseModel
    
# Common Data Model
class Query(TypedDict):
    qid: str
    query: str


class Document(TypedDict):
    docno: str
    body: str


class Result(TypedDict):
    qid: str
    query: str
    docno: str
    score: float


# Input model
class MaxPassageInput(Result):
    qid: str


# Request Model
class IRequest(BaseModel):
    input: Tuple[TypedDict]

class RetrieveRequest(IRequest):
    dataset: str
    wmodel: str
    index_variant: str
    num_results: int | None = 10
    input: List[Query]


class TextSlidingRequest(BaseModel):
    num_results: int | None = 10
    length: int | None = 150
    stride: int | None = 75
    input: Tuple[Document]


class MaxPassageRequest(BaseModel):
    num_results: int | None = 10
    input: List[MaxPassageInput]


# Result Model
class TextSlidingResult(TypedDict):
    Index: int
    docno: str
    body: str


class MaxPassageResult(TypedDict):
    qid: str
    query: str
    body: str
    score: float
    docno: str
    rank: int


# Interactive Feature Props
class IColumns(BaseModel):
    name: str
    width: int = None  # Optional, defaults to None if not provided


class IParameters(BaseModel):
    name: str
    id: str
    type: str
    choices: List[str] = None  # Optional, defaults to None if not provided
    default: Union[str, int]  # Can be either string or integer


class InteractiveFeatureProps(BaseModel):
    example: List[dict]  # Array of objects, in Python it's a list of dictionaries
    defaultDisplayMode: str = None  # Optional, defaults to None if not provided
    columns: List[IColumns]
    parameters: List[IParameters]