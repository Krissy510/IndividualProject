from typing import List

import pyterrier as pt
from fastapi import APIRouter

from model import SequentialDependenceRequest, SequentialDependenceResult

if not pt.started():
    pt.init()

router = APIRouter()

@router.post("/sequential-dependence")
def sequential_dependence(request: SequentialDependenceRequest) -> List[SequentialDependenceResult]:
    pipeline = pt.BatchRetrieve.from_dataset(
        num_results=request.num_results,
        dataset=request.dataset,
        variant=request.index_variant,
        wmodel=request.wmodel) >> pt.rewrite.SequentialDependence()
    result = pipeline(request.input)
    return result.to_dict('records')
