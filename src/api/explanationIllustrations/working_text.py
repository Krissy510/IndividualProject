from typing import List

import pyterrier as pt
from fastapi import APIRouter

from generate import generate_interactive_props
from model import (InteractiveFeatureProps, MaxPassageRequest,
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
            "docno": "d1",
            "body": "This document is about a palico cat that climbs a tower."
        },
        {
            "qid": "1",
            "query": "document",
            "docno": "d2",
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
            "docno": "d1",
            "body": "This document is about a palico cat that climbs a tower."
        },
        {
            "qid": "1",
            "query": "document",
            "docno": "d2",
            "body": "This document is about a buisness man who took a trip and never came back."
        }
    ],
        MaxPassageRequest,
        MaxPassageResult
    )


@router.post("/text-sliding")
def text_sliding(request: TextSlidingRequest) -> List[TextSlidingResult]:
    result = pt.text.sliding(length=request.length,
                             stride=request.stride,
                             prepend_title=False)(request.input)
    return result.head(request.num_results).to_dict('records')


@router.post("/text-scorer")
def text_scorer(request: TextScorerRequest) -> List[TextScorerResult]:
    pipeline = pt.text.sliding(length=request.length,
                               stride=request.stride,
                               prepend_title=False) >> pt.text.scorer(wmodel=request.wmodel)
    result = pipeline(request.input)
    return result.head(request.num_results).to_dict('records')


@router.post("/max-passage")
def max_passage(request: MaxPassageRequest) -> List[MaxPassageResult]:
    pipeline = pt.text.sliding(length=request.length,
                               stride=request.stride,
                               prepend_title=False) >> pt.text.scorer(wmodel=request.wmodel) >> pt.text.max_passage()
    result = pipeline(request.input)
    return result.head(request.num_results).to_dict('records')
