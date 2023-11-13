from enum import Enum
from typing import List, TypedDict

from pydantic import BaseModel


# Data Model
class QueryModel(TypedDict):
    qid: int
    query: str


class DocumentModel(TypedDict):
    docno: str
    title: str
    body: str


class ResultModel(TypedDict):
    qid: int
    query: str
    docno: str
    score: float


# Request Model
class RetrieveRequest(BaseModel):
    queries: List[QueryModel]
    index_variant: str
    num_results: int
    wmodel: str
    dataset: str


class TextSlidingRequest(BaseModel):
    length: int | None = 150
    stride: int | None = 75
    documents: List[DocumentModel]


# Result Model
class TextSlidingResult(TypedDict):
    docno: str
    body: str
