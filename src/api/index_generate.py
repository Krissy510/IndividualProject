import pyterrier as pt
# from pyterrier_pisa import PisaIndex
from helper import pyterrier_init

pyterrier_init()

dataset = pt.get_dataset('vaswani')
indexer = pt.TRECCollectionIndexer("./index")
indexref = indexer.index(dataset.get_corpus())

dataset_pisa = pt.get_dataset('irds:antique/test')
idx = PisaIndex('./pisa-antique-index')
idx.index(dataset_pisa.get_corpus_iter())
