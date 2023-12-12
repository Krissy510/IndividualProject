from typing import List

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
        {
            "qid": "0",
            "query": "cat",
            "docno": "d1%p0",
            "body": "This document is about a palico cat that climbs a tower."
        },
        {
            "qid": "0",
            "query": "cat",
            "docno": "d2%p0",
            "body": "This document is about a buisness man who took a trip and never came back."
        }
    ],
        TextScorerRequest,
        TextScorerResult
    )


@router.get("/max-passage")
def get_max_passage_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {
            "qid": "0",
            "query": "cat",
            "docno": "d1%p0",
            "body": "This document is about a palico cat that climbs a tower.",
            "score": "0.813855"
        },
        {
            "qid": "0",
            "query": "cat",
            "docno": "d2%p0",
            "body": "This document is about a buisness man who took a trip and never came back.",
            "score": "0.00000"
        }
    ],
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
    prepend_title=False)"""
                                 )


@router.post("/text-scorer")
def text_scorer(request: TextScorerRequest) -> List[TextScorerResult]:
    result = pt.text.scorer(wmodel=request.wmodel)(request.input)
    return result.to_dict('records')


@router.post("/max-passage")
def max_passage(request: MaxPassageRequest) -> List[MaxPassageResult]:
    result = pt.text.max_passage()(request.input)
    return result.to_dict('records')
