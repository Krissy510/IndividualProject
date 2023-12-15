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

class QueryExpanssionRequest(IRequest):
    input: List[Result]
    fb_terms: int
    fb_docs: int

class Bo1Request(QueryExpanssionRequest):
    pass

class KLRequest(QueryExpanssionRequest):
    pass

class RM3Request(QueryExpanssionRequest):
    fb_lambda: float

class AxiomaticRequest(QueryExpanssionRequest):
    fb_lambda: float

# Result Model

class TextSlidingResult(Document):
    pass

class TextScorerResult(Result):
    rank: int

class MaxPassageResult(TextScorerResult):
    pass

class QueryExpansionResult(Query):
    query_0: str

class SequentialDependenceResult(QueryExpansionResult):
    pass

class Bo1Result(QueryExpansionResult):
    pass

class KLResult(QueryExpansionResult):
    pass

class RM3Result(QueryExpansionResult):
    pass

class AxiomaticResult(QueryExpansionResult):
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


    