from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceTHETA(Collector):
    _exchange = 'binance'
    symbol = 'THETA/USDT'
    limit = 1000
    
    def THETAcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/THETA/1m')
        timeFrame = '1m'
        filename = 'THETA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceTHETA(timeFrame)
        collector.run_loop(filepath, timestamp='2020-05-27T00:00:00Z',  multiplier=1)

BinanceTHETA.THETAcollector1m()