from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_retreive():
    response = client.post(
        url='/retreive',
        json={
            "input": [
                {
                    "qid": "0",
                    "query": "how to retrieve text"
                },
                {
                    "qid": "1",
                    "query": "what is an inverted index"
                }
            ],
            "dataset": "msmarco_passage",
            "wmodel": "BM25",
            "index_variant": "terrier_stemmed",
            "num_results": 5
        }
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "qid": "0",
            "query": "how to retrieve text",
            "docno": "5821744",
            "score": 28.305131563614037
        },
        {
            "qid": "0",
            "query": "how to retrieve text",
            "docno": "4593337",
            "score": 27.616953718405668
        },
        {
            "qid": "0",
            "query": "how to retrieve text",
            "docno": "5631043",
            "score": 27.543971646805822
        },
        {
            "qid": "0",
            "query": "how to retrieve text",
            "docno": "1961605",
            "score": 27.360035368343077
        },
        {
            "qid": "0",
            "query": "how to retrieve text",
            "docno": "7380248",
            "score": 25.905282536998605
        },
        {
            "qid": "1",
            "query": "what is an inverted index",
            "docno": "7428064",
            "score": 24.796184636593495
        },
        {
            "qid": "1",
            "query": "what is an inverted index",
            "docno": "7626374",
            "score": 22.17926748899773
        },
        {
            "qid": "1",
            "query": "what is an inverted index",
            "docno": "8647671",
            "score": 21.919184610694188
        },
        {
            "qid": "1",
            "query": "what is an inverted index",
            "docno": "4910892",
            "score": 21.52832824564918
        },
        {
            "qid": "1",
            "query": "what is an inverted index",
            "docno": "7378",
            "score": 21.52446096849307
        }
    ]


def test_text_sliding():
    response = client.post(
        url='/text-sliding',
        json={
            "num_results": 5,
            "length": 2,
            "stride": 1,
            "input": [
                {
                    "docno": "d1",
                    "body": "a b c d"
                }
            ]}
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "Index": 0,
            "docno": "d1%p0",
            "body": "a b"
        },
        {
            "Index": 0,
            "docno": "d1%p1",
            "body": "b c"
        },
        {
            "Index": 0,
            "docno": "d1%p2",
            "body": "c d"
        }
    ]