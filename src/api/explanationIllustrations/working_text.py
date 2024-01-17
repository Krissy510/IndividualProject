import pyterrier as pt
from fastapi import APIRouter, Security
from fastapi.security.api_key import APIKey

from auth import get_api_key
from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from model import (ApiResponse, InteractiveFeatureProps, MaxPassageRequest,
                   MaxPassageResult, Result, RetrieveRequest,
                   TextScorerRequest, TextScorerResult, TextSlidingRequest,
                   TextSlidingResult)

pyterrier_init()


router = APIRouter()


@router.get("/text-sliding")
def get_text_sliding_fields(api_key: APIKey = Security(get_api_key)) -> InteractiveFeatureProps:
    return generate_interactive_props([
        {
            "docno": "d1",
            "body": "This document is about a palico cat that climbs a tower."
        },
        {
            "docno": "d2",
            "body": "This document is about a buisness man who took a trip and never came back."
        }
    ],
        TextSlidingRequest,
        TextSlidingResult
    )


@router.get("/text-scorer")
def get_text_scorer_fields(api_key: APIKey = Security(get_api_key)) -> InteractiveFeatureProps:
    return generate_interactive_props([
        {'qid': '0', 'query': 'cat', 'docno': 'd1%p0',
            'body': 'This document is about a'},
        {'qid': '0', 'query': 'cat', 'docno': 'd1%p1',
            'body': 'document is about a palico'},
        {'qid': '0', 'query': 'cat', 'docno': 'd1%p2',
            'body': 'is about a palico cat'},
        {'qid': '0', 'query': 'cat', 'docno': 'd1%p3',
            'body': 'about a palico cat that'},
        {'qid': '0', 'query': 'cat', 'docno': 'd1%p4',
            'body': 'a palico cat that climbs'},
        {'qid': '0', 'query': 'cat', 'docno': 'd1%p5',
            'body': 'palico cat that climbs a'},
        {'qid': '0', 'query': 'cat', 'docno': 'd1%p6',
            'body': 'cat that climbs a tower.'},
    ],
        TextScorerRequest,
        TextScorerResult
    )


@router.get("/max-passage")
def get_max_passage_fields(api_key: APIKey = Security(get_api_key)) -> InteractiveFeatureProps:
    return generate_interactive_props([
        {'qid': '0', 'docno': 'd1%p0', 'body': 'This document is about a',
            'rank': 5, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd1%p1', 'body': 'document is about a palico',
            'rank': 6, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd1%p2', 'body': 'is about a palico cat',
            'rank': 0, 'score': 1.4219103623953206, 'query': 'cat'},
        {'qid': '0', 'docno': 'd1%p3', 'body': 'about a palico cat that',
            'rank': 1, 'score': 1.4219103623953206, 'query': 'cat'},
        {'qid': '0', 'docno': 'd1%p4', 'body': 'a palico cat that climbs',
            'rank': 2, 'score': 1.2094108432919608, 'query': 'cat'},
        {'qid': '0', 'docno': 'd1%p5', 'body': 'palico cat that climbs a',
            'rank': 3, 'score': 1.2094108432919608, 'query': 'cat'},
        {'qid': '0', 'docno': 'd1%p6', 'body': 'cat that climbs a tower.',
            'rank': 4, 'score': 1.2094108432919608, 'query': 'cat'},
    ],
        MaxPassageRequest,
        MaxPassageResult
    )


@router.post("/text-sliding")
def text_sliding(request: TextSlidingRequest, api_key: APIKey = Security(get_api_key)) -> ApiResponse:
    result = pt.text.sliding(length=request.length,
                             stride=request.stride,
                             prepend_title=False)(request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 f"pt.text.sliding(length={request.length},stride={request.stride},prepend_title=False)")


@router.post("/text-scorer")
def text_scorer(request: TextScorerRequest, api_key: APIKey = Security(get_api_key)) -> ApiResponse:
    result = pt.text.scorer(wmodel=request.wmodel)(request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 f"pt.text.scorer(wmodel={repr(request.wmodel)})")


@router.post("/max-passage")
def max_passage(request: MaxPassageRequest, api_key: APIKey = Security(get_api_key)) -> ApiResponse:
    result = pt.text.max_passage()(request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 "pt.text.max_passage()")
