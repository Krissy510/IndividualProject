from typing import List

import pyterrier as pt
from fastapi import APIRouter

from model import (MaxPassageRequest, MaxPassageResult, Result,
                   RetrieveRequest, TextScorerRequest, TextScorerResult,
                   TextSlidingRequest, TextSlidingResult)

if not pt.started():
    pt.init()


router = APIRouter()


@router.post("/retreive")
def terrier_retreive(request: RetrieveRequest) -> List[Result]:
    pipeline = pt.BatchRetrieve.from_dataset(
        num_results=request.num_results,
        dataset=request.dataset,
        variant=request.index_variant,
        wmodel=request.wmodel)
    result = pipeline(request.input)
    return result.to_dict('records')


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
