from typing import TypedDict, get_type_hints, List, Dict, Tuple
from enum import Enum
from model import *
from validation import *

# Define a mapping of field names to their widths
field_widths = {
    "qid": 30,
    "query": 400,
    "docno": 50,
    "body": 300,
}

preset_parameters = {
    "dataset": {
        "name": "Dataset",
        "type": "select",
        "default": "msmarco_passage",
        "id": "dataset",
        "choices": valid_dataset
    },
    "wmodel": {
        "name": "Wmodel",
        "type": "select",
        "default": "BM25",
        "id": "wmodel",
        "choices": valid_wmodel,
    },
    "index_variant": {
        "name": "Index Variant",
        "type": "select",
        "default": "terrier_stemmed",
        "id": "index_variant",
        "choices": valid_index_variant,
    },
    "num_results": {
        "name": "Num of result",
        "type": "number",
        "default": 5,
        "id": "num_results",
    },
    "length": {
        "name": "Length",
        "type": "number",
        "default": 150,
        "id": "length",
    },
    "stride": {
        "name": "Stride",
        "type": "number",
        "default": 75,
        "id": "stride",
    },
}


def generate_columns(cls:type) -> List[IColumns]:
    return [{"name": field_name, "width": field_widths[field_name]}
            for field_name in (get_type_hints(cls).keys())]


def generate_parameters(cls:type) -> List[IParameters]:
    parameters = list(get_type_hints(cls).keys())
    parameters.remove("input")
    return [preset_parameters[parameter] for parameter in parameters]


def generate_interactive_props(example: List[dict], requestClass:type, outputClass: type):
    type_hints = get_type_hints(requestClass)
    query_type = type_hints['input'].__args__[0] 
    return {
        "example": example,
        "input": generate_columns(query_type),
        "parameters": generate_parameters(param_cls)
        "parameters": generate_parameters(requestClass)
    }
