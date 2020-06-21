import multiprocessing as mp
from math import sqrt

def funcA():
    print('im funcA')
def funcB():
    funcA()
    print('im funcB')
 
def funcC():
    funcB()
    print('im funcC')

def funcD():
    print('im funcD')

def funce():
    print('im funcE')
    funcD()
if __name__ == "__main__":
    import multiprocessing as mp

    p1 = mp.Process(target=funcC)
    p2 = mp.dummy.Pool(target=funce)
    p1.start()
    p2.start()