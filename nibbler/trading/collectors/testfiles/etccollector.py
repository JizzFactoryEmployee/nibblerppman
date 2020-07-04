from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceETC(Collector):
    _exchange = 'binance'
    symbol = 'ETC/USDT'
    limit = 1000
    
    def ETCcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ETC/1m')
        timeFrame = '1m'
        filename = 'ETC%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceETC(timeFrame)
        collector.run_loop(filepath, timestamp='2020-01-16T00:00:00Z',  multiplier=1)

BinanceETC.ETCcollector1m()