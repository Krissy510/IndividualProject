import pyterrier as pt
from fastapi import APIRouter

from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from model import (ApiResponse, AQERequest, AQEResult, Bo1Request, Bo1Result,
                   InteractiveFeatureProps, KLRequest, KLResult, RM3Request,
                   RM3Result, SequentialDependenceRequest,
                   SequentialDependenceResult)

pyterrier_init()

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


# GET API start here!
@router.get("/rewrite/sequential-dependence")
def get_sequential_dependence_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {"qid": "0", "query": "how to retrieve text"},
        {"qid": "1", "query": "what is an inverted index"},
    ],
        SequentialDependenceRequest,
        SequentialDependenceResult
    )


@router.get("/rewrite/bo1")
def get_bo1_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(sample_result,
                                      Bo1Request,
                                      Bo1Result
                                      )


@router.get("/rewrite/kl")
def get_kl_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(sample_result,
                                      KLRequest,
                                      KLResult
                                      )


@router.get("/rewrite/rm3")
def get_rm3_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(sample_result,
                                      RM3Request,
                                      RM3Result
                                      )


@router.get("/rewrite/aqe")
def get_aqe_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(sample_result,
                                      AQERequest,
                                      AQEResult
                                      )


# POST API start here!
@router.post("/rewrite/sequential-dependence")
def sequential_dependence(request: SequentialDependenceRequest) -> ApiResponse:
    result = pt.rewrite.SequentialDependence()(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        "pt.rewrite.SequentialDependence()"
    )


@router.post("/rewrite/bo1")
def bo1(request: Bo1Request) -> ApiResponse:
    result = pt.rewrite.Bo1QueryExpansion(index, fb_docs=request.fb_docs,
                                          fb_terms=request.fb_terms)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"pt.rewrite.Bo1QueryExpansion(index, fb_docs={request.fb_docs}, fb_terms={
            request.fb_terms})"
    )


@router.post("/rewrite/kl")
def kl(request: KLRequest) -> ApiResponse:
    result = pt.rewrite.KLQueryExpansion(index, fb_docs=request.fb_docs,
                                         fb_terms=request.fb_terms)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"pt.rewrite.KLQueryExpansion(index, fb_docs={request.fb_docs}, fb_terms={
            request.fb_terms})"
    )


@router.post("/rewrite/rm3")
def rm3(request: RM3Request):
    result = pt.rewrite.RM3(index, fb_docs=request.fb_docs,
                            fb_terms=request.fb_terms, fb_lambda=request.fb_lambda)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"pt.rewrite.RM3(index, fb_docs={request.fb_docs}, fb_terms={
            request.fb_terms}, fb_lambda={request.fb_lambda})"
    )
