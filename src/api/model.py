from enum import Enum
from typing import List, TypedDict

from pydantic import BaseModel

class Query(TypedDict):
    qid: str
    query: str

class RetrieveRequest(BaseModel):
    queries: List[Query]
    groupByQid: bool | None = True
    index_variant: str
    max_results: int | None = 10
    wmodel: str
    dataset: str
