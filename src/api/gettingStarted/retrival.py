from typing import List

import pyterrier as pt
from fastapi import APIRouter, Security
from fastapi.security.api_key import APIKey

from auth import get_api_key
from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from model import ApiResponse, InteractiveFeatureProps, Result, RetrieveRequest

pyterrier_init()

router = APIRouter()


@router.get("/retreive")
def get_terrier_retreive_fields(api_key: APIKey = Security(get_api_key)) -> InteractiveFeatureProps:
    return generate_interactive_props([
        {"qid": "0", "query": "how to retrieve text"},
        {"qid": "1", "query": "what is an inverted index"},
    ],
        RetrieveRequest,
        Result
    )


@router.post("/retreive")
def terrier_retreive(request: RetrieveRequest, api_key: APIKey = Security(get_api_key)) -> ApiResponse:
    result = pt.BatchRetrieve.from_dataset(
        num_results=request.num_results,
        dataset=request.dataset,
        variant=request.index_variant,
        wmodel=request.wmodel)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"""pt.BatchRetrieve.from_dataset(
            num_results={repr(request.num_results)},
            dataset={repr(request.dataset)},
            variant={repr(request.index_variant)},
            wmodel={repr(request.wmodel)})"""
    )
