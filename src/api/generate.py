from enum import Enum
from typing import Dict, List, Tuple, TypedDict, get_type_hints

from model import *
from constant import *

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
        'default': 'vaswani',
        'id': 'dataset',
        'choices': VALID_DATASET,
        'read_only': True,
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
    'k1': {
        'name': 'k1',
        'type': 'number',
        'default': 1.2,
        'id': 'k1'
    },
    'b': {
        'name': 'b',
        'type': 'number',
        'default': 0.4,
        'id': 'b'
    },
    'c': {
        'name': 'c',
        'type': 'number',
        'default': 1.0,
        'id': 'c'
    },
    'mu': {
        'name': 'mu',
        'type': 'number',
        'default': 1000,
        'id': 'mu'
    },
    'qre_dataset': {
        'name': 'Dataset',
        'type': 'select',
        'default': 'vaswani',
        'id': 'qre_dataset',
        'choices': ['vaswani'],
        'read_only': True
    },
    'pisa_dataset': {
        'name': 'Dataset',
        'type': 'select',
        'default': 'antique',
        'id': 'pisa_dataset',
        'choices': ['antique'],
        'read_only': True
    },
    'dr_model': {
        'name': 'Model',
        'type': 'select',
        'default': 'castorini/tct_colbert-msmarco',
        'id': 'model',
        'choices': ['castorini/tct_colbert-msmarco'],
        'read_only': True

    },
    'dr_ance_model': {
        'name': 'Model',
        'type': 'select',
        'default': 'sentence-transformers/msmarco-roberta-base-ance-firstp',
        'id': 'model',
        'choices': ['sentence-transformers/msmarco-roberta-base-ance-firstp'],
        'read_only': True

    }
}


def generate_base_code(template_name: str):
    return f'''import pyterrier as pt
{BASE_TEMPLATES[template_name]}
\nif not pt.started():
    pt.init()
\n'''


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


def generate_multi_interactive_props(optionsName: List[str], defaultOption: str, examples: List[List[dict]], requestClasses: List[type], outputClasses: List[type], parameters: List[str]):
    options = dict()
    for i in range(len(requestClasses)):
        type_hints = get_type_hints(requestClasses[i])
        query_type = type_hints['input'].__args__[0]
        options[optionsName[i]] = {
            'example': examples[i],
            'input': generate_columns(query_type),
            'output': generate_columns(outputClasses[i]),
        }

    parameter = [preset_parameters[parameter] for parameter in parameters]
    parameter.append({
        'name': 'Type',
        'type': 'select',
        'default': defaultOption,
        'id': 'type',
        'choices': optionsName
    })
    return {
        'options': options,
        'parameters': parameter
    }


def generate_api_response(result: List, input: List, pipeline: str, base_template: str = 'none', index_template: str = 'default') -> ApiResponse:
    input_str = '[\n' + ',\n'.join(map(str, input)) + '\n]'
    return ({
        'result': result,
        'code': f'''{generate_base_code(base_template)}\n
{BASE_INDEXES[index_template]}\n
input = {input_str}\n
pipeline = {pipeline}
result = pipeline(input)'''
    })
