"""
Base models for Pyterrier API
"""
from typing import List
from typing_extensions import TypedDict


class Query(TypedDict):
    qid: str
    query: str


class Document(TypedDict):
    docno: str
    body: str


class Result(Query):
    docno: str
    score: float


class T5Model(Result):
    rank: int
    text: str


class DocumentText(TypedDict):
    docno: int
    text: str
