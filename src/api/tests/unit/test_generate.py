import unittest
from typing import List

from constant import FIELD_WIDTHS, VALID_DATASET
from generate import (generate_api_response, generate_base_code,
                      generate_columns, generate_index_code,
                      generate_interactive_props,
                      generate_multi_interactive_props, generate_parameters)


class TestInput():
    qid: str
    query: str


class TestRequest():
    dataset: str
    num_results: int
    input: List[TestInput]


class TestResult(TestInput):
    score: float


EXPECTED_INPUTS = [{'name': 'qid', 'width': FIELD_WIDTHS['qid']},
                   {'name': 'query', 'width': FIELD_WIDTHS['query']}]

EXPECTED_PARAMETERS = [{
    'name': 'Dataset',
            'type': 'select',
            'default': 'vaswani',
            'id': 'dataset',
            'choices': VALID_DATASET,
            'read_only': True,
}, {
    'name': 'Num of result',
            'type': 'number',
            'default': 5,
            'id': 'num_results',
}]

EXPECTED_OUTPUTS = [{'name': 'qid', 'width': FIELD_WIDTHS['qid']},
                    {'name': 'query', 'width': FIELD_WIDTHS['query']},
                    {'name': 'score', 'width': FIELD_WIDTHS['score']}]


class TestGenerateColumns(unittest.TestCase):
    def test_basic(self):
        """
        Test that it can generate columns using class only
        """
        result = generate_columns(TestInput)
        self.assertEqual(result, EXPECTED_INPUTS)


class TestGenerateParameters(unittest.TestCase):
    def test_basic(self):
        """
        Test that it can generate parameter using class only
        """
        result = generate_parameters(TestRequest)
        self.assertEqual(result, EXPECTED_PARAMETERS)


class TestGenerateBaseCode(unittest.TestCase):
    def test_none(self):
        """
        Test that it can generate base code with default
        """
        expected = '''import pyterrier as pt

if not pt.started():
    pt.init()
'''
        result = generate_base_code('none')
        self.assertEqual(result, expected)

    def test_basic(self):
        """
        Test that it can generate base code using non-default parameter
        """
        expected = '''import pyterrier as pt
import pyterrier_t5

if not pt.started():
    pt.init()
'''
        result = generate_base_code('T5')
        self.assertEqual(result, expected)


class TestGenerateIndexCode(unittest.TestCase):
    def test_none(self):
        """
        Test that it can generate none index code
        """
        expected = ''
        result = generate_index_code('none')
        self.assertEqual(result, expected)

    def test_default(self):
        """
        Test that it can generate index using default
        """
        expected = '''dataset = pt.get_dataset('irds:vaswani')
indexer = pt.IterDictIndexer('./vaswani.terrier')
indexref = indexer.index(dataset.get_corpus_iter())
index = pt.IndexFactory.of(indexref)\n\n'''
        result = generate_index_code('default')
        self.assertEqual(result, expected)


class TestGenerateInteractiveProps(unittest.TestCase):
    def test_basic(self):
        """
        Test that it can generate interactive props using request and result class with example
        """
        expected = {
            'example': [],
            'parameters': EXPECTED_PARAMETERS,
            'input': EXPECTED_INPUTS,
            'output': EXPECTED_OUTPUTS
        }
        result = generate_interactive_props([], TestRequest, TestResult)
        self.assertEqual(result, expected)


class TestGenerateMultiInteractiveProps(unittest.TestCase):
    def test_basic(self):
        """
        Test that it can generate multi interactive props using List of request, result, example, and parameter
        """
        EXPECTED_EXAMPLES = [[{'qid': 0, 'query': 'smth'}],
                             [{'qid': 1, 'query': 'smth_2'}]]

        MULTI_EXPECTED_PARAMETERS = EXPECTED_PARAMETERS[:]
        MULTI_EXPECTED_PARAMETERS.append({
            'name': 'Type',
            'type': 'select',
            'default': 'first',
            'id': 'type',
            'choices': ['first', 'second']
        })
        expected = {
            'options': {
                'first': {
                    'example': [{'qid': 0, 'query': 'smth'}],
                    'input': EXPECTED_INPUTS,
                    'output': EXPECTED_OUTPUTS
                },
                'second': {
                    'example': [{'qid': 1, 'query': 'smth2'}],
                    'input': EXPECTED_INPUTS,
                    'output': EXPECTED_OUTPUTS
                }
            },
            'parameters': EXPECTED_PARAMETERS
        }

        result = generate_multi_interactive_props(optionsName=['first', 'second'],
                                                  defaultOption='first',
                                                  examples=EXPECTED_EXAMPLES,
                                                  requestClasses=[
                                                      TestRequest, TestRequest],
                                                  outputClasses=[
                                                      TestResult, TestResult],
                                                  parameters=['dataset', 'num_results'])


class TestGenerateApiResponse(unittest.TestCase):
    def test_default(self):
        """
        Test if it creates API response using default parameters 
        """
        EXPECTED_RESPONSE = {
            'result': [],
            'code': """import pyterrier as pt

if not pt.started():
    pt.init()

dataset = pt.get_dataset('irds:vaswani')
indexer = pt.IterDictIndexer('./vaswani.terrier')
indexref = indexer.index(dataset.get_corpus_iter())
index = pt.IndexFactory.of(indexref)

input = [
{'qid': '0', 'query': 'how to retrieve text'},
{'qid': '1', 'query': 'what is an inverted index'}
]

pipeline = pt.BatchRetrieve(index, num_results=1, wmodel='BM25')
result = pipeline(input)"""
        }
        result = generate_api_response(result=[],
                                       input=[
            {'qid': '0', 'query': 'how to retrieve text'},
            {'qid': '1', 'query': 'what is an inverted index'},
        ],
            pipeline="pt.BatchRetrieve(index, num_results=1, wmodel='BM25')")
        self.assertEqual(result, EXPECTED_RESPONSE)


if __name__ == '__main__':
    unittest.main()
