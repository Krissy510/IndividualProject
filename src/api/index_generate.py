import pyterrier as pt
from pyterrier_pisa import PisaIndex
from helper import pyterrier_init

pyterrier_init()

indexer = pt.IterDictIndexer('./vaswani.terrier')
indexer.index(pt.get_dataset('irds:vaswani').get_corpus_iter())

pisa_idx = PisaIndex('./antique.pisa')
pisa_idx.index(pt.get_dataset('irds:antique/test').get_corpus_iter())
