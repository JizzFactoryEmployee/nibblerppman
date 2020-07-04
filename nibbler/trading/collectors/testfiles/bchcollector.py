from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceBCH(Collector):
    _exchange = 'binance'
    symbol = 'BCH/USDT'
    limit = 1000
    
    def BCHcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/BCH/1m')
        timeFrame = '1m'
        filename = 'BCH%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBCH(timeFrame)
        collector.run_loop(filepath, timestamp='2019-12-19T00:00:00Z',  multiplier=1)

BinanceBCH.BCHcollector1m()