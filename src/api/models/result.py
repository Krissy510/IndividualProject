from typing import List, Union

from .base import Document, DocumentText, Query, Result, T5Model
from .input_type import DrScorerInput
from pydantic import BaseModel


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


class PisaRetrieveResult(Result):
    rank: int
