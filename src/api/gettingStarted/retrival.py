from typing import List

import pyterrier as pt
from fastapi import APIRouter

from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from model import ApiResponse, InteractiveFeatureProps, Result, RetrieveRequest

pyterrier_init()

folder_path = './vaswani.terrier'

index = pt.IndexFactory.of(folder_path)

router = APIRouter()

# Sample data
RETREIVE_SAMPLE = [
    {"qid": "0", "query": "how to retrieve text"},
    {"qid": "1", "query": "what is an inverted index"},
]

# Interactive feature GET API
@router.get("/retreive")
def get_terrier_retreive_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(RETREIVE_SAMPLE,
                                      RetrieveRequest,
                                      Result
                                      )

# POST API start here!
@router.post("/retreive")
def terrier_retreive(request: RetrieveRequest) -> ApiResponse:
    result = pt.BatchRetrieve(index,
                              num_results=request.num_results,
                              wmodel=request.wmodel)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"""pt.BatchRetrieve.from_dataset(index,
            num_results={repr(request.num_results)},
            wmodel={repr(request.wmodel)})"""
    )
