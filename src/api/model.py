from typing import List, TypedDict, Union, Tuple
from pydantic import BaseModel
    
# Common Data Model
class Query(TypedDict):
    qid: str
    query: str


class Document(TypedDict):
    docno: str
    body: str


class Result(Query):
    docno: str
    score: float


# Input model
class TextScorerInput(Query,Document):
    pass

class MaxPassageInput(Result,Document):
    pass


# Request Model
class IRequest(BaseModel):
    input: List[TypedDict]

class RetrieveRequest(IRequest):
    dataset: str
    wmodel: str
    index_variant: str
    num_results: int
    input: List[Query]


class TextSlidingRequest(BaseModel):
    num_results: int
    length: int
    stride: int
    input: List[Document]


class TextScorerRequest(TextSlidingRequest):
    wmodel: str
    input: List[TextScorerInput]


class MaxPassageRequest(BaseModel):
    num_results: int
    input: List[MaxPassageInput]


# Result Model
class TextSlidingResult(Document):
    Index: int


class TextScorerResult(Result,Document):
    rank: int


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
    parameters: List[IParameters]
    input: List[IColumns]
    output: List[IColumns]


    