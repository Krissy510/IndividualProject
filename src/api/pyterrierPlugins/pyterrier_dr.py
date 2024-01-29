import pyterrier as pt
from fastapi import APIRouter
from pyterrier_dr import Ance, Query2Query, TasB, TctColBert

from generate import (generate_api_response, generate_interactive_props,
                      generate_multi_interactive_props)
from helper import pyterrier_init
from model import (ApiResponse, DrDocumentRequest, DrDocumentResult,
                   DrQueryRequest, DrQueryResult, DrRequest, DrScorerRequest,
                   DrScorerResult, InteractiveFeatureProps,
                   MultiInteractiveFeatureProps)

pyterrier_init()

SAMPLE_QUERY = [
    {'qid': '0', 'query': 'Hello Terrier'},
    {'qid': '1', 'query': 'find me some documents'},
]

SAMPLE_DOC = [
    {'docno': '0', 'text': 'The Five Find-Outers and Dog, also known as The Five Find-Outers, is a series of children\'s mystery books written by Enid Blyton.'},
    {'docno': '1', 'text': 'City is a 1952 science fiction fix-up novel by American writer Clifford D. Simak.'},
]

SAMPLE_QUERY_DOC = [
    {'qid': '0', 'query': 'Hello Terrier', 'docno': '0',
        'text': 'The Five Find-Outers and Dog, also known as The Five Find-Outers, is a series of children\'s mystery books written by Enid Blyton.'},
    {'qid': '0', 'query': 'Hello Terrier', 'docno': '1',
     'text': 'City is a 1952 science fiction fix-up novel by American writer Clifford D. Simak.'},
]

KEY_TYPE = {
    "query_encoder": "query_vec",
    "doc_encoder": "doc_vec"
}

# API implementation starts here
router = APIRouter()


def generate_dr_multi_fields() -> MultiInteractiveFeatureProps:
    return generate_multi_interactive_props(
        optionsName=["query_encoder", "doc_encoder", "scorer"],
        defaultOption="query_encoder",
        examples=[SAMPLE_QUERY, SAMPLE_DOC, SAMPLE_QUERY_DOC],
        requestClasses=[DrQueryRequest, DrDocumentRequest, DrScorerRequest],
        outputClasses=[DrQueryResult, DrDocumentResult, DrScorerResult]
    )

# Interactive feature GET API


@router.get('/plugins/pyterrier-dr/tct-bol-bert')
def get_tct_bol_bert_fields() -> MultiInteractiveFeatureProps:
    return generate_dr_multi_fields()


@router.get('/plugins/pyterrier-dr/ance')
def get_ance_fields() -> MultiInteractiveFeatureProps:
    return generate_dr_multi_fields()


@router.get('/plugins/pyterrier-dr/query-2-query')
def get_query_2_query_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(SAMPLE_QUERY, DrQueryRequest, DrQueryResult)


def dr_processing(result, request_type, request_input, code):
    output = result.to_dict('records')
    if (request_type != "scorer"):
        key = KEY_TYPE[request_type]
        for i in range(len(output)):
            output[i][key] = repr(output[i][key])
    return generate_api_response(output,
                                 request_input,
                                 code)


# POST API start here!
@router.post('/plugins/pyterrier-dr/tct-bol-bert')
def tct_bol_bert(request: DrRequest) -> ApiResponse:
    result = TctColBert()(request.input)
    return dr_processing(result, request.type, request.input, "pyterrier_dr.TctColBert()")


@router.post('/plugins/pyterrier-dr/ance')
def tct_bol_bert(request: DrRequest) -> ApiResponse:
    result = Ance()(request.input)
    return dr_processing(result, request.type, request.input, "pyterrier_dr.Ance()")


@router.post('/plugins/pyterrier-dr/query-2-query')
def query_2_query(request: DrQueryRequest) -> ApiResponse:
    result = Query2Query()(request.input)
    result = result.to_dict('records')
    for i in range(len(result)):
        result[i]['query_vec'] = repr(result[i]['query_vec'])
    return generate_api_response(result,
                                 request.input,
                                 "pyterrier_dr.Query2Query()")
