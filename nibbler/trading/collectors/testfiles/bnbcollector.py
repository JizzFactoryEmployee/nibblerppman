from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceBNB(Collector):
    _exchange = 'binance'
    symbol = 'BNB/USDT'
    limit = 1000
    
    def BNBcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/BNB/1m')
        timeFrame = '1m'
        filename = 'BNB%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBNB(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-10T00:00:00Z',  multiplier=1)

BinanceBNB.BNBcollector1m()