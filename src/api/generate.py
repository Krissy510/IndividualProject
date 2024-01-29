from enum import Enum
from typing import Dict, List, Tuple, TypedDict, get_type_hints

from model import *
from validation import *

# Define a mapping of field names to their widths
field_widths = {
    'qid': 30,
    'query': 200,
    'query_0': 200,
    'docno': 80,
    'body': 300,
    'text': 300,
    'score': 80,
    'rank': 30,
    'stashed_results_0': 300,
    'query_vec': 300,
    'doc_vec': 300,
}

preset_parameters = {
    'dataset': {
        'name': 'Dataset',
        'type': 'select',
        'default': 'msmarco_passage',
        'id': 'dataset',
        'choices': VALID_DATASET
    },
    'wmodel': {
        'name': 'Wmodel',
        'type': 'select',
        'default': 'BM25',
        'id': 'wmodel',
        'choices': VALID_WMODEL,
    },
    'index_variant': {
        'name': 'Index Variant',
        'type': 'select',
        'default': 'terrier_stemmed',
        'id': 'index_variant',
        'choices': VALID_INDEX_VARIANT,
    },
    'num_results': {
        'name': 'Num of result',
        'type': 'number',
        'default': 5,
        'id': 'num_results',
    },
    'length': {
        'name': 'Length',
        'type': 'number',
        'default': 5,
        'id': 'length',
    },
    'stride': {
        'name': 'Stride',
        'type': 'number',
        'default': 1,
        'id': 'stride',
    },
    'fb_terms': {
        'name': 'fb_terms',
        'type': 'number',
        'default': 10,
        'id': 'fb_terms'
    },
    'fb_docs': {
        'name': 'fb_docs',
        'type': 'number',
        'default': 3,
        'id': 'fb_docs'
    },
    'fb_lambda': {
        'name': 'fb_lambda',
        'type': 'number',
        'default': 0.6,
        'id': 'fb_lambda'
    },
    'batch_size': {
        'name': 'batch_size',
        'type': 'number',
        'default': 4,
        'id': 'batch_size'
    },
}


def generate_columns(cls: type) -> List[IColumns]:
    return [{'name': field_name, 'width': field_widths[field_name]}
            for field_name in (get_type_hints(cls).keys())]


def generate_parameters(cls: type) -> List[IParameters]:
    parameters = list(get_type_hints(cls).keys())
    parameters.remove('input')
    return [preset_parameters[parameter] for parameter in parameters]


def generate_interactive_props(example: List[dict], requestClass: type, outputClass: type):
    type_hints = get_type_hints(requestClass)
    query_type = type_hints['input'].__args__[0]
    return {
        'example': example,
        'input': generate_columns(query_type),
        'output': generate_columns(outputClass),
        'parameters': generate_parameters(requestClass)
    }


def generate_multi_interactive_props(optionsName: List[str], defaultOption: str, examples: List[List[dict]], requestClasses: List[type], outputClasses: List[type]):
    options = dict()
    for i in range(len(requestClasses)):
        type_hints = get_type_hints(requestClasses[i])
        query_type = type_hints['input'].__args__[0]
        options[optionsName[i]] = {
            'example': examples[i],
            'input': generate_columns(query_type),
            'output': generate_columns(outputClasses[i]),
        }
    return {
        'options': options,
        'parameters': [{
            'name': 'Type',
            'type': 'select',
            'default': defaultOption,
            'id': 'type',
            'choices': optionsName
        }
        ]
    }


def generate_api_response(result: List, input: List, pipeline: str) -> ApiResponse:
    input_str = '[\n' + ',\n'.join(map(str, input)) + '\n]'
    return ({
        'result': result,
        'code': f'import pyterrier as pt\nif not pt.started():\n    pt.init()\ninput = {input_str}\npipeline = {pipeline}\nresult = pipeline(input)'
    })
