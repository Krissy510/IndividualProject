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

class Bo1Request(IRequest):
    input: List[Result]
    fb_terms: int
    fb_docs: int

class KLRequest(Bo1Request):
    pass

class RM3Request(Bo1Request):
    fb_lambda: float

# Result Model

class TextSlidingResult(Document):
    pass

class TextScorerResult(Result):
    rank: int

class MaxPassageResult(TextScorerResult):
    pass

class SequentialDependenceResult(Query):
    query_0: str

class Bo1Result(SequentialDependenceResult):
    pass

class KLResult(Bo1Result):
    pass

class RM3Result(KLResult):
    pass

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


class InteractiveFeatureProps(BaseModel):
    example: List[dict]  # Array of objects, in Python it's a list of dictionaries
    defaultDisplayMode: str = None  # Optional, defaults to None if not provided
    parameters: List[IParameters]
    input: List[IColumns]
    output: List[IColumns]


    