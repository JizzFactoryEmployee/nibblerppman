from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceXMR(Collector):
    _exchange = 'binance'
    symbol = 'XMR/USDT'
    limit = 1000
    
    def XMRcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/XMR/1m')
        timeFrame = '1m'
        filename = 'XMR%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceXMR(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-03T00:00:00Z',  multiplier=1)

BinanceXMR.XMRcollector1m()