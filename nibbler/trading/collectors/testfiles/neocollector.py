from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceNEO(Collector):
    _exchange = 'binance'
    symbol = 'NEO/USDT'
    limit = 1000
    
    def NEOcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/NEO/1m')
        timeFrame = '1m'
        filename = 'NEO%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceNEO(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-17T00:00:00Z',  multiplier=1)

BinanceNEO.NEOcollector1m()