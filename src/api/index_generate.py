import pyterrier as pt
from pyterrier_pisa import PisaIndex
from helper import pyterrier_init

pyterrier_init()

indexer = pt.IterDictIndexer('./vaswani.terrier')
indexer.index(pt.get_dataset('irds:vaswani').get_corpus_iter())

dataset_pisa = pt.get_dataset('irds:antique/test')
idx = PisaIndex('./pisa-antique-index')
idx.index(dataset_pisa.get_corpus_iter())
