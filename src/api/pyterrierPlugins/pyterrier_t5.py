import pyterrier as pt
from fastapi import APIRouter
from pyterrier_t5 import DuoT5ReRanker, MonoT5ReRanker

from generate import generate_api_response, generate_interactive_props
from helper import pyterrier_init
from model import ApiResponse, InteractiveFeatureProps, T5Request, T5Result

pyterrier_init()

folder_path = './index'

index = pt.IndexFactory.of(folder_path)

# Sample data
SAMPLE_DATA = [
    {
        "qid": "0",
        "docid": 1307,
        "docno": "1308",
        "rank": 0,
        "score": 10.280188322370662,
        "query": "digital",
        "text": "electronic digitizing techniques  a  electronic digitizing techniques\nb  a simple analogue to digital converter with nonlinearity compensation\nc  the step by step potentiometer as a digitizer  d  an analogue\ndigital converter with long life  e  a wide range fully automatic\ndigital voltmeter  f  an all electronic four digit digital volmeter\n"
    },
    {
        "qid": "0",
        "docid": 510,
        "docno": "511",
        "rank": 1,
        "score": 9.172706987238703,
        "query": "digital",
        "text": "pulse height to digital signal converter  a transistorized analogue\ndigital converter provides digit binary outputs for an input at a\nmaximum sampling rate fo pulses\n"
    },
    {
        "qid": "0",
        "docid": 10611,
        "docno": "10612",
        "rank": 2,
        "score": 9.172706987238703,
        "query": "digital",
        "text": "digitizer to tape punch coupling unit  the output in twelve binary\ndigits of a digitizer is briefly stored before operating a high speed\nfive track tape punch\n"
    },
    {
        "qid": "0",
        "docid": 7874,
        "docno": "7875",
        "rank": 3,
        "score": 8.962940933558597,
        "query": "digital",
        "text": "programming a digital computer for cell counting programming a digital\ncomputer for cell counting and sizing\n"
    },
    {
        "qid": "0",
        "docid": 10090,
        "docno": "10091",
        "rank": 4,
        "score": 8.849333943513306,
        "query": "digital",
        "text": "digital radiometer\n"
    },
    {
        "qid": "0",
        "docid": 3173,
        "docno": "3174",
        "rank": 5,
        "score": 8.839698765903483,
        "query": "digital",
        "text": "a simple shaft digitizer and store  a shaft position encoder of simple\nconstruction for analogue to digital conversion is described\n"
    }
]


# API implementation starts here
router = APIRouter()

# Interactive feature GET API
@router.get('/plugins/pyterrier-t5/mono')
def get_mono_t5_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        SAMPLE_DATA,
        T5Request,
        T5Result
    )

@router.get('/plugins/pyterrier-t5/duo')
def get_duo_t5_fields() -> InteractiveFeatureProps:
    return generate_interactive_props(
        SAMPLE_DATA,
        T5Request,
        T5Result
    )


@router.post('/plugins/pyterrier-t5/mono')
def mono_t5_re_ranker(request: T5Request) -> ApiResponse:
    result = MonoT5ReRanker(batch_size=request.batch_size) (request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 f"MonoT5ReRanker(batch_size={request.batch_size})")

@router.post('/plugins/pyterrier-t5/duo')
def duo_t5_re_ranker(request: T5Request) -> ApiResponse:
    result = DuoT5ReRanker(batch_size=request.batch_size) (request.input)
    return generate_api_response(result.to_dict('records'),
                                 request.input,
                                 f"DuoT5ReRanker(batch_size={request.batch_size})")