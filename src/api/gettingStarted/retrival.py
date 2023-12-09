from typing import List

import pyterrier as pt
from fastapi import APIRouter

from generate import generate_interactive_props
from model import InteractiveFeatureProps, Result, RetrieveRequest

if not pt.started():
    pt.init()


router = APIRouter()


@router.get("/retreive")
def get_terrier_retreive_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {"qid": "0", "query": "how to retrieve text"},
        {"qid": "1", "query": "what is an inverted index"},
    ],
        RetrieveRequest,
        Result
    )


@router.post("/retreive")
def terrier_retreive(request: RetrieveRequest) -> List[Result]:
    pipeline = pt.BatchRetrieve.from_dataset(
        num_results=request.num_results,
        dataset=request.dataset,
        variant=request.index_variant,
        wmodel=request.wmodel)
    result = pipeline(request.input)
    return result.to_dict('records')
