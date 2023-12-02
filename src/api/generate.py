from typing import TypedDict, get_type_hints, List, Dict, Tuple
from enum import Enum
from model import *
from validation import *

# Define a mapping of field names to their widths
field_widths = {
    "qid": 50,
    "query": 100
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
    }
}


def generate_columns(cls) -> Tuple[IColumns]:
    return ({"name": field_name, "width": field_widths.get(field_name, None)}
            for field_name in get_type_hints(cls).keys())


def generate_parameters(cls) -> Tuple[IParameters]:
    parameters = tuple(get_type_hints(cls).keys())[1::]
    return (preset_parameters[parameter] for parameter in parameters)
