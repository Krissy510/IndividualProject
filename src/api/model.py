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


# Request Model
class IRequest(BaseModel):
    input: List[TypedDict]

class RetrieveRequest(IRequest):
    dataset: str
    wmodel: str
    index_variant: str
    num_results: int
    input: List[Query]


class TextSlidingRequest(IRequest):
    num_results: int
    length: int
    stride: int
    input: List[Document]


class TextScorerRequest(IRequest):
    wmodel: str
    input: List[TextScorerInput]

class MaxPassageRequest(IRequest):
    input: List[Result]

class SequentialDependenceRequest(IRequest):
    input: List[Query]


# Result Model
class TextSlidingResult(Document):
    pass

class TextScorerResult(Result):
    rank: int

class MaxPassageResult(TextScorerResult):
    pass

class SequentialDependenceResult(Query):
    query_0: str


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


    