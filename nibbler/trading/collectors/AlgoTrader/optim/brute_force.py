import multiprocessing as mp
from . import Tester
import numpy as np
from .. import signals
import random
from tqdm import tqdm


def minmaxInitializer(po_max, wl_min, wl_max):
    po = random.randint(1, po_max)
    lower = max(po, wl_min)
    wl = random.randint(lower, wl_max)
    wl_dt = random.randint(lower, wl_max*2)
    args = (wl, po, wl_dt, po)
    kwargs = {}
    return args, kwargs


def splitList(inputList, nSplits):
    divisionSize = len(inputList)//nSplits
    chunks = []
    chunkSetter = chunks.append
    for i in np.arange(nSplits):
        k = i*divisionSize

        if i < nSplits:
            chunkSetter(inputList[k:(k+divisionSize)])
        else:
            chunkSetter(inputList[k:])
    return chunks


class RunOnList:
    def __init__(self, data):
        self.data = data

    def run(self, testList):
        completedPairs = []
        for pair in tqdm(testList):
            pair.testall(
                self.data,
                nSkip=max(
                    pair.buySignal.args[0],
                    pair.buySignal.args[2],
                    pair.sellSignal.args[0],
                    pair.sellSignal.args[2])*2,
                printLog=False,
                logFile=None
            )
            completedPairs.append(pair)
        return completedPairs

    def runmp(self, testList, shared):
        output = self.run(testList)
        shared.put(output)


class BruteForce:
    def __init__(self, basePopulation=50, environment=None, fee=0.0004):
        self.basePopulation = basePopulation
        self.environment = environment
        self.fee = fee

    def calculateFitness(
            self, data, nProcessors=5, multiprocessingMethod='process'):
        testEnv = self.environment(data)
        if nProcessors == 1:
            self.population = testEnv.run(self.population)

        if nProcessors > 1:
            if multiprocessingMethod.lower() == 'default':
                NotImplemented
                # pool = mp.Pool(nProcessors)
                # completed = pool.map(testEnv.run, splitList)
                # final = []
                # list(map(final.extend, completed))
                # self.population = final
            if multiprocessingMethod.lower() == 'process':
                q = mp.Manager().Queue()
                split_list = splitList(self.population, nProcessors)
                processes = [mp.Process(target=testEnv.runmp, args=(item, q))
                             for item in split_list]
                [process.start() for process in processes]
                [process.join() for process in processes]
                managedList = []
                while q.qsize() > 0:
                    managedList.extend(q.get())
                self.population = managedList

    def selectBest(self, fractionToSelect):
        self.population.sort(key=lambda x: x.accountBalance)
        self.selected = []
        nToSelect = int(len(self.population)*fractionToSelect)
        self.selected = self.population[0:nToSelect]

    def initilize(self, same=True):
        initializedPairs = []
        for i in np.arange(self.basePopulation):
            while True:
                try:
                    args_bull, kwargs_bull = self.bullInitializer()
                    if not same:
                        args_bear, kwargs_bear = self.bearInitializer()
                    else:
                        args_bear, kwargs_bear = args_bull, kwargs_bull
                    b_sig = self.bullSignal(*args_bull, **kwargs_bull)
                    r_sig = self.bearSignal(*args_bear, **kwargs_bear)
                    initializedPairs.append(Tester(
                        b_sig,
                        r_sig,
                        risk=1,
                        takerFee=self.fee)
                    )
                    break
                except:
                    pass
        self.population = initializedPairs

    def bullSignal(self): NotImplemented
    def bullInitializer(self): NotImplemented
    def bearSignal(self): NotImplemented
    def bearInitializer(self): NotImplemented


class BruteForceMinMax(BruteForce):
    po_max = 5
    wl_max = 50
    wl_min = 6

    def bullSignal(self, *args, **kwargs):
        return signals.Min(*args, **kwargs)

    def bullInitializer(self, *args, **kwargs):
        return minmaxInitializer(self.po_max, self.wl_min, self.wl_max)

    def bearSignal(self, *args, **kwargs):
        return signals.Max(*args, **kwargs)

    def bearInitializer(self, *args, **kwargs):
        return minmaxInitializer(self.po_max, self.wl_min, self.wl_max)