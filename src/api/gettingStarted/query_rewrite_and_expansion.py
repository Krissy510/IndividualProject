import pyterrier as pt
from fastapi import APIRouter

from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from model import (ApiResponse, AxiomaticRequest, AxiomaticResult, Bo1Request,
                   Bo1Result, InteractiveFeatureProps, KLRequest, KLResult,
                   QEResetRequest, Query, ResetStashRequest, ResetStashResult,
                   RM3Request, RM3Result, SequentialDependenceRequest,
                   SequentialDependenceResult, StashRequest, StashResult,
                   TokeniseRequest, TokeniseResult)

pyterrier_init()

folder_path = './index'

index = pt.IndexFactory.of(folder_path)

# Sample data
QUERY_SAMPLE = [
    {'qid': '0', 'query': 'how to retrieve text'},
    {'qid': '1', 'query': 'what is an inverted index'}
]

RESULT_SAMPLE = [
    {'qid': '1.5', 'docid': 10927, 'docno': '10928',
     'score': 6.483154111971778, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 543, 'docno': '544',
     'score': 4.482228021407042, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 8091, 'docno': '8092',
     'score': 4.482228021407042, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 9394, 'docno': '9395',
     'score': 4.482228021407042, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 8624, 'docno': '8625',
     'score': 4.480573037616728, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 490, 'docno': '491',
     'score': 4.477928999593801, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 9007, 'docno': '9008',
     'score': 4.477928999593801, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 5597, 'docno': '5598',
     'score': 4.476080163023496, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 8253, 'docno': '8254',
     'score': 4.476080163023496, 'query': 'how to retrieve text'},
    {'qid': '1.5', 'docid': 5134, 'docno': '5135',
     'score': 4.462212559101825, 'query': 'how to retrieve text'}
]

EXPANDED_QUERY_SAMPLE = [{'qid': '1.5', 'query_0': 'how to retrieve text',
                          'query': 'applypipeline:off retriev^1.540056510 text^1.669648748 english^0.740023547 field^0.313734530 given^0.257464040 theori^0.248589949 magnet^0.220788358 influenc^0.000000000 cours^0.000000000 ionospher^0.000000000'}]

TOKENISE_SAMPLE = [
    {'qid': '0', 'query': "Question with 'capitals' and other stuff?"},]

STASH_SAMPLE = [{'qid': '1.5', 'docid': 10927, 'docno': '10928',
                 'score': 6.483154111971778, 'query': 'how to retrieve text'},]

RESET_STASH_SAMPLE = [{'qid': '1.5', 'query': 'how to retrieve text',
                       'stashed_results_0': "[{'docid': 10927, 'docno': '10928', 'qid': '1.5', 'score': 6.483154111971778}]"}]


# API implementation starts here
router = APIRouter()

# Interactive feature GET API
@router.get('/rewrite/sequential-dependence')
def get_sequential_dependence_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        QUERY_SAMPLE,
        SequentialDependenceRequest,
        SequentialDependenceResult
    )


@router.get('/rewrite/bo1')
def get_bo1_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(RESULT_SAMPLE,
                                      Bo1Request,
                                      Bo1Result
                                      )


@router.get('/rewrite/kl')
def get_kl_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(RESULT_SAMPLE,
                                      KLRequest,
                                      KLResult
                                      )


@router.get('/rewrite/rm3')
def get_rm3_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(RESULT_SAMPLE,
                                      RM3Request,
                                      RM3Result
                                      )


@router.get('/rewrite/axiomatic')
def get_axiomatic_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(RESULT_SAMPLE,
                                      AxiomaticRequest,
                                      AxiomaticResult
                                      )


@router.get('/rewrite/reset')
def get_reset_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        EXPANDED_QUERY_SAMPLE,
        QEResetRequest,
        Query
    )


@router.get('/rewrite/tokenise')
def get_tokenise_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        TOKENISE_SAMPLE,
        TokeniseRequest,
        TokeniseResult
    )


@router.get('/rewrite/stash')
def get_stash_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        STASH_SAMPLE,
        StashRequest,
        StashResult
    )


@router.get('/rewrite/reset-stash')
def get_reset_stash_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        RESET_STASH_SAMPLE,
        ResetStashRequest,
        ResetStashResult
    )


# POST API start here!
@router.post('/rewrite/sequential-dependence')
def sequential_dependence(request: SequentialDependenceRequest) -> ApiResponse:
    result = pt.rewrite.SequentialDependence()(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        'pt.rewrite.SequentialDependence()'
    )


@router.post('/rewrite/bo1')
def bo1(request: Bo1Request) -> ApiResponse:
    result = pt.rewrite.Bo1QueryExpansion(index, fb_docs=request.fb_docs,
                                          fb_terms=request.fb_terms)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f'pt.rewrite.Bo1QueryExpansion(index, fb_docs={request.fb_docs}, fb_terms={request.fb_terms})'
    )


@router.post('/rewrite/kl')
def kl(request: KLRequest) -> ApiResponse:
    result = pt.rewrite.KLQueryExpansion(index, fb_docs=request.fb_docs,
                                         fb_terms=request.fb_terms)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f'pt.rewrite.KLQueryExpansion(index, fb_docs={request.fb_docs}, fb_terms={request.fb_terms})'
    )


@router.post('/rewrite/rm3')
def rm3(request: RM3Request):
    result = pt.rewrite.RM3(index, fb_docs=request.fb_docs,
                            fb_terms=request.fb_terms, fb_lambda=request.fb_lambda)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f'pt.rewrite.RM3(index, fb_docs={request.fb_docs}, fb_terms={request.fb_terms}, fb_lambda={request.fb_lambda})'
    )


@router.post('/rewrite/axiomatic')
def axiomatic(request: AxiomaticRequest):
    result = pt.rewrite.AxiomaticQE(index, fb_docs=request.fb_docs,
                                    fb_terms=request.fb_terms)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f'pt.rewrite.AxiomaticQE(index, fb_docs={request.fb_docs}, fb_terms={request.fb_terms})'
    )


@router.post('/rewrite/reset')
def qe_reset(request: QEResetRequest) -> ApiResponse:
    result = pt.rewrite.reset()(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        'pt.rewrite.reset()'
    )


@router.post('/rewrite/tokenise')
def tokenise(request: TokeniseRequest) -> ApiResponse:
    result = pt.rewrite.tokenise()(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        'pt.rewrite.tokenise()'
    )


@router.post('/rewrite/stash')
def stash(request: StashRequest) -> ApiResponse:
    results = pt.rewrite.stash_results()(request.input)
    results = results.to_dict('records')
    for result in results:
        result['stashed_results_0'] = repr(result['stashed_results_0'])
    return generate_api_response(
        results,
        request.input,
        'pt.rewrite.tokenise()'
    )


@router.post('/rewrite/reset-stash')
def reset_stash(request: ResetStashRequest) -> ApiResponse:
    rows = request.input
    for row in rows:
        row['stashed_results_0'] = eval(row['stashed_results_0'])
    results = pt.rewrite.reset_results()(rows)
    results = results.to_dict('records')
    return generate_api_response(
        results,
        rows,
        'pt.rewrite.tokenise()'
    )
