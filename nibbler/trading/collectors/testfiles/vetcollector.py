from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceVET(Collector):
    _exchange = 'binance'
    symbol = 'VET/USDT'
    limit = 1000
    
    def VETcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/VET/1m')
        timeFrame = '1m'
        filename = 'VET%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceVET(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-14T00:00:00Z',  multiplier=1)

BinanceVET.VETcollector1m()