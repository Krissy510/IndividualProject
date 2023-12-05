from fastapi import APIRouter

from generate import generate_interactive_props
from model import (InteractiveFeatureProps, MaxPassageRequest,
                   MaxPassageResult, Result, RetrieveRequest,
                   SequentialDependenceRequest, SequentialDependenceResult,
                   TextScorerRequest, TextScorerResult, TextSlidingRequest,
                   TextSlidingResult)

router = APIRouter()

@router.get("/retreive")
def get_terrier_retreive_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {"qid": "0", "query": "how to retrieve text"},
        {"qid": "1", "query": "what is an inverted index"},
    ],
        RetrieveRequest,
        Result
    )


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


@router.get("/sequential-dependence")
def get_sequential_dependence_fields() -> InteractiveFeatureProps:
    return generate_interactive_props([
        {"qid": "0", "query": "how to retrieve text"},
        {"qid": "1", "query": "what is an inverted index"},
    ],
        SequentialDependenceRequest,
        SequentialDependenceResult
    )