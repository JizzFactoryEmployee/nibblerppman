from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceADA(Collector):
    _exchange = 'binance'
    symbol = 'ADA/USDT'
    limit = 1000
    
    def ADAcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ADA/1m')
        timeFrame = '1m'
        filename = 'ADA%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceADA(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-31T00:00:00Z',  multiplier=1)
BinanceADA.ADAcollector1m()
