# Run command
# uvicorn main:app --host 0.0.0.0 --port 8080 --reload

import pyterrier as pt
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from explanationIllustrations import working_text
from gettingStarted import query_rewrite_and_expansion, retrival
from interactiveProps import props

if not pt.started():
    pt.init()

app = FastAPI()


# Interactive Feature props
app.include_router(props.router)
# Getting started
app.include_router(retrival.router)
app.include_router(query_rewrite_and_expansion.router)
# Explanation & Illustrations
app.include_router(working_text.router)

###### For develop only###########

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#################################


@app.get("/")
def hello():
    return {"msg": "Hi, this is PyTerrier Doc API"}
