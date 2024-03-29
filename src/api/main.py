import pyterrier as pt
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from apis.explanationIllustrations import working_text
from apis.gettingStarted import query_rewrite_and_expansion, retrival
from apis.pyterrierPlugins import pyterrier_t5, pyterrier_dr, pyterrier_pisa
from helper import pyterrier_init

pyterrier_init()

app = FastAPI()

###### Router ##############
# Getting started
app.include_router(retrival.router)
app.include_router(query_rewrite_and_expansion.router)

# Explanation & Illustrations
app.include_router(working_text.router)

# Pyterrier Plugins
app.include_router(pyterrier_t5.router)
app.include_router(pyterrier_dr.router)
app.include_router(pyterrier_pisa.router)

##############################

###### CORS ###########
# Whilist
origins = [
    'https://pyterrier-documentation.vercel.app',
]

# Config
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

#################################


@app.get('/')
def hello():
    return {'msg': 'Hi, this is PyTerrier Doc API.'}
