from typing import List

import pyterrier as pt
from fastapi import APIRouter

from model import Result, RetrieveRequest

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
