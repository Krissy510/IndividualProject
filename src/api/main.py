# Run command
# uvicorn main:app --host 0.0.0.0 --port 8080 --reload

import pyterrier as pt
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from explanationIllustrations import working_text
from gettingStarted import query_rewrite_and_expansion, retrival
from helper import pyterrier_init

pyterrier_init()

app = FastAPI()

# Getting started
app.include_router(retrival.router)
app.include_router(query_rewrite_and_expansion.router)

# Explanation & Illustrations
app.include_router(working_text.router)

###### CORS ###########
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://pyterrier-documentation.vercel.app"
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
    return {"msg": "Hi, this is PyTerrier Doc API (secure)"}
