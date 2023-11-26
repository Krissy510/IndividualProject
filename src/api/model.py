from enum import Enum
from typing import List, TypedDict

from pydantic import BaseModel


# Data Model
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


class MaxPassageInput(TypedDict):
    qid: str
    query: str
    docno: str
    body: str
    score: float


# Request Model
class RetrieveRequest(BaseModel):
    queries: List[Query]
    index_variant: str
    num_results: int | None = 10
    wmodel: str
    dataset: str


class TextSlidingRequest(BaseModel):
    num_results: int | None = 10
    length: int | None = 150
    stride: int | None = 75
    documents: List[Document]


class MaxPassageRequest(BaseModel):
    num_results: int | None = 10
    max_passage_input: List[MaxPassageInput]


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
