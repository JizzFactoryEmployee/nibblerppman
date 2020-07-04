from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceBAT(Collector):
    _exchange = 'binance'
    symbol = 'BAT/USDT'
    limit = 1000
    
    def BATcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/BAT/1m')
        timeFrame = '1m'
        filename = 'BAT%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceBAT(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-13T00:00:00Z',  multiplier=1)

BinanceBAT.BATcollector1m()