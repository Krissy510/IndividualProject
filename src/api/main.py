# Run command
# uvicorn main:app --host 0.0.0.0 --port 8080 --reload


from typing import List

import pyterrier as pt
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from model import (MaxPassageRequest, MaxPassageResult, Result,
                   RetrieveRequest, TextSlidingRequest, TextSlidingResult,
                   InteractiveFeatureProps, Query)

from generate import generate_columns, generate_parameters

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
    return {
        "example": [
            {"qid": "0", "query": "how to retrieve text"},
            {"qid": "1", "query": "what is an inverted index"},
        ],
        "columns": generate_columns(Query),
        "parameters": generate_parameters(RetrieveRequest)
    }


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
