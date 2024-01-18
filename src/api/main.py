# Run command
# uvicorn main:app --host 0.0.0.0 --port 8080 --reload

import pyterrier as pt
from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKey

import auth
from explanationIllustrations import working_text
from gettingStarted import query_rewrite_and_expansion, retrival

if not pt.started():
    pt.init()

app = FastAPI()

# Getting started
app.include_router(retrival.router)
app.include_router(query_rewrite_and_expansion.router)
# Explanation & Illustrations
app.include_router(working_text.router)

###### CORS ###########
origins = [
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
def hello(api_key: APIKey = Security(auth.get_api_key)):
    return {"msg": "Hi, this is PyTerrier Doc API (secure)"}
