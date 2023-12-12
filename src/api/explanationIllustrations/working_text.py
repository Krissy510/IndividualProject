import pyterrier as pt
from fastapi import APIRouter

from generate import generate_interactive_props, generate_api_response
from model import (ApiResponse, InteractiveFeatureProps, MaxPassageRequest,
                   MaxPassageResult, Result, RetrieveRequest,
                   TextScorerRequest, TextScorerResult, TextSlidingRequest,
                   TextSlidingResult)

if not pt.started():
    pt.init()


router = APIRouter()


@router.get("/text-sliding")
def get_text_sliding_fields() -> InteractiveFeatureProps:
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
def get_text_scorer_fields() -> InteractiveFeatureProps:
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
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p0',
            'body': 'This document is about a'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p1',
            'body': 'document is about a buisness'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p2',
            'body': 'is about a buisness man'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p3',
            'body': 'about a buisness man who'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p4',
            'body': 'a buisness man who took'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p5',
            'body': 'buisness man who took a'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p6',
            'body': 'man who took a trip'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p7',
            'body': 'who took a trip and'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p8',
            'body': 'took a trip and never'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p9',
            'body': 'a trip and never came'},
        {'qid': '0', 'query': 'cat', 'docno': 'd2%p10',
            'body': 'trip and never came back.'}
    ],
        TextScorerRequest,
        TextScorerResult
    )


@router.get("/max-passage")
def get_max_passage_fields() -> InteractiveFeatureProps:
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
        {'qid': '0', 'docno': 'd2%p0', 'body': 'This document is about a',
            'rank': 7, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p1', 'body': 'document is about a buisness',
            'rank': 8, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p2', 'body': 'is about a buisness man',
            'rank': 9, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p3', 'body': 'about a buisness man who',
            'rank': 10, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p4', 'body': 'a buisness man who took',
            'rank': 11, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p5', 'body': 'buisness man who took a',
            'rank': 12, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p6', 'body': 'man who took a trip',
            'rank': 13, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p7', 'body': 'who took a trip and',
            'rank': 14, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p8', 'body': 'took a trip and never',
            'rank': 15, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p9', 'body': 'a trip and never came',
            'rank': 16, 'score': 0.0, 'query': 'cat'},
        {'qid': '0', 'docno': 'd2%p10', 'body': 'trip and never came back.',
         'rank': 17, 'score': 0.0, 'query': 'cat'}],
        MaxPassageRequest,
        MaxPassageResult
    )


@router.post("/text-sliding")
def text_sliding(request: TextSlidingRequest) -> ApiResponse:
    result = pt.text.sliding(length=request.length,
                             stride=request.stride,
                             prepend_title=False)(request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 f"""pt.text.sliding(length=request.length,
                                    stride=request.stride,
                                    prepend_title=False)""")


@router.post("/text-scorer")
def text_scorer(request: TextScorerRequest) -> ApiResponse:
    result = pt.text.scorer(wmodel=request.wmodel)(request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 f"pt.text.scorer(wmodel=\"{request.wmodel}\")")


@router.post("/max-passage")
def max_passage(request: MaxPassageRequest) -> ApiResponse:
    result = pt.text.max_passage()(request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 f"pt.text.max_passage()")
