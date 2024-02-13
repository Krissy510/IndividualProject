import pyterrier as pt
from fastapi import APIRouter, HTTPException

from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from model import (ApiResponse, InteractiveFeatureProps, MaxPassageRequest,
                   MaxPassageResult, Result, RetrieveRequest,
                   TextScorerRequest, TextScorerResult, TextSlidingRequest,
                   TextSlidingResult)

pyterrier_init()

# Sample data
TEXT_SLIDING_SAMPEL = [
    {
        'docno': 'd1',
        'body': 'This document is about a palico cat that climbs a tower.'
    },
    {
        'docno': 'd2',
        'body': 'This document is about a buisness man who took a trip and never came back.'
    }
]
TEXT_SCORER_SAMPEL = [
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
]
MAX_PASSAGE_SAMPLE = [
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
]

# API implementation starts here
router = APIRouter()

# Interactive feature GET API
@router.get('/text-sliding')
def get_text_sliding_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        TEXT_SLIDING_SAMPEL,
        TextSlidingRequest,
        TextSlidingResult
    )


@router.get('/text-scorer')
def get_text_scorer_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(TEXT_SCORER_SAMPEL,
                                      TextScorerRequest,
                                      TextScorerResult
                                      )


@router.get('/max-passage')
def get_max_passage_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(MAX_PASSAGE_SAMPLE,
                                      MaxPassageRequest,
                                      MaxPassageResult
                                      )

# POST API start here!
@router.post('/text-sliding')
def text_sliding(request: TextSlidingRequest) -> ApiResponse:
        result = pt.text.sliding(length=request.length,
                                 stride=request.stride,
                                 prepend_title=False)(request.input)
        return generate_api_response(
            result=result.to_dict('records'),
            input=request.input,
            pipeline=f'pt.text.sliding(length={request.length},stride={request.stride},prepend_title=False)',
            index_template='none'
        )
    


@router.post('/text-scorer')
def text_scorer(request: TextScorerRequest) -> ApiResponse:
    try:
        result = pt.text.scorer(wmodel=request.wmodel)(request.input)
        return generate_api_response(
                result=result.to_dict('records'),
                input=request.input,
                pipeline=f'pt.text.scorer(wmodel={repr(request.wmodel)})',
                index_template='none'
        )
    except:
        raise HTTPException(status_code=400, detail="INVALID_INPUT")


@router.post('/max-passage')
def max_passage(request: MaxPassageRequest) -> ApiResponse:
    result = pt.text.max_passage()(request.input)
    return generate_api_response(
        result=result.to_dict('records'),
        input=request.input,
        pipeline='pt.text.max_passage()',
        index_template='none'
    )
