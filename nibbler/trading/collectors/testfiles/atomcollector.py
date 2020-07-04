from nibbler import trading as td
from nibbler.trading.collectors.collector_base import Collector



class BinanceATOM(Collector):
    _exchange = 'binance'
    symbol = 'ATOM/USDT'
    limit = 1000
    
    def ATOMcollector1m():
        from pathlib import Path
        import time
        import os
        directory = Path(r'/home/nibbler/nibblerppman/nibbler/trading/collectors/coins/ATOM/1m')
        timeFrame = '1m'
        filename = 'ATOM%s.csv'%timeFrame
        filepath = directory/filename
        collector = BinanceATOM(timeFrame)
        collector.run_loop(filepath, timestamp='2020-02-07T00:00:00Z',  multiplier=1)

BinanceATOM.ATOMcollector1m()