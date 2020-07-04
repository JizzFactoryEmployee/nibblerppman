from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceDASH(Collector):
    _exchange = 'binance'
    symbol = 'DASH/USDT'
    limit = 1000
    
    def DASHcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/DASH/1m')
        timeFrame = '1m'
        filename = 'DASH%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceDASH(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-04T00:00:00Z',  multiplier=1)

BinanceDASH.DASHcollector1m()