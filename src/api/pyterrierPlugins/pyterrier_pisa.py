import pyterrier as pt
from fastapi import APIRouter

from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from models import (ApiResponse, InteractiveFeatureProps, PisaBm25Request,
                    PisaDphRequest, PisaPl2Request, PisaQldRequest,
                    PisaRetrieveResult)

# from pyterrier_pisa import PisaIndex


pyterrier_init()

# folder_path = './pisa-antique-index'

# idx = PisaIndex(folder_path)

# Sample data
QUERY_SAMPLE = [
    {'qid': '0', 'query': 'Cola'},
    {'qid': '1', 'query': 'Sample'}
]

# API implementation starts here
router = APIRouter()

# Interactive feature GET API


@router.get('/plugins/pisa/dph')
def get_pisa_dph_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        QUERY_SAMPLE,
        PisaDphRequest,
        PisaRetrieveResult
    )


@router.get('/plugins/pisa/bm25')
def get_pisa_bm25_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        QUERY_SAMPLE,
        PisaBm25Request,
        PisaRetrieveResult
    )


@router.get('/plugins/pisa/pl2')
def get_pisa_pl2_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        QUERY_SAMPLE,
        PisaPl2Request,
        PisaRetrieveResult
    )


@router.get('/plugins/pisa/qld')
def get_pisa_qld_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        QUERY_SAMPLE,
        PisaQldRequest,
        PisaRetrieveResult
    )

# POST API start here!
@router.post('/plugins/pisa/dph')
def pisa_dph(request: PisaDphRequest) -> ApiResponse:
    result = idx.dph()(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"idx.dph()"
    )

@router.post('/plugins/pisa/bm25')
def pisa_bm25(request: PisaBm25Request) -> ApiResponse:
    result = idx.bm25(k1=request.k1,b=request.b)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"idx.bm25(k1={request.k1},b={request.b})"
    )

@router.post('/plugins/pisa/pl2')
def pisa_pl2(request: PisaPl2Request) -> ApiResponse:
    result = idx.pl2(c=request.c)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"idx.pl2(c={request.c})"
    )

@router.post('/plugins/pisa/qld')
def pisa_qld(request: PisaQldRequest) -> ApiResponse:
    result = idx.qld(mu=request.mu)(request.input)
    return generate_api_response(
        result.to_dict('records'),
        request.input,
        f"idx.qld(mu={request.mu})"
    )
