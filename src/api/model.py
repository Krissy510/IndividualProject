from enum import Enum
from typing import List, TypedDict

from pydantic import BaseModel

# Common Data Model

class Query(TypedDict):
    qid: int
    query: str

class RetrieveRequest(BaseModel):
    queries: List[Query]
    index_variant: str
    num_results: int
    wmodel: str
    dataset: str
