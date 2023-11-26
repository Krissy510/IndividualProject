# Run command
# uvicorn main:app --host 0.0.0.0 --port 8080 --reload

from typing import List, TypedDict

import pyterrier as pt
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

if not pt.started():
    pt.init()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    index_variant: str
    num_results: int | None = 10
    wmodel: str
    dataset: str
    input: List[Query]


class TextSlidingRequest(BaseModel):
    num_results: int | None = 10
    length: int | None = 150
    stride: int | None = 75
    input: List[Document]


class MaxPassageRequest(BaseModel):
    num_results: int | None = 10
    input: List[MaxPassageInput]


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


@app.get("/")
def hello():
    return {"msg": "Hello World"}


@app.post("/retreive")
def terrier_retreive(request: RetrieveRequest) -> List[Result]:
    pipeline = pt.BatchRetrieve.from_dataset(
        num_results=request.num_results,
        dataset=request.dataset,
        variant=request.index_variant,
        wmodel=request.wmodel)
    result = pipeline(request.input)
    return result.to_dict('records')


@app.post("/text-sliding")
def text_sliding(request: TextSlidingRequest) -> List[TextSlidingResult]:
    result = pt.text.sliding(length=request.length,
                             stride=request.stride,
                             prepend_title=False)(request.input)
    return result.head(request.num_results).to_dict('records')


@app.post("/max-passage")
def max_passage(request: MaxPassageRequest) -> List[MaxPassageResult]:
    result = pt.text.max_passage()(request.input)
    return result.head(request.num_results).to_dict('records')
