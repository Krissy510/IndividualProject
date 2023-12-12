import pyterrier as pt
from fastapi import APIRouter

from generate import generate_api_response, generate_interactive_props
from model import (ApiResponse, Bo1QueryExpansionRequest,
                   Bo1QueryExpansionResult, InteractiveFeatureProps,
                   KLQueryExpansionRequest, KLQueryExpansionResult,
                   SequentialDependenceRequest, SequentialDependenceResult)

if not pt.started():
    pt.init()

folder_path = "./index"

index = pt.IndexFactory.of(folder_path)

sample_result = [
    {'qid': '1.5', 'docid': 10927, 'docno': '10928', 'rank': 0,
     'score': 6.483154111971778, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 543, 'docno': '544',
     'score': 4.482228021407042, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 8091, 'docno': '8092',
     'score': 4.482228021407042, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 9394, 'docno': '9395',
     'score': 4.482228021407042, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 8624, 'docno': '8625',
     'score': 4.480573037616728, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 490, 'docno': '491',
     'score': 4.477928999593801, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 9007, 'docno': '9008',
     'score': 4.477928999593801, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 5597, 'docno': '5598',
     'score': 4.476080163023496, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 8253, 'docno': '8254',
     'score': 4.476080163023496, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 5134, 'docno': '5135',
     'score': 4.462212559101825, 'query': 'how to retrieve text'}
]

router = APIRouter()


@router.get("/sequential-dependence")
def get_sequential_dependence_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {"qid": "0", "query": "how to retrieve text"},
        {"qid": "1", "query": "what is an inverted index"},
    ],
        SequentialDependenceRequest,
        SequentialDependenceResult
    )


@router.get("/bo1-query-expansion")
def get_bo1_query_expansion() -> InteractiveFeatureProps:
    return generate_interactive_props(sample_result,
                                      Bo1QueryExpansionRequest,
                                      Bo1QueryExpansionResult
                                      )


@router.get("/kl-query-expansion")
def get_kl_query_expansion() -> InteractiveFeatureProps:
    return generate_interactive_props(sample_result,
                                      KLQueryExpansionRequest,
                                      KLQueryExpansionResult
                                      )


@router.post("/sequential-dependence")
def sequential_dependence(request: SequentialDependenceRequest) -> ApiResponse:
    result = pt.rewrite.SequentialDependence()(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"pt.rewrite.SequentialDependence()"
    )


@router.post("/bo1-query-expansion")
def bo1_query_expansion(request: Bo1QueryExpansionRequest) -> ApiResponse:
    result = pt.rewrite.Bo1QueryExpansion(index, fb_docs=request.fb_docs,
                                          fb_terms=request.fb_terms)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"pt.rewrite.Bo1QueryExpansion(index)"
    )


@router.post("/kl-query-expansion")
def kl_query_expansion(request: KLQueryExpansionRequest) -> ApiResponse:
    result = pt.rewrite.KLQueryExpansion(indexindex, fb_docs=request.fb_docs,
                                         fb_terms=request.fb_terms)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"pt.rewrite.KLQueryExpansion(index)"
    )
