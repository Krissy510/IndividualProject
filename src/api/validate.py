def dataset(dataset_name: str) -> bool:
    valid_datasets = {'vaswani', 'msmarco_document', 'msmarco_passage',
                      'trec-covid', 'trec-deep-learning-docs', 'trec-deep-learning-passages'}
    return dataset_name in valid_datasets


def wmodel(wmodel_name: str) -> bool:
    valid_wmodels = {'BB2', 'BM25', 'BM25F', 'CoordinateMatch', 'DFIC', 'DFIZ',
                     'DFR_BM25', 'DFRee', 'DFReeKLIM', 'DFRWeightingModel', 'DirichletLM', 'Dl',
                     'DLH', 'DLH13', 'DPH', 'Hiemstra_LM', 'IFB2', 'In_expB2', 'In_expC2',
                     'InB2', 'InL2', 'Js_KLs', 'LemurTF_IDF', 'LGD', 'MDL2', 'ML2', 'Null', 'PL2',
                     'TF_IDF', 'XSqrA_M'}
    return wmodel_name in valid_wmodels


def variant(index_variant: str) -> bool:
    valid_index_variant = {'terrier_stemmed', 'terrier_stemmed_positions',
                           'terrier_unstemmed', 'terrier_stemmed_text', 'terrier_unstemmed_text'}
    return index_variant in index_variant
