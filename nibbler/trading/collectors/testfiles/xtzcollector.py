from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceXTZ(Collector):
    _exchange = 'binance'
    symbol = 'XTZ/USDT'
    limit = 1000
    
    def XTZcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/XTZ/1m')
        timeFrame = '1m'
        filename = 'XTZ%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXTZ(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-06T00:00:00Z',  multiplier=1)

BinanceXTZ.XTZcollector1m()