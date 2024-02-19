"""
Models for any API requests.
"""
from typing import List, Union

from pydantic import BaseModel
from typing_extensions import TypedDict

from .base import Document, DocumentText, Query, Result, T5Model
from .input_type import DrScorerInput, ResetStashInput, TextScorerInput
from .result import QueryExpansionResult


class IRequest(BaseModel):
    input: List[TypedDict]


class QueryExpanssionRequest(IRequest):
    input: List[Result]
    fb_terms: int
    fb_docs: int
    qre_dataset: str


class RetrieveRequest(IRequest):
    dataset: str
    wmodel: str
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


class DrMultiRequest(IRequest):
    # There is some issue with Union type in input.
    # Ideally it should be List[Union[Query,DocumentText,DrScorerInput]] or Union[List[Query],List[DocumentText],List[DrScrorerInput]]
    input: List
    type: str
    model: str


class PisaRequest(IRequest):
    input: List[Query]
    dataset_pisa: str


class PisaDphRequest(PisaRequest):
    pass


class PisaBm25Request(PisaRequest):
    k1: float
    b: float


class PisaPl2Request(PisaRequest):
    c: float


class PisaQldRequest(PisaRequest):
    mu: float
