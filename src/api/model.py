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

class IRequest(BaseModel):
    input: List[TypedDict]

class QueryExpanssionRequest(IRequest):
    input: List[Result]
    fb_terms: int
    fb_docs: int

class QueryExpansionResult(Query):
    query_0: str

class T5Model(Result):
    rank: int
    text: str

class DocumentText(TypedDict):
    docno: int
    text: str

# Input model
class TextScorerInput(Query,Document):
    pass

class ResetStashInput(Query):
    stashed_results_0: str

class DrScorerInput(Query,DocumentText):
    pass


# Request Model
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

class Bo1Request(QueryExpanssionRequest):
    pass

class KLRequest(QueryExpanssionRequest):
    pass

class RM3Request(QueryExpanssionRequest):
    fb_lambda: float

class AxiomaticRequest(QueryExpanssionRequest):
    fb_lambda: float

class QEResetRequest(IRequest):
    input: List[QueryExpansionResult]

class TokeniseRequest(IRequest):
    input: List[Query]

class StashRequest(IRequest):
    input: List[Result]

class ResetStashRequest(IRequest):
    input: List[ResetStashInput]

class T5Request(IRequest):
    batch_size: int
    input: List[T5Model]

class DrQueryRequest(IRequest):
    input: List[Query]

class DrDocumentRequest(IRequest):
    input: List[DocumentText]

class DrScorerRequest(IRequest):
    input: List[DrScorerInput]

# Result Model
class TextSlidingResult(Document):
    pass

class TextScorerResult(Result):
    rank: int

class MaxPassageResult(TextScorerResult):
    pass

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

class TokeniseResult(QueryExpansionResult):
    pass

class ResetStashResult(Result):
    pass

class StashResult(Query):
    stashed_results_0: str

class T5Result(T5Model):
    pass

class DrQueryResult(Query):
    query_vec: str

class DrDocumentResult(DocumentText):
    doc_vec: str

class DrScorerResult(DrScorerInput):
    score: float
    rank: int

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

class MultiInteractiveFeatureProps(BaseModel):
    options: List[InteractiveFeatureProps]
