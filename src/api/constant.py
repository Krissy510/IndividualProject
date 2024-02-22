VALID_WMODEL = ('BB2', 'BM25', 'BM25F', 'CoordinateMatch', 'DFIC', 'DFIZ',
                'DFR_BM25', 'DFRee', 'DFReeKLIM', 'DFRWeightingModel', 'DirichletLM',
                'Dl', 'DLH', 'DLH13', 'DPH', 'Hiemstra_LM', 'IFB2', 'In_expB2', 'In_expC2',
                'InB2', 'InL2', 'Js_KLs', 'LemurTF_IDF', 'LGD', 'MDL2',
                'ML2', 'Null', 'PL2', 'TF_IDF', 'XSqrA_M',)

VALID_DATASET = ['vaswani']

VALID_DATASET_PISA = ['irds:antique/test']

VALID_INDEX_VARIANT = ('terrier_stemmed', 'terrier_stemmed_positions', 'terrier_unstemmed',
                       'terrier_stemmed_text', 'terrier_unstemmed_text',)

BASE_TEMPLATES = {
    'T5': 'import pyterrier_t5',
    'DR': 'import pyterrier_dr',
    'PISA': 'from pyterrier_pisa import PisaIndex',
    'none': ''
}


INDEX_TEMPLATES = {
    'default': '''dataset = pt.get_dataset('irds:vaswani')
indexer = pt.IterDictIndexer('./vaswani.terrier')
indexref = indexer.index(dataset.get_corpus_iter())
index = pt.IndexFactory.of(indexref)''',
    'PISA': '''file_path = 'irds:antique/test'
dataset_pisa = pt.get_dataset(file_path)
idx = PisaIndex('./pisa-antique-index')
idx.index(dataset_pisa.get_corpus_iter())''',
    'none': ''
}

# Define a mapping of field names to their widths
FIELD_WIDTHS = {
    'qid': 80,
    'query': 200,
    'query_0': 200,
    'docno': 80,
    'body': 300,
    'text': 300,
    'score': 80,
    'rank': 80,
    'stashed_results_0': 300,
    'query_vec': 500,
    'doc_vec': 500,
}

PRESET_PARAMETERS = {
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
    },
    'dataset_pisa': {
        'name': 'Dataset',
        'type': 'select',
        'default': 'irds:antique/test',
        'id': 'dataset_pisa',
        'choices': VALID_DATASET_PISA,
        'read_only': True,
    },
}
