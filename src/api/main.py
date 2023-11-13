# Run command
# uvicorn main:app --host 0.0.0.0 --port 8080 --reload

import os

import pyterrier as pt
from fastapi import FastAPI, HTTPException, status

import validate as val
from model import *

if not pt.started():
    pt.init()

app = FastAPI()


@app.get("/retreive")
def terrier_retreive(request: RetrieveRequest) -> List[Result]:
    if (not val.dataset(request.dataset)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid dataset")
    if (not val.wmodel(request.wmodel)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid wmodel")
    if (not val.variant(request.index_variant)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid index variant")
    pipeline = pt.BatchRetrieve.from_dataset(
        num_results=request.num_results,
        dataset=request.dataset,
        variant=request.index_variant,
        wmodel=request.wmodel)
    result = pipeline(request.queries)
    return result.to_dict('records')


