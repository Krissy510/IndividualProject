from enum import Enum
from typing import List, TypedDict

from pydantic import BaseModel


# Data Model
class Query(TypedDict):
    qid: int
    query: str


class Document(TypedDict):
    docno: str
    title: str
    body: str


class Result(TypedDict):
    qid: int
    query: str
    docno: str
    score: float


class MaxPassageInput(TypedDict):
    qid: int
    query: str
    docno: str
    body: str
    score: float


# Request Model
class RetrieveRequest(BaseModel):
    queries: List[Query]
    index_variant: str
    num_results: int
    wmodel: str
    dataset: str


class TextSlidingRequest(BaseModel):
    length: int | None = 150
    stride: int | None = 75
    documents: List[Document]


class MaxPassageRequest(BaseModel):
    num_results: int
    max_passage_input: List[MaxPassageInput]


# Result Model
class TextSlidingResult(TypedDict):
    Index: int
    docno: str
    body: str


class MaxPassageResult(TypedDict):
    qid: int
    query: str
    body: str
    score: float
    docno: str
    rank: int
