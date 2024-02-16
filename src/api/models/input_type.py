"""
Models use as a type for list in request class.
"""
from .base import Document, DocumentText, Query


class TextScorerInput(Query, Document):
    pass


class ResetStashInput(Query):
    stashed_results_0: str


class DrScorerInput(Query, DocumentText):
    pass
