VALID_WMODEL = ('BB2', 'BM25', 'BM25F', 'CoordinateMatch', 'DFIC', 'DFIZ',
                'DFR_BM25', 'DFRee', 'DFReeKLIM', 'DFRWeightingModel', 'DirichletLM',
                'Dl', 'DLH', 'DLH13', 'DPH', 'Hiemstra_LM', 'IFB2', 'In_expB2', 'In_expC2',
                'InB2', 'InL2', 'Js_KLs', 'LemurTF_IDF', 'LGD', 'MDL2',
                'ML2', 'Null', 'PL2', 'TF_IDF', 'XSqrA_M',)

VALID_DATASET = ['vaswani']

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
