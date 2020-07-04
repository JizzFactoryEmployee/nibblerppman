from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceLINK(Collector):
    _exchange = 'binance'
    symbol = 'LINK/USDT'
    limit = 1000
    
    def LINKcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/LINK/1m')
        timeFrame = '1m'
        filename = 'LINK%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceLINK(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-17T00:00:00Z',  multiplier=1)

BinanceLINK.LINKcollector1m()