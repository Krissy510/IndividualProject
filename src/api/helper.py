import pyterrier as pt

def pyterrier_init():
    if not pt.started():
        pt.init(boot_packages=["com.github.terrierteam:terrier-prf:-SNAPSHOT"])