"""
This Python module serves as a utility for generating props used in documentation and API response JSON for frontend applications.

The module includes functions for generating base code, index code, columns, parameters, and interactive props. It also provides a function for generating API response with result data, input details, and generated code.

The key components and functionalities of this module are as follows:

1. **Base Code Generation:**
   - `generate_base_code(base_template_name: str)`: Generates base code using a specified template name.

2. **Index Code Generation:**
   - `generate_index_code(index_template_name: str)`: Generates index code using a specified template name.

3. **Columns and Parameters Generation:**
   - `generate_columns(cls: type) -> List[IColumns]`: Generates a list of columns with names and widths from the provided class.
   - `generate_parameters(cls: type) -> List[IParameters]`: Generates a list of parameters with details from the provided class.

4. **Interactive Props Generation:**
   - `generate_interactive_props(example: List[dict], requestClass: type, outputClass: type)`: Generates interactive props including examples, input columns, output columns, and parameters.
   - `generate_multi_interactive_props(optionsName: List[str], defaultOption: str, examples: List[List[dict]], requestClasses: List[type], outputClasses: List[type], parameters: List[str])`: Generates interactive props for multiple options, including examples, input columns, output columns, and parameters.

5. **API Response Generation:**
   - `generate_api_response(result: List, input: List, pipeline: str, base_template: str = 'none', index_template: str = 'default') -> ApiResponse`: Generates API response including result data, input details, and generated code.

Note: The module also includes imports, constants, and presets necessary for its functioning.

Make sure to review and customize the PRESET_PARAMETERS dictionary according to your specific requirements before using the module in your project.
"""

from enum import Enum
from typing import Dict, List, Tuple, TypedDict, get_type_hints

from model import *
from constant import *

def generate_base_code(base_template_name: str):
    base = BASE_TEMPLATES[base_template_name]
    if base != '':
        base += '\n'
    return f'''import pyterrier as pt
{base}
if not pt.started():
    pt.init()
'''

def generate_index_code(index_template_name: str):
    index = INDEX_TEMPLATES[index_template_name]
    if index != '':
        index += '\n\n'
    return index


def generate_columns(cls: type) -> List[IColumns]:
    return [{'name': field_name, 'width': FIELD_WIDTHS[field_name]}
            for field_name in (get_type_hints(cls).keys())]


def generate_parameters(cls: type) -> List[IParameters]:
    parameters = list(get_type_hints(cls).keys())
    parameters.remove('input')
    return [PRESET_PARAMETERS[parameter] for parameter in parameters]


def generate_interactive_props(example: List[dict], requestClass: type, outputClass: type) -> InteractiveFeatureProps:
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

    parameter = [PRESET_PARAMETERS[parameter] for parameter in parameters]
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
    input_str = '[\n' + ',\n'.join(map(str, input)) + '\n]\n'
    generated_code = f'''{generate_base_code(base_template)}
{generate_index_code(index_template)}input = {input_str}
pipeline = {pipeline}
result = pipeline(input)'''
    return ({
        'result': result,
        'code': generated_code
    })
