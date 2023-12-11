from typing import List

import pyterrier as pt
from fastapi import APIRouter

from generate import generate_interactive_props
from model import (InteractiveFeatureProps, SequentialDependenceRequest,
                   SequentialDependenceResult)

if not pt.started():
    pt.init()

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


@router.post("/sequential-dependence")
def sequential_dependence(request: SequentialDependenceRequest) -> List[SequentialDependenceResult]:
    result = pt.rewrite.SequentialDependence() (request.input)
    return result.to_dict('records')
