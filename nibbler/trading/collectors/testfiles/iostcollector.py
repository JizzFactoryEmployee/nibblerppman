from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceIOST(Collector):
    _exchange = 'binance'
    symbol = 'IOST/USDT'
    limit = 1000
    
    def IOSTcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/IOST/1m')
        timeFrame = '1m'
        filename = 'IOST%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceIOST(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-21T00:00:00Z',  multiplier=1)

BinanceIOST.IOSTcollector1m()