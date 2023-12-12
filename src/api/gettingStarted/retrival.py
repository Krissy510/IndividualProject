from typing import List

import pyterrier as pt
from fastapi import APIRouter

from generate import generate_interactive_props, generate_api_response
from model import InteractiveFeatureProps, Result, RetrieveRequest, ApiResponse

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
def terrier_retreive(request: RetrieveRequest) -> ApiResponse:
    result = pt.BatchRetrieve.from_dataset(
        num_results=request.num_results,
        dataset=request.dataset,
        variant=request.index_variant,
        wmodel=request.wmodel)(request.input)
    return generate_api_response(
        result.to_dict('records'), 
        request.input,
        f"""pt.BatchRetrieve.from_dataset(
            num_results={request.num_results},
            dataset=\"{request.dataset}\",
            variant=\"{request.index_variant}\",
            wmodel=\"{request.wmodel}\")"""
    )