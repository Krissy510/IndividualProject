# Run command
# uvicorn main:app --host 0.0.0.0 --port 8080 --reload


from typing import List

import pyterrier as pt
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from generate import generate_interactive_props
from model import (InteractiveFeatureProps, MaxPassageRequest,
                   MaxPassageResult, Result, RetrieveRequest,
                   TextScorerRequest, TextScorerResult, TextSlidingRequest,
                   TextSlidingResult)

if not pt.started():
    pt.init()

app = FastAPI()

###### For develop only###########

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

#################################


@app.get("/")
def hello():
    return {"msg": "Hi, this is PyTerrier Doc API"}


@app.get("/retreive")
def get_terrier_retreive_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {"qid": "0", "query": "how to retrieve text"},
        {"qid": "1", "query": "what is an inverted index"},
    ],
        RetrieveRequest,
        Result
    )


@app.get("/text-sliding")
def get_text_sliding_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {
            "docno": "d1",
            "body": "a b c d"
        }
    ],
        TextSlidingRequest,
        TextSlidingResult
    )


@app.get("/text-scorer")
def get_text_scorer_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {
            "qid": "0",
            "query": "document",
            "docno": "d1",
            "body": "This document is about a palico cat that climbs a tower."
        },
        {
            "qid": "0",
            "query": "document",
            "docno": "d2",
            "body": "This document is about a buisness man who took a trip and never came back."
        }
    ],
        TextScorerRequest,
        TextScorerResult
    )

@app.get("/max-passage")
def get_max_passage_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {
            "qid": "0",
            "query": "document",
            "docno": "d1",
            "body": "This document is about a palico cat that climbs a tower."
        },
        {
            "qid": "0",
            "query": "document",
            "docno": "d2",
            "body": "This document is about a buisness man who took a trip and never came back."
        }
    ],
    MaxPassageRequest,
    MaxPassageResult
    )


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


@app.post("/text-scorer")
def text_scorer(request: TextScorerRequest) -> List[TextScorerResult]:
    pipeline = pt.text.sliding(length=request.length,
                               stride=request.stride,
                               prepend_title=False) >> pt.text.scorer(wmodel=request.wmodel)
    result = pipeline(request.input)
    return result.head(request.num_results).to_dict('records')


@app.post("/max-passage")
def max_passage(request: MaxPassageRequest) -> List[MaxPassageResult]:
    pipeline = pt.text.sliding(length=request.length,
                               stride=request.stride,
                               prepend_title=False) >> pt.text.scorer(wmodel=request.wmodel) >> pt.text.max_passage()
    result = pipeline(request.input)
    return result.head(request.num_results).to_dict('records')
